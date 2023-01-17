# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       @Creation Date: 16th June - 2021
#       Odoo Version: 14.0.0


from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    attachment_name = fields.Char('Name ')
