# -*- coding: utf-8 -*-
# © 2018-Today iTundra.com (http://itundra.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#       @Author: iTundra.com


{
    'name': 'Extra Features',
    'category': 'Extra/Project',
    'summary': 'Project Extra Features',
    'description': """
Project Extra Features
===============================

This module improves the general overall Odoo Modules experience and adds new Features:

- Projects: 
    - Adds 3 Stages to the Main Projects: Blocked, In Progress, Ready for Next Stage
""",
    'version': '13.0.2.32',
    'license': 'OPL-1',
    'author':  'iTundra.com',
    'company': "Tundra Consulting & Advisory SL",
    'website': 'https://www.itundra.com',
    'depends': [
            'account',
            'base',
            'contacts',
            'hr',
            'project',
            'sale',
            'sale_commission',
            'sale_timesheet',
            'event',
            'website',
            'website_event'
        ],
    'data': [
        # --------- < DATA > --------- #
        'data/project_checklist_template.xml',
        'data/project_data.xml',
        'data/sequence_data.xml',
        # --------- < VIEWS > --------- #
        'views/assets.xml',
        'views/project_views.xml',
        'views/sale_views.xml',
        'views/res_partner_views.xml',
        'views/event_templates.xml',
        'views/event_views.xml',
        'views/project_checklist_views.xml',
        'views/project_project_type_views.xml',
        'views/report_invoice.xml',
        # --------- < REPORT > --------- #
        'report/sale_report_templates.xml',
        # --------- < SECURITY > --------- #
        'security/ir.model.access.csv',
        ],
    'qweb': [
        "static/src/xml/widget.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application':  True,
    'sequence': 1,
}