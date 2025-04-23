from odoo import models, fields, api


class firstreport(models.Model):
    _inherit = 'account.move'


    sami = fields.Char(string='sami')

