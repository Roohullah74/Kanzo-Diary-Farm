from  odoo import fields,models,api

class patientReportwizard(models.TransientModel):
    _name = 'patient.report.wizard'
    _description = 'Patiend Report Discription'

    gender= fields.Selection([('male','Male'),('female','Female'),('other','Other')],string='Gender')
    age=fields.Integer(string='Age')

    def action_print_report1(self):
        data={
            'form_data':self.read()[0]
        }
        return self.env.ref('om_hospital19.action_report_all_patient_details').report_action(self,dat=data)

   