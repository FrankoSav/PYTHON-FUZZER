import argparse
import requests
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Fuzzing De Directorios Web")
parser.add_argument("url", help="URL OBJETIVO")
parser.add_argument("diccionario", help="Archivo de Diccionario")
args = parser.parse_args()

with open (args.diccionario) as file:
        wordlist = file.read().splitlines()
try:
        barrita = tqdm(total=len(wordlist), desc="Progreso", unit="urls", dynamic_ncols=True)
        
        for linea in wordlist:
            url_completa = args.url + linea
            
            response = requests.get(url_completa)
            
            if response.status_code == 200:
                tqdm.write(f"Directorio encontrado: {url_completa}")
                
                barrita.update(1)

except KeyboardInterrupt:
        print("\nScript Interrumpido")
finally:
    barrita.close()
    