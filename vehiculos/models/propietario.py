from odoo import models,fields,api

class Propietario(models.Model):
    _name="vehiculos.propietario"
    _description="Propietario de vehiculo"
    _rec_name='name'

    name=fields.Char(string="Nombre del Propietario", required=True)
    dni=fields.Integer(string="DNI", required=True)

    vehiculo_ids=fields.One2many("vehiculos.vehiculo","propietario_id",string="Vehiculos")

    vehiculo_marca=fields.Char(string="Marcas",compute="_compute_vehiculo_marca")

    @api.depends("vehiculo_ids")
    def _compute_vehiculo_marca(self):
        for record in self:
            marcas=record.vehiculo_ids.mapped("marca")
            record.vehiculo_marca = ", ".join(marcas)


    
