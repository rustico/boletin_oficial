import datetime
import os
import requests
import subprocess
import sys
import time
from Queue import Queue
from threading import Thread

from config import *

download_queue = Queue()
pdf_queue = Queue()

class DownloadThread(Thread):
    def run(self):
        while True:
            item = download_queue.get()
            if item == None:
                break
            
            if not os.path.exists(item['filename_path']):
                r = requests.get(BO_URL.format(item['section'], item['date']), timeout = 10)
                if r.content[1:4] == 'PDF':
                    with open(item['filename_path'], 'w') as f:
                        f.write(r.content)

                    print(item['filename_path'])
                    pdf_queue.put({'pdf': item['filename_path']})
                        
            download_queue.task_done()

            
class PDFThread(Thread):
    def run(self):
        while True:
            item = pdf_queue.get()
            if item == None:
                break

            pdf = item['pdf']
            filename = os.path.basename(pdf)
            filename_out = os.path.splitext(filename)[0] + ".txt"
            path_filename_out = os.path.join(TXT_PATH, filename_out)
            
            if not os.path.exists(path_filename_out):
                subprocess.call(['pdftotext', pdf, path_filename_out])

            print(path_filename_out)
            pdf_queue.task_done()


def download(date, path = PDF_PATH, sections = ('01', '02', '03'), until = None):
    """ Download Boletin's PDF and stores it in the PDF_PATH """
    if not until: until = date
    pdfs = []
    delta = datetime.timedelta(days = 1)

    threads_count = 3
    threads = []
    for _ in range(threads_count):
        thread = DownloadThread()
        thread.start()
        threads.append(thread)

        thread = PDFThread()
        thread.start()
        threads.append(thread)
        
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

    download(date, until = date_to)

