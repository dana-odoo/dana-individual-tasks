from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit = fields.Float(
        string="Unit Price",
        compute='_compute_price_unit_custom',
        digits='Product Price',
        store=True, readonly=False, required=True, precompute=True)

    @api.depends('product_id', 'product_uom')
    def _compute_price_unit_custom(self):
        super()._compute_price_unit()