# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    message_employee_ids = fields.Many2many('hr.employee',
                                    string='Message Employee',
                                    compute='_compute_employee_ids',
                                    search='_search_employee_ids',
                                    help="Employee Manager of the Project")

    @api.depends('activity_ids')
    def _compute_employee_ids(self):

        MailActivity = self.env['mail.activity']
        for order in self:
            if order.activity_ids:
                order_activity_by_employees = [activity.id.employee_id.id for activity in MailActivity.sudo().browse(order.activity_ids)]
                order.message_employee_ids = [(6, False, order_activity_by_employees)]
            else:
                order.message_employee_ids = False

    def _search_employee_ids(self, _, operand):

        activities = self.env['mail.activity'].search([
            ('employee_id.name', 'ilike', operand)
        ])
        return [('activity_ids', 'in', activities.ids)]