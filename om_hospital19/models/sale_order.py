# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description')
    task_id = fields.Many2one( 'project.task' ,string='Sale Description')
    custom_template_id = fields.Many2one('product.template', string="")

