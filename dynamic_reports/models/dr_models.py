from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    description_reports = fields.Html(
        string='Description for reports',
    )
