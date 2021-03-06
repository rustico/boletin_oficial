# -*- coding: utf-8 -*-
import unittest
import fixtures
from parser import AdjudicacionParser

class TestAdjudicacion00(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[0])

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name() 
        self.assertEqual(entidad_publica, "FUERZA AEREA ARGENTINA ESTADO MAYOR GENERAL DE LA FUERZA AEREA INSTITUTO DE FORMACION EZEIZA")        
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("METEO S.A", {'moneda': '$', 'valor': 87900.0}))

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Mantenimiento y reparación de Edificios y Locales del Instituto")

class TestAdjudicacion01(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Cursos de Mantenimiento de Motores T-56")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "FUERZA AEREA ARGENTINA DIRECCION GENERAL DE INTENDENCIA DIRECCION DE CONTRATACIONES")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("CAE USA INC", {'moneda': 'U$S', 'valor': 74076.0}))

class TestAdjudicacion02(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[2])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        # self.assertEqual(objeto, "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre 2011 y 1er Trimestre 2012")
        self.assertEqual(objeto, "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "EJERCITO ARGENTINO COLEGIO MILITAR DE LA NACION")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 5)
        self.assertEqual(proveedores[0], ("LEONARDO MAZZEO", {'moneda': '$', 'valor': 19906.0}))
        self.assertEqual(proveedores[1], ("DISTRIBUIDORA SYNERGIA S.R.L", {'moneda': '$', 'valor': 19621.45}))
        self.assertEqual(proveedores[2], ("SUALIER SA", {'moneda': '$', 'valor': 686950.0}))
        self.assertEqual(proveedores[3], ("VIMI S.A", {'moneda': '$', 'valor': 34893.80}))
        self.assertEqual(proveedores[4], ("CAÑUELAS GAS S.A", {'moneda': '$', 'valor': 15561.0}))

class TestAdjudicacion03(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[3])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Adquisición de Equipamiento Técnico para la Dirección de Policía Científica")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "GENDARMERIA NACIONAL ARGENTINA")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 2)
        self.assertEqual(proveedores[0], ("TECNOELECTRIC S.R.L", {'moneda': '$', 'valor': 594.0}))
        self.assertEqual(proveedores[1], ("PROMETIN S.A", {'moneda': '$', 'valor': 8577.0}))

class TestAdjudicacion04(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[4])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Adquisición de Chombas de Piqué identificatorias")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL ADUANERA MENDOZA")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("FEDERICO LOPEZ", {'moneda': '$', 'valor': 44884.66}))

class TestAdjudicacion05(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[5])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Servicio de traslado de agua potable para consumo del ACI Uspallata – Prórroga")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL ADUANERA MENDOZA")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 2)
        self.assertEqual(proveedores[0], ("PINCOLINI Y PINCOLINI S.H", {'moneda': '$', 'valor': 33900.0}))
        self.assertEqual(proveedores[1], ("LOPEZ FEDERICO", {'moneda': '$', 'valor': 2756.85}))

class TestAdjudicacion06(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[6])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Mantenimiento Edilicio")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "MINISTERIO DE DESARROLLO SOCIAL AREA COMPRAS")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("COOP DE TRABAJO PADRE HURATDO LTDA", {'moneda': '$', 'valor': 337853.75}))
        
