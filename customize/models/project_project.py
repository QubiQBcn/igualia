# -*- encoding: utf-8 -*-
from odoo import models, api, fields, _

PROJECT_TYPE_CATEGORY_SELECTION = [
    ('plan_de_igualdad', 'PLAN DE IGUALDAD'),
    ('plan_no_registradomedidas_de_igualdad', 'Plan (No Registrado)/Medidas de Igualdad'),
    ('seguimiento_igualdad_ci', 'SEGUIMIENTO IGUALDAD CI'),
    ('registro_de_plan_en_regcon', 'Registro de Plan en REGCON'),
    ('registro_retributivo', 'Registro Retributivo'),
    ('auditoria_retributiva_vpt_informe', 'Auditoria Retributiva (VPT+ INFORME)'),
    ('investigacion_y_analisis_acoso_sexual_laboral', 'Investigación y Análisis ACOSO Sexual /Laboral'),

    ('general_servicios', 'GENERAL SERVICIOS'),
    ('protocolo_acoso_sexual_labora', 'PROTOCOLO ACOSO SEXUAL /LABORA'),
    ('gestion_denuncias_acoso', 'GESTION DENUNCIAS ACOSO'),
    ('medidas_prevencion_acoso_sexual', 'MEDIDAS PREVENCION ACOSO SEXUAL'),
    ('plan_no_discriminacion_lgtbi', 'PLAN NO DISCRIMINACION LGTBI'),
]
# const variables, keep here for reference or updates
PROJECT_TYPE_LIST_ROOT_VIEW = 'customize.' + 'customize_project_type_category__'
PROJECT_TASK_TYPE_LIST_ROOT_VIEW = 'customize.' + 'customize_project_task_type_category__'

# Default list view of the project.project
PROJECT_DEFAULT_LIST_VIEW = 'project.view_project'
PROJECT_TASK_DEFAULT_LIST_VIEW = 'project.view_task_tree2'
DEFAULT_TAB_NAME = 'Tod@s'
# List of list view defined in /customize/views/project_category/project_type_category_views.xml
PROJECT_CATEGORY_LIST_VIEWS = (
    'customize.customize_project_type_category__plan_de_igualdad',
    'customize.customize_project_type_category__plan_no_registradomedidas_de_igualdad',
    'customize.customize_project_type_category__seguimiento_igualdad_ci',
    'customize.customize_project_type_category__registro_de_plan_en_regcon',
    'customize.customize_project_type_category__registro_retributivo',
    'customize.customize_project_type_category__auditoria_retributiva_vpt_informe',
    'customize.customize_project_type_category__investigacion_y_analisis_acoso_sexual_laboral',

    'customize.customize_project_type_category__general_servicios',
    'customize.customize_project_type_category__protocolo_acoso_sexual_labora',
    'customize.customize_project_type_category__gestion_denuncias_acoso',
    'customize.customize_project_type_category__medidas_prevencion_acoso_sexual',
    'customize.customize_project_type_category__plan_no_discriminacion_lgtbi',
)

PROJECT_TYPE_CATEGORY_MAPPINGS = {
    'plan_de_igualdad':
        {
            'name': '1) PLAN DE IGUALDAD',
            'view': 'customize.customize_project_type_category__plan_de_igualdad',
            'project_type_category': 'plan_de_igualdad',
        },
    'plan_no_registradomedidas_de_igualdad':
        {
            'name': '2) Plan (No Registrado)/Medidas de Igualdad',
            'view': 'customize.customize_project_type_category__plan_no_registradomedidas_de_igualdad',
            'project_type_category': 'plan_no_registradomedidas_de_igualdad',
        },
    'seguimiento_igualdad_ci':
        {
            'name': '3) SEGUIMIENTO IGUALDAD CI',
            'view': 'customize.customize_project_type_category__seguimiento_igualdad_ci',
            'project_type_category': 'seguimiento_igualdad_ci',
        },
    'registro_de_plan_en_regcon':
        {
            'name': '4) Registro de Plan en REGCON',
            'view': 'customize.customize_project_type_category__registro_de_plan_en_regcon',
            'project_type_category': 'registro_de_plan_en_regcon',
        },
    'registro_retributivo':
        {
            'name': '5) Registro Retributivo',
            'view': 'customize.customize_project_type_category__registro_retributivo',
            'project_type_category': 'registro_retributivo',
        },
    'auditoria_retributiva_vpt_informe':
        {
            'name': '6) Auditoria Retributiva (VPT+ INFORME)',
            'view': 'customize.customize_project_type_category__auditoria_retributiva_vpt_informe',
            'project_type_category': 'auditoria_retributiva_vpt_informe',
        },
    'investigacion_y_analisis_acoso_sexual_laboral':
        {
            'name': '7) Investigación y Análisis ACOSO Sexual /Laboral',
            'view': 'customize.customize_project_type_category__investigacion_y_analisis_acoso_sexual_laboral',
            'project_type_category': 'investigacion_y_analisis_acoso_sexual_laboral',
        },

    'general_servicios':
        {
            'name': '8) GENERAL SERVICIOS',
            'view': 'customize.customize_project_type_category__general_servicios',
            'project_type_category': 'general_servicios',
        },

    'protocolo_acoso_sexual_labora':
        {
            'name': '9) PROTOCOLO ACOSO SEXUAL /LABORA',
            'view': 'customize.customize_project_type_category__protocolo_acoso_sexual_labora',
            'project_type_category': 'protocolo_acoso_sexual_labora',
        },
    'gestion_denuncias_acoso':
        {
            'name': '10) GESTION DENUNCIAS ACOSO',
            'view': 'customize.customize_project_type_category__gestion_denuncias_acoso',
            'project_type_category': 'gestion_denuncias_acoso',
        },
    'medidas_prevencion_acoso_sexual':
        {
            'name': '11) MEDIDAS PREVENCION ACOSO SEXUAL',
            'view': 'customize.customize_project_type_category__medidas_prevencion_acoso_sexual',
            'project_type_category': 'medidas_prevencion_acoso_sexual',
        },
    'plan_no_discriminacion_lgtbi':
        {
            'name': '12) PLAN NO DISCRIMINACION LGTBI',
            'view': 'customize.customize_project_type_category__plan_no_discriminacion_lgtbi',
            'project_type_category': 'plan_no_discriminacion_lgtbi',
        },
}

PROJECT_TASK_TYPE_CATEGORY_MAPPINGS = {
    'plan_de_igualdad':
        {
            'name': '1) PLAN DE IGUALDAD',
            'view': 'customize.customize_project_task_type_category__plan_de_igualdad',
            'project_type_category': 'plan_de_igualdad',
        },
    'plan_no_registradomedidas_de_igualdad':
        {
            'name': '2) Plan (No Registrado)/Medidas de Igualdad',
            'view': 'customize.customize_project_task_type_category__plan_no_registradomedidas_de_igualdad',
            'project_type_category': 'plan_no_registradomedidas_de_igualdad',
        },
    'seguimiento_igualdad_ci':
        {
            'name': '3) SEGUIMIENTO IGUALDAD CI',
            'view': 'customize.customize_project_task_type_category__seguimiento_igualdad_ci',
            'project_type_category': 'seguimiento_igualdad_ci',
        },
    'registro_de_plan_en_regcon':
        {
            'name': '4) Registro de Plan en REGCON',
            'view': 'customize.customize_project_task_type_category__registro_de_plan_en_regcon',
            'project_type_category': 'registro_de_plan_en_regcon',
        },
    'registro_retributivo':
        {
            'name': '5) Registro Retributivo',
            'view': 'customize.customize_project_task_type_category__registro_retributivo',
            'project_type_category': 'registro_retributivo',
        },
    'auditoria_retributiva_vpt_informe':
        {
            'name': '6) Auditoria Retributiva (VPT+ INFORME)',
            'view': 'customize.customize_project_task_type_category__auditoria_retributiva_vpt_informe',
            'project_type_category': 'auditoria_retributiva_vpt_informe',
        },
    'investigacion_y_analisis_acoso_sexual_laboral':
        {
            'name': '7) Investigación y Análisis ACOSO Sexual /Laboral',
            'view': 'customize.customize_project_task_type_category__investigacion_y_analisis_acoso_sexual_laboral',
            'project_type_category': 'investigacion_y_analisis_acoso_sexual_laboral',
        },

    'general_servicios':
        {
            'name': '8) GENERAL SERVICIOS',
            'view': 'customize.customize_project_task_type_category__general_servicios',
            'project_type_category': 'general_servicios',
        },

    'protocolo_acoso_sexual_labora':
        {
            'name': '9) PROTOCOLO ACOSO SEXUAL /LABORA',
            'view': 'customize.customize_project_task_type_category__protocolo_acoso_sexual_labora',
            'project_type_category': 'protocolo_acoso_sexual_labora',
        },
    'gestion_denuncias_acoso':
        {
            'name': '10) GESTION DENUNCIAS ACOSO',
            'view': 'customize.customize_project_task_type_category__gestion_denuncias_acoso',
            'project_type_category': 'gestion_denuncias_acoso',
        },
    'medidas_prevencion_acoso_sexual':
        {
            'name': '11) MEDIDAS PREVENCION ACOSO SEXUAL',
            'view': 'customize.customize_project_task_type_category__medidas_prevencion_acoso_sexual',
            'project_type_category': 'medidas_prevencion_acoso_sexual',
        },
    'plan_no_discriminacion_lgtbi':
        {
            'name': '12) PLAN NO DISCRIMINACION LGTBI',
            'view': 'customize.customize_project_task_type_category__plan_no_discriminacion_lgtbi',
            'project_type_category': 'plan_no_discriminacion_lgtbi',
        },
}

