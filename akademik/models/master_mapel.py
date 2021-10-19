#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class master_mapel(models.Model):

    _name               = "cdn.master_mapel"
    _description        = "Tabel Data Mata Pelajaran"

    name                = fields.Char( required=True, string="Nama Mata Pelajaran",  help="",  copy=False)
    jenjang             = fields.Selection(selection=[('sd','SD/MI'),('smp','SMP/MTS'),('sma','SMA/MA')],  string="Jenjang", required=True, help="")
    tingkat             = fields.Selection(selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')],  string="Kelas", required=True, help="")
    jurusan_id          = fields.Many2one(comodel_name='cdn.master_jurusan', string='Jurusan / Peminatan')
    

    _sql_constraints = [('master_mapel_uniq', 'unique(name)', 'Nama Mata Pelajaran harus unik !')]


class master_jurusan(models.Model):
    _name               = 'cdn.master_jurusan'
    _description        = 'Tabel Master Data Jurusan SMA'

    name                = fields.Char(string='Nama Bidang/Jurusan', required=True, copy=False)
    active              = fields.Boolean(string='Active', default=True)
    keterangan          = fields.Char(string='Keterangan')

    _sql_constraints = [('master_jurusan_uniq', 'unique(name)', 'Master Jurusan/Bidang Study harus unik !')]
    
    

