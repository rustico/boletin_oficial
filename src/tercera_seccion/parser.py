# -*- coding: utf-8 -*-
import re

class AdjudicacionParser():
    ENTIDAD_TOKENS = [" LICITACION ", " CONTRATACION "]
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
                return texto[0: find_index]

        return ""

    def get_proveedores(self):
        atributos_regex = re.compile(",|-\sCuit|Cuit|Por\sPesos|–|\(",re.IGNORECASE | re.MULTILINE)

        proveedores = self.__get_elementos_buscados_segun_tokens(self.PROVEEDOR_TOKENS)
        proveedores_nombre = []

        for proveedor in proveedores:
            matchs = atributos_regex.split(proveedor)

            if (matchs[0].upper() != ""):
                proveedores_nombre.append(matchs[0].upper())
            #else:
             #   if (matchs[1]):
              #      proveedores_nombre.append(matchs[0].upper())


        return proveedores_nombre 


    def get_objeto(self):
        # Si no tiene un objeto de adjudicacion, rompe
        return self.__get_elementos_buscados_segun_tokens(self.OBJETO_TOKENS)[0] 

    def get_precios(self):
        precios_regex = re.compile(u"""(\$|U\$S)
                                      \s*
                                      ([\d*\.*]*,\d*|[\d*\.*]*)""",re.MULTILINE | re.VERBOSE | re.UNICODE)

        precios_texto = precios_regex.findall(self.texto)
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
                    elementos.append(matchs[index + 1].strip().replace("\n", " ").replace("  ", " "))

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
