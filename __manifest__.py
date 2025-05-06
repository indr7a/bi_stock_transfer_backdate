# -*- coding : utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name'          : 'Stock Transfer Backdate and Remarks in Odoo',
    'version'       : '16.0.0.5',
    'category'      : 'Warehouse',
    'summary'       : 'Stock transfer backdate stock back date inventory transfer backdating stock backdate stock accounting backdate inventory backdate delivery backdate stock force date on stock transfer inventory force date stock picking backdate inventory force date stock',
    'description'   : """The stock passing same date to move and account
    
     odoo stock transfer backdating stock transfers backdating inventory stock transfer backdating
     odoo inventory transfer backdating inventory transfer backdating
     odoo stock backdate Stock Transfers Backdate inventory Transfers Backdate
     odoo inventory backdating option stock backdating options Inventory Backdate Operations
     odoo Backdate Options backdating options Inventory Backdate Operations Backdate Operations
     odoo warehouse backdate operations warehouse stock backdate operations
     odoo stock backdate odoo stock remarks transfer remarks warehouse delivery remarks warehouse remarks
     odoo inventory remarks odoo stock backdate remarks
     odoo stock accounting backdate transfer backdate on stock odoo


     odoo stock transfer back dating stock transfers back dating inventory stock transfer back dating
     odoo inventory transfer back dating inventory transfer back dating odoo
     odoo stock back date Stock Transfers Back-date inventory Transfers Bac kdate
     odoo inventory back-dating option stock back dating options Inventory Back date Operations
     odoo Back-date Options back dating options Inventory Back date Operations Back date Operations
     odoo warehouse back date operations warehouse stock back date operations
     odoo stock back date odoo stock remarks transfer remarks warehouse delivery remarks warehouse remarks
     odoo inventory remarks odoo stock back date remarks
     odoo stock accounting back date transfer back date on inventory odoo

     odoo delivery backdating stock delivery backdating delivery transfer backdating
     odoo delivery order backdating delivery transfer backdating
     odoo delivery order backdate delivery order Backdate delivery Transfers Backdate
     odoo delivery backdating option delivery backdating options delivery operation Backdate on delivery order
     odoo Backdate Options backdating options delivery order Backdate Operations Backdate Operations for delivery
     odoo warehouse delivery order backdate operations delivery order backdate operations
     odoo delivery backdate odoo delivery remarks delivery order remarks delivery remarks stock delivery remarks
     odoo delivery process remarks odoo delivery process backdate remarks
     odoo delivery accounting backdate delivery backdate on goods transfer odoo
     odoo Inventory Adjustment backdating Inventory Adjustments backdating inventory backdating
     odoo inventory stock backdating inventory back date
     odoo Inventory Adjustment backdate Inventory Adjustment Transfers Backdate Inventory Adjustment Backdate
     odoo Inventory Adjustments backdating option Inventory Adjustments backdating options Inventory Adjustments Backdate Operations
     odoo Backdate Options backdating options Inventory Adjustments Backdate Operations Backdate Operations on Inventory Adjustments
     odoo warehouse backdate operations warehouse stock backdate operations
     odoo stock Inventory backdate odoo stock Inventory Adjustment remarks Inventory Adjustments remarks warehouseInventory Adjustments remarks
     odoo opening inventory remarks odoo Inventory Adjustment backdate remarks opening stock balance backdate
     odoo Inventory Adjustment accounting backdate Inventory Adjustments backdate on stock odoo


     odoo Inventory Adjustment back dating Inventory Adjustments back dating Inventory Adjustments back dating
     odoo Inventory Adjustment back dating Inventory Adjustments back dating odoo
     odoo Inventory Adjustments back date Inventory Adjustments Back-date Inventory Adjustment Back date
     odoo Inventory Adjustment back-dating option Inventory Adjustments back dating options Inventory Adjustment Back date Operations
     odoo Back-date Options back dating options Inventory Back date Operations Back date Operations
     odoo Inventory Adjustment back date operations Inventory Adjustments stock back date operations
     odoo Inventory Adjustment back date odoo Inventory Adjustment remarks transfer remarks Inventory Adjustments remarks warehouse remarks
     odoo Inventory Adjustment remarks odoo Inventory Adjustment back date remarks
     odoo Inventory Adjustment accounting back date Inventory Adjustment back date on inventory odoo

    
     entries so to avoid the problem this app will help to put custom back date and remarks.
     Custom back date will be transfer to stock entries and accounting entries  
    """,
    'author'        : 'BROWSEINFO',
    'website'       : 'https://www.browseinfo.com/demo-request?app=bi_stock_transfer_backdate&version=16&edition=Community',
    'currency': 'EUR',
    'price': 15, 
    'depends'       : ['base','sale_management','stock','stock_account', 'account'],
    'data'          : [
                        'security/ir.model.access.csv',
                        'wizard/stock_wizards_views.xml',
                        'wizard/wizard_scrap_order.xml',
                        'views/stockpicking_views.xml',
                        'views/stock_move_views.xml',
                        ],
    'installable'   : True,
    'auto_install'  : False,
    "live_test_url" : 'https://www.browseinfo.com/demo-request?app=bi_stock_transfer_backdate&version=16&edition=Community',
    "images":["static/description/Banner.gif"],
    'license': 'OPL-1' ,
}
