# -*- coding : utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
import time
from datetime import datetime,date, timedelta


class RemarkSoldItem(models.TransientModel):
	_name = "change.module"
	_description = "Change Info"

	transfer_date = fields.Datetime(string="Transfer Date")
	remark = fields.Char(string="Remarks")

	def action_apply(self):
		if self.transfer_date >= datetime.now():
			raise UserError(_('Please Enter Correct Back Date'))

		active_model = self._context.get('active_model')
		picking_ids = False
		if active_model == 'sale.order':
			sale_order_ids = self.env['sale.order'].browse(self._context.get('active_ids'))
			picking_list = [sale_id.picking_ids.ids for sale_id in sale_order_ids][0]
			picking_ids = self.env['stock.picking'].browse(picking_list)
		elif active_model == 'stock.picking':
			picking_ids = self.env['stock.picking'].browse(self._context.get('active_ids'))
		elif active_model == 'stock.picking.type':
			picking_type_id = self.env['stock.picking.type'].browse(self._context.get('active_id'))
			picking_ids = self.env['stock.picking'].search([('picking_type_id','=', picking_type_id.id),('state','!=','cancel')], order='id desc', limit=1)
			
		if picking_ids:
			for picking in picking_ids.filtered(lambda x: x.state not in ('cancel')):
				for data in picking.move_ids:
					data.write({'date': self.transfer_date, 'move_remark': self.remark, 'move_date': self.transfer_date})
					for line in data.mapped('move_line_ids'):
						line.write({'date': self.transfer_date or fields.Datetime.now()})
				picking.button_validate()
				if picking.state == 'draft':
					picking.action_confirm()
					if picking.state != 'assigned':
						picking.action_assign()
						if picking.state != 'assigned':
							raise UserError(_("Could not reserve all requested products. Please use the \'Mark as Todo\' button to handle the reservation manually."))
				for move in picking.move_ids.filtered(lambda m: m.state not in ['done', 'cancel']):
					for move_line in move.move_line_ids:
						move_line.qty_done = move_line.reserved_uom_qty
						
				picking._action_done()
				for value in picking.move_ids.stock_valuation_layer_ids:
					self.env.cr.execute("""UPDATE stock_valuation_layer SET create_date=%s,product_id=%s,stock_move_id=%s,company_id=%s WHERE id=%s""" ,(self.transfer_date,value.product_id.id,value.stock_move_id.id,value.company_id.id,value.id))
				for account_move in picking.move_ids.account_move_ids:
					self.env.cr.execute("UPDATE account_move SET date = %s WHERE id = %s",
						[data.date, account_move.id]) 
		return True
