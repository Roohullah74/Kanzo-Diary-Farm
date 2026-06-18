from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    invoice_policy = fields.Selection([
        ('test_policy', 'Test Policy'),
        ('order', 'Ordered quantities'),
        ('delivery', 'Delivered quantities'),
    ], string="Invoice Policy")


    invoice_policy1=fields.Selection([('test_olyy','Test_ploycy')])