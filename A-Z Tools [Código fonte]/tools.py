import os
import shutil
import pyqrcode
import requests

# Windows repair
def check():
    x = os.system('DISM /Online /Cleanup-Image /CheckHealt')
    print(x)

def scan():
    x = os.system('DISM /Online /Cleanup-Image /ScanHealt')
    print(x)

def restore():
    x = os.system('DISM /Online /Cleanup-Image /RestoreHealt')
    print(x)

def sfc():
    x = os.system('sfc /scannow')
    print(x)

# Ferramentas adicionais
def make_qrcode(link, name):
    qrcode = pyqrcode.create(link)
    qrcode.png(name + '.png', scale=10)
    path = 'QR code imagens'
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    for root, dirs, files in os.walk('.'):
        for file in files:
            path1 = os.path.join(root, file)
            path2 = os.path.join(path, file)
            if '.png' in file:
                shutil.move(path1, path2)

def search_ip(ip):
    api = f'http://ipwhois.app/json/{ip}'
    response = requests.get(api)
    result = response.json()
    return result

def search_cep(cep):
    api = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(api)
    result = response.json()
    return result
