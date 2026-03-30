# -*- coding:utf-8 -*-
from odoo import models,fields


class ResCompany(models.Model):
    _inherit = "res.company"

    stock_picking_operation_type = fields.Selection([
        ('cancel_only', 'Cancel Only'),
        ('cancel_and_reset_to_draft', 'Cancel and Reset To Draft'),
        ('cancel_and_delete', 'Cancel and Delete')], string="Stock Picking Operation Type")
