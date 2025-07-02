from odoo import models,fields


class Course(models.Model):

    _name="grades.course"
    _description="App grades manager"

    name=fields.Char(string="Nombre",required=True)
    student_qy=fields.Integer(string="Cantidad de estudiantes",required=True)
    grades_average=fields.Float(string="Promedio",required=True)
    description=fields.Text(string = "Descripcion",required=True)
    is_active=fields.Boolean(string ="Activo",default=False)
    course_start=fields.Date(string = "Fecha de inicio")
    course_end=fields.Date(string="Fecha de fin")
    last_evaluation_date=fields.Datetime(string = "Ultima evaluacion")
    course_image=fields.Binary(string="imagen curso")
    course_shift=fields.Selection([("day","Day"),("night","Night")], string="Eleccion curso")
