# -*- coding: utf-8 -*-
import re

class AdjudicacionParser():
    ENTIDAD_TOKENS = [" LICITACION ", " CONTRATACION ", " LICITACIÓN ", " CONTRATACIÓN ", " Expediente "]
    PROVEEDOR_TOKENS = [ "Empresa", "Firma", "Oferente", "Proveedor", "Adjudicatario", "Razón Social", "Empresa adjudicada"]
    OBJETO_TOKENS = ["Objeto", "Objeto de la contratación", "OBJETO DE LA CONTRATACI\xc3\x93N"]
    PRECIO_TOKENS = [ "U$S", "$" ]

    def __init__(self, texto = ""):
        self.texto_original = texto
        self.texto = self.__normalizar(texto)

    def get_entidad_publica(self):		
        texto = self.texto.replace("\n", " ").replace("  ", " ")

        for entidad in self.ENTIDAD_TOKENS:
            find_index = texto.find(entidad)
            if find_index != -1:
                return texto[0: find_index].strip()

        return ""

    def get_proveedores(self):
        # Split the text by the 'Proveedor' tokens
        regex_str = ':|'.join(self.PROVEEDOR_TOKENS) + ':'
        regex = re.compile(regex_str, re.IGNORECASE)
        sections = regex.split(self.texto)
        
        # If we didn't find any 'Proveedor' token return an empty list
        if(len(sections) < 1):
            return []

        # So we need to check if the money is before or after the 'Proveedor' name
        # If this is True we add the proveedor to the list
        first_section = sections[0]
        money_before = False
        proveedor_money = self.get_money(first_section)

        if proveedor_money:
            money_before = True
        else:
            proveedor_money = None

        # We remove the text before the first find
        sections = sections[1:]
        proveedores = []
        regex = re.compile('\s*(.*)\.?\n')
        regex_attribute_name = re.compile('^[\w\s]+:')
        regex_cuit = re.compile('^\n?CUIT', re.IGNORECASE)
        for section in sections:
            if regex_cuit.match(section):
                continue
            
            matches = regex.findall(section)
            if len(matches) > 0:
                proveedor_name = ''
                for i, match in enumerate(matches):
                    if regex_attribute_name.match(match):
                        break
                    
                    proveedor_name += match

                    if proveedor_name[-1] == '.':
                        break
                if not proveedor_name:
                    continue
                
                if '(' in proveedor_name:
                    proveedor_name = proveedor_name.split('(')[0]

                if 'CUIT' in proveedor_name.upper():
                    proveedor_name = proveedor_name.upper().split('CUIT')[0]

                proveedor_name = proveedor_name.strip()

                if proveedor_name[-1] == '.':
                    proveedor_name = proveedor_name[:-1].strip()

                if proveedor_name[-1] == '-':
                    proveedor_name = proveedor_name[:-1].strip()
                    
            else:
                continue

            if money_before:
                proveedores.append((proveedor_name, proveedor_money))
                proveedor_money = self.get_money(section)
            else:
                proveedor_money = self.get_money(section)
                proveedores.append((proveedor_name, proveedor_money))
                
        return proveedores

    def get_objects(self):
        tokens = '|'.join(self.OBJETO_TOKENS)
        regex_str = "^({0}):(.*)".format(tokens)
        regex = re.compile(regex_str, re.IGNORECASE | re.MULTILINE)
        elements = regex.split(self.texto)
        objetos = []
        objeto = None
        last_element = None
        add_next_line = False
        total_elements = len(elements)
        for i, element in enumerate(elements):
            if self.OBJETO_TOKENS[0].lower() == last_element or self.OBJETO_TOKENS[1].lower() == last_element or self.OBJETO_TOKENS[2].lower() == last_element:
                objeto = element.strip().replace('\n', '')
                if objeto[-1] != '.':
                    add_next_line = True
                else:
                    objeto = objeto[:-1]
                    objetos.append(objeto)

            elif add_next_line and objeto:
                # First element is ''
                objeto = objeto + ' ' + element.split('\n')[1].strip()

                # Found the '.'
                if objeto[-1] == '.':
                    objeto = objeto[:-1]

                # Object with two line
                objetos.append(objeto)
                objeto = None
                add_next_line = False


            last_element = element.lower().strip()
        return objetos

    def get_money(self, text):
        precios_regex = re.compile(u"""(\$|U\$S|USD)
                                      \s*
                                      ([\d*\.*]*,\d*|[\d*\.*]*)""",re.MULTILINE | re.VERBOSE | re.UNICODE)

        precios_texto = precios_regex.findall(text)
        precios = []

        for moneda, valor_str in precios_texto:
            try:
                valor = float(valor_str.replace('.', '').replace(',','.'))
            except ValueError, e:
                valor = 0

            precios.append({'moneda' : moneda, 'valor' : valor })

        if len(precios) == 0:
            return None
        
        return precios[0]

    def __get_elementos_buscados_segun_tokens(self, tokens):
        atributos_regex = re.compile("(^[a-záéíóúº\s]*):",re.IGNORECASE | re.MULTILINE)

        # Guardamos a los atributos y sus valores
        # Es una negrada, pero por ejemplo el atributo Proveedor esta en el indice 0
        # su valor en el indice 1. Siempre antes del primer atributo esta la entidad,
        # por eso la descartamos.

        matchs = atributos_regex.split(self.texto)[1:]
        elementos = []

        # Al recorrer la mitad de los elementos, recorremos los atributos solamente
        for index in range(0, len(matchs), 2):
            for token in tokens:
                if token.lower() in matchs[index].lower():
                    elementos.append(matchs[index + 1])

        return elementos

    def __normalizar(self, texto):
        texto =  texto.replace("-\n", "") \
                      .replace("Orden de Compra Nº", "\nOrden de Compra Nº:") \
                      .replace(" ", " ") \
                      .replace("\xc2\xa0", " ") # Non-breaking space = $nbsp;
                      
        # e. 30/11/2011 Nº 157360/11 v. 30/11/2011
        last_line_regex = re.compile("""^e\.
                                         .*
                                         Nº
                                         .*
                                         v\.
                                         .*""", re.VERBOSE | re.MULTILINE | re.UNICODE) 

        return last_line_regex.split(texto)[0]
