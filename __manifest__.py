# # -*- coding: utf-8 -*-
# {
#     'name': 'Supermarket Inventory & Product Management',
#     'version': '17.0.1.0.0',
#     'category': 'Inventory/Inventory',
#     'summary': 'Core Product and Inventory Management for SMS (Phase 1)',
#     'description': """
#         This module inherits Odoo's standard products to:
#         - Add min_stock and max_stock safety thresholds.
#         - Enforce unique and required barcodes for quick scanning.
#         - Depend on the stock module for multi-location & multi-warehouse support.
#     """,
#     'author': 'Supermarket Management System',
#     'depends': [
#         'base',
#         'mail',
#         'stock',
#     ],
#     'data': [
#         'security/ir.model.access.csv',
#         'views/product_template_views.xml',
#         'views/menu_views.xml',
#     ],
#     'application': True,
#     'license': 'LGPL-3',
# }
# -*- coding: utf-8 -*-
{
    'name': 'Supermarket Inventory & Product Management',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Core Product and Inventory Management for SMS (Phase 1)',
    'description': """
        This module inherits Odoo's standard products to:
        - Add min_stock and max_stock safety thresholds.
        - Enforce unique and required barcodes for quick scanning.
        - Depend on the stock module for multi-location & multi-warehouse support.
    """,
    'author': 'Supermarket Management System',
    'depends': [
        'base',
        'mail',
        'product',  # Added: Ensures standard product models/views are loaded
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/product_template_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,   # Added: Explicitly marks module as installable
    'application': True,
    'auto_install': False, # Added: Prevents it from installing automatically
    'license': 'LGPL-3',
}
