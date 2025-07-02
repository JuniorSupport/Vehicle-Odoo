# -*- coding: utf-8 -*-
{
    'name': "Grades Manager",

    'summary': "Handles grades in students and  courses",

    'description':"Handles grades in students and  courses",

    'author': "Junior Cañari",
    'website': "https://www.yourcompany.com",

    'category': 'Base',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/grades_manager_menu.xml',
        'views/res_partner_views.xml'
       
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install':False,
    'application':True
}