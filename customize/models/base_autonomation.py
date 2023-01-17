# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0

from odoo import fields, models

class BaseAutomation(models.Model):
    _inherit = 'base.automation'

    employee_id = fields.Many2one('hr.employee', string='Employee', tracking=True,
                                  help="Employee Manager of the Project")