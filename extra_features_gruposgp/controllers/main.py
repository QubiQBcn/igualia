# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com


import werkzeug
from odoo import http
from odoo.addons.website_event.controllers.main import WebsiteEventController
from odoo.http import request
from odoo.exceptions import AccessError

class WebsiteEventSaleController(WebsiteEventController):


    @http.route(['''/event/<model("event.event", "[('website_id', 'in', (False, current_website_id))]"):event>/registration/confirm'''], type='http', auth="public", methods=['POST'], website=True)
    def registration_confirm(self, event, **post):
        """WARN: Overwritten Function  DIR: /addons/website_event/controllers/main.py"""
        if not event.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()

        Attendees = request.env['event.registration']
        registrations = self._process_registration_details(post)
        registration_emails = {partecipant['email'] for partecipant in event.sudo().registration_ids.read(['email'])
                               if partecipant.get('email', None)}

        exist_users = []
        for registration in registrations:
            duplicate_email = False
            registration['event_id'] = event
            # --------- Overwirtten iTundra.com: Create a new Contact instead of use the default active user (self.env.user.partner_id or request.env.user.partner_id)
            partner_id = registration.pop('partner_id', False)
            is_public_user = request.website.is_public_user()  # Check if is an external User
            logged_user = request.env.user.partner_id
            public_user = request.env.company._get_public_user()  # Default User for not logged in External Users

            def create_event_contact():
                nonlocal duplicate_email
                partner_vals = registration.copy()
                key_to_delete = ['answer_ids', 'ticket_id', 'event_id']
                for key in key_to_delete:
                    if key in partner_vals:
                        partner_vals.pop(key)

                email = partner_vals.get('email').strip()
                if email: # Just make sure to remove the Spaces
                    partner_vals['email'] = email
                if email in registration_emails:
                    duplicate_email = True
                    exist_users.append(registration)
                    return

                if 'comment' in partner_vals: # TODO: this should be change with another value that is not comment
                    partner_vals['comment'] = f"Company Name: {partner_vals['comment']}"

                partner_exists = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)
                partner_id = None
                if partner_exists:  # We do not wont to register them nor to add them in the Event .
                    partner_id = partner_exists
                else:
                    try:
                        partner_id = request.env['res.partner'].sudo().create(partner_vals)
                    except AccessError:  # It should't happen but better to check
                        pass
                if partner_id:
                    registration.update({'partner_id': partner_id})
                    registration_emails.add(email)

            if logged_user:
                logged_user = logged_user.id
            if public_user:
                public_user = public_user.id

            if all([is_public_user, logged_user, public_user]) and logged_user == public_user:  # Only for external users
                create_event_contact()
            elif not is_public_user and not partner_id:  # For internal user and check whether is done from website or the event form
                create_event_contact()

            if not duplicate_email:
                Attendees += Attendees.sudo().create(
                    Attendees._prepare_attendee_values(registration))

        urls = event._get_event_resource_urls()
        return request.render("website_event.registration_complete", {
            'attendees': Attendees.sudo(),
            'event': event,
            'google_url': urls.get('google_url'),
            'iCal_url': urls.get('iCal_url'),
            'exist_users': exist_users  # Here we pass the Duplicate Users
        })