#  HACK: Use this fields in order to 'upgrade' the user (namely it should be the project.group_project_user so the
# User of the Project with most minimal entry. THis is because the fields in PROJECT_CATEGORY_FIELDS are
# exposed in the project.task. I tried to add 'groups' to the fields however it seems that it doesnt have affect
# because the fields are already created. And manually add the groups into the fields with a scripts seems
# overkill (and may cause issue to the DB).
# Right now, the fields are alredy created since a while in production and a delete and re-create them will cause a data loss.
# What was supposed to do since the beginning (if it was known that project.group_project_user needed to change
# the project fields listed in PROJECT_CATEGORY_FIELDS as well) was to create a separeate common table or to add groups='project.group_project_user' in
# this fields (however not sure if this would work neither, hence first solution is the best
PROJECT_CATEGORY_FIELDS = (
    'project_type_category',

    'one__solicitud_de_datos_alta_plataforma',
    'one__recepcion_de_datos_cuanti_cuali',
    'one__1_revision_datos',
    'one__2_revision_datos',
    'one__prevision_de_entrega',
    'one__real_de_entrega',
    'one_s_o_n_de_modificaciones',
    'one__final_de_entrega',
    'one_reunion_presentacion_plan_a_empresa',
    'one_reunion_constitucion_comision_nego',
    'one_anotaciones',
    'one_acta',
    'one__1_reunion_cn',
    'one__2_reunion_cn',
    'one__3_reunion_cn',
    'one__4_reunion',
    'one_notificacion_al_client',
    'one__diagnostico_firmado',
    'one__plan_firmado',


    'two__solicitud_de_datos_alta_plataforma',
    'two__recepcion_de_datos_cuanti_cuali',
    'two__1_revision_datos',
    'two__2_revision_datos',
    'two__prevision_de_entrega',
    'two__real_de_entrega',
    'two_n_de_modificaciones',
    'two__final_de_entrega',
    'two_reunion_presentacion_plan_a_la_empresa',
    'two__diagnostico_firmado',
    'two__plan_firmado',

    'year_first__trimestral',
    'year_first_first_reunion',
    'year_first_second_reunion',
    'year_first_third_reunion',
    'year_first_fourth_reunion',
    'year_first_actas',

    'year_second__trimestral',
    'year_second_first_reunion',
    'year_second_second_reunion',
    'year_second_third_reunion',
    'year_second_fourth_reunion',
    'year_second_actas',

    'year_third__trimestral',
    'year_third_first_reunion',
    'year_third_second_reunion',
    'year_third_third_reunion',
    'year_third_fourth_reunion',
    'year_third_actas',

    'year_fourth__trimestral',
    'year_fourth_first_reunion',
    'year_fourth_second_reunion',
    'year_fourth_third_reunion',
    'year_fourth_fourth_reunion',
    'year_fourth_actas',

    'four__recepcion_de_documentacion_completa',
    'four__presentacion_registro',
    'four_acuse_de_recibo',
    'four__notificacion_1er_requerimiento',
    'four_contestacion_1er_requerimiento',
    'four_notificaciones_1er',
    'four__notificacion_2er_requerimiento',
    'four_contestacion_2er_requerimiento',
    'four_notificaciones_2er',
    'four__inscripcion_plan_a_registro',
    'four__notificacion_3er_requerimiento',
    'four_contestacion_3er_requerimiento',
    'four_notificacion_3rd',
    'four__notificacion_4er_requerimiento',
    'four_contestacion_4er_requerimiento',
    'four__archivo_o_desestimiento',

    'five__solicitud_de_datos',
    'five__recepcion_de_datos',
    'five_revision',
    'five__prevision_de_entrega_mensaje',
    'five__real_de_entrega',
    'five_n_de_modificaciones',
    'five__final_de_entrega',

    'six__solicitud_de_datosalta_plataforma',
    'six__recepcion_de_datos',
    'six_n_dpts',
    'six_revision',
    'six__prevision_de_entrega_informe_',
    'six__real_de_entrega_informe',
    'six_n_de_modificaciones',
    'six__final_de_entrega_informe',

    'seven__recepcion_datos_de_contacto',
    'seven__contacto_persona_denunciante',
    'seven__entrevista_persona_denunciante',
    'seven__contacto_persona_denunciada',
    'seven__entrevista_persona_denunciada',
    'seven_contacto_testigos',
    'seven_entrevista_testigos',
    'seven_envio_informe_final',

    'eight_recepcion_documentacion_datos',
    'eight_revision',
    'eight_entrega_informe',
    'nine_entrega_protocolo_acoso_sexual',
    'nine_entrega_protocolo_acoso_laboral',

    'ten_activacion_canal_denuncias',

    'eleven_inicio_seguimiento',
    'eleven_entrega_de_medidas_de_prevencion',

    'twelve_entrega_protocolo_lgtbi',
    'twelve_entrega_medidas_de_prevencion',
)

