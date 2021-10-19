from odoo import api, fields, models


class absensi(models.Model):
    _name = 'akademik.absensi'
    _description = 'Absensi'

    name        = fields.Char(string='Nama Guru')
    tanggal     = fields.Date(string='Tanggal')
    mata_pelajaran = fields.Text(string='Mata Pelajaran')
    ruang_kelas = fields.Many2one(comodel_name='cdn.ruang_kelas', string='Ruang kelas')
    