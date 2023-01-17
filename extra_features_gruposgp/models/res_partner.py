# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PartnerCompanyType(models.Model):
    _name = 'res.partner.company.type'
    _order = 'name'
    _description = 'Partner Company Type'

    name = fields.Char(string='Company Type', required=True, translate=True)
    shortcut = fields.Char(string='Abbreviation', translate=True)


class Partner(models.Model):
    _inherit = "res.partner"

    # project_ids = fields.One2many(comodel_name='project.project', inverse_name='partner_id') # DEL
    contact_company_type = fields.Many2one('res.partner.company.type')
    agent_ids = fields.Many2one(comodel_name='res.partner',
                                ondelete='cascade',
                                help="List of Customer / Contact",
                                domain=[("agent", "=", True)]
                                )
    creditor_id_many2one_ids = fields.One2many( comodel_name='res.partner',
                                                inverse_name='agent_ids',
                                                help="The Related Agent")

    check_list_ids = fields.One2many(comodel_name='project.checklist', inverse_name='partner_id',
                                     string="Check List")
    company_check_list_ids = fields.One2many(related='parent_id.check_list_ids', string="CheckList of Company")
    has_checklist = fields.Boolean(compute="_compute_has_checklist")
    num_employees = fields.Integer(string="Number of employees")
    deal = fields.Integer(string="Number of deals")

    # ==================================================================================== #
    # ----------------------------------------- MODEL > -----------------------------------#
    # ==================================================================================== #

    @api.model
    @api.returns('project.checklist', lambda value: value.id)
    def find_partner_checklist_or_create(self, customer_id, project_id=None):
        """Finds the Partner's Company Checklist and the Partner's Company """
        parent_id = customer_id.parent_id
        if not parent_id:
            company_id = customer_id
        else:
            company_id = parent_id

        if not company_id.check_list_ids:
            check_list_ids = self.env['project.checklist'].create_new_checklist(partner_id=company_id, project_id=project_id)
        else:
            check_list_ids = company_id.check_list_ids[0]
            if project_id:
                check_list_ids.write({
                    'project_id': [(4, project_id.id)]
                })

        return check_list_ids

    @api.model
    def find_partner_checklist_and_delete(self, project_id) -> bool:
        """Finds the Partner's checklist and deletes it
        The (3, project_id.id, 0) tuple is a special combo do remove a many2many or one2many single
        record, where the project_id.id is the record to remove from the checklist projects_ids one2many lsit
        """
        self.ensure_one()
        parent_id = self.parent_id
        if not parent_id:
            company_id = self
        else:
            company_id = parent_id
        if company_id in project_id.check_list_id.partner_id:
            project_id.check_list_id.write({'project_id': [(3, project_id.id, 0)]})
            return True
        else:
            return False

    # ==================================================================================== #
    # -------------------------------------- COMPUTED > -----------------------------------#
    # ==================================================================================== #

    @api.depends('check_list_ids')
    def _compute_has_checklist(self):
        for contact in self:
            contact.has_checklist = bool(contact.check_list_ids)

    # ==================================================================================== #
    # ---------------------------------- < CLIENT ACTIONS > -------------------------------#
    # ==================================================================================== #

    def action_create_checklist(self, active_id=None, *__, **___):
        if active_id and not self:
            self |= self.browse(active_id)
        if not self.check_list_ids:
            self.env['project.checklist'].create_new_checklist(partner_id=self)
        return True