from odoo import api, fields, models


class absensi(models.Model):
    _name           = 'akademik.absensi'
    _description    = 'Absensi'
    _rec_name       = 'user_guru'

    user_guru       = fields.Many2one(comodel_name='hr.employee', string='Nama Guru', store=True)
    # siswa_ids       = fields.Many2many('cdn.siswa','ruang_kelas_siswa_rel','ruang_kelas_id','siswa_id', string='Daftar Siswa', domain=[('active', '=', True)])
    # petugas_id          = fields.Many2one(comodel_name='hr.employee', string='Petugas Penerima', readonly=True)
    tanggal       = fields.Datetime(string='Waktu', required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
    # mata_pelajaran = fields.Text(string='Mata Pelajaran')
    ruang_kelas     = fields.Many2one(comodel_name='cdn.ruang_kelas', string='Ruang kelas')
    mata_pelajaran  = fields.Selection(string='Status Pernikahan', selection=[('single', 'Belum Kawin'), ('married', 'Menikah'),('divorced', 'Cerai Hidup'),('cerai', 'Cerai Mati'),], related='user_guru.marital')
    # jenjang             = fields.Selection(selection=[('sd','SD/MI'),('smp','SMP/MTS'),('sma','SMA/MA')],  string="Jenjang", related='name.jenjang', help="")
    # siswa_ids       = fields.Many2many(string='Siswa', related='ruang_kelas.siswa_ids')
    # siswa_ids       = fields.Many2many(string='Siswa', related='ruang_kelas.siswa_ids')
    absen_ids        = fields.Many2many('akademik.kehadiran', string='Absen')
    


class kehadiran(models.Model):
    _name           = 'akademik.kehadiran'
    _description    = 'Kehadiran'

    absen_id        = fields.Text(string='Kode Absen')
    siswa_ids       = fields.Many2one(comodel_name='cdn.siswa', string='Siswa')
    absen           = fields.Selection(string='Kehadiran', selection=[('hadir', 'Hadir'), ('sakit', 'Sakit'),])


    @api.model
    def create(self, vals):
        # cek = self.env['res.users'].search([('id', '=', self.env.user.id)])
        # # print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'. cek)
        # if cek.user_id:
        #     vals['user_guru'] = cek.user_id.id

        # set = super(absensi, self).create(vals)
        self.user_guru = self.env.user.name.id
        return set
