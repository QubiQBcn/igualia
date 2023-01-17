from odoo import fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'


    number_work_centers = fields.Integer(string="Number Work Centers")
    rlt = fields.Boolean(string="RLT")
    type_contact = fields.Selection(
        string="Type Contact",
        selection=[
            ('comercial_contact', _('Commercial Contact')),
            ('technical_contact', _('Technical Contact')),
            ('contact_billing', _('Contact Billing')),
            ('contact_training', _('Contact Training')),
            ('student_training', _('Student Training')),
        ]
    )
    department_numbers = fields.Integer(string="Department Numbers")