class ProjectProject(models.Model):
    _inherit = 'project.project'


    # -------------------- WARN: Deprecated BUT  DO NOT DELETE

    task_user_id = fields.Many2one(
        comodel_name='res.users',
        string='Tasks Responsible_')

    def update_task_user_id(self):
        self.ensure_one()
        self.task_ids.write({'user_id': self.task_user_id.id})

    # -------------------- Added Fields iTundra

    task_user_id_no_limit = fields.Many2one(
        comodel_name='res.users',
        string='Tasks User Responsible', help="The User linked to the Employee responsible of the Task.", tracking=True)

    date_order = fields.Datetime(related='sale_order_id.date_order')

    # =================================== < PROJECT TYPE BY CATEGORIES FIELDS > =================================== #
    #  Mapping Index used in case of fields' label or when fields of one category is the same, hence we add the number
    #  on the begging. it can be in form of (1) or one_ depending on where is added-
    #     (1, 'PLAN DE IGUALDAD'),
    #     (2, 'Plan (No Registrado)/Medidas de Igualdad'),
    #     (3, 'SEGUIMIENTO IGUALDAD CI'),
    #     (4, 'Registro de Plan en REGCON'),
    #     (5, 'Registro Retributivo'),
    #     (6, 'Auditoria Retributiva (VPT+ INFORME)'),
    #     (7, 'Investigación y Análisis ACOSO Sexual /Laboral')

    # Relation with the project.type.project_type_category where some pre-determined data has been created
    # (see /customize/data/project_type_data.xml) and shoud hide/show these fields below depending on this field.
    type_id = fields.Many2one(tracking=True) # note: overwritten field module: project_category
    project_type_category = fields.Selection(related='type_id.project_type_category')

    # ===================
    #  1) PLAN DE IGUALDAD
    # ===================
    #

    one__solicitud_de_datos_alta_plataforma = fields.Date(string='(1) Solicitud de datos/ Alta Plataforma',  tracking=True)
    one__recepcion_de_datos_cuanti_cuali = fields.Date(string='(1) Recepción de datos  Cuanti /Cuali', tracking=True)
    one__1_revision_datos = fields.Date(string='(1) 1ª Revisión Datos', tracking=True)
    one__2_revision_datos = fields.Date(string='(1) 2ª Revisión Datos', tracking=True)
    one__prevision_de_entrega = fields.Date(string='(1) Previsión de entrega', tracking=True)
    one__real_de_entrega = fields.Date(string='(1) Real de entrega', tracking=True)
    one_s_o_n_de_modificaciones = fields.Char(string='(1) Nº de modificaciones', tracking=True)  # Is int? or many dates??
    one__final_de_entrega = fields.Date(string='(1) Final de entrega', tracking=True)
    one_reunion_presentacion_plan_a_empresa = fields.Date(string='(1) Reunión Presentación Plan a empresa', tracking=True)
    one_reunion_constitucion_comision_nego = fields.Date(string='(1) Reunión Constitución Comisión Nego', tracking=True)
    one_anotaciones = fields.Text(string='(1) Anotaciones', tracking=True)
    one_acta = fields.Many2one('ir.attachment',  ondelete='cascade', tracking=True)
    one__1_reunion_cn = fields.Date(string='(1) 1ª reunión CN', tracking=True)
    one__2_reunion_cn = fields.Date(string='(1) 2ª reunión CN', tracking=True)
    one__3_reunion_cn = fields.Date(string='(1) 3ª reunión CN', tracking=True)

    # Dependency Start
    one__4_reunion = fields.Date(string='(1) 4ª reunión – notificación al cliente', tracking=True)
    one_notificacion_al_client = fields.Text(string='(1) Notificación al cliente', tracking=True)
    # **** Dependency End

    one__diagnostico_firmado = fields.Date(string='(1) Diagnóstico Firmado', tracking=True)
    one__plan_firmado = fields.Date(string='(1) Plan Firmado', tracking=True)

    # ===================
    #  Plan (No Registrado)/Medidas de Igualdad
    # ===================

    two__solicitud_de_datos_alta_plataforma = fields.Date(string='(2) Solicitud de datos/ Alta Plataforma', tracking=True)
    two__recepcion_de_datos_cuanti_cuali = fields.Date(string='(2) Recepción de datos Cuanti /Cuali', tracking=True)
    two__1_revision_datos = fields.Date(string='(2) 1ª Revisión Datos', tracking=True)
    two__2_revision_datos = fields.Date(string='(2) 2ª Revisión Datos', tracking=True)
    two__prevision_de_entrega = fields.Date(string='(2) Previsión de entrega', tracking=True)
    two__real_de_entrega = fields.Date(string='(2) Real de entrega', tracking=True)
    two_n_de_modificaciones = fields.Char(string='(2) Nº de modificaciones', tracking=True)
    two__final_de_entrega = fields.Date(string='(2) Final de entrega', tracking=True)
    two_reunion_presentacion_plan_a_la_empresa = fields.Date(string='(2) Reunión Presentación Plan a la Empresa', tracking=True)
    two__diagnostico_firmado = fields.Date(string='(2) Diagnóstico Firmado', tracking=True)
    two__plan_firmado = fields.Date(string='(2) Plan Firmado', tracking=True)

    # ===================
    #  SEGUIMIENTO IGUALDAD CI
    # ===================

    # -- First Year
    year_first__trimestral = fields.Date(tracking=True)
    year_first_first_reunion = fields.Date(tracking=True)
    year_first_second_reunion = fields.Date(tracking=True)
    year_first_third_reunion = fields.Date(tracking=True)
    year_first_fourth_reunion = fields.Date(tracking=True)
    year_first_actas = fields.Many2many('ir.attachment', 'projet_project_first_actas_ir_attachments_rel', 'project_id','attachment_id', tracking=True)

    # -- Second Year
    year_second__trimestral = fields.Date(tracking=True)
    year_second_first_reunion = fields.Date(tracking=True)
    year_second_second_reunion = fields.Date(tracking=True)
    year_second_third_reunion = fields.Date(tracking=True)
    year_second_fourth_reunion = fields.Date(tracking=True)
    year_second_actas = fields.Many2many('ir.attachment', 'projet_project_second_actas_ir_attachments_rel', 'project_id', 'attachment_id', tracking=True)

    # -- Third Year
    year_third__trimestral = fields.Date(tracking=True)
    year_third_first_reunion = fields.Date(tracking=True)
    year_third_second_reunion = fields.Date(tracking=True)
    year_third_third_reunion = fields.Date(tracking=True)
    year_third_fourth_reunion = fields.Date(tracking=True)
    year_third_actas = fields.Many2many('ir.attachment', 'projet_project_third_actas_ir_attachments_rel', 'project_id', 'attachment_id', tracking=True)

    # -- Fourth Year
    year_fourth__trimestral = fields.Date(tracking=True)
    year_fourth_first_reunion = fields.Date(tracking=True)
    year_fourth_second_reunion = fields.Date(tracking=True)
    year_fourth_third_reunion = fields.Date(tracking=True)
    year_fourth_fourth_reunion = fields.Date(tracking=True)
    year_fourth_actas = fields.Many2many('ir.attachment', 'projet_project_fourth_actas_ir_attachments_rel', 'project_id', 'attachment_id', tracking=True)

    # ===================
    #  Registro de Plan en REGCON
    # ===================

    four__recepcion_de_documentacion_completa = fields.Date(string='(4) Recepción de documentación completa', tracking=True)

    # Dependency Start
    four__presentacion_registro = fields.Date(string='(4) Presentación Registro', tracking=True)
    four_acuse_de_recibo = fields.Date(string='(4) Acuse de Recibo', tracking=True)
    # **** Dependency End

    # Dependency Start
    four__notificacion_1er_requerimiento = fields.Date(string='(4) Notificación 1er Requerimiento', tracking=True)
    four_contestacion_1er_requerimiento = fields.Date(string='(4) Contestación 1er Requerimiento', tracking=True)
    four_notificaciones_1er = fields.Many2many('ir.attachment', 'projet_project_4_1_ir_attachments_rel', 'project_id', 'attachment_id', tracking=True)
    # **** Dependency End

    # Dependency Start
    four__notificacion_2er_requerimiento = fields.Date(string='(4)  notificación 2º Requerimiento', tracking=True)
    four_contestacion_2er_requerimiento = fields.Date(string='(4) Contestación 2do Requerimiento', tracking=True)
    four_notificaciones_2er = fields.Many2many('ir.attachment', 'projet_project_4_2_ir_attachments_rel', 'project_id', 'attachment_id', tracking=True)
    # **** Dependency End

    # Dependency Start
    four__inscripcion_plan_a_registro = fields.Date(string='(4) Inscripción Plan a Registro', tracking=True)
    four_notificacion_3rd = fields.Many2one('ir.attachment', ondelete='cascade', tracking=True)

    # 10.37 --> add new fields
    four__notificacion_3er_requerimiento = fields.Date(string='(4)  notificación 3º Requerimiento', tracking=True)
    four_contestacion_3er_requerimiento = fields.Date(string='(4) Contestación 3º Requerimiento', tracking=True)
    # **** Dependency End

    # Dependency Start
    four__notificacion_4er_requerimiento = fields.Date(string='(4)  notificación 4º Requerimiento', tracking=True)
    four_contestacion_4er_requerimiento = fields.Date(string='(4) Contestación 4º Requerimiento', tracking=True)
    # **** Dependency End

    # END 10.37 --> add new fields

    four__archivo_o_desestimiento = fields.Date(string='(4) Archivo o Desestento', tracking=True)

    # ===================
    #   Registro Retributivo
    # ===================

    five__solicitud_de_datos = fields.Date(string='(5) Solicitud de datos', tracking=True)
    five__recepcion_de_datos = fields.Date(string='(5) Recepción de datos', tracking=True)
    five_revision = fields.Date(string='(5) Revisión', tracking=True)
    five__prevision_de_entrega_mensaje = fields.Date(string='(5) Previsión de entrega: Mensaje', tracking=True)
    five__real_de_entrega = fields.Date(string='(5) Real de entrega', tracking=True)
    five_n_de_modificaciones = fields.Char(string='(5) Nº de modificaciones', tracking=True) # Is int? or many dates??
    five__final_de_entrega = fields.Date(string='(5) Final de entrega', tracking=True)

    # ===================
    #  Auditoria Retributiva (VPT+ INFORME)
    # ===================

    six__solicitud_de_datosalta_plataforma = fields.Date(string='(6) Solicitud de datos/Alta Plataforma', tracking=True)
    six__recepcion_de_datos = fields.Date(string='(6) Recepción de datos', tracking=True)
    six_n_dpts = fields.Integer(string='(6) NºDPTS', tracking=True)
    six_revision = fields.Date(string='(6) Revisión ', tracking=True)
    six__prevision_de_entrega_informe_ = fields.Date(string='(6) Previsión de entrega informe ', tracking=True)
    six__real_de_entrega_informe = fields.Date(string='(6) Real de entrega informe', tracking=True)
    six_n_de_modificaciones = fields.Char(string='(6) Nº de modificaciones', tracking=True)
    six__final_de_entrega_informe = fields.Date(string='(6) Final de entrega Informe', tracking=True)

    # ===================
    #  Investigación y Análisis ACOSO Sexual /Laboral
    # ===================

    seven__recepcion_datos_de_contacto = fields.Date(string='(7) Recepción datos de contacto', tracking=True)
    seven__contacto_persona_denunciante = fields.Date(string='(7) Contacto persona denunciante', tracking=True)
    seven__entrevista_persona_denunciante = fields.Date(string='(7) Entrevista persona denunciante', tracking=True)
    seven__contacto_persona_denunciada = fields.Date(string='(7) Contacto persona denunciada', tracking=True)
    seven__entrevista_persona_denunciada = fields.Date(string='(7) Entrevista persona denunciada', tracking=True)
    seven_contacto_testigos = fields.Selection([('yes', 'Yes'), ('no', 'No')], tracking=True)
    seven_entrevista_testigos = fields.Selection([('yes', 'Yes'), ('no', 'No')], tracking=True)
    seven_envio_informe_final = fields.Date(string='(7) Envío informe final', tracking=True)

    # ===================
    #  GENERAL SERVICIOS
    # ===================

    eight_recepcion_documentacion_datos = fields.Date(string='8) Recepción Documentación/Datos ', tracking=True)
    eight_revision = fields.Date(string='8) Revisión ', tracking=True)
    eight_entrega_informe = fields.Date(string='8) Entrega Informe ', tracking=True)

    # ===================
    #  PROTOCOLO ACOSO SEXUAL /LABORAL
    # ===================
    nine_entrega_protocolo_acoso_sexual = fields.Date(string='9) Entrega protocolo acoso sexual', tracking=True)
    nine_entrega_protocolo_acoso_laboral = fields.Date(string='9) Entrega protocolo acoso laboral', tracking=True)

    # ===================
    #  GESTION DENUNCIAS ACOSO
    # ===================
    ten_activacion_canal_denuncias = fields.Date(string='10) Activación canal denuncias ', tracking=True)

    # ===================
    #  MEDIDAS PREVENCION ACOSO SEXUAL
    # ===================
    eleven_inicio_seguimiento = fields.Date(string='11) Inicio Seguimiento', tracking=True)
    eleven_entrega_de_medidas_de_prevencion = fields.Date(string='11) Entrega de medidas de prevención ', tracking=True)

    # ===================
    #  PLAN NO DISCRIMINACION LGTBI
    # ===================
    twelve_entrega_protocolo_lgtbi = fields.Date(string='12) Entrega protocolo LGTBI', tracking=True)
    twelve_entrega_medidas_de_prevencion = fields.Date(string='12) Entrega medidas de prevención', tracking=True)

    # ==================================================================================
    #  -------------------------- < ACTION CLIENT-SIDE >  ------------------------------
    # ==================================================================================

    @api.model
    def js_project_get_type_categ_list(self, *__, **___):
        """Function to meant to be called by Front-end Client. Namely JS method
            in order to map the project categories to the LitMultiTab
        """

        project_tab_views = [{
            'id': self.env.ref(PROJECT_DEFAULT_LIST_VIEW).id,
            'name': DEFAULT_TAB_NAME,
            'is_default_view': True,
            'key': None
        }]
        for category in PROJECT_TYPE_CATEGORY_MAPPINGS:
            mapping = PROJECT_TYPE_CATEGORY_MAPPINGS[category]
            project_type_id = self.env['project.type'].search(
                [('is_company_project_category_type', '=', True), ('project_type_category', '=', mapping['project_type_category'])])
            project_tab_views.append({
                'id': self.env.ref(mapping['view']).id,
                'name': project_type_id.name,
                'is_default_view': False,
                'key': category
            })
        return project_tab_views



    # DEPRECATED: Delete at the next 2 version updates
    # # ------ This field Enables the below in the Project View
    # enable_data = fields.Boolean(help="""Enable this field in order to enabled:
    # Data Sent, Data Reception, Data Reception Quali, Data Reception Quant, Data Forecast, Data Delivered, Plan Delivered""")
    #
    # data_sent = fields.Date()
    # data_reception_quali = fields.Date()
    # data_reception_quant = fields.Date()
    # data_forecast = fields.Date()
    # data_delivered = fields.Date()
    # data_plan_delivered = fields.Date()
    # data_report_delivered = fields.Date()
    #
    # # ------ This field Enables the below in the Project View
    # enable_meetings = fields.Boolean(help="""Enable this field in order to enabled:
    #     First Meeting, Second Meeting, Third Meeting, Fourth Meeting""")
    #
    # first_meeting = fields.Date()
    # second_meeting = fields.Date()
    # third_meeting = fields.Date()
    # fourth_meeting = fields.Date()

    def update_task_responsable(self):  # FIXME Split this into separate function
        """
        This function performs the following:

        1) Finds the Task User ID HR (task_user_id_hr -> hr.employee) relation with its res.users (user_id_no_limit)
        and adds it to the Project Tasks User Responsible (task_user_id_no_limit -> res.users)

        2) Adds to the Project AND task followers:
            * Task User ID (task_user_id_hr -> hr.employee)
            * Task User (user_id_no_limit -> res.users)
            * Project Manager (user_id_hr -> hr.employee)
            * Project User (user_id -> res.users)

        3) Detects whether the Task user has changed (project.task.user_id_hr -> hr.employee ), if so it'll remove
        the previous user from the followers and then changes the user's task (the 'Assigned to	' field in the task)
        """
        self.ensure_one()
        # contextualize self, use for mail.message.subtype and displayin the correct Message
        self = self.with_context(update_task_user=True)
        # Add 'Tasks User Responsible' (or 'Task User in Project Form) to the Project
        # ------- Main Task User ID
        task_user_id_hr = self.get_main_project_user_hr_id()
        if task_user_id_hr:
            task_user_id_hr = self.env['hr.employee'].browse(task_user_id_hr)
        else:
            task_user_id_hr = self.env['hr.employee']  # Just give an empty hr.employee rec
        task_user_id_hr_user_no_limit = task_user_id_hr.user_id_no_limit
        task_user_id_partner = task_user_id_hr_user_no_limit.partner_id
        self.write ({
            'task_user_id_no_limit': task_user_id_hr_user_no_limit and task_user_id_hr_user_no_limit.id or None
        })

        # ------ Additional Task User id
        task_user_id_hr_additional = self.task_user_id_hr - task_user_id_hr
        task_user_id_hr_user_no_limit_additional = task_user_id_hr_additional.mapped('user_id_no_limit')
        task_user_id_partner_additional = task_user_id_hr_user_no_limit_additional.mapped('partner_id')
        task_users_partners_all = task_user_id_partner | task_user_id_partner_additional

        ids_to_add = []
        # ------------------------------- < ADDING FOLLOWERS TO THE PROJECT > ------------------------------- #
        # 1) Task User + Task User ID HR
        if task_users_partners_all:
            ids_to_add.extend(task_users_partners_all.ids)
        # 2) Get the Project Employee Manager
        employee_id_manager = self.employee_id_manager.user_id_no_limit.mapped('partner_id')
        if employee_id_manager:
            ids_to_add.extend(employee_id_manager.ids)
        # 3) Project Managers  (hr.employee)
        project_managers_partners = self.user_id_hr.user_id_no_limit.mapped('partner_id')
        if project_managers_partners:
            ids_to_add.extend(project_managers_partners.ids)
        # 4) Project User  (res.users the default field used by Odoo)
        if self.user_id and self.user_id.partner_id:
            ids_to_add.append(self.user_id.partner_id.id)
        # 5) Adding Followers
        if ids_to_add:
            self.message_subscribe(ids_to_add)

        # ------------------------------- < TASK - UPDATING FOLLOWER > ------------------------------- #
        task_ids = self.task_ids

        current_task_user_id_hr = task_ids.user_id_hr  # Remove Follower if Changed
        current_task_user_partner = current_task_user_id_hr.user_id_no_limit.partner_id
        guard = [current_task_user_id_hr, current_task_user_id_hr.user_id_no_limit, current_task_user_partner]
        did_user_id_hr_changed = all(guard) and current_task_user_id_hr != task_user_id_hr
        if did_user_id_hr_changed:
            for task_id in task_ids:
                task_id.message_unsubscribe(current_task_user_partner.ids)

        # ------ Update Task's employee asignation (Assigned to field)
        task_ids.write ({
            'user_id_hr': [(6, False, self.task_user_id_hr.ids)]
        })
        return True

    @api.model
    def get_main_project_user_hr_id(self):
        """Gives the Project main User
        Where the Main user is considered the first 'task_user_id_hr' added to the Project.
        We need to query Postgres directly skipping the ORM because the ORM will order the records by id
        hence throwing away the logic.
        """
        cr = self.env.cr

        query = f"""
                select emp.employee_id, emp.project_id
                from project_project_hr_employees_users_hr_rel as emp
                left join project_project pp on emp.project_id = pp.id
                where pp.id = {self.id} limit 1
                """
        cr.execute (query)
        main_employee = cr.fetchall()
        if main_employee:
            return main_employee[0][0]



