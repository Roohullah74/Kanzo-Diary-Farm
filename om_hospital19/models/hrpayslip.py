from odoo import models

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def action_salary_letter(self):
        # Example action (you can customize)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Salary Letter',
            'res_model': 'hr.payslip',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }