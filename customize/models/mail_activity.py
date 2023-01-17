# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0
from operator import itemgetter
from itertools import groupby
from random import randint
from odoo import api, fields, models
from collections import defaultdict
# todo:move me in separate module (always inside this module)
class MailActivity(models.Model):
    _inherit = 'mail.activity'

    _default_color = lambda self: randint(1, 11)
    color = fields.Integer(string='Color Index', default=_default_color)

    employee_id = fields.Many2one('hr.employee', string='Employee', tracking=True,
                                 help="Employee Manager of the Project")

    # employee_ids = fields.Many2many('hr.employee', string="Activity Employees") todo: make also for employees.
    user_ids = fields.Many2many('res.users', )

    is_main_activity = fields.Boolean(default=True, readonly=True)
    is_sub_activity = fields.Boolean(default=False, readonly=True)
    activity_main_id = fields.Many2one('mail.activity', ondelete='cascade', index=True, auto_join=True, tracking=True, readonly=True,
   help="Indicates the Main activity where an activity with multiple users was created. This is the actual record that is shown to each user.")
    activity_sub_ids = fields.One2many('mail.activity', inverse_name='activity_main_id', readonly=True,
                                       help="Internal Activity record used when creating Activities with multiple Users. This Record is hidden to the end-user and activity_main_id is the one to be shown.")

    # Related fields To its self to show in the child ids.
    # note: These fields are exposed and ready in case , the childs activities should be also exposed to each
    # user (of the user_ids); at the moment, each partecipant of a activity_main_id which has Nth activity_sub_ids
    # will always see only the activity_main_id | activity_sub_ids is used internally to send the activity to each user
    main_create_uid = fields.Many2one(related='activity_main_id.create_uid', readonly=True)
    main_user_ids = fields.Many2many(related='activity_main_id.user_ids', readonly=False)
    main_res_model_id = fields.Many2one(related='activity_main_id.res_model_id', readonly=False)
    main_res_model = fields.Char(related='activity_main_id.res_model', readonly=False)
    main_res_id = fields.Many2oneReference(related='activity_main_id.res_id', readonly=False)
    main_res_name = fields.Char(related='activity_main_id.res_name', readonly=False)
    main_activity_type_id = fields.Many2one(related='activity_main_id.activity_type_id', readonly=False)
    main_summary = fields.Char(related='activity_main_id.summary', readonly=False)
    main_note = fields.Html(related='activity_main_id.note', readonly=False)
    main_date_deadline = fields.Date(related='activity_main_id.date_deadline', readonly=False)

    """Example of a mail.activity dictionary object
           {
            'res_id': 26,
            'res_model': 'res.partner',
            'res_model_id': (78, 'Contact'),
            'res_name': 'Azure Interior, Brandon Freeman',
            'state': 'today',
            'summary': 'Debug 1',
            'user_id': (2, 'Mitchell Admin'),
            'activity_category': 'default',
            'activity_decoration': False,
            'activity_main_id': False,
            'activity_sub_ids': [],
            'activity_type_id': (1, 'Email'),
            'automated': False,
            'calendar_event_id': False,
            'display_name': 'Debug 1',
            'employee_id': (20, 'Abigail Peterson'),
            'employee_ids': [20, 3, 17, 21],
            'force_next': False,
            'has_recommended_activities': False,
            'icon': 'fa-envelope',        
            'is_main_activity': True,
            'is_sub_activity': False,
            'mail_template_ids': [],
            'main_activity_type_id': False,
            'main_create_uid': False,
            'main_employee_ids': [],
            'main_note': '<p><br></p>',
            'main_res_id': 0,
            'main_res_model': False,
            'main_res_model_id': False,
            'main_res_name': False,
            'main_summary': False,
            'note': '<p><br></p>',
            'previous_activity_type_id': False,
            'recommended_activity_type_id': False,        
            }

           """
    @api.model
    def create(self, values):
        activity = super(MailActivity, self).create(values)
        if activity.is_sub_activity:
            return activity

        user_ids = activity._filter_user_ids()
        if not user_ids:
            return activity

        activity_sub_values = []
        for user in user_ids:
            vals = {
                'user_id': user.id,
                # Add the default to the activity even if for the child other fields are used
                'res_model_id': activity.res_model_id.id,
                'res_model': activity.res_model,
                'res_name': activity.res_name,
                'res_id': activity.res_id,
                'activity_type_id': activity.activity_type_id.id,
                'summary': activity.summary,
                'note': activity.note,
                'date_deadline': activity.date_deadline,
                'automated': activity.automated,
                'recommended_activity_type_id': activity.recommended_activity_type_id.id,
                'previous_activity_type_id': activity.previous_activity_type_id.id,

                'is_main_activity': False,
                'is_sub_activity': True,
                'activity_main_id': activity.id,

            }
            activity_sub_values.append((0, 0, vals))

        main_activity_vals = {
            'activity_sub_ids': activity_sub_values,
        }
        activity.write(main_activity_vals)
        return activity

    def name_get(self):
        """WARN: Overwritten method | Original directory: odoo/addons/mail/models/mail_activity.py"""
        res = []
        for record in self:
            if record.is_main_activity:
                name = record.summary or record.activity_type_id.display_name
                res.append((record.id, name))
            else:
                user_id = record.user_id
                name = record.summary or record.activity_type_id.display_name
                name = f'{name} ({user_id.display_name})'
                res.append((record.id, name))
        return res


    def _filter_user_ids(self, ):
        """Returns user_ids that are not in the employee_id and inside the user_id"""
        self.ensure_one()
        activity = self
        employee_id = activity.employee_id
        other_users = self.env['res.users']
        user_id = activity.user_id
        # Remove and other user duplicates
        other_users |= user_id
        other_users |= employee_id.user_id_no_limit

        user_ids = activity.user_ids
        # Remove duplicates
        user_ids = user_ids.filtered(lambda user: user.id not in other_users.ids)
        return user_ids


    @api.model
    def get_activity_data(self, res_model, domain):
        """WARN: Overwritten Function
           Original DIR: odoo/addons/mail/models/mail_activity.py
           HACK 1 (See Notes below)
        """
        activity_domain = [('res_model', '=', res_model)]
        if domain:
            res = self.env[res_model].search(domain)
            activity_domain.append(('res_id', 'in', res.ids))
            operands = []
            operands_count = 0
            # --------------------- NOTE: Overwritten --> Add Additional Filter For filter only by Employee ID
            for d in domain:
                if 'message_employee_ids' in d:
                    operands.append(('employee_id.name', 'ilike', d[-1]))
                    operands_count += 1
            for _ in range(operands_count - 1):
                operands[0:0] = '|'
            activity_domain.extend(operands)
            # ---------------------
        grouped_activities = self.env['mail.activity'].read_group(
            activity_domain,
            ['res_id', 'activity_type_id', 'ids:array_agg(id)', 'date_deadline:min(date_deadline)'],
            ['res_id', 'activity_type_id'],
            lazy=False)
        # filter out unreadable records
        if not domain:
            res_ids = tuple(a['res_id'] for a in grouped_activities)
            res = self.env[res_model].search([('id', 'in', res_ids)])
            grouped_activities = [a for a in grouped_activities if a['res_id'] in res.ids]
        res_id_to_deadline = {}
        activity_data = defaultdict(dict)
        for group in grouped_activities:
            res_id = group['res_id']
            activity_type_id = (group.get('activity_type_id') or (False, False))[0]
            res_id_to_deadline[res_id] = group['date_deadline'] if (
                        res_id not in res_id_to_deadline or group['date_deadline'] < res_id_to_deadline[res_id]) else \
            res_id_to_deadline[res_id]
            state = self._compute_state_from_date(group['date_deadline'], self.user_id.sudo().tz)
            activity_data[res_id][activity_type_id] = {
                'count': group['__count'],
                'ids': group['ids'],
                'state': state,
                'o_closest_deadline': group['date_deadline'],
            }
        activity_type_infos = []
        activity_type_ids = self.env['mail.activity.type'].search(
            ['|', ('res_model_id.model', '=', res_model), ('res_model_id', '=', False)])
        for elem in sorted(activity_type_ids, key=lambda item: item.sequence):
            mail_template_info = []
            for mail_template_id in elem.mail_template_ids:
                mail_template_info.append({"id": mail_template_id.id, "name": mail_template_id.name})
            activity_type_infos.append([elem.id, elem.name, mail_template_info])

        return {
            'activity_types': activity_type_infos,
            'activity_res_ids': sorted(res_id_to_deadline, key=lambda item: res_id_to_deadline[item]),
            'grouped_activities': activity_data,
        }

# =================================================================================================== #
# ------------------------------------------ < NOTES > ----------------------------------------------
# =================================================================================================== #
#
# HACK 1:
#   We Basically control which Activity Ids we finally deliver to the Front-end. In order for this to work
#   the following is needed:
#       For the example we have:
#          A) sale.order as Current Model
#          B) mail.activity as the Activity model (dah..)
#          C) hr.employee filter as Target Field to use to filter Activities
#       Steps:
#           1) A Many2many field to the target DB Model (i.e. hr.employee) within  the **CURRENT MODEL** (i.e sale.order)
#           and have the Many2one Field from the mail.activity, these will be used as Hook.
#
#           2) Compute the Field Many2many, just add all Many2one from mail.activity into sale.order
#
#           3) The field must have a reverse search function which search activities based on the name of the hr.employee
#           This is used when typing the Name into the search bar (obviousle the filter should be addded in the search view too)
#
#           4)  With function get_activity_data get the 'domain' parameter and scan the operand. So Add the result to the
#           read_group