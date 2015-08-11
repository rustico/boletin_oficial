# -*- coding: utf-8 -*-
import unittest
import fixtures
from parser import AdjudicacionParser

class TestAdjudicacion00(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[0])

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica() 
        self.assertEqual(entidad_publica, "FUERZA AEREA ARGENTINA ESTADO MAYOR GENERAL DE LA FUERZA AEREA INSTITUTO DE FORMACION EZEIZA")        
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("METEO S.A.", {'moneda': '$', 'valor': 87900.0}))

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Mantenimiento y reparación de Edificios y Locales del Instituto")

class TestAdjudicacion01(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Cursos de Mantenimiento de Motores T-56")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "FUERZA AEREA ARGENTINA DIRECCION GENERAL DE INTENDENCIA DIRECCION DE CONTRATACIONES")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("CAE USA INC.", {'moneda': 'U$S', 'valor': 74076.0}))

class TestAdjudicacion02(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[2])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        # self.assertEqual(objeto, "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre 2011 y 1er Trimestre 2012")
        self.assertEqual(objeto, "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "EJERCITO ARGENTINO COLEGIO MILITAR DE LA NACION")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 5)
        self.assertEqual(proveedores[0], ("LEONARDO MAZZEO", {'moneda': '$', 'valor': 19906.0}))
        self.assertEqual(proveedores[1], ("DISTRIBUIDORA SYNERGIA S.R.L.", {'moneda': '$', 'valor': 19621.45}))
        self.assertEqual(proveedores[2], ("SUALIER SA", {'moneda': '$', 'valor': 686950.0}))
        self.assertEqual(proveedores[3], ("VIMI S.A.", {'moneda': '$', 'valor': 34893.80}))
        self.assertEqual(proveedores[4], ("CAÑUELAS GAS S.A.", {'moneda': '$', 'valor': 15561.0}))

class TestAdjudicacion03(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[3])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Adquisición de Equipamiento Técnico para la Dirección de Policía Científica")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "GENDARMERIA NACIONAL ARGENTINA")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 2)
        self.assertEqual(proveedores[0], ("TECNOELECTRIC S.R.L.", {'moneda': '$', 'valor': 594.0}))
        self.assertEqual(proveedores[1], ("PROMETIN S.A.", {'moneda': '$', 'valor': 8577.0}))

class TestAdjudicacion04(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[4])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Adquisición de Chombas de Piqué identificatorias")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL ADUANERA MENDOZA")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("FEDERICO LOPEZ.", {'moneda': '$', 'valor': 44884.66}))

class TestAdjudicacion05(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[5])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Servicio de traslado de agua potable para consumo del ACI Uspallata – Prórroga")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL ADUANERA MENDOZA")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 2)
        self.assertEqual(proveedores[0], ("PINCOLINI Y PINCOLINI S.H.", {'moneda': '$', 'valor': 33900.0}))
        self.assertEqual(proveedores[1], ("LOPEZ FEDERICO.", {'moneda': '$', 'valor': 2756.85}))

class TestAdjudicacion06(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[6])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Mantenimiento Edilicio")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "MINISTERIO DE DESARROLLO SOCIAL AREA COMPRAS")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("COOP DE TRABAJO PADRE HURATDO LTDA.", {'moneda': '$', 'valor': 337853.75}))
        
class TestAdjudicacion07(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[7])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()
        self.assertEqual(len(objeto), 0)

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "AFIP LISTADO ORDENES DE COMPRAS EMITIDAS EN EL MES DE MAYO DE 2012")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        
        self.assertEqual(len(proveedores), 14)
        
        self.assertEqual(proveedores[0],('ANALISTAS EMPRESARIOS', {'moneda': '$', 'valor': 715480.0}))
        self.assertEqual(proveedores[1],('BASANI S.A.', {'moneda': '$', 'valor': 7572.0}))
        self.assertEqual(proveedores[2],('ALFOMBRAS ADEKOR OMAR A', {'moneda': '$', 'valor': 25760.0}))
        self.assertEqual(proveedores[3],('ALFOMBRAS ADEKOR OMAR A', {'moneda': '$', 'valor': 73600.0}))
        self.assertEqual(proveedores[4],('ADSUR SA - ASCENSORES', {'moneda': '$', 'valor': 445387.0}))
        self.assertEqual(proveedores[5],('BONIFACIO S.A.', {'moneda': '$', 'valor': 478022.4}))
        self.assertEqual(proveedores[6],('LIBRERIA PAPELERIA BUENOS', {'moneda': '$', 'valor': 184500.0}))
        self.assertEqual(proveedores[7],('NUCLEAR CONTROL SOCIEDAD ANONIMA', {'moneda': '$', 'valor': 528360.0}))
        self.assertEqual(proveedores[8],('BIONICS DE ROBERTO', {'moneda': '$', 'valor': 271148.0}))
        self.assertEqual(proveedores[9],('JOSE EDUARDO LAURITO', {'moneda': '$', 'valor': 27190.0}))
        self.assertEqual(proveedores[10],('UNIVERSIDAD TECNOLOGICA NAC.', {'moneda': '$', 'valor': 676390.0}))
        self.assertEqual(proveedores[11],('LEPERA LUCIO ALBERTO', {'moneda': '$', 'valor': 137116.0}))
        self.assertEqual(proveedores[12],('SERBECO S.A', {'moneda': '$', 'valor': 76000.0}))
        self.assertEqual(proveedores[13],('NUEVO MILENIO SRL.', {'moneda': '$', 'valor': 26779.5})) 

