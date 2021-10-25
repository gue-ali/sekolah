from odoo import models, fields, api
from odoo.exceptions import UserError, Warning


class nilai(models.Model):
    _name               = "cdn.nilai"
    _description        = "Tabel Nilai"
    _rec_name           = 'user_guru'
    
    user_guru           = fields.Many2one(comodel_name='hr.employee', string='Nama Guru', store=True)
    ruang_kelas         = fields.Many2one(comodel_name='cdn.ruang_kelas', string='Ruang kelas')
    mata_pelajaran      = fields.Selection(string='Status Pernikahan', selection=[('single', 'Belum Kawin'), ('married', 'Menikah'),('divorced', 'Cerai Hidup'),('cerai', 'Cerai Mati'),], related='user_guru.marital')
    nilai_ids           = fields.Many2many('akademik.nilai', string='Nilai')  

    @api.onchange('ruang_kelas')
    def onchange_ruang_kelas(self):
        if self.ruang_kelas:
            for rec in self:
                anggota = [(5,0,0)]
                #self.absensi_lines = [(5,0,0)]
                for x in self.ruang_kelas.siswa_ids:
                    val = {
                        'name': x.id,
                        'nilai' : '0'
                    }
                    anggota.append((0,0,val))
                rec.absen_ids = anggota  

class penilaian(models.Model):
    _name           = 'akademik.nilai'
    _description    = 'Nilai'

    siswa_ids       = fields.Many2one(comodel_name='cdn.siswa', string='Siswa')
    nilai           = fields.Integer(string='Nilai')
    