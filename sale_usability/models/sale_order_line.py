# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # add context so show sale data by default
    order_id = fields.Many2one(
        context={'show_sale': True}
    )
