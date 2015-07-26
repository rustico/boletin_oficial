# -*- coding: utf-8 -*-
import re
from unidecode import unidecode

class BoletinParser():
    """ Parser that allow us to get different sections of the Boletin """
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
                         .replace('u', '[úu]+') \
                         .replace('(', '\(') \
                         .replace(')', '\)')
        

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

    def get_section(self, section_name):
        section = self.get_desde_copete(section_name)
        section_without_accents = unidecode(section_name.decode('utf-8')).lower() # And in lowercase

        # We get the name of the next section
        next_section_index = [i + 1 for i, x in enumerate(self.section_names) if x.lower() == section_without_accents]

        # If there is a section after 'section_name'
        if len(next_section_index) > 0:
            next_section_index = next_section_index[0]
            if next_section_index < len(self.section_names):
                # We remove the text that belongs to the other section
                next_section_name = self.section_names[next_section_index].lower()
                next_section_regex = self._get_section_regex(next_section_name)
                next_section_result = next_section_regex.search(section)

                if next_section_result:
                    next_section_start = next_section_result.start()
                    section = section[:next_section_start]

        return section
 
    def get_sections_names(self):
        regex_str = r"(^[A-Z ]+)[ \.]+\.$"
        regex = re.compile(regex_str, re.MULTILINE)
        result = regex.findall(self.boletin)
        section_names = map(str.strip, result)

        return section_names
    
    def get_section_elements(self, seccion):
        seccion_completa = self.get_section(seccion)

        # We get the IDs of the element.
        # Because of a webservice of theirs this could be useful in the future
        regex = re.compile('#I(\d*)I#', re.MULTILINE)
        elements_ids = regex.findall(seccion_completa)
        
        # Match the beginning and the ending of an element
        # They start with #I\d+I# and finish with #F\d+F#
        # They can share the line with other characters of the PDF but they are irrelevant
        regex = re.compile('\n?.*#[FI]\d*[IF]#.*\n', re.MULTILINE)

        # Remove the blank elements
        regex_elements = filter(lambda x: x, regex.split(seccion_completa))

        section_elements = []
        for i, element in enumerate(regex_elements):
            element_id = elements_ids[i]
            section_elements.append((element_id, element))

        return section_elements
