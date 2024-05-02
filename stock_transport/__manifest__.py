# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Transport',
    'version': '1.0',
    'summary': 'Transport Management',
    'category': 'Stock Transport/Management',
    'depends': ['stock_picking_batch','fleet','stock_delivery'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_views.xml',
        'views/stock_picking_batch_views.xml',
        ],
    'application': True,
    'license':'LGPL-3',
}