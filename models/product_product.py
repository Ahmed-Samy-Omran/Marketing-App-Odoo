# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = 'product.product'

    # 1. Make barcode required at the variant level
    barcode = fields.Char(
        string='Barcode',
        required=True,
        help="Unique identifier for scanning at checkout."
    )

    # 2. Database-level uniqueness check it will prevent duplicate barcode it works at database level
    _sql_constraints = [
        ('barcode_unique', 'unique(barcode)', 'Error: This barcode is already assigned to another product!')
    ]

    # 3. Python-level validation for empty strings
    @api.constrains('barcode')
    def _check_barcode_required(self):
        for product in self:
            if not product.barcode or not product.barcode.strip():
                raise ValidationError('Barcode is required for all product variants.')