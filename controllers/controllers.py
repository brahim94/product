# -*- coding: utf-8 -*-
# from odoo import http


# class TechProduct(http.Controller):
#     @http.route('/tech_product/tech_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_product/tech_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_product.listing', {
#             'root': '/tech_product/tech_product',
#             'objects': http.request.env['tech_product.tech_product'].search([]),
#         })

#     @http.route('/tech_product/tech_product/objects/<model("tech_product.tech_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_product.object', {
#             'object': obj
#         })
