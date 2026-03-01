import os
import shutil
from datetime import datetime
from cryptography.fernet import Fernet



class OrganizarArchivos:
    def __init__(self):
        self.base_path = ""
        self.rules = {
            ".pdf": "Documentos",
            ".docx": "Documentos",
            ".img": "Imágenes",
            ".png": "Imágenes",
            ".jpg": "Imágenes",
            ".mp4": "Videos",
            ".avi": "Videos",
            ".mkv": "Videos",
            ".webm": "Videos",
            ".mp3": "Música",
            ".acc": "Música",
            ".ogg": "Música",
            ".wav": "Música",
        }
        self.respaldo_activado = False
        self.encriptado_activado = False
        self.ordenar_por = "carpeta"

        self.key = None
        self.cifrar = None


    def set_ruta_base(self, path):
        self.base_path = path

    def activar_respaldo(self, value: bool):
        self.respaldo_activado = value

    def activar_encriptado(self, value: bool):
        self.encriptado_activado = value
        if value:
            self.key = Fernet.generate_key()
            self.cifrar = Fernet(self.key)

