# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True, copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string="Patient Image")
    appointment_count = fields.Integer(
        string='Appointment Count',
        compute='_compute_appointment_count'
    )
    active = fields.Boolean(string="Active", default=True)
    # hospital_doctor.py
    user_id = fields.Many2one('res.users', string="Linked User")

    def copy(self, default=None):


        self.ensure_one()

        default = dict(default or {})

        base_name = self.doctor_name or ''

        # Always set same copy name
        default['doctor_name'] = f"{base_name} copy"
        default['note'] = "Copied Record"


        return super().copy(default)

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count(
                [('doctor_id', '=', rec.id)]
            )

