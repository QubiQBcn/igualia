# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com


from odoo import api, fields, models


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    company_name = fields.Char('Company Name')
    function = fields.Char(string='Job Position')

    @api.model
    def _prepare_attendee_values(self, registration):
        """ Override to add Function and Company Name"""

        data = super(EventRegistration, self)._prepare_attendee_values(registration)
        data.update({
            'function': registration.get('function', ''),
            'company_name': registration.get('comment', ''),
        })
        return data

    @api.onchange('partner_id')
    def _onchange_partner(self):
        res = super(EventRegistration, self)._onchange_partner()
        if self.partner_id:
            contact_id = self.partner_id.address_get().get('contact', False)
            if contact_id:
                contact = self.env['res.partner'].browse(contact_id)
                self.function = contact.function or self.function
        return res