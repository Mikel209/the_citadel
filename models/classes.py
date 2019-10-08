from odoo import models
from odoo import fields


class Classes(models.Model):
    _name = "classes"
    _description = "Description Classes"

    name = fields.Char(string='Nombre', required=True)
    themes = fields.Integer(string='Temas')
    kindofsubject = fields.Selection([('Mat', 'Matematicas'), ('Len', 'Lengua'), ('His','Historia'), ('EF', 'Educacion_fisica')], string='Tipo de asignatura')
    fk_teachers = fields.Many2one("teachers", string='Profesor FK')