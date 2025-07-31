{
    'name': "owl_project",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': "OWL Tests",
    'author': "Junior Cañari",
    'category': 'Uncategorized',
    'version': '0.1',
    'assets':{
        'web.assets_backend':[
            'owl_project/static/src/components/**/*',
            'owl_project/static/src/components/intl_phone_field/intl_phone_field.js',
            'owl_project/static/src/components/intl_phone_field/intl_phone_field.xml',
        ],
    },
    'depends': ['base','web'],
    "data": [
        "views/res_partner_views.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}