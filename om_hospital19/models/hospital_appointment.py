# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _order = "doctor_id,name,age"
    # it is  (desc,asc)mean that _order='doctor_id, this one show it like  order sequence of name 12345678 like that

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True, store=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], default='draft', string="Status", tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")

    prescription = fields.Text(string="Prescription")

    prescription_line_ids = fields.One2many(
        'appointment.prescription.lines', 'appointment_id',
        string="Prescription Lines"
    )



    def action_confirm(self):
        patients = self.env['hospital.patient'].search([])
        print(patients.mapped('name'))

        print('check user id',self.env.user.name)

        if self.env.user.name == 'Mitchell Admin':
            print("Full Access Granted")
        else:
            print("Limited Access")

        for rec in self:
            rec.state = 'confirm'




    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            if self.prescription_line_ids:
                pass
            rec.state = 'cancel'
        self.action_draft()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals_list)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''
            self.note = ''

    #        unlike
    # when us check the condition of the delete fuction you do not delete that whent done state many work we doing on this okay

    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError(
                    _("You Cannot Delete %s as it is in Done State") % rec.name
                )
        return super(HospitalAppointment, self).unlink()

    def action_url_lindin(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.linkedin.com/in/rooh-ullah-b21b07241/',
            'target': 'new',
        }


    # def action_url(self):
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'target': 'new',
    #         'url': 'https://apps.odoo.com/apps/modules/19.0/%s/' % self.prescription,
    #     } 









class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"

    name = fields.Char(string="Medicine", required=True)
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