# -------------------- Added iTundra

class Task(models.Model):
    _inherit = 'project.task'

    def write(self, vals):
        #  HACK: Use this fields in order to 'upgrade' the user (namely it should be the project.group_project_user so the
        # User of the Project with most minimal entry. THis is because the fields in PROJECT_CATEGORY_FIELDS are
        # exposed in the project.task. I tried to add 'groups' to the fields however it seems that it doesnt have affect
        # because the fields are already created. And manually add the groups into the fields with a scripts seems
        # overkill (and may cause issue to the DB).
        # Right now, the fields are alredy created since a while in production and a delete and re-create them will cause a data loss.
        # What was supposed to do since the beginning (if it was known that project.group_project_user needed to change
        # the project fields listed in PROJECT_CATEGORY_FIELDS as well) was to create a separeate common table or to add groups='project.group_project_user' in
        # this fields (however not sure if this would work neither, hence first solution is the best
        upgrade = False
        for field in vals.keys():
            if field in PROJECT_CATEGORY_FIELDS:
                upgrade = True
                break
        if upgrade:
            self = self.sudo()
        res = super(Task, self).write(vals)
        return res

    # NOTE: It shold be employee_id_hr was named by mistake but WARN: Do not change the name because will delete all existing record!!!!
    # user_id_hr = fields.Many2one('hr.employee',
    #                           string='Assigned to',
    #                           default=lambda self: self.env.uid,
    #                           index=True, tracking=True)

    user_id_hr = fields.Many2many(
        comodel_name='hr.employee',
        relation='project_task_hr_employees_user_hr_rel',
        column1='task_id',
        column2='employee_id',
        help="Users assigned to the task",
        tracking=True
    )

    # -------------------- sale.order related
    date_order = fields.Datetime(related='project_id.date_order')

    sale_user_id = fields.Many2one(related='project_id.sale_user_id')
    sale_agent_id = fields.Many2one(related='project_id.sale_agent_id')


    # =================================== < PROJECT TYPE BY CATEGORIES FIELDS > =================================== #
    #  Mapping Index used in case of fields' label or when fields of one category is the same, hence we add the number
    #  on the begging. it can be in form of (1) or one_ depending on where is added-
    #     (1, 'PLAN DE IGUALDAD'),
    #     (2, 'Plan (No Registrado)/Medidas de Igualdad'),
    #     (3, 'SEGUIMIENTO IGUALDAD CI'),
    #     (4, 'Registro de Plan en REGCON'),
    #     (5, 'Registro Retributivo'),
    #     (6, 'Auditoria Retributiva (VPT+ INFORME)'),
    #     (7, 'Investigación y Análisis ACOSO Sexual /Laboral')

    # Relation with the project.type.project_type_category where some pre-determined data has been created
    # (see /customize/data/project_type_data.xml) and shoud hide/show these fields below depending on this field.
    project_type_category = fields.Selection(related='project_id.project_type_category')

    # ===================
    #  1) PLAN DE IGUALDAD
    # ===================
    #

    one__solicitud_de_datos_alta_plataforma = fields.Date(related='project_id.one__solicitud_de_datos_alta_plataforma', readonly=False)
    one__recepcion_de_datos_cuanti_cuali = fields.Date(related='project_id.one__recepcion_de_datos_cuanti_cuali', readonly=False)
    one__1_revision_datos = fields.Date(related='project_id.one__1_revision_datos', readonly=False)
    one__2_revision_datos = fields.Date(related='project_id.one__2_revision_datos', readonly=False)
    one__prevision_de_entrega = fields.Date(related='project_id.one__prevision_de_entrega', readonly=False)
    one__real_de_entrega = fields.Date(related='project_id.one__real_de_entrega', readonly=False)
    one_s_o_n_de_modificaciones = fields.Char(related='project_id.one_s_o_n_de_modificaciones', readonly=False)  # Is int? or many dates??
    one__final_de_entrega = fields.Date(related='project_id.one__final_de_entrega', readonly=False)
    one_reunion_presentacion_plan_a_empresa = fields.Date(related='project_id.one_reunion_presentacion_plan_a_empresa', readonly=False)
    one_reunion_constitucion_comision_nego = fields.Date(related='project_id.one_reunion_constitucion_comision_nego', readonly=False)
    one_anotaciones = fields.Text(related='project_id.one_anotaciones', readonly=False)
    one_acta = fields.Many2one(related='project_id.one_acta', readonly=False)
    one__1_reunion_cn = fields.Date(related='project_id.one__1_reunion_cn', readonly=False)
    one__2_reunion_cn = fields.Date(related='project_id.one__2_reunion_cn', readonly=False)
    one__3_reunion_cn = fields.Date(related='project_id.one__3_reunion_cn', readonly=False)

    # Dependency Start
    one__4_reunion = fields.Date(related='project_id.one__4_reunion', readonly=False)
    one_notificacion_al_client = fields.Text(related='project_id.one_notificacion_al_client', readonly=False)
    # **** Dependency End

    one__diagnostico_firmado = fields.Date(related='project_id.one__diagnostico_firmado', readonly=False)
    one__plan_firmado = fields.Date(related='project_id.one__plan_firmado', readonly=False)

    # ===================
    #  Plan (No Registrado)/Medidas de Igualdad
    # ===================

    two__solicitud_de_datos_alta_plataforma = fields.Date(related='project_id.two__solicitud_de_datos_alta_plataforma', readonly=False)
    two__recepcion_de_datos_cuanti_cuali = fields.Date(related='project_id.two__recepcion_de_datos_cuanti_cuali', readonly=False)
    two__1_revision_datos = fields.Date(related='project_id.two__1_revision_datos', readonly=False)
    two__2_revision_datos = fields.Date(related='project_id.two__2_revision_datos', readonly=False)
    two__prevision_de_entrega = fields.Date(related='project_id.two__prevision_de_entrega', readonly=False)
    two__real_de_entrega = fields.Date(related='project_id.two__real_de_entrega', readonly=False)
    two_n_de_modificaciones = fields.Char(related='project_id.two_n_de_modificaciones', readonly=False)
    two__final_de_entrega = fields.Date(related='project_id.two__final_de_entrega', readonly=False)
    two_reunion_presentacion_plan_a_la_empresa = fields.Date(related='project_id.two_reunion_presentacion_plan_a_la_empresa', readonly=False)
    two__diagnostico_firmado = fields.Date(related='project_id.two__diagnostico_firmado', readonly=False)
    two__plan_firmado = fields.Date(related='project_id.two__plan_firmado', readonly=False)

    # ===================
    #  SEGUIMIENTO IGUALDAD CI
    # ===================

    # -- First Year
    year_first__trimestral = fields.Date(related='project_id.year_first__trimestral', readonly=False)
    year_first_first_reunion = fields.Date(related='project_id.year_first_first_reunion', readonly=False)
    year_first_second_reunion = fields.Date(related='project_id.year_first_second_reunion', readonly=False)
    year_first_third_reunion = fields.Date(related='project_id.year_first_third_reunion', readonly=False)
    year_first_fourth_reunion = fields.Date(related='project_id.year_first_fourth_reunion', readonly=False)
    year_first_actas = fields.Many2many(related='project_id.year_first_actas', readonly=False)

    # -- Second Year
    year_second__trimestral = fields.Date(related='project_id.year_second__trimestral', readonly=False)
    year_second_first_reunion = fields.Date(related='project_id.year_second_first_reunion', readonly=False)
    year_second_second_reunion = fields.Date(related='project_id.year_second_second_reunion', readonly=False)
    year_second_third_reunion = fields.Date(related='project_id.year_second_third_reunion', readonly=False)
    year_second_fourth_reunion = fields.Date(related='project_id.year_second_fourth_reunion', readonly=False)
    year_second_actas = fields.Many2many(related='project_id.year_second_actas', readonly=False)

    # -- Third Year
    year_third__trimestral = fields.Date(related='project_id.year_third__trimestral', readonly=False)
    year_third_first_reunion = fields.Date(related='project_id.year_third_first_reunion', readonly=False)
    year_third_second_reunion = fields.Date(related='project_id.year_third_second_reunion', readonly=False)
    year_third_third_reunion = fields.Date(related='project_id.year_third_third_reunion', readonly=False)
    year_third_fourth_reunion = fields.Date(related='project_id.year_third_fourth_reunion', readonly=False)
    year_third_actas = fields.Many2many(related='project_id.year_third_actas', readonly=False)

    # -- Fourth Year
    year_fourth__trimestral = fields.Date(related='project_id.year_fourth__trimestral', readonly=False)
    year_fourth_first_reunion = fields.Date(related='project_id.year_fourth_first_reunion', readonly=False)
    year_fourth_second_reunion = fields.Date(related='project_id.year_fourth_second_reunion', readonly=False)
    year_fourth_third_reunion = fields.Date(related='project_id.year_fourth_third_reunion', readonly=False)
    year_fourth_fourth_reunion = fields.Date(related='project_id.year_fourth_fourth_reunion', readonly=False)
    year_fourth_actas = fields.Many2many(related='project_id.year_fourth_actas', readonly=False)

    # ===================
    #  Registro de Plan en REGCON
    # ===================

    four__recepcion_de_documentacion_completa = fields.Date(related='project_id.four__recepcion_de_documentacion_completa', readonly=False)

    # Dependency Start
    four__presentacion_registro = fields.Date(related='project_id.four__presentacion_registro', readonly=False)
    four_acuse_de_recibo = fields.Date(related='project_id.four_acuse_de_recibo', readonly=False)
    # **** Dependency End

    # Dependency Start
    four__notificacion_1er_requerimiento = fields.Date(related='project_id.four__notificacion_1er_requerimiento', readonly=False)
    four_contestacion_1er_requerimiento = fields.Date(related='project_id.four_contestacion_1er_requerimiento', readonly=False)
    four_notificaciones_1er = fields.Many2many(related='project_id.four_notificaciones_1er', readonly=False)
    # **** Dependency End

    # Dependency Start
    four__notificacion_2er_requerimiento = fields.Date(related='project_id.four__notificacion_2er_requerimiento', readonly=False)
    four_contestacion_2er_requerimiento = fields.Date(related='project_id.four_contestacion_2er_requerimiento', readonly=False)
    four_notificaciones_2er = fields.Many2many(related='project_id.four_notificaciones_2er', readonly=False)
    # **** Dependency End

    # Dependency Start
    four__inscripcion_plan_a_registro = fields.Date(related='project_id.four__inscripcion_plan_a_registro', readonly=False)
    four_notificacion_3rd = fields.Many2one(related='project_id.four_notificacion_3rd', readonly=False)
    # **** Dependency End

    # 10.37 --> add new fields
    four__notificacion_3er_requerimiento = fields.Date(related='project_id.four__notificacion_3er_requerimiento', readonly=False)
    four_contestacion_3er_requerimiento = fields.Date(related='project_id.four_contestacion_3er_requerimiento', readonly=False)
    # **** Dependency End

    # Dependency Start
    four__notificacion_4er_requerimiento = fields.Date(related='project_id.four__notificacion_4er_requerimiento', readonly=False)
    four_contestacion_4er_requerimiento = fields.Date(related='project_id.four_contestacion_4er_requerimiento', readonly=False)
    # **** Dependency End

    # END 10.37 --> add new fields

    four__archivo_o_desestimiento = fields.Date(related='project_id.four__archivo_o_desestimiento', readonly=False)

    # ===================
    #   Registro Retributivo
    # ===================

    five__solicitud_de_datos = fields.Date(related='project_id.five__solicitud_de_datos', readonly=False)
    five__recepcion_de_datos = fields.Date(related='project_id.five__recepcion_de_datos', readonly=False)
    five_revision = fields.Date(related='project_id.five_revision', readonly=False)
    five__prevision_de_entrega_mensaje = fields.Date(related='project_id.five__prevision_de_entrega_mensaje', readonly=False)
    five__real_de_entrega = fields.Date(related='project_id.five__real_de_entrega', readonly=False)
    five_n_de_modificaciones = fields.Char(related='project_id.five_n_de_modificaciones', readonly=False) # Is int? or many dates??
    five__final_de_entrega = fields.Date(related='project_id.five__final_de_entrega', readonly=False)

    # ===================
    #  Auditoria Retributiva (VPT+ INFORME)
    # ===================

    six__solicitud_de_datosalta_plataforma = fields.Date(related='project_id.six__solicitud_de_datosalta_plataforma', readonly=False)
    six__recepcion_de_datos = fields.Date(related='project_id.six__recepcion_de_datos', readonly=False)
    six_n_dpts = fields.Integer(related='project_id.six_n_dpts', readonly=False)
    six_revision = fields.Date(related='project_id.six_revision', readonly=False)
    six__prevision_de_entrega_informe_ = fields.Date(related='project_id.six__prevision_de_entrega_informe_', readonly=False)
    six__real_de_entrega_informe = fields.Date(related='project_id.six__real_de_entrega_informe', readonly=False)
    six_n_de_modificaciones = fields.Char(related='project_id.six_n_de_modificaciones', readonly=False)
    six__final_de_entrega_informe = fields.Date(related='project_id.six__final_de_entrega_informe', readonly=False)

    # ===================
    #  Investigación y Análisis ACOSO Sexual /Laboral
    # ===================

    seven__recepcion_datos_de_contacto = fields.Date(related='project_id.seven__recepcion_datos_de_contacto', readonly=False)
    seven__contacto_persona_denunciante = fields.Date(related='project_id.seven__contacto_persona_denunciante', readonly=False)
    seven__entrevista_persona_denunciante = fields.Date(related='project_id.seven__entrevista_persona_denunciante', readonly=False)
    seven__contacto_persona_denunciada = fields.Date(related='project_id.seven__contacto_persona_denunciada', readonly=False)
    seven__entrevista_persona_denunciada = fields.Date(related='project_id.seven__entrevista_persona_denunciada', readonly=False)
    seven_contacto_testigos = fields.Selection(related='project_id.seven_contacto_testigos', readonly=False)
    seven_entrevista_testigos = fields.Selection(related='project_id.seven_entrevista_testigos', readonly=False)
    seven_envio_informe_final = fields.Date(related='project_id.seven_envio_informe_final', readonly=False)

    # ===================
    #  GENERAL SERVICIOS
    # ===================

    eight_recepcion_documentacion_datos = fields.Date(related='project_id.eight_recepcion_documentacion_datos', readonly=False)
    eight_revision = fields.Date(related='project_id.eight_revision', readonly=False)
    eight_entrega_informe = fields.Date(related='project_id.eight_entrega_informe', readonly=False)

    # ===================
    #  PROTOCOLO ACOSO SEXUAL /LABORAL
    # ===================
    nine_entrega_protocolo_acoso_sexual = fields.Date(related='project_id.nine_entrega_protocolo_acoso_sexual', readonly=False)
    nine_entrega_protocolo_acoso_laboral = fields.Date(related='project_id.nine_entrega_protocolo_acoso_laboral', readonly=False)

    # ===================
    #  GESTION DENUNCIAS ACOSO
    # ===================
    ten_activacion_canal_denuncias = fields.Date(related='project_id.ten_activacion_canal_denuncias', readonly=False)

    # ===================
    #  MEDIDAS PREVENCION ACOSO SEXUAL
    # ===================
    eleven_inicio_seguimiento = fields.Date(related='project_id.eleven_inicio_seguimiento', readonly=False)
    eleven_entrega_de_medidas_de_prevencion = fields.Date(related='project_id.eleven_entrega_de_medidas_de_prevencion', readonly=False)

    # ===================
    #  PLAN NO DISCRIMINACION LGTBI
    # ===================
    twelve_entrega_protocolo_lgtbi = fields.Date(related='project_id.twelve_entrega_protocolo_lgtbi', readonly=False)
    twelve_entrega_medidas_de_prevencion = fields.Date(related='project_id.twelve_entrega_medidas_de_prevencion', readonly=False)


    # DEPRECATED: Delete at the next 2 version updates
    # ------ This field Enables the below in the Project View
    # enable_data = fields.Boolean(related='project_id.enable_data', store=True, readonly=False)
    #
    # data_sent = fields.Date(related='project_id.data_sent', store=True, readonly=False)
    # data_reception_quali = fields.Date(related='project_id.data_reception_quali', store=True, readonly=False)
    # data_reception_quant = fields.Date(related='project_id.data_reception_quant', store=True, readonly=False)
    # data_forecast = fields.Date(related='project_id.data_forecast', store=True, readonly=False)
    # data_delivered = fields.Date(related='project_id.data_delivered', store=True, readonly=False)
    # data_plan_delivered = fields.Date(related='project_id.data_plan_delivered', store=True, readonly=False)
    # data_report_delivered = fields.Date(related='project_id.data_report_delivered', store=True, readonly=False)
    #
    #
    # # ------ This field Enables the below in the Project View
    # enable_meetings = fields.Boolean(related='project_id.enable_meetings', store=True, readonly=False)
    #
    # first_meeting = fields.Date(related='project_id.first_meeting', store=True, readonly=False)
    # second_meeting = fields.Date(related='project_id.second_meeting', store=True, readonly=False)
    # third_meeting = fields.Date(related='project_id.third_meeting', store=True, readonly=False)
    # fourth_meeting = fields.Date(related='project_id.fourth_meeting', store=True, readonly=False)

    # ==================================================================================
    #  -------------------------- < ACTION CLIENT-SIDE >  ------------------------------
    # ==================================================================================

    @api.model
    def js_project_get_type_categ_list(self, *__, **___):
        """Function to meant to be called by Front-end Client. Namely JS method
            in order to map the project categories to the LitMultiTab
        """

        project_tab_views = [{
            'id': self.env.ref(PROJECT_TASK_DEFAULT_LIST_VIEW).id,
            'name': DEFAULT_TAB_NAME,
            'is_default_view': True,
            'key': None
        }]
        for category in PROJECT_TASK_TYPE_CATEGORY_MAPPINGS:
            mapping = PROJECT_TASK_TYPE_CATEGORY_MAPPINGS[category]
            project_type_id = self.env['project.type'].search(
                [('is_company_project_category_type', '=', True),
                 ('project_type_category', '=', mapping['project_type_category'])])
            project_tab_views.append({
                'id': self.env.ref(mapping['view']).id,
                'name': project_type_id.name,
                'is_default_view': False,
                'key': category
            })
        return project_tab_views

