from odoo import fields, models, _

class SaleOrderTemplate(models.Model):
    _inherit = 'sale.order.template'


    report_cover = fields.Selection(
        selection=[
            ('ppi', _('Business equality project')),
            ('pma', _('Planning measures for legislative compliance on equality, diversity and harassment management')),
            ('pand', _('Application of the comprehensive law for equal treatment and non-discrimination and the law of comprehensive guarantee of sexual freedom'))
        ]
    )