class TestAdjudicacion07(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[7])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()
        self.assertEqual(len(objeto), 0)

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "AFIP")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        
        self.assertEqual(len(proveedores), 14)
        
        self.assertEqual(proveedores[0],('ANALISTAS EMPRESARIOS SRL', {'moneda': '$', 'valor': 715480.0}))
        self.assertEqual(proveedores[1],('BASANI S.A', {'moneda': '$', 'valor': 7572.0}))
        self.assertEqual(proveedores[2],('ALFOMBRAS ADEKOR OMAR A COSTANTINO', {'moneda': '$', 'valor': 25760.0}))
        self.assertEqual(proveedores[3],('ALFOMBRAS ADEKOR OMAR A COSTANTINO', {'moneda': '$', 'valor': 73600.0}))
        self.assertEqual(proveedores[4],('ADSUR SA - ASCENSORES DEL SUR', {'moneda': '$', 'valor': 445387.0}))
        self.assertEqual(proveedores[5],('BONIFACIO S.A', {'moneda': '$', 'valor': 478022.4}))
        self.assertEqual(proveedores[6],('LIBRERIA PAPELERIA BUENOS AIRES SRL', {'moneda': '$', 'valor': 184500.0}))
        self.assertEqual(proveedores[7],('NUCLEAR CONTROL SOCIEDAD ANONIMA', {'moneda': '$', 'valor': 528360.0}))
        self.assertEqual(proveedores[8],('BIONICS DE ROBERTO VALLOUD', {'moneda': '$', 'valor': 271148.0}))
        self.assertEqual(proveedores[9],('JOSE EDUARDO LAURITO', {'moneda': '$', 'valor': 27190.0}))
        self.assertEqual(proveedores[10],('UNIVERSIDAD TECNOLOGICA NAC', {'moneda': '$', 'valor': 676390.0}))
        self.assertEqual(proveedores[11],('LEPERA LUCIO ALBERTO', {'moneda': '$', 'valor': 137116.0}))
        self.assertEqual(proveedores[12],('SERBECO S.A', {'moneda': '$', 'valor': 76000.0}))
        self.assertEqual(proveedores[13],('NUEVO MILENIO SRL', {'moneda': '$', 'valor': 26779.5})) 

class TestAdjudicacion08(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[8])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Suscripción a la Editorial La Ley año 2011-2012")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA INSTITUTO NACIONAL DE INVESTIGACION Y DESARROLLO PESQUERO")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("LA LEY S.A", {'moneda': '$', 'valor': 9500.0}))

