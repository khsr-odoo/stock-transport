# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    volume = fields.Float(string="Volume",compute='_compute_volume')  

    @api.depends('move_ids')
    def _compute_volume(self):
        for record in self:
            if record.move_ids:
                vol=0
                for rec in record.move_ids:
                    vol+=(rec.product_id.volume*rec.quantity)
                record.volume=vol
        return True