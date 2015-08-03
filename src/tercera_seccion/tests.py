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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
        self.assertEqual(objeto, "Mantenimiento y reparación de Edificios y Locales del Instituto")

class TestAdjudicacion01(unittest.TestCase):
    def setUp(self):
        self.adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
        self.assertEqual(objeto, "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre 2011 y 1er Trimestre 2012")

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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
        self.assertEqual(objeto, None)

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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
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

    def test_get_objeto(self):
        objeto = self.adjudicacion.get_objeto()
        self.assertEqual(objeto, "Servicio de Limpieza de los edificios sede de las Agencias")

    def test_get_entidad_publica(self):
        entidad_publica = self.adjudicacion.get_entidad_publica()
        self.assertEqual(entidad_publica, "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL PALERMO")
        
    def test_get_proveedores(self):
        proveedores = self.adjudicacion.get_proveedores()
        self.assertEqual(len(proveedores), 1)
        self.assertEqual(proveedores[0], ("UADEL SRL.", {'moneda': '$', 'valor': 27944.0}))                
        self.assertEqual(proveedores[0], ("INGENIERIA CAAMAÑO SA.", {'moneda': '$', 'valor': 34012.0}))        
    
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
