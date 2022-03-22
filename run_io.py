import logging
import requests
import urllib.request
import uuid
import shutil
import time

logging.basicConfig(format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def download_file():
    url = 'http://httpd-download:8080/10kb'
    r = requests.get(url, allow_redirects=True)

    open('/mnt/10kb', 'wb').write(r.content)

def url_checker():
    url = 'http://httpd-download:8080'
    while True:
        try:
            status_code = urllib.request.urlopen(url).getcode()
            if status_code == 200:
                return 0
            logging.info(status_code)
        except urllib.error.URLError:
            time.sleep(2)
            logging.info("failed to get the data")
            continue

def run_io():
    src = "/mnt/10kb"
    # while True:
    for i in range(1 , 300):
        dst = f"/mnt/10kb-{uuid.uuid4()}"
        shutil.copy(src, dst)
        logging.info(f"Data written {dst}")
        time.sleep(2)


url_checker()
download_file()
run_io()

