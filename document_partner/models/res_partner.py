# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       @Creation Date: 16th June - 2021
#       Odoo Version: 14.0.0


from odoo import api, fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    document_count = fields.Integer(
        compute="_compute_document_count", string="Document Count",
    )

    message_owned_documents_ids = fields.Many2many(comodel_name="ir.attachment", compute="_compute_message_owned_documents_ids",
                                                   )

    def _compute_message_owned_documents_ids(self):

        for partner in self:
            documents_owned = self.env["ir.attachment"].search([
                ("res_model", "=", "res.partner"), ("res_id", "=", partner.id)
            ])
            if documents_owned:
                partner.message_owned_documents_ids = [(6, False, documents_owned.ids)]
            else:
                partner.message_owned_documents_ids = None

    def _compute_document_count(self):
        self.document_count = 0
        attachment_groups = self.env["ir.attachment"].read_group(
            [("res_model", "=", "res.partner"), ("res_id", "in", self.ids)],
            ["res_id"],
            ["res_id"],
        )
        count_dict = {x["res_id"]: x["res_id_count"] for x in attachment_groups}
        for record in self:
            record.document_count = count_dict.get(record.id, 0)

    def action_get_attachment_tree_view(self):
        action = self.env.ref("base.action_attachment").read()[0]
        action["context"] = {
            "default_res_model": self._name,
            "default_res_id": self.ids[0],
        }
        action["domain"] = str(
            [("res_model", "=", self._name), ("res_id", "in", self.ids)]
        )
        form_view = self.env.ref("document_partner.view_attachment_form_document_partner").id
        action["views"] = [(False, 'kanban'), (False, 'tree'), (form_view, 'form')]
        action["search_view_id"] = (
            self.env.ref("document_partner.ir_attachment_view_search_document_partner").id,
        )
        return action

# class IrAttachment(models.Model):
#     _inherit = "ir.attachment"
#
#     partner_id = fields.Many2one(comodel_name='res.partner', ondelete='cascade')