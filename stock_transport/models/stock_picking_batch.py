# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models 
from odoo.exceptions import ValidationError

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"
    
    dock=fields.Many2one('stock.transport.dock',string='Dock')
    vehicle=fields.Many2one('fleet.vehicle',string='Vehicle')
    vehicle_category=fields.Many2one('fleet.vehicle.model.category',string='Vehicle Category')

    weight = fields.Float(string="Weight" , compute='_compute_weight',store=True)
    computed_volume = fields.Float(string="Volume", compute='_compute_volume',store=True)
    graph_volume=fields.Float(string="Volume")
    graph_weight=fields.Float(string="Weight")
    volume_percentage = fields.Float(string="Volume percent",compute='_compute_volume_percent')
    weight_percentage=fields.Float(string="Weight percent" ,  compute='_compute_weight_percentage')
    no_line = fields.Integer(string="Lines" ,compute='_compute_line',store=True)
    no_transfer = fields.Integer(string="Transfer", compute='_compute_transfer',store=True)

    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.no_transfer = len(record.picking_ids)

    @api.depends('picking_ids')
    def _compute_line(self):
        for record in self:
            for picking in record.picking_ids:
                record.no_line = len(picking.move_ids)

    @api.depends('picking_ids.volume')
    def _compute_volume(self):
        for rec in self:     
            vol=0   
            for record in rec.picking_ids:
                vol+=record.volume
            rec.computed_volume=vol
            rec.graph_volume=rec.computed_volume

    @api.depends('picking_ids.shipping_weight')
    def _compute_weight(self):
        for rec in self: 
            wei=0       
            for record in rec.picking_ids:
                wei+= record.shipping_weight
            rec.weight=wei
            rec.graph_weight=rec.weight

    @api.depends('computed_volume','vehicle_category')
    def _compute_volume_percent(self):
        for rec in self:
            if rec.vehicle_category.max_volume:
                rec.volume_percentage=(rec.computed_volume/rec.vehicle_category.max_volume)*100
            else:
                rec.volume_percentage=0

    @api.depends('weight','vehicle_category')
    def _compute_weight_percentage(self):
        for rec in self:
            if rec.vehicle_category.max_weight :
                rec.weight_percentage = (rec.weight/rec.vehicle_category.max_weight)*100
            else:
                rec.weight_percentage = 0
                
    @api.constrains('computed_volume')
    def _check_volume(self):
        for rec in self:
            if rec.computed_volume>rec.vehicle_category.max_volume:
                raise ValidationError("User must Enter Volume smaller than Max Volume")
            
    @api.constrains('weight')
    def _check_volume(self):
        for rec in self:
            if rec.weight>rec.vehicle_category.max_weight:
                raise ValidationError("User must Enter Volume smaller than Max Volume")