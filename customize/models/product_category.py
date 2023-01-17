# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0

from odoo import models, api, fields, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    commission_qty = fields.Float(
        string='Default Commission')

    commission_ids = fields.One2many(
        comodel_name='product.category.agent.commission',
        inverse_name='category_id',
        string='Commissions By Agent')


class ProductCategoryAgentCommission(models.Model):
    _name = 'product.category.agent.commission'
    _description = 'Agent Commission by Category'

    category_id = fields.Many2one(
        comodel_name='product.category',
        string='Category',
        required=True)
    # -------------------- WARN: Deprecated BUT DO NOT DELETE
    agent_id = fields.Many2one(
        comodel_name='res.partner',
        string='Agent',
        domain=[("agent", "=", True)],
        required=True)
    # --------------------

    commission = fields.Float(
        string='Commission',
        required=True)

    # -------------------- Added Fields iTundra

    agent_id_hr = fields.Many2one(
        comodel_name='hr.employee',
        domain=[("agent", "=", True)],
        required=True)