# -*- coding: utf-8 -*-
from odoo import http

# class MethodGroupSumProduct(http.Controller):
#     @http.route('/method_group_sum_product/method_group_sum_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_group_sum_product/method_group_sum_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_group_sum_product.listing', {
#             'root': '/method_group_sum_product/method_group_sum_product',
#             'objects': http.request.env['method_group_sum_product.method_group_sum_product'].search([]),
#         })

#     @http.route('/method_group_sum_product/method_group_sum_product/objects/<model("method_group_sum_product.method_group_sum_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_group_sum_product.object', {
#             'object': obj
#         })