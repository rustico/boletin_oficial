# -*- coding: utf-8 -*-
import re

class BoletinParser():
    """Lo que hacemos es obtener el texto completo del boletin y a partir de ahi
       vamos diviendo las diferentes secciones
    """

    def __init__(self, boletin):
        self.boletin = boletin.replace("\r", "")
        self.section_names = self.get_sections_names()

    def _get_section_regex(self, section):
        # Because a section title could be splitted in several lines.
        # So we look also for a splited title
        # Also we add optional accents because the section title in uppercase
        # does not have accents when it should.

        section = section.replace(" ", "[\n\s]+") \
                         .replace('a', '[áa]+') \
                         .replace('e', '[ée]+') \
                         .replace('i', '[íi]+') \
                         .replace('o', '[óo]+') \
                         .replace('u', '[úu]+') 

        regex_str = "^{0}$".format(section)
        regex = re.compile(regex_str, re.IGNORECASE | re.MULTILINE)

        return regex
        
    def tiene_seccion(self, section):
        regex = self._get_section_regex(section)
        return regex.search(self.boletin)

    def get_desde_copete(self, section):
        regex = self._get_section_regex(section)
        regex_split = regex.split(self.boletin)

        return regex_split[1] if len(regex_split) > 1 else ""


    def get_seccion(self, seccion):
        desde_copete_seccion = self.get_desde_copete(seccion)
        proximo_copete = self.get_proximo_copete(desde_copete_seccion)
        index_proximo_copete = desde_copete_seccion.find(proximo_copete)

        if index_proximo_copete:
            return desde_copete_seccion[:index_proximo_copete] # Incluye el \n
        
        return desde_copete_seccion

    def get_modulos_seccion(self, seccion):
        seccion_completa = self.get_seccion(seccion)
        regex =  re.compile(r"\%\s\d*\s\%\s\#.*\#\n\#.*\#\s\%\s\d*\s\%\s\#.*\#|\#.*\#\n\#.*\#", re.IGNORECASE)
        return regex.split(seccion_completa)

    def get_sections_names(self):
        regex_str = r"(^[A-Z ]+)[ \.]+\.$"
        regex = re.compile(regex_str, re.MULTILINE)
        result = regex.findall(self.boletin)
        section_names = map(str.strip, result)

        return section_names
    
