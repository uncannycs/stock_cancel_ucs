# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2023 Uncanny Consulting Services LLP (<https://uncannycs.com>).
#
##############################################################################
{
    "name": "Stock Picking Cancel",
    "summary": "Stock Picking Cancel",
    "version": "15.0.1.0.0",
    "category": "Extra Tools",
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    "license": "Other proprietary",
    "depends": [
        "stock", "sale_management"
    ],
    "data": [
        "security/stock_cancel_security.xml",
        "views/res_config_settings_views.xml",
        "views/res_company.xml",
        "views/stock_picking.xml",
    ],
    "images": ["static/description/banner.gif"],
    "application": False,
    "installable": True,
    "preloadable": True,
    "price": 70,
    "currency": "USD",
}
