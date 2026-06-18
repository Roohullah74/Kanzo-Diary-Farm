# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date', required=False)
    patient_id = fields.Many2one(
        'hospital.patient',
        string="Patient",
        required=True
    )
    doctor_id = fields.Many2one(
        'hospital.doctor',
        string="Doctor",
        required=True
    )

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'date_appointment': self.date_appointment,
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)

        # Whatdoes “Return View from Python” mean?
        # opens a form view How to return a view (action) from Python code in Odoo 19

        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'target': 'new',
        }

    # @api.model
    # def default_get(self, fields):
    #     # EXTENDS 'base'
    #     results = super().default_get(fields)
    #     if 'move_ids' in fields and 'move_ids' not in results:
    #         move_ids = self.env.context.get('active_ids', [])
    #         results['move_ids'] = [Command.set(move_ids)]
    #     return results

    # method2 ✅ 🔥 WAY 4: Open Wizard (Popup)
    # def action_open_wizard(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Wizard',
    #         'res_model': 'hospital.wizard',
    #         'view_mode': 'form',
    #         'target': 'new',
    #     }

    #     ✅ 🔥 WAY 5: Use Only Domain (Without XML)
    # def action_view_appointments(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'hospital.appointment',
    #         'view_mode': 'tree,form',
    #         'domain': [('patient_id', '=', self.id)],
    #     }
    # 📌 4. Example 2 → Open Tree + Form View
    # def action_view_patients(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Patients',
    #         'res_model': 'hospital.patient',
    #         'view_mode': 'tree,form',
    #         'target': 'current',
    #     }
    # 📌 5. Example 3 → Open Related Records (IMPORTANT)
    # def action_view_appointments(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Appointments',
    #         'res_model': 'hospital.appointment',
    #         'view_mode': 'tree,form',
    #         'domain': [('patient_id', '=', self.id)],
    #         'context': {'default_patient_id': self.id},
    #     }
    # 🔥 6. Example 4 → Smart Button (Best Practice)
    # < button
    # name = "action_view_appointments"
    # type = "object"
    # string = "Appointments"
    #
    # class ="oe_stat_button" / >

    # 📌 7. Example 5 → Open Specific View ID
    # def action_open_custom_view(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Patient Form',
    #         'res_model': 'hospital.patient',
    #         'view_mode': 'form',
    #         'view_id': self.env.ref('your_module.patient_form_view').id,
    #         'res_id': self.id,
    #     }


    # 📌 8. Example 6 → Open Popup (Wizard)
    # def action_open_wizard(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Wizard',
    #         'res_model': 'hospital.wizard',
    #         'view_mode': 'form',
    #         'target': 'new',  # popup
    #     }

    # ⚠️ Important Fields Explained
    # Key	Meaning
    # type	must be ir.actions.act_window
    # res_model	model name
    # view_mode	tree, form, kanban
    # res_id	specific record
    # domain	filter records
    # context	pass default values
    # target	current or new (popup)

    # def action_view_appointments(self):
    #     self.ensure_one()
    #
    #     action = self.env.ref('om_hospital19.action_hospital_appointment').read()[0]
    #
    #     action['domain'] = [('patient_id', '=', self.id)]
    #     # action['context'] = {'default_patient_id': self.id}
    #
    #     return action
   # it is using for ressult same if pringt like appointment rooullah name all will display

    def action_view_appointments(self):
        action = self.env['ir.actions.actions']._for_xml_id(
            'om_hospital19.action_hospital_appointment'
        )
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    @api.model
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)

        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')

        # ADD THIS FOR SEQUENCE
        res['name'] = self.env['ir.sequence'].next_by_code('appointment.sequence')

        return res
