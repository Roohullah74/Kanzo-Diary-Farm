# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _order = "reference"

    name = fields.Char(string='Name', required=True, tracking=True)

    # ✅ Links to hospital.doctor
    doctor_id = fields.Many2one(
        'hospital.doctor',
        string="Doctor",
        ondelete='set null'
    )

    reference = fields.Char(
        string='Order Reference',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New')
    )

    age = fields.Integer(string='Age', tracking=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)

    note = fields.Text(string='Description')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], default='draft', string="Status", tracking=True)

    responsible_id = fields.Many2one('res.partner', string="Responsible")

    appointment_count = fields.Integer(
        string='Appointment Count',
        compute='_compute_appointment_count'
    )

    image = fields.Binary(string="Patient Image")

    appointment_ids = fields.One2many(
        'hospital.appointment',
        'patient_id',
        string="Appointments"
    )

    product_ids = fields.Many2many('product.product', string="Products")
    product_count = fields.Integer(compute="_compute_product_count")

    stock_move_ids = fields.One2many(
        'stock.move',
        'reference_id',
        string="Stock Moves"
    )
    stock_move_count = fields.Integer(compute="_compute_stock_moves")

    def _compute_product_count(self):
        for rec in self:
            rec.product_count = len(rec.product_ids)

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([
                ('patient_id', '=', rec.id)
            ])

    def _compute_stock_moves(self):
        for rec in self:
            rec.stock_move_count = self.env['stock.move'].search_count([
                ('reference_id', '=', rec.id)
            ])

    # ✅ Fixed — added @api.depends
    @api.depends('name', 'reference')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.reference or ''} - {rec.name or ''}"

    def action_confirm(self):
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
            rec.state = 'cancel'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('note'):
                vals['note'] = 'New Patient'
            if vals.get('reference', _('New')) == _('New'):
                vals['reference'] = self.env['ir.sequence'].next_by_code(
                    'hospital.patient'
                ) or _('New')
        return super().create(vals_list)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if self.search([('name', '=', rec.name), ('id', '!=', rec.id)]):
                raise ValidationError("Name already exists!")

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 0:
                raise ValidationError("Age must be greater than 0!")

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if 'age' in fields:
            res['age'] = 12
        if 'note' in fields:
            res['note'] = 'This is a new patient'
        return res

    # ✅ Fixed view_mode
    def action_open_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'context': {'default_patient_id': self.id},
            'view_mode': 'list,form',
        }

    # ✅ Fixed view_mode
    def action_open_inventory(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Inventory Moves',
            'res_model': 'stock.move',
            'view_mode': 'list,form',
            'domain': [('reference_id', '=', self.id)],
        }


class StockMove(models.Model):
    _inherit = 'stock.move'

    reference_id = fields.Many2one(
        'hospital.patient',
        string="Patient"
    )

# # -*- coding: utf-8 -*-
# from odoo import api, fields, models, _
# from odoo.exceptions import ValidationError

