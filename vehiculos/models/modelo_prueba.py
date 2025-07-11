from odoo import models,api,fields

class ModeloPrueba(models.Model):
    _name="vehiculos.prueba"
    _description="Esto es un modelo de prueba"

    name=fields.Char(string="Nombre",required=True)

    def mostrar_valores(self):

        data=self.env['res.partner'].search([])

        for i in data:
            print(i.name)


    def crear_registros_ejemplo(self):
        partners = self.env['res.partner'].browse([])

        for nombre in ['Juan Pérez', 'Ana Torres', 'Carlos Díaz']:
            nuevo = self.env['res.partner'].create({
                'name': nombre,
                'company_type': 'person',
                'phone': '+51912948032'
            })
            partners += nuevo
        return True

    def modificar_valor(self):
        partners=self.env["res.partner"].search([("name","=","Keane")])

        if partners:
            partners.write({"phone":"+51935615523"})
            print("Se modificó correctamente")
        else:
            print("No se encontró el registro")


    def funcion_prueba_dominio(self):

        domain=[
            '&',
            ("marca","ilike","mazda"),
            ("anio",">","2016")
        ]

        vehiculos=self.env["vehiculos.vehiculo"].search(domain)

        for vehiculo in vehiculos:
            print(vehiculo.placa)

    #***************Combinando de RecordSets - COMBINING RECORDSETS*****************

    def mostrar(self,data):
        for d in data:
            print(d.marca)

    def suma_registros(self):

        vehicles1 = self.env["vehiculos.vehiculo"].search([("id","in",[1,2])])
        vehicles2 = self.env["vehiculos.vehiculo"].search([("id","in",[11,13])])

        combined=vehicles1+vehicles2

        self.mostrar(combined)

    def union_sin_duplicados(self):

        vehicles1 = self.env["vehiculos.vehiculo"].search([("id", "in", [1, 2])])
        vehicles2 = self.env["vehiculos.vehiculo"].search([("id", "in", [2, 13])])
        combined=vehicles1 | vehicles2
        self.mostrar(combined)

    def agregar_vehiculo_propietario(self):

        propietario=self.env["vehiculos.propietario"].browse(6)
        vehiculo = self.env["vehiculos.vehiculo"].browse(11)

        propietario.vehiculo_ids|=vehiculo

    #*****************Filtrando Recordsets - FILTERING RECORDSETS*************++
    # dame los propietarios que tienen mas de un carro

    def filter_vehiculo(self):

        #   vehiculo = self.env['vehiculos.vehiculo'].search([]).filtered(lambda v:v.anio>2017)

        #    vehiculos=self.env['vehiculos.vehiculo'].search([]).filtered(lambda v: v.propietario_id and v.propietario_id.name =="Pepe")

        # lista de las marcas que fueron vendidos  y mayores al año 2015
        """    vehiculos=self.env['vehiculos.vehiculo'].search([
                ("anio",">",2015),
                ("estado","=","vendido")
            ])"""

        vehiculos = self.env['vehiculos.vehiculo'].search([]).filtered(
            lambda v: v.anio > 2015 and v.estado == "vendido")
        self.mostrar(vehiculos)

    # *****************Relaciones entre modelos - TRAVERSING RECORDSET RELATIONS***************

    def propietario_vehiculo(self):

        vehiculos = self.env['vehiculos.vehiculo'].search([
            ('estado','=','vendido'),
            ('anio','>',2015)
        ])
        propietarios=vehiculos.mapped('propietario_id.name')
        print(propietarios)

    def vehiculo_anio(self):

        vehiculos=self.env['vehiculos.vehiculo'].search([]).filtered(lambda v:v.anio>2017)

        marcas=vehiculos.mapped('marca')

        print(marcas)

    # *****************Relaciones entre modelos - SORTING RECORDSETS***************

    def fecha_venta_desc(self):

        vehiculos = self.env['vehiculos.vehiculo'].search([("estado","=","vendido")])

        orden_desc=vehiculos.sorted(key='fecha_venta',reverse=True)

        for i in orden_desc:
            print(f"{i.fecha_venta} - {i.marca}")

    @api.model
    def contar_por_estado(self, *args, **kwargs):
        resultado = self.env['vehiculos.vehiculo'].read_group(
            [],
            ['estado', 'anio:sum'],
            ['estado']
        )
        for r in resultado:
            print(f"Estado: {r['estado']}, Suma de Años: {r['anio']}")
        print(resultado)

    @api.model
    def vehiculos_actuales(self, *args,**kwargs):
        resultado=self.env['vehiculos.vehiculo'].read_group(
            [('estado','=','vendido')],
            ['estado','anio:count'],
            ['estado']
        )
        for r in resultado:
            print(f"Estado: {r['estado']}")
        print(resultado)