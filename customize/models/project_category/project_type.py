# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com

from odoo import fields, models


PROJECT_TYPE_CATEGORY_SELECTION = [
    ('plan_de_igualdad', '1) PLAN DE IGUALDAD'),
    ('plan_no_registradomedidas_de_igualdad', '2) Plan (No Registrado)/Medidas de Igualdad'),
    ('seguimiento_igualdad_ci', '3) SEGUIMIENTO IGUALDAD CI'),
    ('registro_de_plan_en_regcon', '4) Registro de Plan en REGCON'),
    ('registro_retributivo', '5) Registro Retributivo'),
    ('auditoria_retributiva_vpt_informe', '6) Auditoria Retributiva (VPT+ INFORME)'),
    ('investigacion_y_analisis_acoso_sexual_laboral', '7) Investigación y Análisis ACOSO Sexual /Laboral'),

    ('general_servicios', '8) GENERAL SERVICIOS'),
    ('protocolo_acoso_sexual_labora', '9) PROTOCOLO ACOSO SEXUAL /LABORA'),
    ('gestion_denuncias_acoso', '10) GESTION DENUNCIAS ACOSO'),
    ('medidas_prevencion_acoso_sexual', '11) MEDIDAS PREVENCION ACOSO SEXUAL'),
    ('plan_no_discriminacion_lgtbi', '12) PLAN NO DISCRIMINACION LGTBI'),
]

