from odoo import models,fields,api
from datetime import date,timedelta

class Vehiculo(models.Model):
    _inherit="vehiculos.vehiculo"

    fecha_mantenimiento=fields.Date(string="Fecha de mantenimiento previsto")

    def check_mantenimiento_automatico(self):
        for vehiculo in self:
            if vehiculo.anio:
                edad = date.today().year - vehiculo.anio
                if edad > 5 and vehiculo.estado != 'mantenimiento':
                    vehiculo.estado = 'mantenimiento'
                    vehiculo.fecha_mantenimiento = date.today() + timedelta(days=30)

                    self.env['vehiculos.historial'].create({
                        'descripcion': f'Vehiculo para mantenimiento.',
                        'vehiculo_id': vehiculo.id
                    })