from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
 

    user_id = fields.Many2one(
        'res.users',
        string='Buyer'
    )
