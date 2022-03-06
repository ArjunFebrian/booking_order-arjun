# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrder-arjun(http.Controller):
#     @http.route('/booking_order-arjun/booking_order-arjun/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order-arjun/booking_order-arjun/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order-arjun.listing', {
#             'root': '/booking_order-arjun/booking_order-arjun',
#             'objects': http.request.env['booking_order-arjun.booking_order-arjun'].search([]),
#         })

#     @http.route('/booking_order-arjun/booking_order-arjun/objects/<model("booking_order-arjun.booking_order-arjun"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order-arjun.object', {
#             'object': obj
#         })
