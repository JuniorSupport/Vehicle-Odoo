from email.policy import default

from odoo import models, fields,api
from odoo.exceptions import ValidationError

from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class vehiculos(models.Model):
    _name='vehiculos.vehiculo'
    _description='Información acerca de los vehículos'

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


    def write(self,vals):
        if 'color' in vals:
            if not self.env.user.has_group('vehiculos.group_vehiculos_manager'):
                raise UserError("Solo manager puede cambiar el color")
        return super().write(vals)

    #******************Customizing how records are searched ***************************

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = [] if args is None else args.copy()
        if not (name == '' and operator == 'ilike'):
            args += ['|', '|',
                     ('marca', operator, name),
                     ('modelo', operator, name),
                     ('placa', operator, name)
                     ]
        return super(vehiculos, self).name_search(name=name, args=args, operator=operator, limit=limit,
                                                  name_get_uid=name_get_uid)

    # ******************FETCHING DATA IN GROUPS USING READ_GROUP()***************************

    @api.model
    def contar_por_estado(self):
        resultado=self.read_group(
            [('estado','!=',False)],
            ['estado','anio:sum'],
            ['estado']
        )
        print(resultado)