class TestAdjudicacion09(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[9])

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 24)
        self.assertEqual(objects[0], "Servicio de Limpieza de los edificios sede de las Agencias Nº 06 y 51")
        self.assertEqual(objects[1], "Servicio de mantenimiento de los Ascensores del edificio sede de la Agencia Nº 11")
        self.assertEqual(objects[2], "Custodia del Edificio sede de la Dirección Regional Palermo")
        self.assertEqual(objects[3], "Custodia del Edificio Sede de la Agencia Nº 11")
        self.assertEqual(objects[4], "Custodia del Edificio sede de la Agencia Nº 46")
        self.assertEqual(objects[5], "Custodia del edificio sede de la Agencia Nº 51")
        self.assertEqual(objects[6], "Custodia del edificio sede de la Agencia Nº 06")
        # TODO
        # self.assertEqual(objects[7], "Reparación de Cañería Estanca del tanque cisterna del edificio sede de la Agencia Nº 51") 
        self.assertEqual(objects[7], "Reparación de Cañería Estanca del tanque cisterna del edificio") 
        self.assertEqual(objects[8], "Provisión de Papel Alcalino 80 grs./m2")
        self.assertEqual(objects[9], "Provisión de Utiles de Oficina")
        self.assertEqual(objects[10], "Batería del Gel p/ UPS")
        self.assertEqual(objects[11], "Mantenimiento de Equipos de Aire Acondicionado para el edificio")
        # self.assertEqual(objects[11], "Mantenimiento de Equipos de Aire Acondicionado para el edificio sede de la Dirección Regional Palermo")
        self.assertEqual(objects[12], "Servicio de Desinfección del edificios sede de la Dirección Regional Palermo y de las Agencias Nº  6, 11,")
        #self.assertEqual(objects[12], "Servicio de Desinfección del edificios sede de la Dirección Regional Palermo y de las Agencias Nº  6, 11, 46 y 51")
        self.assertEqual(objects[13], "Servicio de mantenimiento de los Ascensores del edificio sede de la Dirección Regional Palermo")
        self.assertEqual(objects[14], "Provisión de Indumentaria para operativos")
        self.assertEqual(objects[15], "Adquisición de Papel Obra A4")
        self.assertEqual(objects[16], "Serv. Correctivo y de mantenimiento de los Ascensores de la")
        #self.assertEqual(objects[16], "Serv. Correctivo y de mantenimiento de los Ascensores de la Agencia Nº 51")
        self.assertEqual(objects[17], "CD-UPS de Agencia Nº 46, reubicación /adecuación")
        self.assertEqual(objects[18], "Locación del Edificio Sede de la Agencia Nº 06")
        self.assertEqual(objects[19], "Mantenimiento de la iluminación de las Salidas de Emergencia de")
        #self.assertEqual(objects[19], "Mantenimiento de la iluminación de las Salidas de Emergencia de la Dirección Regional Palermo y de las Agencias Nº 6, 11, 46 y 51")
        self.assertEqual(objects[20], "Adquisición de Estanterías para la Agencia Nº 51")
        self.assertEqual(objects[21], "Servicio de Limpieza de Tanques de Agua Potable para los edificios sede de la Dirección Regional Palermo")
        #self.assertEqual(objects[21], "Servicio de Limpieza de Tanques de Agua Potable para los edificios sede de la Dirección Regional Palermo y de la Agencia Nº 51")
        self.assertEqual(objects[22], "Servicio de verificación y/o recarga de Matafuegos de la Dirección Regional Palermo y de las Agencias Nº 6, 11, 46 y 51")
        self.assertEqual(objects[23], "Servicio de p Limpieza del edificio sede de la Agencia")
        #self.assertEqual(objects[23], "Servicio de p Limpieza del edificio sede de la Agencia Nº 46")

    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica, "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL PALERMO")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 24)
        self.assertEqual(proveedores[0], ("UADEL SRL", {'moneda': '$', 'valor': 27944.0}))                
        self.assertEqual(proveedores[1], ("INGENIERIA CAAMAÑO SA", {'moneda': '$', 'valor': 34012.0}))
        self.assertEqual(proveedores[2], ("POLICIA FEDERAL ARGENTINA", {'moneda': '$', 'valor': 307440.0}))
        self.assertEqual(proveedores[3], ("POLICIA FEDERAL ARGENTINA", {'moneda': '$', 'valor': 307440.0}))
        self.assertEqual(proveedores[4], ("POLICIA FEDERAL ARGENTINA", {'moneda': '$', 'valor': 307440.0}))
        self.assertEqual(proveedores[5], ("POLICIA FEDERAL ARGENTINA", {'moneda': '$', 'valor': 307440.0}))
        self.assertEqual(proveedores[6], ("POLICIA FEDERAL ARGENTINA", {'moneda': '$', 'valor': 307440.0}))
        self.assertEqual(proveedores[7], ("VAZQUEZ JAVIER RICARDO", {'moneda': '$', 'valor': 360.0}))
        self.assertEqual(proveedores[8], ("PAPELERA ALSINA SA", {'moneda': '$', 'valor': 49126.0}))
        self.assertEqual(proveedores[9], ("CONGRESO INSUMOS SA", {'moneda': '$', 'valor': 33192.80}))
        self.assertEqual(proveedores[10], ("SIECO SA", {'moneda': '$', 'valor': 7156.0 }))
        self.assertEqual(proveedores[11], ("SICA SRL", {'moneda': '$', 'valor': 49800.0 }))
        self.assertEqual(proveedores[12], ("CIA. FUMIGADORA DEL NORTE SRL", {'moneda': '$', 'valor': 33840.0 }))
        self.assertEqual(proveedores[13], ("PISO CERO SA", {'moneda': '$', 'valor': 56280.0 }))
        self.assertEqual(proveedores[14], ("FARIÑA ANDREA VIVIANA", {'moneda': '$', 'valor': 9000.0}))
        self.assertEqual(proveedores[15], ("PAPELERA ALSINA SA", {'moneda': '$', 'valor': 47934.60 }))
        self.assertEqual(proveedores[16], ("CACCEM SRL", {'moneda': '$', 'valor': 16200.0}))
        self.assertEqual(proveedores[17], ("SIECO SA", {'moneda': '$', 'valor': 11855.96}))
        self.assertEqual(proveedores[18], ("MARIA ISABEL BAIOCCHINI", {'moneda': '$', 'valor': 510000.0}))
        self.assertEqual(proveedores[19], ("AELINEC SA", {'moneda': '$', 'valor': 34557.60}))
        self.assertEqual(proveedores[20], ("D GROISMAN Y CIA SCA", {'moneda': '$', 'valor': 29001.60 }))
        self.assertEqual(proveedores[21], ("VAZQUEZ JAVIER RICARDO", {'moneda': '$', 'valor': 6581.0 }))
        self.assertEqual(proveedores[22], ("RANKO SRL", {'moneda': '$', 'valor':   17475.0}))
        self.assertEqual(proveedores[23], ("BET-CLEAN SRL", {'moneda': '$', 'valor': 197844.0 }))
        
    