# ====================
# Utility
# ====================

PROJECT_TYPE_CATEGORY_LIST = (
    'PLAN DE IGUALDAD',
    'Plan (No Registrado)/Medidas de Igualdad',
    'SEGUIMIENTO IGUALDAD CI',
    'Registro de Plan en REGCON',
    'Registro Retributivo',
    'Auditoria Retributiva (VPT+ INFORME)',
    'Investigación y Análisis ACOSO Sexual /Laboral',
)

PROJECT_TYPE_CATEGORY_LIST_INDEX = [
    (1, 'PLAN DE IGUALDAD'),
    (2, 'Plan (No Registrado)/Medidas de Igualdad'),
    (3, 'SEGUIMIENTO IGUALDAD CI'),
    (4, 'Registro de Plan en REGCON'),
    (5, 'Registro Retributivo'),
    (6, 'Auditoria Retributiva (VPT+ INFORME)'),
    (7, 'Investigación y Análisis ACOSO Sexual /Laboral')
]

plan_de_igualdad_mapped = [
    ('one__solicitud_de_datos_alta_plataforma', ' solicitud de datos/ Alta Plataforma'),
    ('one__recepcion_de_datos_cuanti_cuali', ' recepción de datos  Cuanti /Cuali'),
    ('one__1_revision_datos', ' 1ª Revisión Datos'),
    ('one__2_revision_datos', ' 2ª Revisión Datos'),
    ('one__prevision_de_entrega', ' previsión de entrega'),
    ('one__real_de_entrega', ' real de entrega'),
    ('one_s_o_n_de_modificaciones', 'Nº de modificaciones:'),
    ('one__final_de_entrega', ' final de entrega'),
    ('one_reunion_presentacion_plan_a_empresa', 'Reunión Presentación Plan a empresa'),
    ('one_reunion_constitucion_comision_nego', 'Reunión Constitución Comisión Nego'),
    ('one_anotaciones', 'Anotaciones'),
    ('one_acta', 'ACTA'),
    ('one__1_reunion_cn', ' 1ª reunión CN'),
    ('one__2_reunion_cn', ' 2ª reunión CN'),
    ('one__3_reunion_cn', ' 3ª reunión CN'),

    ('one__4_reunion', ' 4ª reunión – notificación al cliente'),
    ('one_notificacion_al_client', 'Notificación al cliente'),

    ('one__diagnostico_firmado', ' Diagnóstico Firmado'),
    ('one__plan_firmado', ' Plan Firmado')
]

