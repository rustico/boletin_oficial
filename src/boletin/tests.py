# -*- coding: utf-8 -*-
import unittest

import fixtures
from parser import BoletinParser

BOLETIN_PATH = './fixture_files'

class TestBoletinSeccion(unittest.TestCase):
    def test_when_boletin_has_seccion_adjudicaciones(self):
        boletin =  BoletinParser(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Adjudicaciones"))

    def test_when_boletin_has_seccion_adjudicaciones2(self):
        boletin =  BoletinParser(fixtures.boletines[3]);
        self.assertTrue(boletin.tiene_seccion("Adjudicaciones"))

    def test_when_boletin_has_seccion_dictamenes_de_evaluacion(self):
        boletin =  BoletinParser(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Dictámenes de Evaluación"))

    def test_when_boletin_has_seccion_dictamenes_de_evaluacion_without_accents(self):
        boletin =  BoletinParser(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Dictamenes de Evaluacion"))        

    def test_when_boletin_has_seccion_servicios(self):
        boletin =  BoletinParser(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Servicios Tres Palabras Audiovisuales"))

    def test_when_boletin_has_seccion_locaciones(self):
        boletin =  BoletinParser(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Locaciones INMUEBLES (LOC)"))

    def test_when_boletin_doesnot_has_seccion_adjudicaciones(self):
        boletin =  BoletinParser(fixtures.boletines[1].replace("Adjudicaciones", "Preadjudicaciones"));
        self.assertFalse(boletin.tiene_seccion("Adjudicaciones"))

    def test_when_boletin_returns_from_seccion_adjudicaciones_copete(self):
        boletin = BoletinParser(fixtures.boletines[0]);
        self.assertEqual(boletin.get_desde_copete("Adjudicaciones"),
                         """
#I4284951I# % 23 % #N157178/11N#
BANCO DE LA NACION ARGENTINA
AREA COMPRAS Y CONTRATACIONES""")

    def test_when_boletin_returns_from_seccion_adjudicaciones_copete2(self):
        boletin = BoletinParser(fixtures.boletines[4]);
        self.assertEqual(boletin.get_desde_copete("Adjudicaciones"),
                         """
#I4080874I#
EJERCITO ARGENTINO
COMANDO DE REMONTA
""")

    def test_when_boletin_returns_from_seccion_dictamenes_de_evaluacion_copete(self):
        boletin = BoletinParser(fixtures.boletines[1]);
        self.assertEqual(boletin.get_desde_copete("Dictámenes de Evaluación"),
                         """
#I4284955I# % 23 % #N157178/11N#
BANCO DE LA NACION ARGENTINA
BANCO PIRULO
% 19 % #F4284955F#
Locaciones
INMUEBLES (LOC)
#I4286333I# % 19 % #N159046/11N#
AFIP
#F4286333F#
""")

    def test_when_boletin_returns_nothing_from_seccion_adjudicaciones_copete(self):
        boletin = BoletinParser(fixtures.boletines[0].replace("Adjudicaciones", r"#I4284951I# % 23 % #N157178/11N#\nAdjudicaciones"))
        self.assertFalse(boletin.get_desde_copete("Adjudicaciones"))

    def test_when_boletin_return_seccion_adjudicacion(self):
        boletin = BoletinParser(fixtures.boletines[1]);
        boletin.section_names = ['SUMINISTROS', 'OBRAS', 'SERVICIOS', 'VENTAS Y OFRECIMIENTOS DEL ESTADO', 'LOCACIONES', 'PREADJUDICACIONES', 'ADJUDICACIONES', 'DICTAMENES DE EVALUACION']
        self.assertEqual(boletin.get_section("Adjudicaciones"), """
#I4284952I# % 23 % #N157178/11N#
BANCO DE LA NACION ARGENTINA
AREA COMPRAS Y CONTRATACIONES
% 23 % #F4284952F#
#I4285623I# % 23 % #N158007/11N#
BLOQUE1
% 23 % #F4285623F#
#I4285624I# % 23 % #N158007/11N#
BLOQUE2
% 23 % #F4285624F#
#I4285625I# % 23 % #N158007/11N#
BLOQUE3
% 23 % #F4285625F#
""")

    def test_when_boletin_return_seccion_adjudicacion2(self):
        boletin = BoletinParser(fixtures.boletines[3]);
        boletin.section_names = ['ADJUDICACIONES', 'SERVICIOS COMUNICACIONES']
        self.assertEqual(boletin.get_section("Adjudicaciones"), """
#I4080874I#
EJERCITO ARGENTINO
COMANDO DE REMONTA 
Y VETERINARIA SUBASTA PUBLICA 
Nº 03/2010
Expediente Nº AF 10 – 219/5
DESIERTO DE OFERENTES
Objeto de la contratación: Subasta de 450 To-
neladas de Soja a granel, en el Establecimiento 
General Paz, Ruta Provincial 6 Km 153.5 – Or-
dóñez – Provincia de Córdoba.
Observaciones Generales:
Consulta del expediente: Comando de Remonta y 
Veterinaria - División Compras y Contrataciones, 2do 
Piso - Arévalo 3065 - Ciudad Autónóma de Buenos 
Aires - De lunes a viernes de 08:00 a 12:00 horas.
e. 15/03/2010 Nº 24766/10 v. 15/03/2010
#F4080896F#
""")

    def test_when_boletin_return_seccion_dictamenes_de_evaluacion(self):
        boletin = BoletinParser(fixtures.boletines[1]);
        boletin.section_names = ['ADJUDICACIONES', 'DICTAMENES DE EVALUACION', 'LOCACIONES INMUEBLES (LOC)']
        self.assertEqual(boletin.get_section("Dictámenes de Evaluación"), """
#I4284955I# % 23 % #N157178/11N#
BANCO DE LA NACION ARGENTINA
BANCO PIRULO
% 19 % #F4284955F#
""")

    def test_when_boletin_return_seccion_servicios(self):
        boletin = BoletinParser(fixtures.boletines[1]);
        boletin.section_names = ['Servicios Tres Palabras Audiovisuales', 'Adjudicaciones', 'DICTAMENES DE EVALUACION']
        self.assertEqual(boletin.get_section("Servicios Tres Palabras Audiovisuales"), """
#I4284951I# % 23 % #N157178/11N#
BLOQUE1
% 23 % #F4284951F#
#I4285722I# % 23 % #N158007/11N#
BLOQUE2
% 23 % #F4285722F#
""")
    
    def test_when_boletin_returns_modulos_seccion_adjudicaciones(self):
        boletin = BoletinParser(fixtures.boletines[1])
        boletin.section_names = ['ADJUDICACIONES', 'DICTAMENES DE EVALUACION', 'LOCACIONES INMUEBLES (LOC)']
        modulos = boletin.get_section_elements("Adjudicaciones")
        self.assertEqual(len(modulos), 4)
        self.assertEqual(modulos[0][1], "BANCO DE LA NACION ARGENTINA\nAREA COMPRAS Y CONTRATACIONES")
        self.assertEqual(modulos[2][1], "BLOQUE2")

    def test_when_boletin_returns_modulos_seccion_servicios(self):
        boletin = BoletinParser(fixtures.boletines[1])
        boletin.section_names = ['Servicios Tres Palabras Audiovisuales', 'ADJUDICACIONES', 'DICTAMENES DE EVALUACION', 'LOCACIONES INMUEBLES (LOC)']
        modulos = boletin.get_section_elements("Servicios Tres Palabras Audiovisuales")
        self.assertEqual(len(modulos), 2)

    def test_when_boletin_returns_modulos_seccion_dictamenes(self):
        boletin = BoletinParser(fixtures.boletines[1])
        boletin.section_names = ['ADJUDICACIONES', 'DICTAMENES DE EVALUACION', 'LOCACIONES INMUEBLES (LOC)']
        modulos = boletin.get_section_elements("Dictámenes de Evaluación")
        self.assertEqual(len(modulos), 1)

    def test_get_third_section_titles(self):
        boletin = BoletinParser(fixtures.boletines[6])
        section_names = boletin.get_sections_names()
        self.assertEqual(len(section_names), 8)
        self.assertEqual(section_names[7], 'DICTAMENES DE EVALUACION')

    def test_get_boletin_section_elements_from_a_boletin_file(self):
        boletin_filename = '/20150720-03.txt'
        with open(BOLETIN_PATH + boletin_filename, 'r') as boletin_file:
            boletin_str = boletin_file.read()
            
        boletin = BoletinParser(boletin_str)
        elements = boletin.get_section_elements("Adjudicaciones")
        self.assertEqual(len(elements), 16)

if __name__ == '__main__':
    unittest.main()
