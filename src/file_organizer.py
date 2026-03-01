import os


def escanear_archivos(self):
    if not self.carpeta:
        return []

    archivos_validos = []

    archivos = os.listdir(self.carpeta)

    for archivo in archivos:
        ruta_entera = os.path.join(self.carpeta, archivo)

        if os.path.isfile(ruta_entera):
            archivos_validos.append(archivo)

    if self.orden == "tamanio":
        archivos_validos.sort(key=lambda a: os.path.getsize(os.path.join(self.carpeta, a)), reverse=False)
    elif self.orden == "fecha":
        archivos_validos.sort(key=lambda a: os.path.getmtime(os.path.join(self.carpeta, a)), )

    else:
        archivos_validos.sort()
    return archivos_validos

