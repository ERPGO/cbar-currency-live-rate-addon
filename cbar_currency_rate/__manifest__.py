# -*- coding: utf-8 -*-
{
    'name': "CBAR live currency rate",

    'summary': """
        Central Bank of Azerbaijan as a Currency provider""",

    'description': """
        Central Bank of Azerbaijan as a Currency provider
    """,

    'author': "ERPGO",
    'website': "https://erpgo.az",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base','currency_rate_live'],

    # always loaded
    'data': [],
}