PROJECT_TYPE_CATEGORY_HELP = """
Project Type Category list
==========================
Este campo refleja los tipos the proyectos y sus listado de campos relacionados.

- PLAN DE IGUALDAD (plan_de_igualdad)
------------------

-  solicitud de datos/ Alta Plataforma  | Nombre interno one__solicitud_de_datos_alta_plataforma
-  recepción de datos  Cuanti /Cuali  | Nombre interno one__recepcion_de_datos_cuanti_cuali
-  1ª Revisión Datos  | Nombre interno one__1_revision_datos
-  2ª Revisión Datos  | Nombre interno one__2_revision_datos
-  previsión de entrega  | Nombre interno one__prevision_de_entrega
-  real de entrega  | Nombre interno one__real_de_entrega
- /s o nº de modificaciones:  | Nombre interno one_s_o_n_de_modificaciones
-  final de entrega  | Nombre interno one__final_de_entrega
- Reunión Presentación Plan a empresa  | Nombre interno one_reunion_presentacion_plan_a_empresa
- Reunión Constitución Comisión Nego  | Nombre interno one_reunion_constitucion_comision_nego
- Anotaciones  | Nombre interno one_anotaciones
- ACTA  | Nombre interno one_acta
-  1ª reunión CN  | Nombre interno one__1_reunion_cn
-  2ª reunión CN  | Nombre interno one__2_reunion_cn
-  3ª reunión CN  | Nombre interno one__3_reunion_cn
-  4ª reunión – notificación al cliente  | Nombre interno _4_reunion
- Notificación al cliente  | Nombre interno one_notificacion_al_client
-  Diagnóstico Firmado  | Nombre interno one__diagnostico_firmado
-  Plan Firmado  | Nombre interno one__plan_firmado


- Plan (No Registrado)/Medidas de Igualdad  (plan_no_registradomedidas_de_igualdad) 
------------------------------------------

-  solicitud de datos/ Alta Plataforma  | Nombre interno two__solicitud_de_datos_alta_plataforma
-  recepción de datos  Cuanti /Cuali  | Nombre interno two__recepcion_de_datos_cuanti_cuali
-  1ª Revisión Datos:  | Nombre interno two__1_revision_datos
-  2ª Revisión Datos:  | Nombre interno two__1_revision_datos
-  previsión de entrega  | Nombre interno two__prevision_de_entrega
-  real de entrega  | Nombre interno two__real_de_entrega
- /s o nº de modificaciones:  | Nombre interno two_s_o_n_de_modificaciones
-  final de entrega :  | Nombre interno two__final_de_entrega
- Reunión Presentación Plan a la Empresa:  | Nombre interno two_reunion_presentacion_plan_a_la_empresa
-  Diagnóstico Firmado:  | Nombre interno two__diagnostico_firmado
-  Plan Firmado  | Nombre interno two__plan_firmado


- SEGUIMIENTO IGUALDAD CI (seguimiento_igualdad_ci) 
-------------------------

-  TRIMESTRAL  | Nombre interno year_first__trimestral
- 1º Reunión (1T)  | Nombre interno year_first_first_reunion
- 2ª Reunión(2T)  | Nombre interno year_first_second_reunion
- 3º Reunión (3T)  | Nombre interno year_first_third_reunion
- 4º Reunión(4T)  | Nombre interno year_first_fourth_reunion
- ACTAS  | Nombre interno year_first_actas
-  TRIMESTRAL  | Nombre interno year_second__trimestral
- 1º Reunión (1T)  | Nombre interno year_second_first_reunion
- 2ª Reunión(2T)  | Nombre interno year_second_second_reunion
- 3º Reunión (3T)  | Nombre interno year_second_third_reunion
- 4º Reunión(4T)  | Nombre interno year_second_fourth_reunion
- ACTAS  | Nombre interno year_second_actas
-  TRIMESTRAL  | Nombre interno year_third__trimestral
- 1º Reunión (1T)  | Nombre interno year_third_first_reunion
- 2ª Reunión(2T)  | Nombre interno year_third_second_reunion
- 3º Reunión (3T)  | Nombre interno year_third_third_reunion
- 4º Reunión(4T)  | Nombre interno year_third_fourth_reunion
- ACTAS  | Nombre interno year_third_actas
-  TRIMESTRAL  | Nombre interno year_fourth__trimestral
- 1º Reunión (1T)  | Nombre interno year_fourth_first_reunion
- 2ª Reunión(2T)  | Nombre interno year_fourth_second_reunion
- 3º Reunión (3T)  | Nombre interno year_fourth_third_reunion
- 4º Reunión(4T)  | Nombre interno year_fourth_fourth_reunion
- ACTAS  | Nombre interno year_fourth_actas


- Registro de Plan en REGCON (registro_de_plan_en_regcon) 
-----------------------------

-  recepción de documentación completa  | Nombre interno four__recepcion_de_documentacion_completa
-  Presentación Registro  | Nombre interno four__presentacion_registro
- Acuse de Recibo  | Nombre interno four_acuse_de_recibo
-  notificación 1er Requerimiento  | Nombre interno four__notificacion_1er_requerimiento
- Contestación 1er Requerimiento  | Nombre interno four_contestacion_1er_requerimiento
- Notificaciones  | Nombre interno four_notificaciones_1er
-  notificación 2º Requerimiento  | Nombre interno four__notificacion_2er_requerimiento
- Contestación 2do Requerimiento  | Nombre interno four_contestacion_2er_requerimiento
- Notificaciones  | Nombre interno four_notificaciones_2er
-  Inscripción Plan a Registro  | Nombre interno four__inscripcion_plan_a_registro
- Notificación  | Nombre interno four_notificacion_3rd
-  Archivo o Desestento  | Nombre interno four__archivo_o_desestimiento

- Registro Retributivo (registro_de_plan_en_regcon)
----------------------

-  solicitud de datos  | Nombre interno five__solicitud_de_datos
-  recepción de datos  | Nombre interno five__recepcion_de_datos
- Revisión  | Nombre interno five_revision
-  previsión de entrega: Mensaje  | Nombre interno five__prevision_de_entrega_mensaje
-  real de entrega  | Nombre interno five__real_de_entrega
- /s o nº de modificaciones  | Nombre interno five_s_o_n_de_modificaciones
-  final de entrega  | Nombre interno five__final_de_entrega


- Auditoria Retributiva (VPT+ INFORME) (auditoria_retributiva_vpt_informe) 
--------------------------------------

-  solicitud de datos/Alta Plataforma  | Nombre interno six__solicitud_de_datosalta_plataforma
-  recepción de datos  | Nombre interno six__recepcion_de_datos
- NºDPTS  | Nombre interno six_n_dpts
- Revisión   | Nombre interno six_revision
-  previsión de entrega informe   | Nombre interno six__prevision_de_entrega_informe_
-  real de entrega informe  | Nombre interno six__real_de_entrega_informe
- /s o nº de modificaciones  | Nombre interno six_s_o_n_de_modificaciones
-  final de entrega Informe  | Nombre interno six__final_de_entrega_informe



- Investigación y Análisis ACOSO Sexual /Laboral (investigacion_y_analisis_acoso_sexual_laboral) 
------------------------------------------------

-  recepción datos de contacto  | Nombre interno seven__recepcion_datos_de_contacto
-  contacto persona denunciante  | Nombre interno seven__contacto_persona_denunciante
-  entrevista persona denunciante  | Nombre interno seven__entrevista_persona_denunciante
-  contacto persona denunciada  | Nombre interno seven__contacto_persona_denunciada
-  entrevista persona denunciada  | Nombre interno seven__entrevista_persona_denunciada
- Contacto testigos (SI/NO)  | Nombre interno seven_contacto_testigos
- Entrevista testigos (SI/NO)  | Nombre interno seven_entrevista_testigos
- Envío informe final  | Nombre interno seven_envio_informe_final


- GENERAL SERVICIOS (investigacion_y_analisis_acoso_sexual_laboral) 
------------------------------------------------

-Recepción Documentación/Datos 
-Revisión 
-Entrega Informe 

- PROTOCOLO ACOSO SEXUAL /LABORAL (investigacion_y_analisis_acoso_sexual_laboral) 
------------------------------------------------

-Entrega protocolo acoso sexual
- Entrega protocolo acoso laboral

- GESTION DENUNCIAS ACOSO  (investigacion_y_analisis_acoso_sexual_laboral) 
------------------------------------------------

-Activación canal denuncias 

- MEDIDAS PREVENCION ACOSO SEXUAL (investigacion_y_analisis_acoso_sexual_laboral) 
------------------------------------------------

- Inicio Seguimiento
-Entrega de medidas de prevención 

- PLAN NO DISCRIMINACION LGTBI(investigacion_y_analisis_acoso_sexual_laboral) 
------------------------------------------------

-Entrega protocolo LGTBI
-Entrega medidas de prevención

"""

class ProjectType(models.Model):
    _inherit = "project.type"

    # As requested by GrupoSGP, this field is quite hard code but is needed for their daily work
    project_type_category = fields.Selection(PROJECT_TYPE_CATEGORY_SELECTION, copy=False, help=PROJECT_TYPE_CATEGORY_HELP)
    is_company_project_category_type = fields.Boolean(default=True,
  help="If True is a project type specifically created for the Company, it will be shown as a Tab in the List Tab view. ")