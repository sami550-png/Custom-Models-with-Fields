from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    cnic = fields.Char(string='CNIC')
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    ], string='Blood Group')
    email = fields.Char(string='Email')