class TestAdjudicacion10(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[10])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "GENDARMERÍA NACIONAL ARGENTINA")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('REDIMEC S.R.L', {'moneda': 'USD', 'valor': 996000.0}))

class TestAdjudicacion11(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[11])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO DE EDUCACIÓN DE LA NACIÓN")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(objects[0], "ADQUISICIÓN DE PROVISIÓN Y MONTAJE DE MOBILIARIO PARA EL CENTRO DE FORMACIÓN ALFONSINA STORNI UBICADO EN LA CIUDAD DE MAR DEL PLATA")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 0)

class TestAdjudicacion12(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[12])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "EJÉRCITO ARGENTINO COMANDO DE LA IRA BRIGADA BLINDADA")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "ADQUISICION DE ELEMENTOS DE LIMPIEZA PARA EL 2DO TRIM 2015")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 4)
        self.assertEqual(proveedores[0], ('KLOSTER NORMA ROSA', {'moneda': '$', 'valor': 15612.08}))
        self.assertEqual(proveedores[1], ('SUAREZ SANTOS CESAR', {'moneda': '$', 'valor': 30273.86}))
        self.assertEqual(proveedores[2], ('MAXXILIMP SRL', {'moneda': '$', 'valor': 26586.09}))
        self.assertEqual(proveedores[3], ('HENNING JUAN FEDERICO', {'moneda': '$', 'valor': 31949.20}))

class TestAdjudicacion13(unittest.TestCase):
    """ Same Adjudicacion has Adjudicacion2 but we have the first Proveedor without money """
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[13])
            
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 5)
        self.assertEqual(proveedores[0], ("LEONARDO MAZZEO", None))
        self.assertEqual(proveedores[1], ("DISTRIBUIDORA SYNERGIA S.R.L", {'moneda': '$', 'valor': 19621.45}))
        self.assertEqual(proveedores[2], ("SUALIER SA", {'moneda': '$', 'valor': 686950.0}))
        self.assertEqual(proveedores[3], ("VIMI S.A", {'moneda': '$', 'valor': 34893.80}))
        self.assertEqual(proveedores[4], ("CAÑUELAS GAS S.A", {'moneda': '$', 'valor': 15561.0}))

class TestAdjudicacion14(unittest.TestCase):
    """ Same Adjudicacion has Adjudicacion2 but we have the second Proveedor without money """
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[14])
            
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 5)
        self.assertEqual(proveedores[0], ("LEONARDO MAZZEO", {'moneda': '$', 'valor': 19906.0}))
        self.assertEqual(proveedores[1], ("DISTRIBUIDORA SYNERGIA S.R.L", None))
        self.assertEqual(proveedores[2], ("SUALIER SA", {'moneda': '$', 'valor': 686950.0}))
        self.assertEqual(proveedores[3], ("VIMI S.A", {'moneda': '$', 'valor': 34893.80}))
        self.assertEqual(proveedores[4], ("CAÑUELAS GAS S.A", {'moneda': '$', 'valor': 15561.0}))

