from email.policy import default

from odoo import models, fields,api
from odoo.exceptions import ValidationError

class vehiculos(models.Model):
    _name='vehiculos.vehiculo'
    _description='Información acerca de los vehículos'
    _rec_name="placa"

    marca=fields.Char(string='Marca',required=True)
    modelo=fields.Char(string='Modelo',required=True)
    anio=fields.Integer(string ='Año de Fabricación/Modelo')
    color=fields.Char(string='color',required=True)
    placa=fields.Char(string='placa',required=True)
    estado=fields.Selection(selection=[
        ("disponible","Disponible"),
        ("vendido","Vendido"),
        ("mantenimiento","Mantenimiento")
    ], string="Estado", default="disponible")
    fecha_venta=fields.Date(string="Fecha de venta",compute='_compute_fecha_venta',store=True)

    propietario_id=fields.Many2one("vehiculos.propietario",string="Propietario",required=True)

    historial_ids=fields.One2many("vehiculos.historial","vehiculo_id")

    historial=fields.Char(string="Historial de Vehiculo",compute="_compute_historial_vehiculo")

    #validaciones 
    _sql_constraints = [
    ('unique_placa', 'unique(placa)', 'La placa debe ser única.'),
    ]

    @api.constrains('anio')
    def validar_anio_vehiculo(self):
        for record in self:
            anio_actual=fields.Date.today().year+1
            if record.anio<1900 or record.anio> anio_actual:
                raise ValidationError("Año inválido")
    
    #campos computados
    @api.depends("estado")
    def _compute_fecha_venta(self):
        for record in self:
            if record.estado=="vendido" and not record.fecha_venta:
                record.fecha_venta=fields.Date.today()


    def _compute_historial_vehiculo(self):
        for record in self:
            historial=record.historial_ids.mapped("descripcion")
            record.historial=",".join(historial)