plan_no_registradomedidas_de_igualdad_mapped = [
    ('two__solicitud_de_datos_alta_plataforma', ' solicitud de datos/ Alta Plataforma'),
    ('two__recepcion_de_datos_cuanti_cuali', ' recepción de datos  Cuanti /Cuali'),
    ('two__1_revision_datos', ' 1ª Revisión Datos:'),
    ('two__1_revision_datos', ' 2ª Revisión Datos:'),
    ('two__prevision_de_entrega', ' previsión de entrega'),
    ('two__real_de_entrega', ' real de entrega'),
    ('two_n_de_modificaciones', 'Nº de modificaciones:'),
    ('two__final_de_entrega', ' final de entrega :'),
    ('two_reunion_presentacion_plan_a_la_empresa', 'Reunión Presentación Plan a la Empresa:'),
    ('two__diagnostico_firmado', ' Diagnóstico Firmado:'),
    ('two__plan_firmado', ' Plan Firmado')
]

seguimiento_igualdad = [
    # -- First Year
    ('year_first__trimestral', " TRIMESTRAL"),
    ('year_first_first_reunion', "1º Reunión (1T)"),
    ('year_first_second_reunion', "2ª Reunión(2T)"),
    ('year_first_third_reunion', "3º Reunión (3T)"),
    ('year_first_fourth_reunion', "4º Reunión(4T)"),
    ('year_first_actas', "ACTAS"),
    # -- Second Year
    ('year_second__trimestral', " TRIMESTRAL"),
    ('year_second_first_reunion', "1º Reunión (1T)"),
    ('year_second_second_reunion', "2ª Reunión(2T)"),
    ('year_second_third_reunion', "3º Reunión (3T)"),
    ('year_second_fourth_reunion', "4º Reunión(4T)"),
    ('year_second_actas', "ACTAS"),
    # -- Third Year
    ('year_third__trimestral', " TRIMESTRAL"),
    ('year_third_first_reunion', "1º Reunión (1T)"),
    ('year_third_second_reunion', "2ª Reunión(2T)"),
    ('year_third_third_reunion', "3º Reunión (3T)"),
    ('year_third_fourth_reunion', "4º Reunión(4T)"),
    ('year_third_actas', "ACTAS"),
    # -- Fourth Year
    ('year_fourth__trimestral', " TRIMESTRAL"),
    ('year_fourth_first_reunion', "1º Reunión (1T)"),
    ('year_fourth_second_reunion', "2ª Reunión(2T)"),
    ('year_fourth_third_reunion', "3º Reunión (3T)"),
    ('year_fourth_fourth_reunion', "4º Reunión(4T)"),
    ('year_fourth_actas', "ACTAS"),

]

