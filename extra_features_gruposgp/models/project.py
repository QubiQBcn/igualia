# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       @Creation Date: 19th May - 2021
#       Odoo Version: 13.0.0

from odoo import api, fields, models, tools, SUPERUSER_ID, _


class ProjectProjectType(models.Model):
    _name = 'project.project.type'
    _description = 'Task Stage'
    _order = 'sequence, id'

    def _get_default_project_ids(self):
        default_project_id = self.env.context.get('default_project_id')
        return [default_project_id] if default_project_id else None

    name = fields.Char(string='Stage Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)
    project_ids = fields.Many2many('project.project', 'project_project_type_rel', 'type_id', 'project_id', string='Projects',
        default=_get_default_project_ids)

    _default_project_type_color = lambda self: self.search_count([]) % 12
    color = fields.Integer(string='Color Index', default=_default_project_type_color)

    fold = fields.Boolean(string='Folded in Kanban',
        help='This stage is folded in the kanban view when there are no records in that stage to display.')

FIELD_TO_UPGRADE = [  # HACK_ACCESS_RIGHTS
    'project_type_ids', 'stage_id',
]

class ProjectExtra(models.Model):
    _name = "project.project"
    _inherit = ["project.project", "mail.activity.mixin"]

    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('processed', 'Yellow'),
        ('done', 'Green'),
        ('blocked', 'Red')], string='Project Kanban State',
        copy=False, default='normal', required=True)


    employee_id_manager = fields.Many2one('hr.employee', tracking=True,
                                 help="Employee Manager of the Project")

    # NOTE: It shold be employee_id_hr was named by mistake but WARN: Do not change the name because will delete all existing record!!!!
    user_id_hr = fields.Many2many(
        comodel_name='hr.employee',
        relation='project_project_hr_employee_project_manager_rel',
        column1='project_id',
        column2='employee_id',
        tracking=True,
        help="Employee Manager of the Project")

    # NOTE: It shold be task_employee_id_hr was named by mistake but WARN: Do not change the name because will delete all existing record!!!!
    task_user_id_hr = fields.Many2many(
        comodel_name='hr.employee',
        relation='project_project_hr_employees_users_hr_rel',
        column1='project_id',
        column2='employee_id',
        help="Employee responsible of the Project",
        tracking=True,
        track_visibility='always')

    # ==================================== < PROJECT STAGE > =============================== #  FIXME
    legend_normal = fields.Char(
        'Grey Kanban Label', default=lambda s: 'En curso', translate=True, required=True,
        help='Override the default value displayed for the normal state for kanban selection, when the task or issue is in that stage.')
    legend_processed = fields.Char(
        'Blue Kanban Label', default=lambda s: 'Tramitado', translate=True, required=True,
        help='Override the default value displayed for the normal state for kanban selection, when the task or issue is in that stage.')
    legend_done = fields.Char(
        'Green Kanban Label', default=lambda s: 'Finalizado', translate=True, required=True,
        help='Override the default value displayed for the done state for kanban selection, when the task or iss?ue is in that stage.')
    legend_blocked = fields.Char(
        'Red Kanban Label', default=lambda s: 'Cancelado', translate=True, required=True,
        help='Override the default value displayed for the blocked state for kanban selection, when the task or issue is in that stage.')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        search_domain = [('id', 'in', stages.ids)]
        if self:
            search_domain = ['|', ('project_ids', '=', self.id)] + search_domain
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

    project_type_ids = fields.Many2many('project.project.type', 'project_project_type_rel', 'project_id', 'type_id',
                                string='Project Stages', groups='project.group_project_user')
    stage_id = fields.Many2one('project.project.type', string='Stage', ondelete='restrict', tracking=True, index=True, group_expand='_read_group_stage_ids',
                               domain="[('project_ids.id', '=', id)]", copy=False)
    stage_color = fields.Integer(related='stage_id.color', string="Stage Color")

    # ----------------------------------------
    # Case management
    # ----------------------------------------

    def stage_find(self, section_id, domain=[], order='sequence'):
        """ Override of the base.stage method
            Parameter of the stage search taken from the lead:
            - section_id: if set, stages must belong to this section or
              be a default stage; if not set, stages must be default
              stages
        """
        # collect all section_ids
        section_ids = []
        if section_id:
            section_ids.append(section_id)
        section_ids.extend(self.ids)
        search_domain = []
        if section_ids:
            search_domain = [('|')] * (len(section_ids) - 1)
            for section_id in section_ids:
                search_domain.append(('project_ids', '=', section_id))
        search_domain += list(domain)
        # perform search, return the first found
        return self.env['project.task.type'].search(search_domain, order=order, limit=1).id

    # ==================================== < PROJECT CHECK LIST REL > =============================== #  FIXME

    check_list_id = fields.Many2one(comodel_name='project.checklist', string="Check List", ondelete='set null')

    # -------------------- sale.order related
    sale_user_id = fields.Many2one(related='sale_order_id.user_id')
    sale_agent_id = fields.Many2one(related='sale_order_id.agent_id')

    @api.depends('kanban_state')
    def _compute_kanban_state_label(self): # Deprecated however keep it here for reference
        for project in self:
            if project.kanban_state == 'normal':
                project.kanban_state_label = project.legend_normal
            elif project.kanban_state == 'processed':
                project.kanban_state_label = project.legend_processed
            elif project.kanban_state == 'blocked':
                project.kanban_state_label = project.legend_blocked
            else:
                project.kanban_state_label = project.legend_done

    def project_stage_quick_form_deliver(self):
        """NOTE: ir.actions.server Server Function
           Gets the Active Id of the Current Project which is been open in the client on Kanban View -> 'Edit Stage'
        """

        target_view = "extra_features_gruposgp.project_task_stage_quick_form_extra_features"
        active_id = self.env.context.get('active_id', None)
        project_active = self.browse(active_id)
        view_id = self.env.ref(target_view, raise_if_not_found=False)
        if active_id and view_id:
            return {
                "type": "ir.actions.act_window",
                "views": [[view_id.id, "form"]],
                "res_model": self._name,
                "view_mode": "form",
                "res_id": project_active and project_active.id or False
            }
    def project_stage_quick_form(self):
        """NOTE: ir.actions.server Server Function
           Gets the Active Id of the Current Project which is been open in the client on Kanban View -> 'Edit Stage'
        """

        target_view = "extra_features_gruposgp.project_project_stage_quick_form_extra_features"
        active_id = self.env.context.get('active_id', None)
        project_active = self.browse(active_id)
        view_id = self.env.ref(target_view, raise_if_not_found=False)
        if active_id and view_id:
            return {
                "type": "ir.actions.act_window",
                "views": [[view_id.id, "form"]],
                "res_model": self._name,
                "view_mode": "form",
                "res_id": project_active and project_active.id or False
            }



    @api.model
    def create(self, vals):
        res = super(ProjectExtra, self).create(vals)
        # ----- Add Checklist of Partner's Company to the project, creates a new checklist if not found
        if 'partner_id' in vals:
            partner_id = self.env['res.partner'].browse(vals['partner_id'])
            self.env['res.partner'].find_partner_checklist_or_create(partner_id, project_id=res)
        return res

    def write(self, vals):
        if 'partner_id' in vals:
            is_deleted = vals.get('partner_id', "NOFALSE")
            if is_deleted is False and self.partner_id: # If the partner is delete , we need to delete the project to the partner's checlist
                self.partner_id.find_partner_checklist_and_delete(project_id=self)
            else:# Switching the Checklist with the new one of the partner
                partner_id = self.env['res.partner'].browse(vals['partner_id'])
                self.env['res.partner'].find_partner_checklist_or_create(partner_id, project_id=self)

        #  HACK_ACCESS_RIGHTS HACK: Use this fields in order to 'upgrade' the user (namely it should be the project.group_project_user so the
        # User of the Project with most minimal entry. THis is because the fields in FIELD_TO_UPGRADE are
        # use by Project user as well however the project.project fileds are readonly for the Project Users.
        # I tried to add 'groups' to the fields however it seems that it doesnt have affect
        # because the fields are already created. And manually add the groups into the fields with a scripts seems
        # overkill (and may cause issue to the DB).
        # Right now, the fields are alredy created since a while in production and a delete and re-create them will cause a data loss.
        # What was supposed to do since the beginning (if it was known that project.group_project_user needed to change
        # the project fields listed in FIELD_TO_UPGRADE as well) was to create a separeate common table or to add groups='project.group_project_user' in
        # this fields (however not sure if this would work neither, hence first solution is the best
        upgrade = False
        for field in vals.keys():
            if field in FIELD_TO_UPGRADE:
                upgrade = True
                break
        if upgrade:
            self = self.sudo()

        res = super(ProjectExtra, self).write(vals)
        if 'project_type_ids' in vals:
            if not self.stage_id:
                stage_id = self.project_type_ids[0]
                if stage_id:
                    self.write({'stage_id': stage_id})
        return res

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('stage_id'):
            default['stage_id'] = self.stage_id.id
        return super(ProjectExtra, self).copy(default)

    # ==================================================================================
    #  -------------------------- < ACTION CLIENT-SIDE >  ------------------------------
    # ==================================================================================

    def project_project_open_project(self, active_id=None):
        self.ensure_one()
        action = {
            'name': _('Project'),
            'view_mode': 'form',
            'res_model': 'project.project',
            'view_id': self.env.ref('project.edit_project').id,
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'current',
            'context': self._context,
        }

        return action

    def _track_subtype(self, init_values):
        self.ensure_one()
        update_task_user = self._context.get('update_task_user', False)

        if update_task_user:
            # m2o
            user_id = self.user_id
            user_id_name = user_id.name and user_id.name or ''
            task_user_id_no_limit = self.task_user_id_no_limit
            task_user_id_no_limit_name = task_user_id_no_limit.name and task_user_id_no_limit.name or ''
            employee_id_manager = self.employee_id_manager
            employee_id_manager_name = employee_id_manager.name and employee_id_manager.name or ''
            #m2m
            user_id_hr = self.user_id_hr
            user_id_hr_names = ', '.join([name for name in user_id_hr.mapped('name')])

            task_user_id_hr = self.task_user_id_hr
            task_user_id_hr_names = ', '.join([name for name in task_user_id_hr.mapped('name')])

            body = f"""
            <div class="alert alert-info" role="alert">
                <p class="text-bold">Project Task users & managers update</p>
                <ul>
                    <li>
                        <span class="text-bold"> Project User: </span> <span class="text-secondary"> {user_id_name} </span>  
                    </li>                    
                    <li>
                        <span class="text-bold"> Task User: </span> <span class="text-secondary"> {task_user_id_no_limit_name} </span>  
                    </li>                    
                    <li>
                        <span class="text-bold"> Manager: </span> <span class="text-secondary"> {employee_id_manager_name} </span>  
                    </li>                    
                    <li>
                        <span class="text-bold"> Project Managers: </span> <span class="text-secondary"> {user_id_hr_names} </span>  
                    </li>                    
                    <li>
                        <span class="text-bold"> Task users: </span> <span class="text-secondary"> {task_user_id_hr_names} </span>  
                    </li>
                </ul>
            </div>
                            """
            self.message_post(body=_(body))
        elif 'employee_id_manager' in init_values:
            return self.env.ref('extra_features_gruposgp.project_update_employee_manager')
        elif 'task_user_id_no_limit' in init_values:
            return self.env.ref('extra_features_gruposgp.project_update_project_task_user')

        # m2m fields : NOte: CUrrently Odoo don't supports "mail.message.subtype" for m2m fields (maybe o2m too)
        elif 'task_user_id_hr' in init_values:
            task_user_id_hr = self.task_user_id_hr
            if task_user_id_hr:
                task_user_id_hr_names = ', '.join([name for name in task_user_id_hr.mapped('name')])
                body = f"""<p class="text-bold">Task employees updated </p>
                <ul>
                    <li>
                    <span class="text-secondary"> {task_user_id_hr_names} </span> 
                    </li>
                </ul>
                """
                self.message_post(body=_(body))
        elif 'user_id_hr' in init_values:
            user_id_hr = self.user_id_hr
            if user_id_hr:
                user_id_hr_names = ', '.join([name for name in user_id_hr.mapped('name')])
                body = f"""
                    <p class="text-bold">Project Managers updated </p>
                    <ul>
                        <li>
                        <span class="text-secondary"> {user_id_hr_names} </span> 
                        </li>
                    </ul>
                """
                self.message_post(body=_(body))
        return super(ProjectExtra, self)._track_subtype(init_values)


