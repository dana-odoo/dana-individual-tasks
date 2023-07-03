from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    main_active_potency = fields.Integer(string="Main Active Potency")
    main_active_quantity = fields.Float(string="Main Active Quantity", compute="_compute_main_active_quantity")

    @api.depends('quantity', 'main_active_potency')
    def _compute_main_active_quantity(self):
        for record in self:
            record.main_active_quantity = record.quantity * record.main_active_potency / 1000
    
    @api.constrains('main_active_potency')
    def _check_main_active_potency_within_range(self):
        for record in self:
            if not (1 <= record.main_active_potency <= 1000):
                raise ValidationError("Main Active Potency must be set in the range [1, 1000]")