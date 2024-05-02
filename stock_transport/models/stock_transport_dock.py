# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models

class StockTransportDock(models.Model):

    _name = "stock.transport.dock"
    _description = "Stock Transport Dock"
    
    name = fields.Char(string='Dock')
    
    _sql_constraints=[
        ('uniqui_tag_name','UNIQUE(name)',
        'Tag names must be unique')
    ]
