{
    'name': 'Flous Flow Shop Floor',
    'version': '19.0.1.0.2',
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Dedicated standard-style Shop Floor work order screen.',
    'description': """
Dedicated Shop Floor entry point for manufacturing work orders.

The module intentionally uses Odoo's native mrp.workorder model, actions,
timers and work order buttons. Employee productivity and payroll integration
remain in the separate ff_mrp_employee_productivity module.
""",
    'author': 'Flous Flow',
    'website': 'https://flousflow.com',
    'license': 'LGPL-3',
    'depends': ['mrp'],
    'data': [
        'views/shop_floor_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
