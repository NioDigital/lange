# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website.controllers.main import Website


class WebsiteTransform(Website):

    @http.route('/', type='http', auth="user", website=True, sitemap=True)
    def index(self, **kw):
        return super(WebsiteTransform, self).index(**kw)
