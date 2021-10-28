from odoo import api, fields, models


class web(models.Model):
  _name = 'akademik.web'
  _description = 'Coba'

  name  = fields.Char(string='Name')
  email = fields.Char(string='Email')
