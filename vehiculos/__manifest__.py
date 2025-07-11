# -*- coding: utf-8 -*-
{
    'name': "vehiculos",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """Long description of module's purpose""",
    'author': "Junior Cañari",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/vehiculos_view.xml',
        'views/propietario_view.xml',
        'views/vehiculo_historial_view.xml',
        'views/modelo_prueba_view.xml',
        'data/data.xml',
        'demo/demo_propietarios.xml'
      #  'data/vehiculos.vehiculo.csv'

    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

