# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class ServerActions(models.Model):
    """ Add email option in server actions. """
    _inherit = 'ir.actions.server'

    @api.model
    def run_action_next_activity(self, action, eval_context=None):
        """WARN: Overwritten Function!!!
           Original DOCS: N/A
           Dir: odoo/addons/mail/models/ir_actions.py
        """

        if not action.activity_type_id or not self._context.get('active_id') or self._is_recompute(action):
            return False

        records = self.env[action.model_name].browse(self._context.get('active_ids', self._context.get('active_id')))

        vals = {
            'summary': action.activity_summary or '',
            'note': action.activity_note or '',
            'activity_type_id': action.activity_type_id.id,
        }
        # ---------- Overwritten
        employee_id = None
        if action.activity_user_type == 'specific':
            action_done = self.env.context.get("__action_done")
            if action_done and isinstance(action_done, dict):
                base_automation_instance = [*action_done.keys()][0]
                if base_automation_instance._name == 'base.automation':
                    employee_id = base_automation_instance.employee_id and base_automation_instance.employee_id.id or None
        if employee_id:
            vals['employee_id'] = employee_id
        # ----------
        if action.activity_date_deadline_range > 0:
            vals['date_deadline'] = fields.Date.context_today(action) + relativedelta(**{action.activity_date_deadline_range_type: action.activity_date_deadline_range})
        for record in records:
            user = False
            if action.activity_user_type == 'specific':
                user = action.activity_user_id
            elif action.activity_user_type == 'generic' and action.activity_user_field_name in record:
                user = record[action.activity_user_field_name]
            if user:
                vals['user_id'] = user.id
            record.activity_schedule(**vals)
        return False