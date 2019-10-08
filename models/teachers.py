from odoo import fields
from odoo import models


class Teacher(models.Model):
    _name = "teachers"
    _description = "Description Teachers"

    name = fields.Char(string='Nombre', required=True)
    first_last_name = fields.Char(string='Primer apellido', required=True)
    second_last_name = fields.Char(string='Segundo apellido', required=True)
    age = fields.Integer(string="Edad")
    gender = fields.Selection([('M', 'Masculino'), ('F', 'Femenino')], string='Genero')