class Task(models.Model):
    _inherit = 'project.task'

    project_stage_id = fields.Many2one(related='project_id.stage_id',  string="Project Stage")
    # These project_kanban_states are deprecated
    project_kanban_state = fields.Selection(related='project_id.kanban_state')
    project_legend_normal = fields.Char(related='project_id.legend_normal')
    project_legend_processed = fields.Char(related='project_id.legend_processed')
    project_legend_done = fields.Char(related='project_id.legend_done')
    project_legend_blocked = fields.Char(related='project_id.legend_blocked')

    check_list_id = fields.Many2one(related='project_id.check_list_id')

    check_list_name = fields.Char(related='check_list_id.name')

    # ---------- MAIN INFO PROJECT RE   LATED
    check_list_project_id = fields.One2many(related='check_list_id.project_id', string="Checklist Project")
    check_list_partner_id = fields.Many2one(related='check_list_id.partner_id')
    check_list_company_id = fields.Many2one(related='check_list_id.company_id', string="Checklist Company")
    check_list_title = fields.Many2one(related='check_list_id.title', string="Checklist Title")
    check_list_phone = fields.Char(related='check_list_id.phone', string="Checklist phone")
    check_list_mobile = fields.Char(related='check_list_id.mobile', string="Checklist mobile")
    check_list_street = fields.Char(related='check_list_id.street', string="Checklist street")
    check_list_email = fields.Char(related='check_list_id.email', string="Checklist email")
    check_list_rlt_company = fields.Selection(related='check_list_id.rlt_company')
    check_list_rlt_all_working_place = fields.Selection(related='check_list_id.rlt_all_working_place')

    # ---------- DATOS DE IGUALDAD  Equality Data
    check_list_sale_agent_id = fields.Many2one(related='check_list_id.sale_agent_id')
    check_list_equality_commission = fields.Char(related='check_list_id.equality_commission')
    check_list_working_people_number = fields.Integer(related='check_list_id.working_people_number')
    check_list_work_place = fields.Char(related='check_list_id.work_place')
    check_list_agreement = fields.Char(related='check_list_id.agreement')

    check_list_line = fields.One2many(related='check_list_id.check_list_line', readonly=False)

    # WARN: overwritten just to change the string (label)
    user_id = fields.Many2one('res.users',
                              string='User_id (dont\' used)',
                              default=lambda self: self.env.uid,
                              index=True, tracking=False)

    employee_id_manager = fields.Many2one(related="project_id.employee_id_manager", tracking=True)


    def _track_subtype(self, init_values):
        self.ensure_one()
        # m2m fields : NOte: CUrrently Odoo don't suppports "mail.message.subtype" for m2m fields (maybe o2m too)
        if 'user_id_hr' in init_values:
            user_id_hr = self.user_id_hr
            if user_id_hr:
                user_id_hr_names = ', '.join([name for name in user_id_hr.mapped('name')])
                body = f"""
                    <p class="text-bold">Task employees updated </p>
                    <ul>
                        <li>
                        <span class="text-secondary"> {user_id_hr_names} </span> 
                        </li>
                    </ul>
                """
                self.message_post(body=_(body))

        return super(Task, self)._track_subtype(init_values)

    # ==================================================================================
    #  -------------------------- < ACTION CLIENT-SIDE >  ------------------------------
    # ==================================================================================

    def project_task_open_task(self, active_id=None):
        self.ensure_one()
        action = {
            'name': _('Task'),
            'view_mode': 'form',
            'res_model': 'project.task',
            'view_id': self.env.ref('project.view_task_form2').id,
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'current',
            'context': self._context,
        }

        return action




