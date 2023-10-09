from pytube import YouTube
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

'''
importar las librerias

(1)
pip install pydrive
pip install pandas
pip install pydrive2
pip install openpyxl
'''


#variables excel
file_path = 'enlaces_videos/enlaces.xlsx'
sheet_name = 'Hoja1'
column_name = 'Videos'


#credenciales google drive
directorio_credenciales = 'credentials_module.json'
id_folder ='1UurMbAWJWstBHcS1KJOhsUK3z25NgAXT'  #Se extrae de la carpeta que creas en tu google drive

# INICIAR SESION en drive
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales


# SUBIR UN ARCHIVO A DRIVE
def subir_archivo(ruta_archivo,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo['title'] = ruta_archivo.split("/")[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()


def main():
    #Leer los links del excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    column_data = df[column_name]
    videos = column_data.values
    #print(videos)  #Para ver como captura los link y se construye el array o lista de link a buscar en la hoja de calculo
        
    #Descargar videos de youtube y subirlo a drive
    for link_video in videos:
        #descarga
        yt = YouTube(link_video)
        video = yt.streams.get_highest_resolution() #Para obtener la resolucion maxima del video
        video.download('./YT')

        #subir
        subir_archivo(f'YT/{video.title}.mp4',id_folder)


if __name__ == "__main__":
    main()






