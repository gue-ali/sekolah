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
    semester            = fields.Selection(string='Semester', selection=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'),])
    
    nilai_ids = fields.One2many(comodel_name='akademik.nilai', inverse_name='penilaian_id', string='Nilai')
     

    @api.onchange('ruang_kelas')
    def onchange_ruang_kelas(self):
        if self.ruang_kelas:
            for rec in self:
                anggota = [(5,0,0)]
                for x in self.ruang_kelas.siswa_ids:
                    val = {
                        'name': x.id,
                        'nilai': '0'
                    }  
                    anggota.append((0,0,val))
                    rec.nilai_ids = anggota


class penilaian(models.Model):
    _name           = 'akademik.nilai'
    _description    = 'Nilai'

    penilaian_id    = fields.Many2one(comodel_name='cdn.nilai', string='Penilaian', required=True, ondelete='cascade')
    absen_id        = fields.Text(string='Kode Absen')
    name            = fields.Many2one(comodel_name='cdn.siswa', string='Siswa')
    P1              = fields.Integer(string='Nilai 1')
    P2              = fields.Integer(string='Nilai 2')
    P3              = fields.Integer(string='Nilai 3')
    P4              = fields.Integer(string='Nilai 4')
    P5              = fields.Integer(string='Nilai 5')
    P6              = fields.Integer(string='Nilai 6')

    