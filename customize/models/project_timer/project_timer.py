# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountAnalyticLine(models.Model):
   _inherit = 'account.analytic.line'

   def start_stop_fast_timesheet(self,count):
        if count == 1:
                return False
        else:
                return True

   def start_fast_timesheet(self , count):
        if count == 1:
                return True
        else:
                return False

class ProjectTask(models.Model):
   _inherit = 'project.task'

   time_count = fields.Float("Time", store=True)
   is_user_working = fields.Boolean("Is User Working")
   task_run = fields.Boolean("Task Run")
   task_pause = fields.Boolean("Task Pause",default=False)
   duration_ids = fields.One2many(
        'project.calculate.duration','production_id',string="Duraction")
   is_started = fields.Boolean("Started" ,default=False)
   chack_if_play = fields.Boolean("Check Play",default=False)

   @api.depends('duration_ids.duration')
   def _compute_duration(self):
        self.time_count = sum(self.duration_ids.mapped('duration'))

   def run_task(self):

        all_task = self.env['project.task'].search([('chack_if_play','=',True),('project_id','=',self.project_id.id)])
        if all_task :
                return {
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'task.start.wiz',
                        'type': 'ir.actions.act_window',
                        'target': 'new',
                        'res_id': False,
                        'name' : 'You have certain running task'
                }
        else:
                self.start_play()

   def start_play(self):
        self.is_started = True
        self.is_user_working = True
        self.task_run = True
        self.task_pause = False
        self.is_started = True
        self.chack_if_play = True
        self.ensure_one()
        timeline = self.env['project.calculate.duration']

        for taskes in self:
                timeline.create({
                        'production_id': taskes.id,
                        'date_start': datetime.now(),
                        'user_id': self.env.user.id
                })

   def unpause_task(self):
        self.is_user_working = True
        self.task_pause = False
        self.is_started = True
        self.chack_if_play = True
        self.ensure_one()
        timeline = self.env['project.calculate.duration']

        for taskes in self:
                timeline.create({
                        'production_id': taskes.id,
                        'date_start': datetime.now(),
                        'user_id': self.env.user.id
                })

   def pause_task(self):
        self.is_user_working = False
        self.task_pause = True
        self.is_started = True
        self.chack_if_play = False
        self.end_previous()
        return True

   def stop_task(self):
        self.end_previous()

        total_duration = self.env["wiz.stop.task"].sudo().get_task_current_timer(self)
        context = {
                'default_time_spent': total_duration
        }
        return {
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'wiz.stop.task',
                        'type': 'ir.actions.act_window',
                        'target': 'new',
                        'res_id': False,
                        'name': 'Description',
                        'context': context
                }

   def end_previous(self, doall=False):
        calculate_obj = self.env['project.calculate.duration']
        domain = [('production_id', 'in', self.ids), ('date_end', '=', False)]
        if not doall:
                domain.append(('user_id', '=', self.env.user.id))

        not_calculate_timelines = calculate_obj.browse()
        for dur in calculate_obj.search(domain, limit=None if doall else 1):
                wo = dur.production_id
                not_calculate_timelines += dur
                dur.write({'date_end': fields.Datetime.now()})
        return True

class project_duration_calculation(models.Model):
   _name = "project.calculate.duration"
   _description = "project duration calculation"

   production_id = fields.Many2one('project.task', string='Manufacturing Order', readonly='True')
   user_id = fields.Many2one(
        'res.users', "User",
        default=lambda self: self.env.uid)
   date_start = fields.Datetime('Start Date', default=fields.Datetime.now, required=True)
   date_end = fields.Datetime('End Date')
   duration = fields.Float('Duration', compute='_compute_duration', store=True)

   @api.depends('date_end', 'date_start')
   def _compute_duration(self):
        for blocktime in self:
                if blocktime.date_end:
                        d1 = fields.Datetime.from_string(blocktime.date_start)
                        d2 = fields.Datetime.from_string(blocktime.date_end)
                        diff = d2 - d1
                        blocktime.duration = round(diff.total_seconds() / 60.0, 2) + 0.01
                else:
                        blocktime.duration = 0.0

class WizardStopTask(models.TransientModel):
   _name = "wiz.stop.task"
   _description = "wizard stop task"

   description = fields.Char("Description",required=True)
   _sql_constraints = [('time_positive', 'CHECK(time_spent > 0.00)', 'The timesheet\'s time must be positive')]
   time_spent = fields.Float('Time', digits=(16, 2), required=True)

   def _get_default_employee_id(self):
        user_id = self.env.user
        return [('user_id_no_limit', '=', user_id.id)]

   employee_id = fields.Many2one("hr.employee", required=True, domain=lambda self: self._get_default_employee_id())
   image_128 = fields.Image(related='employee_id.image_1920')

   def get_task_current_timer(self, task_id):
        total_duration = 0.0
        for pro_task in task_id:
                for lines in pro_task.duration_ids:
                        total_duration += lines.duration / 60
        return total_duration

   def submit_desc(self):
        active_model_id = self.env['project.task']._context.get('active_id')
        task_project = self.env['project.task'].browse(active_model_id)
        task_project.is_user_working = False
        task_project.task_run = False

        total_duration = self.time_spent
        if not total_duration:
                total_duration = self.get_task_current_timer(task_project)
        # if total_duration: original implementation it divides this by 60 ???
        #       total_duration /= 60

        employee_id = self.employee_id
        if not employee_id:
                raise UserError(_("You must select an employee before submit the worksheet hours"))

        task_project.timesheet_ids.create({
                'date' : fields.date.today(),
                'employee_id' : employee_id.id,
                'name' : self.description,
                'task_id' : task_project.id,
                'project_id' : task_project.project_id.id,
                'unit_amount': total_duration,
                })

        task_project.duration_ids.unlink()
        task_project.is_started = False
        task_project.chack_if_play = False

        return True

class TaskStartWiz(models.TransientModel):
   _name = "task.start.wiz"
   _description = "wizard stop task"


   def sub_start(self):
        tasks = self.env['project.task']._context.get('active_id')
        bro_task = self.env['project.task'].browse(tasks)
        count = 0
        all_task_id = self.env['project.task'].search([('chack_if_play','=',True),('project_id','=',bro_task.project_id.id)])

        for i in all_task_id:
                i.is_user_working = False
                i.task_pause = True
                i.is_started = True
                i.chack_if_play = False
                i.end_previous()
                count = 1

        if count == 1:
                bro_task.start_play()

        return {
                        'type': 'ir.actions.client',
                        'tag': 'reload',
                        }