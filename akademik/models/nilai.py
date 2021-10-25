from odoo import models, fields, api
from odoo.exceptions import UserError, Warning


class nilai(models.Model):
    _name               = "cdn.nilai"
    _description        = "Tabel Nilai"
    _rec_name           = 'user_guru'

    #user_guru           = fields.One2many(comodel_name='cdn.guru', inverse_name='guru_id', string='Nama Guru')
    
    user_guru           = fields.Many2one(comodel_name='hr.employee', string='Nama Guru', store=True)
    ruang_kelas         = fields.Many2one(comodel_name='cdn.ruang_kelas', string='Ruang kelas')
    mata_pelajaran      = fields.Selection(string='Status Pernikahan', selection=[('single', 'Belum Kawin'), ('married', 'Menikah'),('divorced', 'Cerai Hidup'),('cerai', 'Cerai Mati'),], related='user_guru.marital')
    nilai_ids           = fields.Many2many('akademik.nilai', string='Nilai')    

class penilaian(models.Model):
    _name           = 'akademik.nilai'
    _description    = 'Nilai'

    absen_id        = fields.Text(string='Kode Absen')
    siswa_ids       = fields.Many2one(comodel_name='cdn.siswa', string='Siswa')
    nilai           = fields.Integer(string='Nilai')
    