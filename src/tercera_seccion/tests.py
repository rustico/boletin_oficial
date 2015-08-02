# -*- coding: utf-8 -*-
import unittest
import fixtures
from parser import AdjudicacionParser

class TestAdjudicaciones(unittest.TestCase):
    def test_when_empty_return_texto_empty(self):
        adjudicacion = AdjudicacionParser()
        self.assertFalse(bool(adjudicacion.texto))
    
    def test_when_nestor_return_texto_nestor(self):
        adjudicacion = AdjudicacionParser("Nestor")
        self.assertEqual(adjudicacion.texto, "Nestor")

    def test_when_adjudicacion_0_return_entidad_publica(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[0])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "FUERZA AEREA ARGENTINA ESTADO MAYOR GENERAL DE LA FUERZA AEREA INSTITUTO DE FORMACION EZEIZA")

    def test_when_adjudicacion_0_return_proveedor(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[0])
        proveedores = adjudicacion.get_proveedores()
        self.assertTrue("METEO S.A. " in proveedores)

    def test_when_adjudicacion_0_return_proveedor2(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[8])
        proveedores = adjudicacion.get_proveedores()
        precios = adjudicacion.get_precios()

        self.assertTrue("LA LEY S.A." in proveedores)
        self.assertEqual("LA LEY S.A.", proveedores[0])
        self.assertEqual(len(proveedores), len(precios))

    def test_when_adjudicacion_0_return_proveedor3(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[9])
        proveedores = adjudicacion.get_proveedores()
        precios = adjudicacion.get_precios()
        self.assertEqual(len(proveedores), len(precios))
    
    def test_when_adjudicacion_0_return_precios(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[0])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 87900)

    def test_when_adjudicacion_1_return_entidad_publica(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "FUERZA AEREA ARGENTINA DIRECCION GENERAL DE INTENDENCIA DIRECCION DE CONTRATACIONES")

    def test_when_adjudicacion_1_return_proveedor(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])
        self.assertTrue("CAE USA INC." in adjudicacion.get_proveedores());

    def test_when_adjudicacion_1_return_objeto(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])
        self.assertEqual(adjudicacion.get_objeto(), "Cursos de Mantenimiento de Motores T-56.")

    def test_when_adjudicacion_1_return_precios(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[1])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "U$S" and precios[0]["valor"] == 74076)

    def test_when_adjudicacion_2_return_entidad_publica(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[2])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "EJERCITO ARGENTINO COLEGIO MILITAR DE LA NACION")

    def test_when_adjudicacion_2_return_objeto(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[2])
        self.assertEqual(adjudicacion.get_objeto(), "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre 2011 y 1er Trimestre 2012.")

    def test_when_adjudicacion_2_return_proveedores(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[2])
        proveedores = adjudicacion.get_proveedores()
        self.assertTrue("LEONARDO MAZZEO" in proveedores)
        self.assertTrue("DISTRIBUIDORA SYNERGIA S.R.L." in proveedores)
        self.assertTrue("SUALIER SA" in proveedores)
        self.assertTrue("VIMI S.A." in proveedores)

    def test_when_adjudicacion_2_return_precios(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[2])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 19906)
        self.assertTrue(precios[1]["moneda"] == "$" and precios[1]["valor"] == 19621.45)
        self.assertTrue(precios[2]["moneda"] == "$" and precios[2]["valor"] == 686950)
        self.assertTrue(precios[3]["moneda"] == "$" and precios[3]["valor"] == 34893.80)

    def test_when_adjudicacion_3_return_entidad_publica(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[3])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "GENDARMERIA NACIONAL ARGENTINA")

    def test_when_adjudicacion_3_return_objeto(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[3])
        self.assertEqual(adjudicacion.get_objeto(), "Adquisición de Equipamiento Técnico para la Dirección de Policía Científica.")

    def test_when_adjudicacion_3_return_proveedores(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[3])
        proveedores = adjudicacion.get_proveedores()
        self.assertTrue("PROMETIN S.A." in proveedores)
        self.assertTrue("TECNOELECTRIC S.R.L." in proveedores)

    def test_when_adjudicacion_3_return_precios(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[3])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 594)
        self.assertTrue(precios[1]["moneda"] == "$" and precios[1]["valor"] == 8577)

    def test_when_adjudicacion_4_return_entidad_publica(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[4])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL ADUANERA MENDOZA")

    def test_when_adjudicacion_4_return_objeto(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[4])
        self.assertEqual(adjudicacion.get_objeto(), "Adquisición de Chombas de Piqué identificatorias.")

    def test_when_adjudicacion_4_return_proveedores(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[4])
        proveedores = adjudicacion.get_proveedores()    
        self.assertTrue("FEDERICO LOPEZ." in proveedores)

    def test_when_adjudicacion_4_return_precios(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[4])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 44884.66)

    def test_when_adjudicacion_5_return_precios(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[5])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 33900,00)

    def test_when_adjudicacion_6_return_objeto(self):
        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[6])
        self.assertEqual(adjudicacion.get_objeto(), "Mantenimiento Edilicio.")

#    def test_when_adjudicacion_7_return_objeto(self):
#        adjudicacion = AdjudicacionParser(fixtures.adjudicaciones[7])
#        self.assertEqual(adjudicacion.get_objeto(), "No tiene un objeto de adjudicacion")

if __name__ == '__main__':
    unittest.main()
