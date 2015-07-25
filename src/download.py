import datetime
import os
import requests
import subprocess
import sys
import time
import logging
from Queue import Queue
from threading import Thread

from config import *

# Queue of the PDFs to Download
download_queue = Queue()

# Queue of the PDFs to parse
pdf_queue = Queue()


class DownloadThread(Thread):
    """ It's the worker in charge of download the PDFs """
    
    def run(self):
        while True:
            item = download_queue.get()
            
            # If there is no more PDF's to download we exit
            if item == None:
                break
            
            if not os.path.exists(item['filename_path']):
                logging.info('[%s]: Downloading', item['filename_path'])
                try:
                    r = requests.get(BO_URL.format(item['section'], item['date']), timeout = 10)
                    
                    # Check if the response is a PDF, weekends and national holiday there is no PDF
                    if r.content[1:4] == 'PDF':
                        with open(item['filename_path'], 'w') as f:
                            f.write(r.content)

                            logging.info('[%s]: Downloading OK', item['filename_path'])

                            # We store the PDF downloaded for parsing
                            pdf_queue.put({'pdf': item['filename_path']})
                except:
                    # If there is a Timeout error we try again
                    logging.error('[%s]: Downloading Timeout', item['filename_path'])
                    download_queue.put(item)
            else:
                # We don't know if this PDF was parsed
                pdf_queue.put({'pdf': item['filename_path']})
                logging.warning('[%s]: Downloading Already Existed', item['filename_path'])
                        
            download_queue.task_done()

            
class PDFThread(Thread):
    """ It's the worker in charge of parsing the PDFs """
    
    def run(self):
        while True:
            item = pdf_queue.get()

            # If there is no more PDF's to parse we exit
            if item == None:
                break

            pdf = item['pdf']

            # Output filename
            filename = os.path.basename(pdf)
            filename_out = os.path.splitext(filename)[0] + ".txt"
            path_filename_out = os.path.join(TXT_PATH, filename_out)

            logging.info('[%s]: Parsing', pdf)
            if not os.path.exists(path_filename_out):
                subprocess.call(['pdftotext', pdf, path_filename_out])
                logging.info('[%s]: Parsing OK', pdf)
            else:
                logging.warning('[%s]: Parsing Already Existed', pdf)                
                
            pdf_queue.task_done()


def download(date, path = PDF_PATH, sections = ('01', '02', '03'), until = None):
    """ Download Boletin's PDF and stores it in the PDF_PATH """
    
    if not until: until = date
    
    pdfs = []
    delta = datetime.timedelta(days = 1)

    # Init the Threads
    threads_count = 3
    threads = []
    for _ in range(threads_count):
        thread = DownloadThread()
        thread.start()
        threads.append(thread)

        thread = PDFThread()
        thread.start()
        threads.append(thread)

    # Iterate through all the dates
    while date <= until:
        for section in sections:
            date_str =  date.strftime('%Y%m%d')
            filename = '{0}-{1}.pdf'.format(date_str, section)
            download_queue.put({
                'date': date_str,
                'section': section,
                'filename_path': os.path.join(path, filename)
            })

        download_queue.join()
        date += delta

    # Close all the threads and the queues
    for _ in range(threads_count):
        download_queue.put(None)
        pdf_queue.put(None)
        
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print >>sys.stderr, 'usage: python download.py <from date: yyyymmdd> <to date: yyyymmdd>'
        sys.exit(1)

    
    date = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
    date_to = date
    if len(sys.argv) == 3:
        date_to = datetime.datetime.strptime(sys.argv[2], '%Y%m%d')

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='logs/download.log')
    
    download(date, until = date_to)

