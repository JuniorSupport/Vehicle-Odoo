from odoo import models, fields,api


class VehiculoHistorial(models.Model):
    _name='vehiculos.historial'
    _description="historial de eventos de vehiculos"
    _rec_name = 'descripcion'


    descripcion=fields.Text(string="Descripcion del evento")
    fecha=fields.Datetime(string="Fecha",default=fields.Datetime.now)

    vehiculo_id=fields.Many2one("vehiculos.vehiculo", string="Vehiculo")

    vehiculo_marca=fields.Char(string = "Marca", compute="_compute_marca")

    @api.depends('vehiculo_id')
    def _compute_marca(self):
        for record in self:
            marca= record.vehiculo_id.mapped("marca")
            record.vehiculo_marca=",".join(marca)


