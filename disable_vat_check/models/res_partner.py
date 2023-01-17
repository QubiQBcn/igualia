# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (https://www.itundra.com).
# License OPL-1 or later.
#       @Author: iTundra.com

from odoo import api, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat', 'country_id')
    def check_vat(self):
        # ignore vat check
        pass