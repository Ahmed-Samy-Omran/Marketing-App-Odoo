# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    min_stock = fields.Float(
        string='Minimum Safety Stock',
        default=0.0,
        help='The minimum stock level below which alerts should be triggered.'
    )
    max_stock = fields.Float(
        string='Maximum Safety Stock',
        default=0.0,
        help='The maximum desired stock level for this product.'
    )

    @api.constrains('min_stock', 'max_stock')
    def _check_stock_thresholds(self):
        for product in self:
            if product.min_stock < 0 or product.max_stock < 0:
                raise ValidationError('Safety stock thresholds cannot be negative.')
            if product.max_stock < product.min_stock:
                raise ValidationError('Maximum safety stock cannot be less than minimum safety stock.')

    def cron_check_low_stock(self):
        """
        This function is called by a Scheduled Action (Cron).
        It creates an activity for the manager if stock is low.
        """
        low_stock_products = self.search([('type', '=', 'product')]) # Only storable products
        for product in low_stock_products:
            if product.qty_available < product.min_stock:
                # Create a notification (Activity)
                self.env['mail.activity'].create({
                    'res_id': product.id,
                    'res_model_id': self.env.ref('product.model_product_template').id,
                    'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                    'summary': f'Low Stock: {product.name}',
                    'note': f'Stock level is {product.qty_available}, which is below the minimum of {product.min_stock}.',
                    'user_id': self.env.user.id,
                })