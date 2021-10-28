from odoo import http
from odoo.http import request

class absensi(http.Controller):
   @http.route('/absensi', type='http', auth='public', website=True)
   def absensi(self , **kw):
     return  request.render('akademik.absensi', {})

   @http.route('/create/coba', type='http', auth='public', website=True)
   def create_coba(self , **kw):
     request.env['akademik.web'].sudo().create(kw)
     return  request.render('akademik.peringatan', {})
