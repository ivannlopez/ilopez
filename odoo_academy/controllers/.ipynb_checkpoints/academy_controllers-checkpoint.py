# -*- coding_ utf-8 -*-

from odoo import http

class Academy(http.Controller):
    @http.route('/academy', auth='public', website=True)
    def index(self, )