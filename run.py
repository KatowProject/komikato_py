import os

try:
    if os.name == 'nt':
        os.system("py manage.py runserver --insecure")
    else:
        os.system("python3 manage.py runserver")
except KeyboardInterrupt:
    print("\n\n[!] Exiting...")
    exit()
    
    