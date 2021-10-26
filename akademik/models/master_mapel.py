from odoo import models, fields, api


class master_mapel(models.Model):

    _name               = "master.mapel"
    _description        = "Tabel Master Mata Pelajaran"

    name                = fields.Text(string="Nama Mata Pelajaran",  help="", required=True, copy=False)
    jenjang             = fields.Selection(selection=[('sd','SD/MI'),('smp','SMP/MTS'),('sma','SMA/MA')],  string="Jenjang", required=True, help="")
    jurusan_id          = fields.Many2one(comodel_name='cdn.master_jurusan', string='Jurusan / Peminatan', required=True)

    keterangan          = fields.Char(string="Keterangan",  help="")