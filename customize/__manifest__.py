# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       Odoo Version: 13.0.0



{
    'name': 'Customize',
    'category': 'Custom',
    'version': '13.0.0.1.41',
    'license': 'OPL-1',
    'author':  'iTundra.com',
    'company': "Tundra Consulting & Advisory SL",
    'website': 'https://www.itundra.com',
    'summary': 'Customized Odoo Features',
    'description': """
Customize
=========

Add features and customized the Default Odoo implementation across different 
modules. 

""",
    'depends': [
        'base_automation',
        'mail',
        'hr',
        'sale',
        'sale_crm',
        'sale_management',
        'sale_commission',
        'sale_timesheet',
        'project',
        'base',
        'mass_mailing',
        'extra_features_gruposgp',

        # Third Party
        'project_description',
        'project_category'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/project_type_data.xml',
        'views/assets.xml',
        'views/base_autonomation_view.xml',
        'views/product_category_views.xml',
        'views/project_project_views.xml',
        'views/mailing_views.xml',
        'views/hr_employee_view.xml',
        'views/mail_activity_views.xml',
        'views/sale_views.xml',
        'views/res_partner_views.xml',
        'views/project_category/project_type_views.xml',
        'views/project_category/project_type_category_views.xml',
        'views/project_timer/project_timer_views.xml'
    ],
    'qweb': [
        'static/src/xml/web_kanban_activity.xml',
        'static/src/xml/list_multi_tab.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application':  False,
    'sequence': 1,
}