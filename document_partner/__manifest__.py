# -*- coding: utf-8 -*-
# © 2018-Today Tundra Consulting (http://tundra-consulting.com).
# License OPL-1 or later.
#       @Author: iTundra.com
#       @Creation Date: 16th June - 2021
#       Odoo Version: 14.0.0

{
    'name': 'Contacts Document',
    'category': 'Tools / Extension',
    'summary': 'Customers & Contacts Document Management',
    'description': """
Adds and improves management of Attachment for Customers or Contacts.
    
""",
    'version': '14.0.0.0.4',
    'license': 'OPL-1',
    'author':  'iTundra.com',
    'company': "Tundra Consulting & Advisory SL",
    'website': 'https://www.itundra.com',
    'depends': [
            "base",
            "mail",
        ],
    'data': [
        'views/assets.xml',
        'views/res_partner_views.xml',
        'views/ir_attachment_views.xml',
        ],
    'installable': True,
    'auto_install': False,
    'application':  False,
    'sequence': 1,
}
