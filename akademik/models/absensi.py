from odoo import api, fields, models


class absensi(models.Model):
    _name           = 'akademik.absensi'
    _description    = 'Absensi'
    _rec_name       = 'user_guru'
    
    name            = fields.Datetime(string='Waktu', required=True, readonly=False, select=True, default=lambda self: fields.datetime.now())
    user_guru       = fields.Many2one(comodel_name='hr.employee', string='Nama Guru')
    ruang_kelas     = fields.Many2one(comodel_name='cdn.ruang_kelas', string='Ruang kelas',  required=True)
    mata_pelajaran  = fields.Selection(string='Status Pernikahan', selection=[('single', 'Belum Kawin'), ('married', 'Menikah'),('divorced', 'Cerai Hidup'),('cerai', 'Cerai Mati'),], related='user_guru.marital')
    absen_ids       = fields.One2many(comodel_name='akademik.kehadiran', inverse_name='absen_id', string='Absen')
    
    @api.onchange('ruang_kelas')
    def onchange_ruang_kelas(self):
        if self.ruang_kelas:
            for rec in self:
                anggota = [(5,0,0)]
                #self.absensi_lines = [(5,0,0)]
                for x in self.ruang_kelas.siswa_ids:
                    val = {
                        'name': x.id
                    }
                    anggota.append((0,0,val))
                rec.absen_ids = anggota


class kehadiran(models.Model):
    _name           = 'akademik.kehadiran'
    _description    = 'Kehadiran'

    absen_id        = fields.Many2one('akademik.absensi', string='Nama Guru', required=True, ondelete='cascade')
    tanggal         = fields.Datetime(string='Waktu', related='absen_id.name')
    name            = fields.Many2one(comodel_name='cdn.siswa', string='Siswa')
    nis             = fields.Char(string="No Induk Siswa", required=True,  help="", related='name.nis')
    absen           = fields.Selection(string='Kehadiran', selection=[('hadir', 'Hadir'), ('sakit', 'Sakit'),  ('ijin', 'Ijin'),  ('alpa', 'Alpa'),])    
    keterangan      = fields.Text(string='Keterangan')