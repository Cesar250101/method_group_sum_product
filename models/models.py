# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Productos(models.Model):
    _inherit = 'product.template'

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None,
                   orderby=False, lazy=True):
        res = super(Productos, self).read_group(domain, fields, groupby,
            offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        if 'qty_available' in fields:
            for line in res:
                if '__domain' in line:
                    stock = 0.0
                    lines = self.search(line['__domain'])
                    for item in lines:
                        stock += item.qty_available
                    line['qty_available'] = stock
        return res
