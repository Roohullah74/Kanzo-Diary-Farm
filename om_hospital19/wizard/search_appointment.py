from odoo import api, fields, models, _


class SearchAppointmentWizard(models.TransientModel):
    _name = "search.appointment.wizard"
    _description = "Search Appointment Wizard"

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    def action_search_appointment_m1(self):
        action = self.env.ref('om_hospital19.action_hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    def action_search_appointment_m2(self):
        action = self.env['ir.actions.actions']._for_xml_id("om_hospital19.action_hospital_appointment")
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    def action_search_appointment_m3(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'form',
            'target': 'new',
        }












# -*- coding: utf-8 -*-
# from odoo import api, fields, models, _
#
#
# class SearchAppointmentWizard(models.TransientModel):
#     _name = "search.appointment.wizard"
#     _description = "Search Appointment Wizard"
#
#     patient_id = fields.Many2one(
#         'hospital.patient',
#         string="Patient",
#         required=True
#     )
#     date_from = fields.Date(string="Date From")
#     date_to = fields.Date(string="Date To")
#
#     def action_search_appointment(self):
#         domain = [('patient_id', '=', self.patient_id.id)]
#         if self.date_from:
#             domain.append(('date_appointment', '>=', self.date_from))
#         if self.date_to:
#             domain.append(('date_appointment', '<=', self.date_to))
#         return {
#             'type': 'ir.actions.act_window',
#             'name': 'Appointments',
#             'res_model': 'hospital.appointment',
#             'view_mode': 'list,form',
#             'domain': domain,
#             'target': 'current',
#         }
#
#     def action_search_appointment_m1(self):
#         action = self.env['ir.actions.actions']._for_xml_id(
#             'om_hospital19.action_hospital_appointment'
#         )
#         action['domain'] = [('patient_id', '=', self.patient_id.id)]
#         return action
#
#     def action_search_appointment_m2(self):
#         action = self.env['ir.actions.actions']._for_xml_id(
#             'om_hospital19.action_hospital_appointment'
#         )
#         action['domain'] = [('patient_id', '=', self.patient_id.id)]
#         return action
#
#     def action_search_appointment_m3(self):
#         return {
#             'type': 'ir.actions.act_window',
#             'name': 'Appointments',
#             'res_model': 'hospital.appointment',
#             'view_mode': 'list,form',
#             'domain': [('patient_id', '=', self.patient_id.id)],
#             'target': 'current',
#         }

