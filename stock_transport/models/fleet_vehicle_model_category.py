# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,exceptions

class FleetVehicleModelCategory(models.Model):

    _inherit = 'fleet.vehicle.model.category'

    max_weight=fields.Integer(string="Max Weight(kg)")
    max_volume=fields.Integer(string="Max Volume(m³)")


    @api.depends('max_weight','max_volume','name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.name}({rec.max_weight}kg,{rec.max_volume}m³)'
