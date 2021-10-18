from odoo import api, fields, models


class absensi(models.Model):
    _name = 'akademik.absensi'
    _description = 'Absensi'

    name = fields.Char(string='Name')