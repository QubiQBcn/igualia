# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com

from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    agent_id = fields.Many2one(
        comodel_name='res.partner',
        compute='_compute_agent_ids',
        store=True)
    
    def update_agent_ids(self):
        self._compute_agent_ids()
    
    @api.depends('partner_id.agent_ids')
    def _compute_agent_ids(self):
        for record in self:
            record.agent_id = record.partner_id and record.partner_id.agent_ids and record.partner_id.agent_ids[0]
        


class SaleOrderLine(models  .Model):
    _inherit = 'sale.order.line'

    def name_get(self):

        if self.env.context.get('sale_order_line_custom', False):
            result = []
            for so_line in self.sudo():
                result.append((so_line.id, so_line.product_id.name))
            return result

        return super().name_get()


class SaleReport(models.Model):
    _inherit = "sale.report"

    agent_id = fields.Many2one('res.partner', string="Agent", readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['agent_id'] = ", partner.agent_ids as agent_id"
        groupby += ', partner.agent_ids'
        res = super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
        return res