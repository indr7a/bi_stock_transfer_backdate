# -*- coding : utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from  datetime import datetime
from odoo import SUPERUSER_ID
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError,Warning


class StockPickingUpdate(models.Model):
	_inherit = 'stock.picking'

	remark = fields.Char(string="Remarks")

	def button_validate_custom(self):
		custom = self.env['stock.picking'].browse(self.id)

		for order in self:

			if custom.picking_type_id.code in ('outgoing'):
				return {
						'name':'Process Backdate and Remarks',
						'binding_view_types': 'form',
						'view_mode': 'form',
						'res_model': 'change.module',
						'type': 'ir.actions.act_window',
						'target': 'new',
						'res_id': False,
						'context': order.env.context,
					}
			else:
				return order.button_validate()