seguimiento_igualdad_mapped = [
    ('four__recepcion_de_documentacion_completa', ' recepción de documentación completa'),

    # Dependency Start
    ('four__presentacion_registro', ' Presentación Registro'),
    ('four_acuse_de_recibo', 'Acuse de Recibo'),
    # **** Dependency End

    # Dependency Start
    ('four__notificacion_1er_requerimiento', ' notificación 1er Requerimiento'),
    ('four_contestacion_1er_requerimiento', 'Contestación 1er Requerimiento'),
    ('four_notificaciones_1er', 'Notificaciones'),
    # **** Dependency End

    # Dependency Start
    ('four__notificacion_2er_requerimiento', ' notificación 2º Requerimiento'),
    ('four_contestacion_2er_requerimiento', 'Contestación 2do Requerimiento'),
    ('four_notificaciones_2er', 'Notificaciones'),
    # **** Dependency End

    # 10.37 --> add new fields
    # Dependency Start
    ('four__notificacion_3er_requerimiento', ' notificación 3º Requerimiento'),
    ('four_contestacion_3er_requerimiento', 'Contestación 3º Requerimiento'),
    # **** Dependency End

    # Dependency Start
    ('four__notificacion_4er_requerimiento', ' notificación 4º Requerimiento'),
    ('four_contestacion_4er_requerimiento', 'Contestación 4º Requerimiento'),
    # **** Dependency End

    # Dependency Start
    ('four__inscripcion_plan_a_registro', ' Inscripción Plan a Registro'),
    ('four_notificacion_3rd', 'Notificación'),
    # **** Dependency End

    ('four__archivo_o_desestimiento', ' Archivo o Desestento')
]

registro_retributivo_mapped = [
    ('five__solicitud_de_datos', ' solicitud de datos'),
    ('five__recepcion_de_datos', ' recepción de datos'),
    ('five_revision', 'Revisión'),
    ('five__prevision_de_entrega_mensaje', ' previsión de entrega: Mensaje'),
    ('five__real_de_entrega', ' real de entrega'),
    ('five_n_de_modificaciones', 'Nº de modificaciones'),
    ('five__final_de_entrega', ' final de entrega')
]

auditoria_retributiva_vpt_informe_mapped = [
    ('six__solicitud_de_datosalta_plataforma', ' solicitud de datos/Alta Plataforma'),
    ('six__recepcion_de_datos', ' recepción de datos'),
    ('six_n_dpts', 'NºDPTS'),
    ('six_revision', 'Revisión '),
    ('six__prevision_de_entrega_informe_', ' previsión de entrega informe '),
    ('six__real_de_entrega_informe', ' real de entrega informe'),
    ('six_n_de_modificaciones', 'Nº de modificaciones'),
    ('six__final_de_entrega_informe', ' final de entrega Informe')
]

