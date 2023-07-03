from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.product'

    product_group = fields.Selection([('group1', 'G1'), ('group2', 'G2')], string='Product Group',required=True)
    barcode = fields.Char('Barcode', compute='_compute_barcode_custom', store=True, readonly=True)

    @api.depends('product_group', 'barnum')
    def _compute_barcode_custom(self):
        for record in self:
            product_group_str =  dict(self._fields['product_group'].selection).get(record.product_group)
            if product_group_str:
                record.barcode = f"{product_group_str[:2]}.{record.barnum}"