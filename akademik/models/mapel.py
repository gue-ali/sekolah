from odoo import models, fields, api


class mapel(models.Model):

    _name               = "akademik.mapel"
    _description        = "Tabel Mata Pelajaran"


    name                = fields.Text(string='Mata Pelajaran', required=True)
    pengajar_id         = fields.Many2one(comodel_name="cdn.guru",  string="Pengajar",  help="", required=True)
    tahunajaran_id      = fields.Many2one(comodel_name="cdn.ref_tahunajaran",  string="Tahun Pelajaran", required=True, help="")
    jenjang             = fields.Selection(selection=[('sd','SD/MI'),('smp','SMP/MTS'),('sma','SMA/MA')],  string="Jenjang", help="", required=True)
    tingkat             = fields.Selection(selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')],  string="Kelas", help="", required=True)
    jurusan_id          = fields.Many2one(comodel_name='cdn.master_jurusan', string='Jurusan / Peminatan', required=True)

    keterangan          = fields.Char( string="Keterangan",  help="")

