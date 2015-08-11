# -*- coding: utf-8 -*-
import re

class AdjudicacionParser():
    ENTIDAD_TOKENS = [" LICITACION ", " CONTRATACION ", " LICITACIÓN ", " CONTRATACIÓN ", " Expediente "]
    PROVEEDOR_TOKENS = [ "Empresa", "Firma", "Oferente", "Proveedor", "Adjudicatario", "Razón Social"]
    OBJETO_TOKENS = ["Objeto", "Objeto de la contratación"]
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
        atributos_regex = re.compile(",|-\sCuit|Cuit|Por\sPesos|–|\(|CONTRATACION DIRECTA",re.IGNORECASE | re.MULTILINE)

        proveedores = self.__get_elementos_buscados_segun_tokens(self.PROVEEDOR_TOKENS)
        proveedores_nombre = []
        for proveedor in proveedores:
            match = atributos_regex.split(proveedor)
            if (match[0] != "" and match[0] != "\n"):
                proveedores_nombre.append(match[0].strip())

        # We are going to associate each 'Proveedor' with the money
        # For that we first split the text by the 'Proveedores'
        #  then we look if the money is specified before or after the 'Proveedor'
        #  once we find the money we increment the index 'i' to point to the next 'Proveedor'
        i = 0
        proveedores_regex = re.compile('|'.join(proveedores_nombre), re.IGNORECASE)
        proveedores_sections = proveedores_regex.split(self.texto)
        proveedores_money = []
        for section in proveedores_sections:
            money = self.get_money(section)
            if len(money) > 0:
                proveedor_nombre = proveedores_nombre[i].replace('\n', '').strip()
                proveedores_money.append((proveedor_nombre, money[0]))
                i += 1

        return proveedores_money


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
            if self.OBJETO_TOKENS[0].lower() == last_element or self.OBJETO_TOKENS[1].lower() == last_element:
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

        return precios

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