class ProfitabilityAnalysis(models.Model):
    _inherit = "project.profitability.report"

    # NOTE: It shold be employee_id_hr was named by mistake but WARN: Do not change the name because will delete all existing record!!!!
    user_id_hr = fields.Many2many('hr.employee', string='Project Responsible', readonly=True)
    kanban_state = fields.Char(string='Project State')

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        query = """
            CREATE VIEW %s AS (
                SELECT
                    ROW_NUMBER() OVER (ORDER BY P.id, SOL.id) AS id,
                    P.id AS project_id,
                    P.user_id AS user_id,
                    
                    CASE 
                        WHEN P.kanban_state = 'normal' THEN P.legend_normal 
                        WHEN P.kanban_state = 'processed' THEN P.legend_processed 
                        WHEN P.kanban_state = 'done' THEN P.legend_done 
                        WHEN P.kanban_state = 'blocked' THEN P.legend_blocked 
                    END AS kanban_state,
                    
                    SOL.id AS sale_line_id,
                    P.analytic_account_id AS analytic_account_id,
                    P.partner_id AS partner_id,
                    C.id AS company_id,
                    C.currency_id AS currency_id,
                    S.id AS sale_order_id,
                    S.date_order AS order_confirmation_date,
                    SOL.product_id AS product_id,
                    SOL.qty_delivered_method AS sale_qty_delivered_method,
                    CASE
                       WHEN SOL.qty_delivered_method = 'analytic' THEN (SOL.untaxed_amount_to_invoice / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)
                       ELSE 0.0
                    END AS expense_amount_untaxed_to_invoice,
                    CASE
                       WHEN SOL.qty_delivered_method = 'analytic' AND SOL.invoice_status != 'no'
                       THEN
                            CASE
                                WHEN T.expense_policy = 'sales_price'
                                THEN (SOL.price_reduce / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END) * SOL.qty_invoiced
                                ELSE -COST_SUMMARY.expense_cost
                            END
                       ELSE 0.0
                    END AS expense_amount_untaxed_invoiced,
                    CASE
                       WHEN SOL.qty_delivered_method IN ('timesheet', 'manual', 'stock_move') THEN (SOL.untaxed_amount_to_invoice / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)
                       ELSE 0.0
                    END AS amount_untaxed_to_invoice,
                    CASE
                       WHEN SOL.qty_delivered_method IN ('timesheet', 'manual', 'stock_move') THEN (COALESCE(SOL.untaxed_amount_invoiced, COST_SUMMARY.downpayment_invoiced) / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)
                       ELSE 0.0
                    END AS amount_untaxed_invoiced,
                    COST_SUMMARY.timesheet_unit_amount AS timesheet_unit_amount,
                    COST_SUMMARY.timesheet_cost AS timesheet_cost,
                    COST_SUMMARY.expense_cost AS expense_cost
                FROM project_project P
                    JOIN res_company C ON C.id = P.company_id
                    LEFT JOIN (
                        SELECT
                            project_id,
                            analytic_account_id,
                            sale_line_id,
                            SUM(timesheet_unit_amount) AS timesheet_unit_amount,
                            SUM(timesheet_cost) AS timesheet_cost,
                            SUM(expense_cost) AS expense_cost,
                            SUM(downpayment_invoiced) AS downpayment_invoiced
                        FROM (
                            SELECT
                                P.id AS project_id,
                                P.analytic_account_id AS analytic_account_id,
                                TS.so_line AS sale_line_id,
                                SUM(TS.unit_amount) AS timesheet_unit_amount,
                                SUM(TS.amount) AS timesheet_cost,
                                0.0 AS expense_cost,
                                0.0 AS downpayment_invoiced
                            FROM account_analytic_line TS, project_project P
                            WHERE TS.project_id IS NOT NULL AND P.id = TS.project_id AND P.active = 't' AND P.allow_timesheets = 't'
                            GROUP BY P.id, TS.so_line

                            UNION

                            SELECT
                                P.id AS project_id,
                                P.analytic_account_id AS analytic_account_id,
                                AAL.so_line AS sale_line_id,
                                0.0 AS timesheet_unit_amount,
                                0.0 AS timesheet_cost,
                                CASE
                                  WHEN AAL.product_id != CAST((COALESCE((SELECT value FROM ir_config_parameter WHERE key='sale.default_deposit_product_id'), '-1')) as INT)
                                  THEN (SUM(AAL.amount))
                                  ELSE 0.0
                                END AS expense_cost,
                                0.0 AS downpayment_invoiced
                            FROM project_project P
                                LEFT JOIN account_analytic_account AA ON P.analytic_account_id = AA.id
                                LEFT JOIN account_analytic_line AAL ON AAL.account_id = AA.id
                            WHERE AAL.amount < 0.0 AND AAL.project_id IS NULL AND P.active = 't' AND P.allow_timesheets = 't'
                            GROUP BY P.id, AA.id, AAL.so_line, AAL.product_id

                            UNION

                            SELECT
                                P.id AS project_id,
                                P.analytic_account_id AS analytic_account_id,
                                MY_SOLS.id AS sale_line_id,
                                0.0 AS timesheet_unit_amount,
                                0.0 AS timesheet_cost,
                                0.0 AS expense_cost,
                                CASE WHEN MY_SOLS.invoice_status = 'invoiced' THEN MY_SOLS.price_reduce ELSE 0.0 END AS downpayment_invoiced
                            FROM project_project P
                                LEFT JOIN sale_order_line MY_SOL ON P.sale_line_id = MY_SOL.id
                                LEFT JOIN sale_order MY_S ON MY_SOL.order_id = MY_S.id
                                LEFT JOIN sale_order_line MY_SOLS ON MY_SOLS.order_id = MY_S.id
                            WHERE MY_SOLS.is_downpayment = 't'
                            GROUP BY P.id, MY_SOLS.id

                            UNION

                            SELECT
                                P.id AS project_id,
                                P.analytic_account_id AS analytic_account_id,
                                OLIS.id AS sale_line_id,
                                0.0 AS timesheet_unit_amount,
                                0.0 AS timesheet_cost,
                                OLIS.price_reduce AS expense_cost,
                                0.0 AS downpayment_invoiced
                            FROM project_project P
                                LEFT JOIN account_analytic_account ANAC ON P.analytic_account_id = ANAC.id
                                LEFT JOIN account_analytic_line ANLI ON ANAC.id = ANLI.account_id
                                LEFT JOIN sale_order_line OLI ON P.sale_line_id = OLI.id
                                LEFT JOIN sale_order ORD ON OLI.order_id = ORD.id
                                LEFT JOIN sale_order_line OLIS ON ORD.id = OLIS.order_id
                            WHERE OLIS.product_id = ANLI.product_id AND OLIS.is_downpayment = 't' AND ANLI.amount < 0.0 AND ANLI.project_id IS NULL AND P.active = 't' AND P.allow_timesheets = 't'
                            GROUP BY P.id, OLIS.id

                            UNION

                            SELECT
                                P.id AS project_id,
                                P.analytic_account_id AS analytic_account_id,
                                SOL.id AS sale_line_id,
                                0.0 AS timesheet_unit_amount,
                                0.0 AS timesheet_cost,
                                0.0 AS expense_cost,
                                0.0 AS downpayment_invoiced
                            FROM sale_order_line SOL
                                INNER JOIN project_project P ON SOL.project_id = P.id
                            WHERE P.active = 't' AND P.allow_timesheets = 't'

                            UNION

                            SELECT
                                P.id AS project_id,
                                P.analytic_account_id AS analytic_account_id,
                                SOL.id AS sale_line_id,
                                0.0 AS timesheet_unit_amount,
                                0.0 AS timesheet_cost,
                                0.0 AS expense_cost,
                                0.0 AS downpayment_invoiced
                            FROM sale_order_line SOL
                                INNER JOIN project_task T ON SOL.task_id = T.id
                                INNER JOIN project_project P ON P.id = T.project_id
                            WHERE P.active = 't' AND P.allow_timesheets = 't'
                        ) SUB_COST_SUMMARY
                        GROUP BY project_id, analytic_account_id, sale_line_id
                    ) COST_SUMMARY ON COST_SUMMARY.project_id = P.id
                    LEFT JOIN sale_order_line SOL ON COST_SUMMARY.sale_line_id = SOL.id
                    LEFT JOIN sale_order S ON SOL.order_id = S.id
                    LEFT JOIN product_product PP on (SOL.product_id=PP.id)
                    LEFT JOIN product_template T on (PP.product_tmpl_id=T.id)
                    WHERE P.active = 't' AND P.analytic_account_id IS NOT NULL
            )
        """ % self._table
        self._cr.execute(query)

        # query = """
        #           CREATE VIEW %s AS (
        #               SELECT
        #                   ROW_NUMBER() OVER (ORDER BY P.id, SOL.id) AS id,
        #                   P.id AS project_id,
        #                   P.user_id AS user_id,
        #
        #                   P.user_id_hr as user_id_hr,
        #                   CASE
        #                       WHEN P.kanban_state = 'normal' THEN P.legend_normal
        #                       WHEN P.kanban_state = 'processed' THEN P.legend_processed
        #                       WHEN P.kanban_state = 'done' THEN P.legend_done
        #                       WHEN P.kanban_state = 'blocked' THEN P.legend_blocked
        #                   END AS kanban_state,
        #
        #                   SOL.id AS sale_line_id,
        #                   P.analytic_account_id AS analytic_account_id,
        #                   P.partner_id AS partner_id,
        #                   C.id AS company_id,
        #                   C.currency_id AS currency_id,
        #                   S.id AS sale_order_id,
        #                   S.date_order AS order_confirmation_date,
        #                   SOL.product_id AS product_id,
        #                   SOL.qty_delivered_method AS sale_qty_delivered_method,
        #                   CASE
        #                      WHEN SOL.qty_delivered_method = 'analytic' THEN (SOL.untaxed_amount_to_invoice / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)
        #                      ELSE 0.0
        #                   END AS expense_amount_untaxed_to_invoice,
        #                   CASE
        #                      WHEN SOL.qty_delivered_method = 'analytic' AND SOL.invoice_status != 'no'
        #                      THEN
        #                           CASE
        #                               WHEN T.expense_policy = 'sales_price'
        #                               THEN (SOL.price_reduce / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END) * SOL.qty_invoiced
        #                               ELSE -COST_SUMMARY.expense_cost
        #                           END
        #                      ELSE 0.0
        #                   END AS expense_amount_untaxed_invoiced,
        #                   CASE
        #                      WHEN SOL.qty_delivered_method IN ('timesheet', 'manual', 'stock_move') THEN (SOL.untaxed_amount_to_invoice / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)
        #                      ELSE 0.0
        #                   END AS amount_untaxed_to_invoice,
        #                   CASE
        #                      WHEN SOL.qty_delivered_method IN ('timesheet', 'manual', 'stock_move') THEN (COALESCE(SOL.untaxed_amount_invoiced, COST_SUMMARY.downpayment_invoiced) / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)
        #                      ELSE 0.0
        #                   END AS amount_untaxed_invoiced,
        #                   COST_SUMMARY.timesheet_unit_amount AS timesheet_unit_amount,
        #                   COST_SUMMARY.timesheet_cost AS timesheet_cost,
        #                   COST_SUMMARY.expense_cost AS expense_cost
        #               FROM project_project P
        #                   JOIN res_company C ON C.id = P.company_id
        #                   LEFT JOIN (
        #                       SELECT
        #                           project_id,
        #                           analytic_account_id,
        #                           sale_line_id,
        #                           SUM(timesheet_unit_amount) AS timesheet_unit_amount,
        #                           SUM(timesheet_cost) AS timesheet_cost,
        #                           SUM(expense_cost) AS expense_cost,
        #                           SUM(downpayment_invoiced) AS downpayment_invoiced
        #                       FROM (
        #                           SELECT
        #                               P.id AS project_id,
        #                               P.analytic_account_id AS analytic_account_id,
        #                               TS.so_line AS sale_line_id,
        #                               SUM(TS.unit_amount) AS timesheet_unit_amount,
        #                               SUM(TS.amount) AS timesheet_cost,
        #                               0.0 AS expense_cost,
        #                               0.0 AS downpayment_invoiced
        #                           FROM account_analytic_line TS, project_project P
        #                           WHERE TS.project_id IS NOT NULL AND P.id = TS.project_id AND P.active = 't' AND P.allow_timesheets = 't'
        #                           GROUP BY P.id, TS.so_line
        #
        #                           UNION
        #
        #                           SELECT
        #                               P.id AS project_id,
        #                               P.analytic_account_id AS analytic_account_id,
        #                               AAL.so_line AS sale_line_id,
        #                               0.0 AS timesheet_unit_amount,
        #                               0.0 AS timesheet_cost,
        #                               CASE
        #                                 WHEN AAL.product_id != CAST((COALESCE((SELECT value FROM ir_config_parameter WHERE key='sale.default_deposit_product_id'), '-1')) as INT)
        #                                 THEN (SUM(AAL.amount))
        #                                 ELSE 0.0
        #                               END AS expense_cost,
        #                               0.0 AS downpayment_invoiced
        #                           FROM project_project P
        #                               LEFT JOIN account_analytic_account AA ON P.analytic_account_id = AA.id
        #                               LEFT JOIN account_analytic_line AAL ON AAL.account_id = AA.id
        #                           WHERE AAL.amount < 0.0 AND AAL.project_id IS NULL AND P.active = 't' AND P.allow_timesheets = 't'
        #                           GROUP BY P.id, AA.id, AAL.so_line, AAL.product_id
        #
        #                           UNION
        #
        #                           SELECT
        #                               P.id AS project_id,
        #                               P.analytic_account_id AS analytic_account_id,
        #                               MY_SOLS.id AS sale_line_id,
        #                               0.0 AS timesheet_unit_amount,
        #                               0.0 AS timesheet_cost,
        #                               0.0 AS expense_cost,
        #                               CASE WHEN MY_SOLS.invoice_status = 'invoiced' THEN MY_SOLS.price_reduce ELSE 0.0 END AS downpayment_invoiced
        #                           FROM project_project P
        #                               LEFT JOIN sale_order_line MY_SOL ON P.sale_line_id = MY_SOL.id
        #                               LEFT JOIN sale_order MY_S ON MY_SOL.order_id = MY_S.id
        #                               LEFT JOIN sale_order_line MY_SOLS ON MY_SOLS.order_id = MY_S.id
        #                           WHERE MY_SOLS.is_downpayment = 't'
        #                           GROUP BY P.id, MY_SOLS.id
        #
        #                           UNION
        #
        #                           SELECT
        #                               P.id AS project_id,
        #                               P.analytic_account_id AS analytic_account_id,
        #                               OLIS.id AS sale_line_id,
        #                               0.0 AS timesheet_unit_amount,
        #                               0.0 AS timesheet_cost,
        #                               OLIS.price_reduce AS expense_cost,
        #                               0.0 AS downpayment_invoiced
        #                           FROM project_project P
        #                               LEFT JOIN account_analytic_account ANAC ON P.analytic_account_id = ANAC.id
        #                               LEFT JOIN account_analytic_line ANLI ON ANAC.id = ANLI.account_id
        #                               LEFT JOIN sale_order_line OLI ON P.sale_line_id = OLI.id
        #                               LEFT JOIN sale_order ORD ON OLI.order_id = ORD.id
        #                               LEFT JOIN sale_order_line OLIS ON ORD.id = OLIS.order_id
        #                           WHERE OLIS.product_id = ANLI.product_id AND OLIS.is_downpayment = 't' AND ANLI.amount < 0.0 AND ANLI.project_id IS NULL AND P.active = 't' AND P.allow_timesheets = 't'
        #                           GROUP BY P.id, OLIS.id
        #
        #                           UNION
        #
        #                           SELECT
        #                               P.id AS project_id,
        #                               P.analytic_account_id AS analytic_account_id,
        #                               SOL.id AS sale_line_id,
        #                               0.0 AS timesheet_unit_amount,
        #                               0.0 AS timesheet_cost,
        #                               0.0 AS expense_cost,
        #                               0.0 AS downpayment_invoiced
        #                           FROM sale_order_line SOL
        #                               INNER JOIN project_project P ON SOL.project_id = P.id
        #                           WHERE P.active = 't' AND P.allow_timesheets = 't'
        #
        #                           UNION
        #
        #                           SELECT
        #                               P.id AS project_id,
        #                               P.analytic_account_id AS analytic_account_id,
        #                               SOL.id AS sale_line_id,
        #                               0.0 AS timesheet_unit_amount,
        #                               0.0 AS timesheet_cost,
        #                               0.0 AS expense_cost,
        #                               0.0 AS downpayment_invoiced
        #                           FROM sale_order_line SOL
        #                               INNER JOIN project_task T ON SOL.task_id = T.id
        #                               INNER JOIN project_project P ON P.id = T.project_id
        #                           WHERE P.active = 't' AND P.allow_timesheets = 't'
        #                       ) SUB_COST_SUMMARY
        #                       GROUP BY project_id, analytic_account_id, sale_line_id
        #                   ) COST_SUMMARY ON COST_SUMMARY.project_id = P.id
        #                   LEFT JOIN sale_order_line SOL ON COST_SUMMARY.sale_line_id = SOL.id
        #                   LEFT JOIN sale_order S ON SOL.order_id = S.id
        #                   LEFT JOIN product_product PP on (SOL.product_id=PP.id)
        #                   LEFT JOIN product_template T on (PP.product_tmpl_id=T.id)
        #                   WHERE P.active = 't' AND P.analytic_account_id IS NOT NULL
        #           )
        #       """ % self._table