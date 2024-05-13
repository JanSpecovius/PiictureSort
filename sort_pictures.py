import os
import shutil
from datetime import datetime
import exifread

def sortiere_dateien(bilder_ordner):
    for datei in os.listdir(bilder_ordner):
        datei_pfad = os.path.join(bilder_ordner, datei)
        if os.path.isfile(datei_pfad):
            aufnahmedatum = get_aufnahmedatum(datei_pfad)
            if aufnahmedatum:
                ziel_ordner = os.path.join(bilder_ordner, aufnahmedatum.strftime("%Y-%m-%d"))
                if not os.path.exists(ziel_ordner):
                    os.makedirs(ziel_ordner)
                shutil.move(datei_pfad, ziel_ordner)

def get_aufnahmedatum(datei_pfad):
    try:
        if datei_pfad.lower().endswith((".jpg", ".jpeg", ".png", ".arw", ".mp4")):
            with open(datei_pfad, 'rb') as bild_datei:
                tags = exifread.process_file(bild_datei, stop_tag='EXIF DateTimeOriginal')
                aufnahmedatum_str = str(tags.get('EXIF DateTimeOriginal'))
                aufnahmedatum = datetime.strptime(aufnahmedatum_str, '%Y:%m:%d %H:%M:%S')
                return aufnahmedatum
    except Exception as e:
        print(f"Fehler beim Lesen des Aufnahmedatums von {datei_pfad}: {e}")
        return None

if __name__ == "__main__":
    bilder_ordner = input("Geben Sie den Pfad zum Ordner mit den Bildern ein: ")
    sortiere_dateien(bilder_ordner)
    print("Dateien wurden sortiert.")