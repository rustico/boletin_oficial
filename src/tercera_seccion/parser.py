# -*- coding: utf-8 -*-
import re
import logging
from unidecode import unidecode

class AdjudicacionParser():
    ENTIDAD_TOKENS = ["LICITACION", "CONTRATACION", "LICITACIÓN", "CONTRATACIÓN", "Expediente", "SUBASTA", "CONCURSO", 'LP N°', 'LEGAJO DE COMPRA', 'TRAMITE SIMPLIFICADO', 'COMPRA DIRECTA', 'N°', 'COMPRAS', 'LISTADO']
    PROVEEDOR_TOKENS = [ "Empresa", "Firma", "Oferente", "Proveedor", "Adjudicatario", "Razón Social", "Empresa adjudicada", "Nombre del Contratista"]
    OBJETO_TOKENS = ["Objeto", "Objeto de la contratación", "OBJETO DE LA CONTRATACI\xc3\x93N"]
    PRECIO_TOKENS = [ "U$S", "$" ]

    def __init__(self, texto = ""):
        self.texto_original = texto
        self.texto = self.__normalizar(texto)

    def get_government_department_name(self):		
        regex_str = '^' + '|^'.join(self.ENTIDAD_TOKENS)
        regex = re.compile(regex_str, re.IGNORECASE | re.MULTILINE)
        sections = regex.split(self.texto)
        if sections == None:
            return ""
        
        government_department = sections[0].replace('\n', ' ').replace('  ', ' ').upper()
        
        if '-' in government_department:
            government_department = government_department.split('-')[0]

        if 'MINISTERIO DE DEFENSA' in government_department:
            government_department = re.sub('SSSLD|SERVICIO LOGISTICO|SSSL|SSL|DGSLD', 'SLD', government_department)

        if 'A.F.I.P.':
            government_department = government_department.replace('A.F.I.P.', 'AFIP')

        return government_department.strip()

    @staticmethod
    def get_government_department(name):
        government_department_regex = {
            'AFIP': ['^A[.\s]*F[.\s]*I[.\s]*P[.\s]*', 'ADMINISTRACION FEDERAL DE INGRESO', 'AFP'],
            'ARMADA ARGENTINA': ['^ARMADA ARGEN?TINA\s*'],
            'BANCO DE LA NACION ARGENTINA': ['^BANCO DE LA NACION ARGENTINA\s*'],
            'BIBLIOTECA DEL CONGRESO DE LA NACION': ['^BIBLIOTECA DEL CONGRESO DE LA NACION\s*'],
            'CENTRO NACIONAL DE REEDUCACION SOCIAL': ['^CENTRO NACIONAL DE REEDUCACION SOCIAL\s*'],
            'COMANDO GENERAL ELECTORAL': ['^COMANDO GENERAL ELECTORAL\s*'],
            'COMISION NACIONAL DE COMUNICACIONES': ['^COMISION NACIONAL DE COMUNICACIONES\s*'],
            'COMISION NACIONAL DE ENERGIA ATOMICA': ['^COMISION NACIONAL DE ENERGIA ATOMICA\s*'],
            'DIRECCION NACIONAL DE MIGRACIONES': ['^DIRECCION NACIONAL DE MIGRACIONES\s*'],
            'EJERCITO ARGENTINO': ['^EJERCITI?O\s*ARGEN?TINO\s*', '^EJERCITO ARGENTIN?COMANDO\s*'],
            'ESTADO MAYOR CONJUNTO': ['^ESTADO MAYOR CONJUNTO\s*'],
            'FUERZA AEREA ARGENTINA': ['^ESTADO MAYOR GENERAL DE LA FUERZA AEREA\s*', '^FUERZA AE?REA ARGENTINA\s*'],
            'GENDARMERIA NACIONAL ARGENTINA': ['^GENDARMER[IL]A NACIONAL\s*'],
            'H. CAMARA DE DIPUTADOS DE LA NACION': ['^H. CAMARA DE DIPUTADOS DE LA NACION\s*'],
            'INTA': ['^INTA\s*'],
            'MINISTERIO DE DESARROLLO SOCIAL': ['^MINISTERIO DE\s*DESARROLLO SOCIAL\s*'],
            'MINISTERIO DE AGRICULTURA, GANADERIA Y PESCA': ['^MINISTERIO DE AGRICULTURA\s*'],
            'MINISTERIO DE DEFENSA': ['^MINISTERIO DE DEFENSA\s*', 'MINISTERIO DEFENSA\s*'],
            'MINISTERIO DE DESARROLLO SOCIAL': ['^MINISTERIO\s+DE\s+DESARROLLO\s+SOCIAL\s*', '^MINISTERIO DESARROLLO? SOCIAL\s*'],
            'MINISTERIO DE ECONOMIA': ['^MINISTERIO DE ECONOMIA\s*', '^MINISTERIO DE ECONOMLA\s*'],
            'MINISTERIO DE EDUCACION': ['^MINISTERIO DE EDUCACION\s*'],
            'MINISTERIO DE INDUSTRIA': ['^MINISTERIO DE INDUSTRIA\s*'],
            'MINISTERIO DE JUSTICIA': ['^MINISTERIO DE JUSTICIA\s*', '^REPUBLICA ARGENTINA MINISTERIO DE JUSTICIA\s*'],
            'MINISTERIO DE PLANIFICACION': ['^MINISTERIO DE PLANIFICACION\s*', '^PRESIDENCIA DE LA NACION MINISTERIO DE PLANIFICACION FEDERAL\s*'],
            'MINISTERIO DE PRODUCCION': ['^MINISTERIO DE PRODUCCION\s*'],
            'MINISTERIO DE RELACIONES EXTERIORES': ['^MINISTERIO DE RELACIONES EXTERIORES\s*'],
            'MINISTERIO DE SALUD': ['^MINISTERIO DE SALUD\s*', '^PRESIDENCIA DE LA NACION MINISTERIO DE SALUD\s*'],
            'MINISTERIO DE SEGURIDAD': ['^MINISTERIO DE SEGURIDAD\s*', '^REPUBLICA ARGENTINA MINISTERIO DE SEGURIDAD\s*'],
            'MINISTERIO DE TRABAJO': ['^MINISTERIO DE TRABAJO\s*'],
            'MINISTERIO PUBLICO DE LA DEFENSA DEFENSORIA GENERAL DE LA NACION': ['^MINISTERIO\s+PUBLICO\s+DE\s+LA\s+DEFENSA\s+DEFENSORIA\s+GENERAL\s+DE\s+LA\s+NACION\s*'],
            'ONABE': ['^ONABE\s*', '^ORGANISMO NACIONAL DE\s?ADMINISTRACION DE BIENES\s*'],
            'POLICIA FEDERAL ARGENTINA': ['^POLICIA FEDERAL ARGENTINA\s*'],
            'PREFECTURA NAVAL ARGENTINA': ['^PR?EFECTURA NAVAL ARGENTINA\s*'],
            'MINISTERIO DEL INTERIOR': ['^MINISTERIO DEL INTERIOR\s*', '^PRESIDENCIA DE LA NACION MINISTERIO DEL INTERIOR Y TRANSPORTE\s*', '^REPUBLICA ARGENTR?INA MINISTERIO DEL INTERIOR\s*'],
            'UNIVERSIDAD DE BUENOS AIRES': ['^UNIVERSIDAD DE BUENOS AIRES\s*'],
            'UNIVERSIDAD NACIONAL DEL SUR': ['^UNIVERSIDAD NACIONAL DEL SUR\s*'],
            'UNIVERSIDAD TECNOLOGICA NACIONAL': ['^UNIVERSIDAD TECNOLOGICA NACIONAL\s*'],
            'JEFATURA DE GABINETE DE MINISTROS': ['^JEFATURA DE GABINETE DE MINISTROS\s*'],
            'MINISTERIO DE CIENCIA, TECNOLOGIA E INNOVACION PRODUCTIVA': ['^MINISTERIO DE CIENCIA, TECNOLOGIA E INNOVACION PRODUCTIVA\s*'],
            'AUTORIDAD REGULATORIA NUCLEAR': ['^AUTORIDAD REGULATORIA NUCLEAR\s*', '^AUTORIDAD REGULADORA NUCLEAR\s*', '^PRESIDENCIA DE LA NACION AUTORIDAD REGULATORIA NUCLEAR\s*'],
            'SECRETARIA DE PROGRAMACION PARA LA PREVENCION DE LA DROGADICCION Y LA LUCHA CONTRA EL NARCOTRAFICO': ['^PRESIDENCIA DE LA NACION SECRETARIA DE PROGRAMACION PARA LA PREVENCION DE LA DROGADICCION Y LA LUCHA CONTRA EL NARCOTRAFICO\s*'],
            'SECRETARIA DE TURISMO': ['^PRESIDENCIA DE LA NACION SECRETARIA DE TURISMO\s*'],
            'SECRETARIA GENERAL DIRECCION DE PATRIMONIO Y SUMINISTROS': ['^PRESIDENCIA DE LA NACION SECRETARIA GENERAL DIRECCION DE PATRIMONIO Y SUMI?NISTROS?\s*', '^PRESIDENCIA DE LA NACION SECRETARIA GENERAL SUBSECRETARIA DE COORDINACION DIRECCION DE PATRIMONIO Y SUMINISTROS\s*'],
            'SERVICIO PENITENCIARIO FEDERAL': ['^SERVICIO PENITENCIARIO FEDERAL\s*'],
            'UNIVERSIDAD NACIONAL DE CORDOBA': ['^UNIVERSIDAD NACIONAL DE CORDOBA\s*'],
            'UNIVERSIDAD NACIONAL DE LA MATANZA': ['^UNIVERSIDAD NACIONAL DE LA MATANZA\s*'],
        }

        for government_name, regex_values in government_department_regex.iteritems():
            regex_str = '|'.join(regex_values)
            regex = re.compile(regex_str)
            if regex.match(name):
                return government_name

        return name
        

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
        regex_cuit = re.compile('^[\s\n]*CUIT', re.IGNORECASE)
        for section in sections:
            if regex_cuit.match(section):
                continue
            
            matches = regex.findall(section)
            matches = filter(lambda x: x, matches)
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

    @staticmethod
    def get_adjudicaciones(date_str, elements):
        adjudicaciones = []
        
        for element in elements:
            element_id = element[0]
            
            adjudicacion_id, adjudicacion_str = element
            adjudicacion  = AdjudicacionParser(adjudicacion_str)
            
            government_department_name = adjudicacion.get_government_department_name()
            government_department_name = unidecode(government_department_name.decode('utf-8'))
            government_department = adjudicacion.get_government_department(government_department_name)
            
            objects = adjudicacion.get_objects()
            proveedores = adjudicacion.get_proveedores()
            objects_total = len(objects)
            proveedores_total = len(proveedores)
            
            if objects_total == 0 or proveedores_total == 0:
                logging.warning('[%s - %s] %s | %s', date_str, element_id, government_department, proveedores)
            else:
                if objects_total == 1:
                    logging.info('[%s - %s] %s | %s', date_str, element_id, government_department, proveedores)
                    
                    for proveedor in proveedores:
                        adjudicaciones.append({
                            'd': date_str,
                            'e': government_department,
                            #'e_n': government_department_name,
                            'o': unidecode(objects[0].decode('utf-8')).replace('"', ''),
                            'p': unidecode(proveedor[0].decode('utf-8')).replace('"', ''),
                            'm': proveedor[1],
                            'i': adjudicacion_id
                        })
                elif proveedores_total == objects_total:
                    logging.info('[%s - %s] %s | %s', date_str, element_id, government_department, proveedores)
                    
                    for x in zip(objects, proveedores):
                            adjudicaciones.append({
                                'd': date_str,
                                'e': government_department,
                                #'e_n': government_department_name,
                                'o': unidecode(x[0].decode('utf-8')).replace('"', ''),
                                'p': unidecode(x[0][0].decode('utf-8')).replace('"', ''),
                                'm': unidecode(x[0][1].decode('utf-8')),
                                'i': adjudicacion_id
                            })
                else:
                    logging.warning('[%s - %s] %s | %s', date_str, element_id, government_department, proveedores)
                    
            print(adjudicacion, government_department, proveedores)
            
        return  adjudicaciones
                


