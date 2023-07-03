from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_group = fields.Selection([('group1', 'G1group'), ('group2', 'G2group')], string='Product Group', required=True)
    barcode = fields.Char('Barcode', compute='_compute_barcode_custom', store=True, readonly=True)
    barnum = fields.Char(default='000000', copy=False, required=True) 

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('barnum', ('000000')) == ('000000'):
                vals['barnum'] = self.env['ir.sequence'].next_by_code('product.barnum') 
        return super().create(vals_list)

    @api.depends('product_group', 'barnum')
    def _compute_barcode_custom(self):
        for record in self:
            product_group_str =  dict(self._fields['product_group'].selection).get(record.product_group)
            if product_group_str:
                record.barcode = f"{product_group_str[:2]}.{record.barnum}"