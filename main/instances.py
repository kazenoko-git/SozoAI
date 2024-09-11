import subprocess, os, tracemalloc, datetime
def install(to_install:str):
    sub = subprocess.run(f'pip install {to_install}')
    if sub.returncode == 1:
        print("ERROR: Check the module name or your internet connection.")
    elif sub.returncode == 0:
        print(f"Installed {to_install}")

def geturl():
    return os.getcwd().split('kazai')[0].replace('\\\\', '/')

def datetime(help:bool=False):
    today = datetime.date.today()
    year = int(str(today).split('-')[0])
    monthnum = int(str(today).split('-')[1])
    daynum = int(str(today).split('-')[2])
    print(datetime.datetime.time().strftime(format="%m-%d-%Y-%H-%M-%S"))
    return

def none(): pass

def translate():
    pass

def list_models():
    return ["Sozomi", "Sozomi-Discord", "BakriWalaDev", "BakriWalaDev-Discord"]