# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inventory',
    'version': '1.0',
    'summary': 'Settings',
    'category': 'Inventory/Inventory',
    'depends': ['stock_transport','stock'],
    'data': [
        'views/res_config_settings_views.xml',
        ],
    'auto-install': True,
    'license':'LGPL-3',
}