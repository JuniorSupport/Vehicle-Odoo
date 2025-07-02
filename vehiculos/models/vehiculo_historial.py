from odoo import models, fields

class VehiculoHistorial(models.Model):
    _name='vehiculos.historial'
    _description="historial de eventos de vehiculos"
    _rec_name = 'descripcion'


    descripcion=fields.Text(string="Descripcion del evento")
    fecha=fields.Datetime(string="Fecha",default=fields.Datetime.now)

    vehiculo_id=fields.Many2one("vehiculos.vehiculo", string="Vehiculo")