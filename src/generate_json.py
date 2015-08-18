import sys
import os
import json
import logging
from datetime import datetime

import config
from boletin.parser import BoletinParser
from tercera_seccion.parser  import AdjudicacionParser

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
    adjudicaciones = []
    os.chdir(config.TXT_PATH) 
    for filename in os.listdir('.'):
        # We only want the third section
        if filename.endswith("03.txt"):
            date_filename_str = filename.split('-')[0]
            date_filename = datetime.strptime(date_filename_str, '%Y%m%d')
            if date_filename >= date_from and (date_to == None or date_filename <= date_to):
                with open(filename, 'r') as boletin_file:
                    # Boletin Parser
                    boletin_str = boletin_file.read()
                    boletin = BoletinParser(boletin_str)

                print(date_filename_str)
                
                try:
                    elements = boletin.get_section_elements("Adjudicaciones")
                    boletin_adjudicaciones = AdjudicacionParser.get_adjudicaciones(date_filename_str, elements)
                    if boletin_adjudicaciones:
                        adjudicaciones +=  boletin_adjudicaciones
                except Exception as e:
                    logging.error('[%s] %s', date_filename_str, e)

    os.chdir(config.JSON_PATH)                 
    with open('adjudicaciones.json', 'w+') as adjudicaciones_file:
        json.dump(adjudicaciones, adjudicaciones_file)
        
    exit(0)        
