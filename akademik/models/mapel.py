from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class mapel(models.Model):

    _name               = "cdn.mapel"
    _description        = "Tabel Mata Pelajaran"

    mapel                = fields.Text(string='Nama Mapel')    
