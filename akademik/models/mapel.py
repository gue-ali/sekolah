from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class mapel(models.Model):

    _name               = "cdn.mapel"
    _description        = "Tabel Nilai Siswa"

    name                = fields.Many2one(comodel_name="cdn.master_mapel",  string="Mata Pelajaran", required=True, copy=False, help="")
    # siswa_ids           = fields.Many2many('cdn.siswa','mapel_siswa_rel','mapel_id','siswa_id', string='Daftar Siswa', domain=[('active', '=', True)])
    tahunajaran_id      = fields.Many2one(comodel_name="cdn.ref_tahunajaran",  string="Tahun Pelajaran", required=True, help="")
    pengajar_id        = fields.Many2one(comodel_name="cdn.guru",  string="Pengajar",  help="")
    jenjang             = fields.Selection(selection=[('sd','SD/MI'),('smp','SMP/MTS'),('sma','SMA/MA')],  string="Jenjang", related='name.jenjang', help="")
    tingkat             = fields.Selection(selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')],  string="Kelas", related='name.tingkat', help="")
    jurusan_id          = fields.Many2one(comodel_name='cdn.master_jurusan', string='Jurusan / Peminatan', related='name.jurusan_id')
    # mapel_lines   = fields.One2many(comodel_name='cdn.mapel_lines', inverse_name='mapel_id', string='')
    
    

    keterangan          = fields.Char( string="Keterangan",  help="")

    _sql_constraints = [('mapel_uniq', 'unique(name, tahunajaran_id)', 'Data Mata Pelajaran dan Tahun Pelajaran harus unik !')]

    def update_kelas_siswa(self):
        for rec in self.siswa_ids:
            if (rec.mapel_id) and (rec.mapel_id.id != self.id):
                raise UserError(("Siswa atas nama %s Sudah Terdaftar di Ruang %s ! Silakan dihapus dulu data siswa ybs di ruang tersebut" % (rec.name,rec.mapel_id.display_name)))
            rec.write({'mapel_id': self.id})

        message_id = self.env['message.wizard'].create({'message': _("Update Mata Pelajaran - SUKSES !!")})
        return {
            'name': _('Successfull'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'message.wizard',
            # pass the id
            'res_id': message_id.id,
            'target': 'new'
        }
        # return True

class MessageWizard(models.TransientModel):
    _name = 'message.wizard'

    message = fields.Text('Informasi', required=True)

    def action_ok(self):
        """ close wizard"""
        return {'type': 'ir.actions.act_window_close'}
    
    
    
    
    
