# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com

from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
class ProjectCheckList(models.Model):
    _name = "project.checklist"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Project CheckList"
    _order = 'create_date desc'

    name = fields.Char()
    active = fields.Boolean(default=True)
    is_template = fields.Boolean(default=False, help="Set this as a Template CheckList, when used, an excact copy of the Template will be used instead.")

    # ---------- MAIN INFO PARTNER RELATED
    partner_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict')
    # ---------- MAIN INFO PROJECT RELATED
    project_id = fields.One2many(comodel_name='project.project', inverse_name='check_list_id', string="Project")
    company_id = fields.Many2one(related='partner_id.company_id', store=True)
    title = fields.Many2one(related='partner_id.title', store=True)
    phone = fields.Char(related='partner_id.phone')
    mobile = fields.Char(related='partner_id.mobile')
    street = fields.Char(related='partner_id.street')
    email = fields.Char(related='partner_id.email', store=True)
    employee_id_manager = fields.Many2one(related='project_id.employee_id_manager')
    user_id_hr = fields.Many2many(related='project_id.user_id_hr')

    rlt_company = fields.Selection([ ('yes', 'Yes'), ('no', 'No')])
    rlt_all_working_place = fields.Selection([ ('yes', 'Yes'), ('no', 'No')])

    # ---------- DATOS DE IGUALDAD  Equality Data
    sale_agent_id = fields.Many2one(related='project_id.sale_agent_id', domain=[("agent", "=", True)], store=True, readonly=False, string="Project Agent")
    equality_commission = fields.Char()
    working_people_number = fields.Integer()
    work_place = fields.Char()
    agreement = fields.Char()

    check_list_line = fields.One2many('project.checklist.line', 'check_list_id', string='Questions', auto_join=True)

    # HACK_group_by
    employee_id_manager_groupby = fields.Char(string='Manager', compute='_get_project_managers', store=True)
    user_id_hr_groupby = fields.Char(string='Manager', compute='_get_project_managers', store=True)
    group_by_trigger = fields.Integer(compute='_compute_trigger_groupby')

    @api.model
    @api.depends('employee_id_manager', 'employee_id_manager.name', 'user_id_hr', 'user_id_hr.name')
    def _get_project_managers(self): # HACK_group_by
        for rec in self:
            managers_names = set(rec.project_id.mapped('employee_id_manager').mapped('display_name'))
            rec.employee_id_manager_groupby = ', '.join(list(managers_names))

            project_managers_name = set(rec.project_id.mapped('user_id_hr').mapped('display_name'))
            rec.user_id_hr_groupby = ', '.join(list(project_managers_name))

    def _compute_trigger_groupby(self): # HACK_group_by
        self.group_by_trigger = 1
        self._get_project_managers()

    # --------------------------- < HACK_group_by > --------------------------- #
    # Odoo does not support Group by related m2o fields and by m2m fields or related m2m fields
    # This simple hack uses instead Char type computed field, collecting name of the related fields and
    # smash them together into a unique string. In same cases, it may be pretty ugly (where many related fields withb many
    # name are. That's why we first convert the name into a set, in order to remove at least the duplicates.
    # NOTE: very important is the '_compute_trigger_groupby' function which is trigger by the field, which can by of any
    # type really but an Integer was choose as representitive of a True Value. It must be present in the View (Tree, kanban etc..)
    # What it does is computing every time, as then triggers the real group by funcitin. That's because, the group by
    # fields need to be stored, but if not trigger of the depends function are called, as well as older records, the depends
    # function won't be called.



    # ==================================================================================== #
    # ------------------------------------- < MODEL > ------------------------------------ #
    # ==================================================================================== #

    @api.model
    @api.returns('self', lambda value: value.id)
    def create_new_checklist(self, partner_id, *args, **kwargs):
        """Create a Checklist
        it will check all partner_id childs and partner_id projects and creates them
        if project_id in kwargs will also add that project
        @partner_id: Partner should be a company or the highest contact Rank, means that parent_id is
        none.
        """
        if not partner_id:
            raise UserError(_("Customer Contact is required when creating a Check List but it was not provided."))
        project_id = kwargs.get('project_id', None)

        checklist_template = self.env.ref('extra_features_gruposgp.project_checklist_list_template')
        if not checklist_template:
            raise UserError(_(f'Checklist Template not found'))

        check_list_id = checklist_template.copy()
        lines = checklist_template.mapped('check_list_line').mapped(lambda l: l.copy())

        name = f'{self.env.ref("extra_features_gruposgp.project_checklist_list__seq").next_by_id()}/'
        partner_name = partner_id.display_name.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace(' ', '_').strip()
        name += partner_name
        vals = {
            "name": name,
            "partner_id": partner_id.id,
            "active": True,
            "check_list_line": [(4, line) for line in lines.ids],
            "is_template": False,
        }
        # Add all the existing project to the Checklist
        partners = partner_id.child_ids
        all_partners = partners | partner_id
        projects = self.env['project.project'].search([('partner_id', 'in', all_partners.ids)])

        if project_id:
            projects |= project_id
        project_ids_vals = [(4, pr.id) for pr in projects]
        if project_ids_vals:
            vals.update({'project_id': project_ids_vals })
        check_list_id.write(vals)
        return check_list_id

    @api.model
    @api.returns('self',
        upgrade=lambda self, value, args, offset=0, limit=None, order=None, count=False: value if count else self.browse(value),
        downgrade=lambda self, value, args, offset=0, limit=None, order=None, count=False: value if count else value.ids)
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """ search(args[, offset=0][, limit=None][, order=None][, count=False])

        Searches for records based on the ``args``
        :ref:`search domain <reference/orm/domains>`.

        :param args: :ref:`A search domain <reference/orm/domains>`. Use an empty
                     list to match all records.
        :param int offset: number of results to ignore (default: none)
        :param int limit: maximum number of records to return (default: all)
        :param str order: sort string
        :param bool count: if True, only counts and returns the number of matching records (default: False)
        :returns: at most ``limit`` records matching the search criteria

        :raise AccessError: * if user tries to bypass access rules for read on the requested object.
        """
        datetime_len = 8
        datetime_len_final = 10
        for domain in args:
            if domain[0] == 'check_list_line.document_date':
                value = domain[-1]
                if len(value) != datetime_len:
                    raise UserError(_(f"Wrong value entered {value} | expected value like : 10092021 which if for date 10/09/2021 day/month/year"))
                day = ''
                month = ''
                year = ''
                f = 0
                for idx, v in enumerate(value):
                    print(idx, v)
                    if idx % 2 != 0 and idx < 4:
                        if f == 0:
                            day += v
                            f += 1
                        elif f == 1:
                            month += v
                            f += 1
                        else:
                            year += v

                    else:
                        if f == 0:
                            day += v
                        elif f == 1:
                            month += v
                        else:
                            year += v
                final_value = f'{year}-{month}-{day}'
                try:
                    datetime.strptime(final_value, DEFAULT_SERVER_DATE_FORMAT)
                except ValueError as err:
                    print(err)
                    UserError(
                        _(f"Wrong value entered {value} |expected value like : 10092021 which if for date 10/09/2021 day/month/year"))
                else:
                    if final_value and len(final_value) == datetime_len_final:
                        domain[-1] = final_value
                    else:
                        UserError(
                            _(f"Wrong value entered {value} |expected value like : 10092021 which if for date 10/09/2021 day/month/year"))


        return super().search(args, offset=offset, limit=limit, order=order, count=count)



    # ==================================================================================== #
    # -------------------------------------- < CRUD > ------------------------------------ #
    # ==================================================================================== #
    def name_get(self):
        result = []
        for check_list in self:
            result.append((check_list.id, check_list.name))
        return result

class ProjectCheckListLine(models.Model):
    _name = 'project.checklist.line'
    _description = 'Project Checklist Line'
    _order = 'id'
    _check_company_auto = True

    name = fields.Char(string='Cuestiones a responder por parte de RRHH', required=True, trim=False)
    active = fields.Boolean(default=True)

    check_list_id = fields.Many2one('project.checklist', string='Check List', required=True, ondelete='cascade', index=True)

    answer = fields.Selection([ ('no_answer', ''), ('yes', 'Yes'),('no', 'No'),], default='no_answer')
    document_date = fields.Date()
    comment = fields.Text()
    display_type = fields.Selection([('line_section', "Section"),], default=False, help="Technical field for UX purpose.")

    def name_get(self):
        result = []
        for check_list in self:
            result.append((check_list.id, check_list.name))
        return result