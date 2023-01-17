# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    message_employee_ids = fields.Many2many('hr.employee',
                                    string='Message Employee (contact)',
                                    compute='_compute_employee_ids',
                                    search='_search_employee_ids',
                                    help="Employee Manager of the Project")

    @api.depends('activity_ids')
    def _compute_employee_ids(self):

        MailActivity = self.env['mail.activity']
        for partner in self:
            if partner.activity_ids:
                activity_by_employees = [activity.id.employee_id.id for activity in MailActivity.sudo().browse(partner.activity_ids)]
                partner.message_employee_ids = [(6, False, activity_by_employees)]
            else:
                partner.message_employee_ids = False

    def _search_employee_ids(self, _, operand):

        activities = self.env['mail.activity'].search([
            ('employee_id.name', 'ilike', operand)
        ])
        return [('activity_ids', 'in', activities.ids)]