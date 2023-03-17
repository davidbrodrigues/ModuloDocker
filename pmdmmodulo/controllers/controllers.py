# -*- coding: utf-8 -*-
# from odoo import http


# class Pmdmmodulo(http.Controller):
#     @http.route('/pmdmmodulo/pmdmmodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pmdmmodulo/pmdmmodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pmdmmodulo.listing', {
#             'root': '/pmdmmodulo/pmdmmodulo',
#             'objects': http.request.env['pmdmmodulo.pmdmmodulo'].search([]),
#         })

#     @http.route('/pmdmmodulo/pmdmmodulo/objects/<model("pmdmmodulo.pmdmmodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pmdmmodulo.object', {
#             'object': obj
#         })
