# -*- coding : utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from  datetime import datetime
from odoo.exceptions import UserError,Warning 


class StockMoveUpdate(models.Model):
    _inherit = 'stock.move'

    move_date = fields.Date(string="Move Date")
    move_remark = fields.Char(string="Remarks")

    def _action_done(self,cancel_backorder=False):
        res = super(StockMoveUpdate, self)._action_done()
        custom_stock_picking_ids = self.env['stock.picking'].browse(self._context.get('active_id'))
        stock_type_id = self.env['stock.picking.type'].browse(self._context.get('active_id'))
        active_models1 = self._context.get('active_model')
        if active_models1 == 'stock.picking.type':
            if stock_type_id.code != 'outgoing':
                for move in res:
                    move.write({'date': move.move_date or fields.Datetime.now()})
                    for line in move.mapped('move_line_ids'):
                        line.write({'date': move.move_date or fields.Datetime.now()})
            elif stock_type_id.code == 'outgoing':
                for move in res:
                    move.write({'date': move.move_date or fields.Datetime.now()})
                    for line in move.mapped('move_line_ids'):
                        line.write({'date': move.move_date or fields.Datetime.now()})

        elif active_models1 == 'stock.picking' :
            if custom_stock_picking_ids.picking_type_id.code != 'outgoing':
                for move in res:
                    move.write({'date': move.move_date or fields.Datetime.now()})
                    for line in move.mapped('move_line_ids'):
                        line.write({'date': move.move_date or fields.Datetime.now()})
            elif custom_stock_picking_ids.picking_type_id.code =='outgoing':
                for move in res:
                    move.write({'date': move.move_date or fields.Datetime.now()})
                    for line in move.mapped('move_line_ids'):
                        line.write({'date': move.move_date or fields.Datetime.now()})

        elif active_models1 == 'sale.order':
            for move in res:
                move.write({'date': move.move_date or fields.Datetime.now()})
                for line in move.mapped('move_line_ids'):
                    line.write({'date': move.move_date or fields.Datetime.now()})
        return res

    def _create_account_move_line(self, credit_account_id, debit_account_id, journal_id, qty, description, svl_id, cost):
        self.ensure_one()
        AccountMove = self.env['account.move'].with_context(default_journal_id=journal_id)

        move_lines = self._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id, description)

        if move_lines:

            date = self.move_date or self._context.get('force_period_date', fields.Date.context_today(self))
            new_account_move = AccountMove.sudo().create({
                'journal_id': journal_id,
                'line_ids': move_lines,
                'date': date,
                'ref': description,
                'stock_move_id': self.id,
                'stock_valuation_layer_ids': [(6, None, [svl_id])],
                'type': 'entry',
            })
            new_account_move.post()
            
            