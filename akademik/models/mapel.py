from odoo import models, fields, api


class mapel(models.Model):

    _name               = "akademik.mapel"
    _description        = "Tabel Mata Pelajaran"

    name                = fields.Many2one(comodel_name="cdn.master_kelas",  string="Mata pelajaran", required=True, copy=False, help="")
    tahunajaran_id      = fields.Many2one(comodel_name="cdn.ref_tahunajaran",  string="Tahun Pelajaran", required=True, help="")
    pengajar_id         = fields.Many2one(comodel_name="cdn.guru",  string="Pengajar",  help="")
    jenjang             = fields.Selection(selection=[('sd','SD/MI'),('smp','SMP/MTS'),('sma','SMA/MA')],  string="Jenjang", related='name.jenjang', help="")
    tingkat             = fields.Selection(selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')],  string="Kelas", related='name.tingkat', help="")
    jurusan_id          = fields.Many2one(comodel_name='cdn.master_jurusan', string='Jurusan / Peminatan', related='name.jurusan_id')
       

    keterangan          = fields.Char( string="Keterangan",  help="")

    _sql_constraints = [('ruang_kelas_uniq', 'unique(name, tahunajaran_id)', 'Data Mata Pelajaran dan Tahun Pelajaran harus unik !')] 