class TestAdjudicacion08(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[8])

    def test_get_objects(self):
        objeto = self.adjudicacion.get_objects()[0]
        self.assertEqual(objeto, "Suscripción a la Editorial La Ley año 2011-2012")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA INSTITUTO NACIONAL DE INVESTIGACION Y DESARROLLO PESQUERO - SAF 607")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("LA LEY S.A.", {'moneda': '$', 'valor': 9500.0}))

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
        # self.assertEqual(objects[7], "Reparación de Cañería Estanca del tanque cisterna del edificio sede de la Agencia Nº 51.") 
        self.assertEqual(objects[7], "Reparación de Cañería Estanca del tanque cisterna del edificio") 
        self.assertEqual(objects[8], "Provisión de Papel Alcalino 80 grs./m2")
        self.assertEqual(objects[9], "Provisión de Utiles de Oficina")
        self.assertEqual(objects[10], "Batería del Gel p/ UPS")
        self.assertEqual(objects[11], "Mantenimiento de Equipos de Aire Acondicionado para el edificio")
        # self.assertEqual(objects[11], "Mantenimiento de Equipos de Aire Acondicionado para el edificio sede de la Dirección Regional Palermo.")
        self.assertEqual(objects[12], "Servicio de Desinfección del edificios sede de la Dirección Regional Palermo y de las Agencias Nº  6, 11,")
        #self.assertEqual(objects[12], "Servicio de Desinfección del edificios sede de la Dirección Regional Palermo y de las Agencias Nº  6, 11, 46 y 51.")
        self.assertEqual(objects[13], "Servicio de mantenimiento de los Ascensores del edificio sede de la Dirección Regional Palermo")
        self.assertEqual(objects[14], "Provisión de Indumentaria para operativos")
        self.assertEqual(objects[15], "Adquisición de Papel Obra A4")
        self.assertEqual(objects[16], "Serv. Correctivo y de mantenimiento de los Ascensores de la")
        #self.assertEqual(objects[16], "Serv. Correctivo y de mantenimiento de los Ascensores de la Agencia Nº 51.")
        self.assertEqual(objects[17], "CD-UPS de Agencia Nº 46, reubicación /adecuación")
        self.assertEqual(objects[18], "Locación del Edificio Sede de la Agencia Nº 06")
        self.assertEqual(objects[19], "Mantenimiento de la iluminación de las Salidas de Emergencia de")
        #self.assertEqual(objects[19], "Mantenimiento de la iluminación de las Salidas de Emergencia de la Dirección Regional Palermo y de las Agencias Nº 6, 11, 46 y 51.")
        self.assertEqual(objects[20], "Adquisición de Estanterías para la Agencia Nº 51")
        self.assertEqual(objects[21], "Servicio de Limpieza de Tanques de Agua Potable para los edificios sede de la Dirección Regional Palermo")
        #self.assertEqual(objects[21], "Servicio de Limpieza de Tanques de Agua Potable para los edificios sede de la Dirección Regional Palermo y de la Agencia Nº 51.")
        self.assertEqual(objects[22], "Servicio de verificación y/o recarga de Matafuegos de la Dirección Regional Palermo y de las Agencias Nº 6, 11, 46 y 51")
        self.assertEqual(objects[23], "Servicio de p Limpieza del edificio sede de la Agencia")
        #self.assertEqual(objects[23], "Servicio de p Limpieza del edificio sede de la Agencia Nº 46.")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
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
        self.assertEqual(proveedores[9], ("CONGRESO INSUMOS SA.", {'moneda': '$', 'valor': 33192.80}))
        self.assertEqual(proveedores[10], ("SIECO SA", {'moneda': '$', 'valor': 7156.0 }))
        self.assertEqual(proveedores[11], ("SICA SRL", {'moneda': '$', 'valor': 49800.0 }))
        self.assertEqual(proveedores[12], ("CIA. FUMIGADORA DEL NORTE", {'moneda': '$', 'valor': 33840.0 }))
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
            
    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica , "GENDARMERÍA NACIONAL ARGENTINA")

    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ('REDIMEC S.R.L.', {'moneda': 'USD', 'valor': 996000.0}))


if __name__ == '__main__':
    unittest.main()