class TestAdjudicacion15(unittest.TestCase):
    """ Same Adjudicacion has Adjudicacion2 but we have the last Proveedor without money """
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[15])
            
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 5)
        self.assertEqual(proveedores[0], ("LEONARDO MAZZEO", {'moneda': '$', 'valor': 19906.0}))
        self.assertEqual(proveedores[1], ("DISTRIBUIDORA SYNERGIA S.R.L", {'moneda': '$', 'valor': 19621.45}))        
        self.assertEqual(proveedores[2], ("SUALIER SA", {'moneda': '$', 'valor': 686950.0}))
        self.assertEqual(proveedores[3], ("VIMI S.A", {'moneda': '$', 'valor': 34893.80}))
        self.assertEqual(proveedores[4], ("CAÑUELAS GAS S.A", None))

class TestAdjudicacion16(unittest.TestCase):
    """ Same Adjudicacion has Adjudicacion2 but we have the multiples Proveedor without money """
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[16])
            
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 5)
        self.assertEqual(proveedores[0], ("LEONARDO MAZZEO", None))
        self.assertEqual(proveedores[1], ("DISTRIBUIDORA SYNERGIA S.R.L", {'moneda': '$', 'valor': 19621.45}))
        self.assertEqual(proveedores[2], ("SUALIER SA", None))
        self.assertEqual(proveedores[3], ("VIMI S.A", {'moneda': '$', 'valor': 34893.80}))
        self.assertEqual(proveedores[4], ("CAÑUELAS GAS S.A", None))

class TestAdjudicacion17(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[17])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "EJÉRCITO ARGENTINO DIRECCIÓN DE INGENIEROS E INFRAESTRUCTURA")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "SERVICIO DE MANTENIMIENTO Y REPARACION DE VEHICULOS PERTENECIENTE AL BATALLON DE INGENIEROS 601 Y LA DIRECCION DE INGENIEROS E INFRAESTRUCTURA")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('AIELLO MARTIN EZEQUIEL', {'moneda': '$', 'valor': 156506.0}))

class TestAdjudicacion18(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[18])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL PALERMO")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "Servicio de limpieza integral de la Agencia Nº 6, ubicada en la calle Luis María Campos Nº 112, CABA")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('EZCA SERVICIOS GENERALES S.A', {'moneda': '$', 'valor': 407400.0}))


class TestAdjudicacion19(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[19])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO PUBLICO DE LA DEFENSA DEFENSORIA GENERAL DE LA NACION")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "Adquisición de cinco (5) Equipos de PC de avanzada para el Departamento de")
        #self.assertEqual(objects[0], "Adquisición de cinco (5) Equipos de PC de avanzada para el Departamento de Arquitectura")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('CORADIR S.A.', {'moneda': '$', 'valor': 27465.0}))

        
class TestAdjudicacion20(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[20])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA INSTITUTO NACIONAL DE INVESTIGACION Y DESARROLLO PESQUERO")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "Mantenimiento sistemas de cámaras IP")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('SEGCON S.A', {'moneda': '$', 'valor': 36300.0}))

        
class TestAdjudicacion21(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[21])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "UNIVERSIDAD NACIONAL DE MAR DEL PLATA")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "Adquisición de equipo de espectroscopia infrarroja con transformada de Fourier")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('PERKIN ELMER ARGENTINA S.A', {'moneda': 'U$S', 'valor': 28200.0}))                        

class TestAdjudicacion22(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[22])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "EJERCITO ARGENTINO DPTO CONT Y FIN – EMGE")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "Adquisición de Servicios de Consultoría necesaria para el")
        #self.assertEqual(objects[0], "Adquisición de Servicios de Consultoría necesaria para el marco de trabajo de Ingeniería definido")        

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('UNIVERSIDAD TECNOLOGICA NACIONAL', {'moneda': '$', 'valor': 106000.0}))


class TestAdjudicacion23(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[23])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "ARMADA ARGENTINA ESTADO MAYOR GENERAL DE LA ARMADA")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "Contratación de servicio de ómnibus")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('TRANSPORTES AUTOMOTORES PLUSMAR S.A. - Pedro Mendoza 3453', {'moneda': '$', 'valor': 171600.0}))

# Fix
class TestAdjudicacion24(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[24])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO DE TURISMO")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "“SERVICIO DE INFORMACION COMERCIAL”")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('NOSIS LABORATORIO DE INVESTIGACION Y DESARROLLO S.A', {'moneda': '$', 'valor': 7200.0}))
        

class TestAdjudicacion25(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[25])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO DE TURISMO")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "“ADQUISICION DE NEUMATICOS Y CAMARAS PARA DISTINTAS DEPENDENCIAS DE ESTE MINISTERIO”")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 2)
        self.assertEqual(proveedores[0], ('FERNANDEZ LUIS ALBERTO', {'moneda': '$', 'valor': 77692.0}))
        self.assertEqual(proveedores[1], ('LAROCCA NEUMATICOS S.A.', {'moneda': '$', 'valor': 67893.0 }))


class TestAdjudicacion26(unittest.TestCase):
    """ Remove the '-' character from the government department name """
    """ When the government department is MINISTERIO DE DEFENSA we replace SSSL, SSL, DGSLD by SLD"""
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[26])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO DE DEFENSA SLD")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "“ADQUISICIÓN DE LUBRICANTES Y FLUIDOS ENVASADOS PARA CAV-2015/2016”")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('YPF S.A', {'moneda': '$', 'valor': 223774.10}))


class TestAdjudicacion27(unittest.TestCase):
    """ When the government department is MINISTERIO DE DEFENSA we replace SSSL, SSL, DGSLD by SLD"""
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[27])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "MINISTERIO DE DEFENSA SLD")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "ADQUISICIÓN DE NEUMÁTICOS – PACID 2014")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('LARROCA NEUMÁTICOS S.A', {'moneda': '$', 'valor': 637162.0}))


class TestAdjudicacion28(unittest.TestCase):
    """ When the government department is A.F.I.P we replace it by AFIP"""
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[28])
            
    def test_get_government_department_name(self):
        entidad_publica = self.adjudicacion.get_government_department_name()
        self.assertEqual(entidad_publica , "AFIP DIRECCIÓN REGIONAL RÍO GALLEGOS")

    def test_get_objects(self):
        objects = self.adjudicacion.get_objects()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0], "SERVICIO DE LIMPIEZA DE EDIFICIOS PARA LA DIRECCIÓN REGIONAL RÍO GALLEGOS DEPENDIENTE DE LA ADMINISTRACIÓN FEDERAL DE INGRESOS PÚBLICOS")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('LUNA ANICETO MIGUEL', {'moneda': '$', 'valor': 383400.0}))

class TestGovernmentDepartment(unittest.TestCase):
    def test_government_department_afip(self):
        government_department_names = [
            'A.F. I .P.',
            'A.F.I.P - DGI DIRECCION REGIONAL SUR'
            'A.F.IP.',
            'ADMINISTRACION FEDERAL DE INGRESO PUBLICOS D.G.I.',
            'ADMINISTRACION FEDERAL DE INGRESOS DIRECCION REGIONAL POSADAS ADJUDICACIONES REALIZADAS EN EL MES DE FEBRERO DE 2014',
            'ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS D.G.I.',
            'ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION GENERAL IMPOSITIVA  DIRECCION REGIONAL SALTA',
            'ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL JUNIN',
            'AFIP',
            'AFIP - D.G.I. DIRECCION REGIONAL BAHIA BLANCA',
            'AFIP - DGA DIRECCION REGIONAL ADUANERA CORDOBA',
            'AFIP ADUANA DE EZEIZA',
            'AFIP LISTADO ORDENES DE COMPRAS EMITIDAS EN EL MES DE JUNIO DE 2014',
            'AFIP-D.G.I. DIRECCION REGIONAL SUR C.D. No 25/2008'
        ]

        for name in government_department_names:
            self.assertEqual('AFIP', AdjudicacionParser.get_government_department(name))


    def test_government_department_armada_argentina(self):
        government_department_names = [
            'ARMADA ARGENTINA',
            'ARMADA ARGENTINA AGRUPACION SERVICIOS DE CUARTEL',
            'ARMADA ARGENTINA ESTADO MAYOR GENDE LA ARMADA',
            'ARMADA ARGENTINAESTADO MAYOR GENERAL DE LA ARMADA - SIAF DEPARTAMENTO CONTRATACIONES',
            'ARMADA ARGETINA ARSENAL NAVAL PUERTO BELGRANO 2'
        ]

        for name in government_department_names:
            self.assertEqual('ARMADA ARGENTINA', AdjudicacionParser.get_government_department(name))

    def test_government_department_banco_nacion(self):
        government_department_names = [
            'BANCO DE LA NACION ARGENTINA',
            'BANCO DE LA NACION ARGENTINA AREA COMPRAS Y'
        ]

        for name in government_department_names:
            self.assertEqual('BANCO DE LA NACION ARGENTINA', AdjudicacionParser.get_government_department(name))

    def test_government_department_ejercito_argentino(self):
        government_department_names = [
            'EJERCITIO ARGENTINO COMANDO DE BRIGADA MECANIZADA XI',
            'EJERCITO  ARGENTINO REGIMIENTO DE CABALLERIA DE MONTANA 4',
            'EJERCITO ARGENTINO  DPTO CONT Y FIN - EMGE',
            'EJERCITO ARGENTINO',
            'EJERCITO ARGETINO',
            'EJERCITO ARGENTICOMANDO BRIGADA BLINDADA I',
            'EJERCITO ARGENTINCOMANDO BRIGADA DE MONTE XII'
        ]

        for name in government_department_names:
            self.assertEqual('EJERCITO ARGENTINO', AdjudicacionParser.get_government_department(name))

    def test_government_department_fuerza_area_argentina(self):
        government_department_names = [
            'FUERZA AEREA ARGENTINA SUBJEFATURA DEL ESTADO MAYOR GENERAL CIRCULO DE LA FUERZA AEREA DTO. ECONOMICO FINANCIERO',
            'FUERZA AREA ARGENTINA COMANDO DE ADIESTRAMIENTO Y ALISTAMIENTO II BRIGADA AEREA',
            'FUERZA AEREA ARGENTINA',
            'ESTADO MAYOR GENERAL DE LA FUERZA AEREA ARGENTINA DIRECCION GENERAL DE EDUCACION LICEO AERONAUTICO MILITAR DIVISION ECONOMIA'
        ]

        for name in government_department_names:
            self.assertEqual('FUERZA AEREA ARGENTINA', AdjudicacionParser.get_government_department(name))

    def test_government_department_gendarmeria_nacional(self):
        government_department_names = [
            'GENDARMERIA NACIONAL',
            'GENDARMERIA NACIONAL ARGENTINA AGRUPACION III "CORRIENTES" DE GENDARMERIA NACIONAL',
            'GENDARMERIA NACIONAL ARGENTINA',
            'GENDARMERIA NACIONAL ESCUADRON 27 "USPALLATA" DE GENDARMERIA NACIONAL',
            'GENDARMERIA NACIONALARGENTINA',
            'GENDARMERLA NACIONAL ARGENTINA'
        ]

        for name in government_department_names:
            self.assertEqual('GENDARMERIA NACIONAL ARGENTINA', AdjudicacionParser.get_government_department(name))

    def test_government_department_ministerio_agricultura(self):
        government_department_names = [
            'MINISTERIO DE AGRICULTURA GANADERIA Y PESCA INSTITUTO NACIONAL DE INVESTIGACION Y DESARROLLO PESQUERO',
            'MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA',
            'MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA  COMISION EVALUADORA',
            'MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA INTA',
            'MINISTERIO DE AGRICULTURA, GANADERLA Y PESCA',
            'MINISTERIO DE AGRICULTURA, GANDERIA Y PESCA INSTITUTO NACIONAL DE TECNOLOGIA AGROPECUARIA'
        ]

        for name in government_department_names:
            self.assertEqual('MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA', AdjudicacionParser.get_government_department(name))

    def test_government_department_ministerio_defensa(self):
        government_department_names = [
            'MINISTERIO DE DEFENSA',
            'MINISTERIO DE DEFENSA  DGA',
            'MINISTERIO DE DEFENSA DGA - UOC 35/04 LICITCION PUBLICA Ndeg 56/2010',
            'MINISTERIO DE DEFENSA INSTITUTO GEOGRAFICO MILITAR',
            'MINISTERIO DE DEFENSA SLA',
            'MINISTERIO DE DEFENSA SLDD',
            'MINISTERIO DEFENSA DGA'
        ]

        for name in government_department_names:
            self.assertEqual('MINISTERIO DE DEFENSA', AdjudicacionParser.get_government_department(name))

    def test_government_department_ministerio_desarrollo_social(self):
        government_department_names = [
            'MINISTERIO DESARROLL SOCIAL AREA COMPRAS',
            'MINISTERIO DE  DESARROLLO SOCIAL',
            'MINISTERIO DE  DESARROLLO SOCIAL AREA COMPRAS',
            'MINISTERIO DE DESARROLLO SOCIAL',
            'MINISTERIO DESARROLLO SOCIAL'
        ]

        for name in government_department_names:
            self.assertEqual('MINISTERIO DE DESARROLLO SOCIAL', AdjudicacionParser.get_government_department(name))

    def test_government_department_prefectura_naval(self):
        government_department_names = [
            'PEFECTURA NAVAL ARGENTINA',
            'PREFECTURA NAVAL ARGENTINA',
            'PREFECTURA NAVAL ARGENTINA DICTAMEN DE EVALUACION No 139/2012'
        ]

        for name in government_department_names:
            self.assertEqual('PREFECTURA NAVAL ARGENTINA', AdjudicacionParser.get_government_department(name))

    def test_government_department_jefatura_de_gabinete(self):
        government_department_names = [
            'JEFATURA DE GABINETE DE MINISTROS DIRECCION GENERAL DEL SERVICIO ADMINISTRATIVO FINANCIERO DE APOYO A LA ACUMAR',
            'JEFATURA DE GABINETE DE MINISTROS SECRETARIA DE AMBIENTE Y DESARROLLO SUSTENTABLE',
            'JEFATURA DE GABINETE DE MINISTROS SECRETARIA DE COORDINACION ADMINISTRATLVA Y EVALUACION PRESUPUESTARIA SUBSECRETARIA DE COORDINACIN ADMINISTRATIVA DIRECCION GENERAL TECNICO ADMINISTRATIVA',
            'JEFATURA DE GABINETE DE MINISTROS SECRETARIA DE MEDIOS DE COMUNICACION COMITE FEDERAL DE RADIODIFUSION',
            'JEFATURA DE GABINETE DE MINISTROS SECRETARLA DE COORDINACION ADMINISTRATIVA Y EVALUACION PRESUPUESTARIA SUBSECRETARIA DE COORDINACION ADMINISTRATIVA DIRECCION GENERAL TECNICO ADMINISTRATIVA'
        ]

        for name in government_department_names:
            self.assertEqual('JEFATURA DE GABINETE DE MINISTROS', AdjudicacionParser.get_government_department(name))

    def test_government_department_autoridad_regulatoria_nuclear(self):
        government_department_names = [
            'AUTORIDAD REGULADORA NUCLEAR DEPENDIENTE DE LA PRESIDENCIA DE LA NACION',
            'AUTORIDAD REGULATORIA NUCLEAR',
            'PRESIDENCIA DE LA NACION AUTORIDAD REGULATORIA NUCLEAR PUBLICACIoN DE LOS CONTRATOS PERFECCIONADOS RES. 368/2000',
            'PRESIDENCIA DE LA NACION AUTORIDAD REGULATORIA NUCLEAR'
        ]

        for name in government_department_names:
            self.assertEqual('AUTORIDAD REGULATORIA NUCLEAR', AdjudicacionParser.get_government_department(name))                        
        
if __name__ == '__main__':
    unittest.main()
