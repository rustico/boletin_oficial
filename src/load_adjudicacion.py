import sys
import os
import logging
from datetime import datetime
from unidecode import unidecode

import config
from boletin.parser import BoletinParser
from tercera_seccion.parser  import AdjudicacionParser

def load(date, boletin_str):
    boletin = BoletinParser(boletin_str)
    elements = boletin.get_section_elements("Adjudicaciones")
    
    for element in elements:
        adjudicacion_id, adjudicacion_str = element
        adjudicacion  = AdjudicacionParser(adjudicacion_str)

        import ipdb; ipdb.set_trace()
        entidad_publica = adjudicacion.get_entidad_publica()
        entidad_publica = unidecode(entidad_publica.decode('utf-8'))
        objeto = adjudicacion.get_objeto()
        objeto = unidecode(objeto.decode('utf-8'))
        precios = adjudicacion.get_precios()
        proveedores = adjudicacion.get_proveedores()
        proveedores_precios = zip(proveedores, precios)

        print(date)
        print(adjudicacion_str)
        print(adjudicacion, entidad_publica, objeto, proveedores_precios)
        break

    exit(1)
    
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print >>sys.stderr, 'usage: load_adjudicaciones.py <from date: yyyymmdd> <to date: yyyymmdd>'
        sys.exit(1)

    # Date Range
    date_from = datetime.strptime(sys.argv[1], '%Y%m%d')
    date_to = None

    # Date To
    if len(sys.argv) == 3:
        date_to = datetime.strptime(sys.argv[2], '%Y%m%d')

    # Logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='logs/adjudicaciones.log')

    # Looking for the files to parse
    os.chdir(config.TXT_PATH) 
    for filename in os.listdir('.'):
        # We only want the third section
        if filename.endswith("03.txt"):
            date_filename_str = filename.split('-')[0]
            date_filename = datetime.strptime(date_filename_str, '%Y%m%d')
            if date_filename >= date_from and (date_to == None or date_filename <= date_to):
                with open(filename, 'r') as boletin_file:
                    boletin_str = boletin_file.read()

                total = load(date_filename, boletin_str)

        