investigacion_y_analisis_acoso_sexual_laboral_mapped = [
    ('seven__recepcion_datos_de_contacto', ' recepción datos de contacto'),
    ('seven__contacto_persona_denunciante', ' contacto persona denunciante'),
    ('seven__entrevista_persona_denunciante', ' entrevista persona denunciante'),
    ('seven__contacto_persona_denunciada', ' contacto persona denunciada'),
    ('seven__entrevista_persona_denunciada', ' entrevista persona denunciada'),
    ('seven_contacto_testigos', 'Contacto testigos (SI/NO)'),
    ('seven_entrevista_testigos', 'Entrevista testigos (SI/NO)'),
    ('seven_envio_informe_final', 'Envío informe final')
]

maps = [plan_de_igualdad_mapped, plan_no_registradomedidas_de_igualdad_mapped, seguimiento_igualdad,
        seguimiento_igualdad_mapped, registro_retributivo_mapped, auditoria_retributiva_vpt_informe_mapped,
        investigacion_y_analisis_acoso_sexual_laboral_mapped]


def make_project_type_category_selection_list(data):
    """Utility function, use this to update the selection of project_type_category or The Fields
        @param: data (iterable) use PROJECT_TYPE_CATEGORY_LIST or ... todo
    """

    def clean_up(string):
        clean_char = (
        ' ', 'ó', 'á', 'ª', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
        '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~')
        for char in clean_char:
            if char == '_': continue
            if char == ' ':
                string = string.replace(char, '_')
            elif char == 'ó':
                string = string.replace(char, 'o')
            elif char == 'á':
                string = string.replace(char, 'a')
            else:
                string = string.replace(char, '')
        return string

    return [(clean_up(categ.strip()).lower(), categ.strip())
            for categ in data if not categ.isspace()]


def make_fields(maps, categ, add_label=True):
    for field in maps:
        if add_label:
            print(f"{field[0]} = fields.Datetime(string='({categ}) {field[1]}')")
        else:
            print(f"{field[0]} = fields.Datetime()")

def list_fields(m):
    for field in m:
        print(f'- {field[1]}  | Nombre interno {field[0]}')

def make_fields_xml(maps, root, categ):

    fields = ''
    for field in maps:
        fields += f'\n<field name="{field[0]}" string="{field[1]}"/>'

    print(f'''
<group name="group_{root}" string="{categ}">
    {fields} 
</group>
    ''')

if __name__ == '__main__':

    run = False
    if run:
        selection_list = make_project_type_category_selection_list(PROJECT_TYPE_CATEGORY_LIST)
        print(selection_list)
        print('\n\n\n\n')
        plan_de_igualdad = """    
         solicitud de datos/ Alta Plataforma
         recepción de datos  Cuanti /Cuali 
         1ª Revisión Datos           
         2ª Revisión Datos
         previsión de entrega   
         real de entrega 
        /s o nº de modificaciones:
         final de entrega 
        Reunión Presentación Plan a empresa
        Reunión Constitución Comisión Nego        
        Anotaciones   
        ACTA
         1ª reunión CN
         2ª reunión CN
         3ª reunión CN
         4ª reunión – notificación al cliente. A partir de ahora el resto de las posibles reuniones se facturarán aparte.    
         Diagnóstico Firmado
         Plan Firmado     
        """
        plan_de_igualdad_ready = make_project_type_category_selection_list(plan_de_igualdad.split('\n'))
        print(plan_de_igualdad_ready)
        print('\n\n\n\n')

        plan_no_registradomedidas_de_igualdad = """
             solicitud de datos/ Alta Plataforma
             recepción de datos  Cuanti /Cuali 
             1ª Revisión Datos:           
             2ª Revisión Datos:
             previsión de entrega   
             real de entrega 
            /s o nº de modificaciones:
             final de entrega :
            Reunión Presentación Plan a la Empresa:
             Diagnóstico Firmado:
             Plan Firmado
        """
        plan_no_registradomedidas_de_igualdad_ready = make_project_type_category_selection_list(
            plan_no_registradomedidas_de_igualdad.split('\n'))
        print(plan_no_registradomedidas_de_igualdad_ready)
        print('\n\n\n\n')

        seguimiento_igualdad_ci = """
        1er Año :      
         TRIMESTRAL      1º Reunión (1T):             2ª Reunión(2T):       3º Reunión (3T):           4º Reunión(4T)       ACTAS

        2do Año :     
          TRIMESTRAL      1º Reunión (1T):             2ª Reunión(2T):       3º Reunión (3T):           4º Reunión(4T)      ACTAS
        3er  Año :     
          TRIMESTRAL      1º Reunión (1T):             2ª Reunión(2T):       3º Reunión (3T):           4º Reunión(4T)      ACTAS
        4to Año :     
          TRIMESTRAL      1º Reunión (1T):             2ª Reunión(2T):       3º Reunión (3T):           4º Reunión(4T)      ACTAS

        """
        # seguimiento_igualdad_ci_mapped = make_project_type_category_selection_list(seguimiento_igualdad_ci.split('\n'))
        # print(seguimiento_igualdad_ci_mapped)

        registro_retributivo = """
             solicitud de datos
             recepción de datos  :          
            Revisión :
             previsión de entrega: Mensaje  
             real de entrega 
            /s o nº de modificaciones
             final de entrega
        """
        registro_retributivo_ready = make_project_type_category_selection_list(registro_retributivo.split('\n'))
        print(registro_retributivo_ready)
        print('\n\n\n\n')

        auditoria_retributiva_vpt_informe = """
             solicitud de datos/Alta Plataforma
             recepción de datos
            NºDPTS:   
            Revisión :
             previsión de entrega informe : 
             real de entrega informe
            /s o nº de modificaciones
             final de entrega Informe
        """
        auditoria_retributiva_vpt_informe_ready = make_project_type_category_selection_list(
            auditoria_retributiva_vpt_informe.split('\n'))
        print(auditoria_retributiva_vpt_informe_ready)
        print('\n\n\n\n')

        investigacion_y_analisis_acoso_sexual_laboral = """
             recepción datos de contacto
             contacto persona denunciante 
             entrevista persona denunciante
             contacto persona denunciada
             entrevista persona denunciada
            Contacto testigos (SI/NO)
            Entrevista testigos (SI/NO)
            Envío informe final

        """
        investigacion_y_analisis_acoso_sexual_laboral_ready = make_project_type_category_selection_list(
            investigacion_y_analisis_acoso_sexual_laboral.split('\n'))
        print(investigacion_y_analisis_acoso_sexual_laboral_ready)
        print('\n\n\n\n')

        registro_de_plan_en_regcon = """        
                 recepción de documentación completa 
                 Presentación Registro:                       
                - Acuse de Recibo
                 notificación 1er Requerimiento       
                - Contestación 1er Requerimiento:         
                 -  Notificaciones 
                 notificación 2º Requerimiento        
                -  Contestación 2do Requerimiento:  
                -  Notificaciones
                 Inscripción Plan a Registro:                
                 Notificación
                 Archivo o Desestimiento:
                """
        registro_de_plan_en_regcon_mapped = make_project_type_category_selection_list(
            registro_de_plan_en_regcon.split('\n'))
        print(registro_de_plan_en_regcon_mapped)

        for idx, map in enumerate(maps):
            index_map = PROJECT_TYPE_CATEGORY_LIST_INDEX[idx]
            root = index_map[0]
            root_name = index_map[1]
            add_label = True
            if root_name == 'SEGUIMIENTO IGUALDAD CI':
                add_label = False
            print(f'    CRETING FIELDS FOR {root_name}')
            print('\n\n\n')
            make_fields(map, root, add_label)
            print('\n\n\n')

        for idx, map in enumerate(maps):
            index_map = PROJECT_TYPE_CATEGORY_LIST_INDEX[idx]
            root_name = index_map[1]
            print(f'{root_name}')
            print('\n\n\n')
            list_fields(map)
            print('\n\n\n')

        for idx, map in enumerate(maps):
            index_map = PROJECT_TYPE_CATEGORY_LIST_INDEX[idx]
            root = index_map[0]
            root_name = index_map[1]
            add_label = True
            if root_name == 'SEGUIMIENTO IGUALDAD CI':
                add_label = False
            print(f'<!-- {root_name} -->')
            print('\n\n\n')
            make_fields_xml(map, root, root_name)
            print('\n\n\n')
    mapping = {}
    for idx, p in enumerate(PROJECT_TYPE_CATEGORY_SELECTION):
        view = PROJECT_CATEGORY_LIST_VIEWS[idx]
        mapping[p[0]] = {'name': p[1], 'view': view}
    print(mapping)


