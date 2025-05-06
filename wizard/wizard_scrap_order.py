# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime,date, timedelta
from odoo.tools import float_compare
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class WizardScrapOrder(models.TransientModel):
	_name = 'wizard.scrap.order.backdate'
	_description="Wizard Scrap Order"

	scrap_backdate = fields.Datetime('Backdate',required=True)
	scrap_remarks = fields.Char('Remarks', required=True)

	def scrap_order_confirm(self):

		today = datetime.now().strftime(DEFAULT_SERVER_DATE_FORMAT)
		back_date = self.scrap_backdate.strftime(DEFAULT_SERVER_DATE_FORMAT)
		
		if back_date == today or back_date > today:
			raise ValidationError(_('You Can Select Back Date Only.'))

		stock_scrap_id = self.env['stock.scrap'].browse(self._context.get('active_id'))

		stock_scrap_id.do_scrap()

		jornal_id = self.env['account.journal'].search([('code', '=', 'MISC')])

		stock_scrap_id.write({'date_done':self.scrap_backdate,'move_remarks_scrap':self.scrap_remarks})

		for stock_scrap_move in stock_scrap_id.move_id:
			stock_scrap_move.write({'date':self.scrap_backdate,'move_remark':self.scrap_remarks})

			for stock_scrap_move_line in stock_scrap_move.move_line_ids:
				stock_scrap_move_line.write({'date':stock_scrap_move.date,
					'move_remarks_line':self.scrap_remarks})

			for value in stock_scrap_move.stock_valuation_layer_ids:
					self.env.cr.execute("""UPDATE stock_valuation_layer SET create_date=%s,product_id=%s,stock_move_id=%s,company_id=%s WHERE id=%s""" ,(self.scrap_backdate,value.product_id.id,value.stock_move_id.id,value.company_id.id,value.id))

			for account_move in stock_scrap_move.account_move_ids:
				self.env.cr.execute("UPDATE account_move SET date = %s WHERE id = %s",
					[self.scrap_backdate, account_move.id]) 



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: