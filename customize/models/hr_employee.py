# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0

from odoo import fields, models


class HrEmployeePrivate(models.Model):
    _inherit = "hr.employee"

    # The naming is because, hr.employee has a user_id but has a constraits which limits a res.users -> hr.employee per Company
    user_id_no_limit = fields.Many2one('res.users', 'Task User', readonly=False,
                                       help="The user linked to this employee")

class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    # The naming is because, hr.employee has a user_id but has a constraits which limits a res.users -> hr.employee per Company
    user_id_no_limit = fields.Many2one('res.users', 'Task User', readonly=False,
                                       help="The user linked to this employee")