from odoo import models, fields


class UCP(models.Model):
    _name = 'ucp'
    _description='university of central punjab management'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    cnic = fields.Integer(string='CNIC')
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-')
    ], string='Blood Group')
    email = fields.Char(string='Email')
