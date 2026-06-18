from odoo import fields, models, _
from odoo.exceptions import UserError


class CreateAppointmentWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Appointment Report Wizard"

    patient_id1 = fields.Many2one(
        'hospital.patient',
        string="Patient",
        ondelete='set null'
    )
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')

    def action_print_report(self):
        # build filter domain
        domain = []
        if self.patient_id1:
            domain.append(('patient_id', '=', self.patient_id1.id))
        if self.date_from:
            domain.append(('date_appointment', '>=', self.date_from))
        if self.date_to:
            domain.append(('date_appointment', '<=', self.date_to))

        # fetch appointment records
        appointments = self.env['hospital.appointment'].search(domain)

        if not appointments:
            raise UserError(_("No appointments found for the selected filters."))

        return self.env.ref(
            'om_hospital19.action_report_appointment'
        ).with_context(
            patient_name=self.patient_id1.name if self.patient_id1 else 'All Patients',
            date_from=str(self.date_from) if self.date_from else '',
            date_to=str(self.date_to) if self.date_to else '',
        ).report_action(appointments)

# # appointment_report_wizard.py
# from odoo import fields, models, _
#
#
# class CreateAppointmentWizard(models.TransientModel):
#     _name = "appointment.report.wizard"  # ← must match XML model
#     _description = "Appointment Report Wizard"
#
#     patient_id1 = fields.Many2one(
#         'hospital.patient',
#         string="Patient",
#         ondelete='set null'
#     )
#     date_from = fields.Date(string='Date From')
#     date_to = fields.Date(string='Date To')
#
#
#     def action_print_report(self):
#         domain = []
#
#         if self.patient_id1:
#             domain.append(('patient_id', '=', self.patient_id1.id))
#         if self.date_from:
#             domain.append(('date_appointment', '>=', self.date_from))
#         if self.date_to:
#             domain.append(('date_appointment', '<=', self.date_to))
#
#         appointments = self.env['hospital.appointment'].search(domain)
#
#         return self.env.ref(
#             'om_hospital19.action_report_appointment'
#         ).with_context(
#             patient_name=self.patient_id1.name if self.patient_id1 else '',
#             date_from=self.date_from,
#             date_to=self.date_to,
#         ).report_action(appointments)
