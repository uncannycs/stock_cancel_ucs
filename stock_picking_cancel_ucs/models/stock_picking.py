# -*- coding:utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    company_id = fields.Many2one('res.company')
    picking_operation_type = fields.Selection(related='company_id.stock_picking_operation_type')

    def action_picking_cancel(self):
        for picking in self:
            if self.env.company.stock_picking_operation_type:
                if picking.state == 'done':
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.unlink()
                picking.write({'state': 'draft'})
                picking.move_ids_without_package.write({'quantity_done': 0})
                picking.move_ids.write({'state': 'draft'})
                picking.write({'state': 'draft'})
                picking.action_cancel()
                picking.write({'state': 'cancel'})
                picking.sale_id.write({'state': 'draft'})

    def action_picking_cancel_reset(self):
        for picking in self:
            if self.env.company.stock_picking_operation_type:
                if picking.state == 'done':
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                picking.write({'state': 'draft'})
                picking.move_ids_without_package.write({'quantity_done': 0})
                picking.move_ids.write({'state': 'draft'})
                picking.write({'state': 'draft'})
                picking.sale_id.write({'state': 'draft'})

    def action_picking_cancel_delete(self):
        for picking in self:
            if self.env.company.stock_picking_operation_type:
                if picking.state == 'cancel':
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                    picking.sale_id.write({'state': 'draft'})
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                    picking.unlink()

                elif picking.state == 'done':
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            print("======================> VALUATION", valuation)
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                    picking.write({'state': 'assigned'})
                    picking.move_ids_without_package.write({'quantity_done': 0})
                    picking.move_ids.write({'state': 'draft'})
                    picking.write({'state': 'draft'})
                    picking.sale_id.write({'state': 'draft'})
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                    picking.action_cancel()
                    picking.unlink()

                else:
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                    picking.write({'state': 'assigned'})
                    picking.move_ids_without_package.write({'quantity_done': 0})
                    picking.move_ids.write({'state': 'draft'})
                    picking.write({'state': 'draft'})
                    picking.sale_id.write({'state': 'draft'})
                    picking.do_unreserve()
                    for move in picking.move_ids.filtered(lambda r: r.stock_valuation_layer_ids):
                        for valuation in move.stock_valuation_layer_ids:
                            if valuation.account_move_id:
                                valuation.account_move_id.button_draft()
                                valuation.account_move_id.with_context(force_delete=True).sudo().unlink()
                            valuation.sudo().unlink()
                    picking.action_cancel()
                    picking.unlink()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