# class HospitalPatient(models.Model):
#     _name = "hospital.patient"
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#     _description = "Hospital Patient"
#     _order = "reference"
#
#     # ---------------- BASIC FIELDS ----------------
#
#     # Patient Name
#     name = fields.Char(string='Name', required=True, tracking=True)
#
#     # ✅ Links to hospital.doctor model
#     doctor_id = fields.Many2one(
#         'hospital.doctor',
#         string="Doctor",
#         ondelete='set null'  # ✅ when doctor deleted → patient doctor becomes empty
#     )
#     # Unique reference number (auto sequence)
#     reference = fields.Char(
#         string='Order Reference',
#         required=True,
#         copy=False,
#         readonly=True,
#         default=lambda self: _('New')
#     )
#
#     # Age of patient
#     age = fields.Integer(string='Age', tracking=True)
#
#     # Gender selection field
#     gender = fields.Selection([
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     ], required=True, default='male', tracking=True)
#
#     # Extra notes / description
#     note = fields.Text(string='Description')
#
#     # ---------------- IMPORTANT FIELD (FOR SECURITY RULES) ----------------
#
#     # 👇 This field is used in RECORD RULE (ir.rule)
#     # Each patient is assigned to a doctor (logged-in user)
#     # doctor_id = fields.Many2one(
#     #     'res.users',
#     #     string='Doctor'
#     # )
#
#     # ---------------- STATUS FIELD ----------------
#
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('confirm', 'Confirmed'),
#         ('done', 'Done'),
#         ('cancel', 'Cancelled')
#     ], default='draft', string="Status", tracking=True)
#
#     # Who is responsible (optional partner)
#     responsible_id = fields.Many2one('res.partner', string="Responsible")
#
#     # ---------------- COMPUTED FIELDS ----------------
#
#     # Count of appointments related to this patient
#     appointment_count = fields.Integer(
#         string='Appointment Count',
#         compute='_compute_appointment_count'
#     )
#
#     # Patient image
#     image = fields.Binary(string="Patient Image")
#
#     # One patient → many appointments
#     appointment_ids = fields.One2many(
#         'hospital.appointment',
#         'patient_id',
#         string="Appointments"
#     )
#
#     # Many2many relation with products (inventory/items)
#     product_ids = fields.Many2many('product.product', string="Products")
#
#     # Count products
#     product_count = fields.Integer(compute="_compute_product_count")
#
#     # ---------------- STOCK / INVENTORY ----------------
#
#     # One patient → many stock moves
#     stock_move_ids = fields.One2many(
#         'stock.move',
#         'reference_id',
#         string="Stock Moves"
#     )
#
#     stock_move_count = fields.Integer(compute="_compute_stock_moves")
#
#     # ---------------- COMPUTE METHODS ----------------
#
#     # Count products
#     def _compute_product_count(self):
#         for rec in self:
#             rec.product_count = len(rec.product_ids)
#
#     # Count appointments
#     def _compute_appointment_count(self):
#         for rec in self:
#             rec.appointment_count = self.env['hospital.appointment'].search_count([
#                 ('patient_id', '=', rec.id)
#             ])
#
#     # Count stock moves
#     def _compute_stock_moves(self):
#         for rec in self:
#             rec.stock_move_count = self.env['stock.move'].search_count([
#                 ('reference_id', '=', rec.id)
#             ])
#
#     # ---------------- DISPLAY NAME ----------------
#
#     # Custom display name (shown in UI dropdowns)
#     def _compute_display_name(self):
#         for rec in self:
#             rec.display_name = f"{rec.reference or ''} - {rec.name or ''}"
#
#     # ---------------- STATE ACTIONS ----------------
#
#     def action_confirm(self):
#         for rec in self:
#             rec.state = 'confirm'
#
#     def action_done(self):
#         for rec in self:
#             rec.state = 'done'
#
#     def action_draft(self):
#         for rec in self:
#             rec.state = 'draft'
#
#     def action_cancel(self):
#         for rec in self:
#             rec.state = 'cancel'
#
#     # ---------------- CREATE OVERRIDE ----------------
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         for vals in vals_list:
#
#             # default note if empty
#             if not vals.get('note'):
#                 vals['note'] = 'New Patient'
#
#             # auto generate reference number
#             if vals.get('reference', _('New')) == _('New'):
#                 vals['reference'] = self.env['ir.sequence'].next_by_code(
#                     'hospital.patient'
#                 ) or _('New')
#
#         return super().create(vals_list)
#
#     # ---------------- VALIDATION (CONSTRAINTS) ----------------
#
#     # Prevent duplicate patient names
#     @api.constrains('name')
#     def check_name(self):
#         for rec in self:
#             if self.search([('name', '=', rec.name), ('id', '!=', rec.id)]):
#                 raise ValidationError("Name already exists!")
#
#     # Age must be greater than 0
#     @api.constrains('age')
#     def check_age(self):
#         for rec in self:
#             if rec.age <= 0:
#                 raise ValidationError("Age must be greater than 0!")
#
#     # ---------------- DEFAULT VALUES ----------------
#
#     @api.model
#     def default_get(self, fields):
#         res = super().default_get(fields)
#
#         if 'age' in fields:
#             res['age'] = 12
#
#         if 'note' in fields:
#             res['note'] = 'This is a new patient'
#
#         return res
#
#     # ---------------- ACTION BUTTON ----------------
#
#     def action_open_appointments(self):
#         return {
#             'type': 'ir.actions.act_window',
#             'name': 'Appointments',
#             'res_model': 'hospital.appointment',
#             'domain': [('patient_id', '=', self.id)],
#             'context': {'default_patient_id': self.id},
#             'view_mode': 'form,list',
#         }
#
#     def action_open_inventory(self):
#         return {
#             'type': 'ir.actions.act_window',
#             'name': 'Inventory Moves',
#             'res_model': 'stock.move',
#             'view_mode': 'form,list',
#             'domain': [('reference_id', '=', self.id)],
#         }
#
#
# # ---------------- STOCK MOVE EXTENSION ----------------
#
# class StockMove(models.Model):
#     _inherit = 'stock.move'
#
#     # Link stock move to patient
#     reference_id = fields.Many2one(
#         'hospital.patient',
#         string="Patient"
#     )