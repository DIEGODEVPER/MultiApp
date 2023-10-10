#---LIBRERIAS---

#---From principal
from streamlit_option_menu import option_menu
import time
#from st_paywall import add_auth  #pip install st-paywall
#---YT
import speech_recognition  as sr
import moviepy.editor as mp

import pytube
from pytube import YouTube

import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
#---PDFs
import streamlit as st #importo la libreria de STREAMLIT
import PyPDF2          #importo la libreria PyPDF2 para trabajar con archivos pdfs
from PIL import Image
#---Imagen
import streamlit as st    # Importar la biblioteca Streamlit para crear la interfaz
#from PIL import Image     # Importa la clase Image de la biblioteca PIL (Python Imaging Library)
from rembg import remove  # Importa la funcion 'remove' del paquete 'rembg' para quitar fondos de imagen
import io                 # Importa la biblioteca 'io' para trabajar con datos en memoria
#import os                 # Importa la biblioteca 'os' para realizar operaciones con el sistema operativo

from tempfile import NamedTemporaryFile



#---FROMT---
#--Pantalla inicial
st.set_page_config(page_title="Multiapp", page_icon="", layout="centered")
st.title("App Multi-usos")
st.write("###")

#--Navigation Menu--
selected = option_menu(
    menu_title= None,
    options= ["Home","Youtube Donwloader","Extraer texto de video","Eliminar Fondo", "Unir PDFs","Cuenta"],
    icons=["house","caret-right-square-fill","body-text","camera","filetype-pdf","file-person"], # https://icons.getbootstrap.com/ #Me falta saber como importarlos
    orientation="horizontal",
)
#Abrir las imagenes --esta por mejorar 
#Imagen_welcome = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\welcome.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
#Imagen_Google  = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\google.png") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
#Imagen_yt      = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\logoyt.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
#Imagen_camaro = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\camaro_remove.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
#imagen_combine_pdf = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\combine-pdf.png")
#imagen_usuario = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\usuario.png")

Imagen_welcome = ("assets/Bienvenido.png") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
Imagen_Google  = ("assets/google.png") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
Imagen_yt      = ("assets/logoyt.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
imagen_convertidor = ("assets/Convertidoratxt.png")
Imagen_camaro = ("assets/camaro_remove.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
imagen_combine_pdf = ("assets/combine-pdf.png")
imagen_usuario = ("assets/usuario.png")



if selected == "Home":
   #st.image("assets/welcome.jpg") #No me cuadro
   st.image(Imagen_welcome, caption="", use_column_width=True)
   st.write("###")
   st.write("Esperamos disfrutes de nuestro producto.")
   st.write("En esta app podras:")
   st.write("- Descargar videos de Youtube")
   st.write("- Eliminar el fondo de una imagen")
   st.write("- Unir varios PDFs en uno solo")
   st.write("###")
   st.write("Te da la bienvenida el programador DGSR")

with st.sidebar:
   #st.image("assets/google.png")
   st.image(Imagen_Google, caption="")
   
   st.write("###")
   st.warning("Esta App es totalmente gratuita, pero nos gustaria tener un apoyo economico de tu parte para poder continuar")
   #pagar= st.button(Label = "Pagar suscripcion") # https://mpago.la/19tVAX9")
   #add_auth(required=True)
   #####################################
   #autenticacion + suscripcion
   #st.write("Pagar a:")
   st.link_button(label = "Tu aporte", url="https://link.mercadopago.com.pe/appmultiusosperu" )
                                  # url="https://www.mercadopago.com.pe/subscriptions/checkout?preapproval_plan_id=2c9380848b053057018b064fd7d50114"
   #st.write("https://www.mercadopago.com.pe/subscriptions/checkout?preapproval_plan_id=2c9380848b053057018b064fd7d50114")
   st.success("!!! Muchas gracias ¡¡¡")
   
   
   # Using object notation
   #add_selectbox = st.sidebar.selectbox(
       #"How would you like to be contacted?",
       #("Email", "Home phone", "Mobile phone")
       #)

   # Using "with" notation
   #with st.sidebar:
       #add_radio = st.radio(
         #"Choose a shipping method",
         #("Standard (5-15 days)", "Express (2-5 days)")
         #)

   

   #with st.sidebar:
      #with st.echo():
           #st.write("This code will be printed to the sidebar.")

      #with st.spinner("Loading..."):
          #time.sleep(5)
          #st.success("Done!")




if selected == "Youtube Donwloader":
   
   #---FRONT---
   
   #st.image("assets/logoyt.jpg")
   st.image(Imagen_yt,caption="", width=300)   #use_column_width=True cuando quiero que hagarre todo el ancho
   st.header("Descargador de Youtube")

   c1, c2 = st.columns(2)
   formato = c1.radio(label="¿Qué quieres descargar?", options = ["Video (.mp4)", "Audio (.mp3)"] )
   if formato == "Video (.mp4)":
      resolucion = c2.radio(label="¿En qué resolucion?", options=["480p", "720p", "La mas alta"])

   link_video = st.text_input(label="Link del video")
   st.write(link_video)
   yt2 = YouTube(link_video)

   try:
       streams = yt2.streams
   except pytube.exceptions.VideoUnavailable:
        st.write("Este video no esta disponible")
        Disponible = False
   else:
        st.write("Este video si esta disponible")
        disponible = True

   descargar = st.button(label = "Descargar")
   
   #yt = YouTube(link_video)

   if disponible:
      if descargar:
         if link_video == "":
            st.warning("Debes introducir un link")
      
         elif "youtube.com" not in link_video:
              st.warning("Debes introducir un link de youtube")
      
         elif "youtube.com" in link_video:
              #st.warning("Estas aqui") 
              yt = YouTube(link_video)
                       
              if formato == "Video (.mp4)":
                 if resolucion == "480p":
                    video = yt.streams.filter(res='480p').first() ##all() #.first() #Para obtener la resolucion a 720p
                    #video.download('./YT')
                    video.download(filename=f"{video.title}.mp4")
                    #for e in video:
                         #st.write(e)
                    st.success("480p")
                 elif resolucion == "720p":
                     video = yt.streams.filter(res='720p').first() #Para obtener la resolucion a 1800p
                     #video.download('./YT')
                     video.download(filename=f"{video.title}.mp4")
                     st.success("720p")
                 elif resolucion == "La mas alta":
                      video = yt.streams.get_highest_resolution() #Para obtener la resolucion maxima del video
                      #video.download('./YT')
                      video.download(filename=f"{video.title}.mp4")
                      #video.download(filename=f"videodescargado.mp4")
                      st.success("alta")
              else:
                   video =  yt.streams.filter(only_audio=True).first() #Para obtener el audio
                   video.download(filename=f"{video.title}.mp3")
                   #video.download('./YT')
                   st.success("audio")
         
      with st.spinner('Descargando...'):
           time.sleep(5)
           st.success('Felicitaciones!') 
   else:
       st.exception("El video debe estar disponible para descargarlo")
if selected == "Extraer texto de video":
   
   #---FRONT---
   
   #st.image("assets/logoyt.jpg")
   st.image(imagen_convertidor,caption="", width= 800)   #use_column_width=True cuando quiero que hagarre todo el ancho
   st.header("Convertidor de audio-video a texto")

   #Lectura de video:
   
   #ruta = st.file_uploader("Subir Video", type = ["mp4"])
   #st.write(ruta.name)
   #clip = mp.VideoFileClip(ruta.name)

   #from tempfile import NamedTemporaryFile
   #import streamlit as st

   uploaded_file = st.file_uploader("File upload", type='mp4')
   st.write(uploaded_file)
   with NamedTemporaryFile(dir='.', suffix='.mp4') as f:
        f.write(uploaded_file.getbuffer())
        f.write(f.name)
        #your_function_which_takes_a_path(f.name)
   
   clip = mp.VideoFileClip(f.name)

   
   clip.audio.write_audiofile("extracted_audio.wav")

   #Iniciar 'Speechrecognition':
   r = sr.Recognizer()

   #Lectura de archivo de audio:
   audio = sr.AudioFile("extracted_audio.wav")

   # Lectura de audio
   with audio as source:
       r.adjust_for_ambient_noise(source)
       audio_file = r.record(source)

   # Reconocimiento de voz  en audio:
   resul = r.recognize_google(audio_file, language= 'es-ES')

   #Escritura de archivo de texto

   with open('recognized_txt','w') as file:
        file.write("Recognized speech: \n")
        file.write(resul)

   print("\nTask COMPLETED")






   st.write("Todo bien")


if selected == "Eliminar Fondo":
 

#---BACKEND---
#-------------

#---FUNCTIONS--

 def process_image(image_uploaded):
    #Abre la imagen cargada
    image = Image.open(image_uploaded)
    #Procesa la imagen para quitar el fondo 
    proccesed_image = remove_background(image)

    return proccesed_image

 def remove_background(image):
    # Crea un objeto de BytesIO para almacenar la imagen en memoria 
    image_byte = io.BytesIO()
    # Guarda la imagen en formato PNG en el objeto BytesIO
    image.save(image_byte, format= "PNG")
    # Establece la posicion en el objeto BytesIO al incio
    image_byte.seek(0)
    # Elimina el fondo de la imagen utilizando la funcion 'remove'de rembg
    proccesed_image_bytes = remove(image_byte.read())
    # Crea una nueva imagen PIL a partir de los bytes de la imagen procesada 
    return Image.open(io.BytesIO(proccesed_image_bytes))


#---FRONT---
#-----------

 st.image(Imagen_camaro, caption="")   # Muestra una imagen en la interfaz de usuario  #use_column_width=True
 st.header("Background Removal APP")        # Muestra un encabezado en la interfaz
 st.subheader("Upload an Image")            # Muestra un subencabezado en la interfaz
 uploaded_image = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"]) # Permite al usuario cargar una imagen 

 if uploaded_image is not None:  # Comprueba si se ha subido una imagen 

    st.image(uploaded_image, caption = "Imagen subida", use_column_width=True) # Muestra la imagen cargada en la interfaz

    remove_button = st.button(label = "Quitar fondo") # Crea un boton llamado "Quitar fondo"

    if remove_button:  # Comprueba si se ha cargado una imagen
       
       proccesed_image = process_image(uploaded_image) # Procesa la imagen para quitar el fondo 

       st.image(proccesed_image, caption ="Background Remove", use_column_width=True) # Muestra la imagen con el fondo eliminado en la interfaz

       proccesed_image.save("processed_image.png") # Guarda la imagen procesada en un archivo llamado 'proccesed_image.png'

       with open("processed_image.png", "rb") as f:  # Abro el archivo con la sentencia 'with'
           image_data = f.read() # Lee los datos de la imagen procesada
           # Muestra un boton de descarga para que el usuario pueda descargar la imagen procesada
           st.download_button("Download Processed Image", data=image_data, file_name="processed_image.png")

    #os.remove("processed_image.png") # Elimina el archivo temporal de la imagen procesada del sistema operativo 

if selected == "Unir PDFs":
   
   #---BACKEND--- 

# Variables
   output_pdf = "documents/pdf_final.pdf"

# Functions

   def unir_pdfs(output_pdf, documents):
       # Crea un objeto PdfMerger de PDF2 para combinar archivos PDF
       pdf_final = PyPDF2.PdfMerger()

       for document in documents:
           pdf_final.append(document) #Agrega cada documento PDF a la fusión

           pdf_final.write(output_pdf) #Guarda el PDF combinado en la ruta de salida


#---FROM---

   st.image(imagen_combine_pdf, caption = "") #("assets/combine-pdf.png")         # Muestra una imagen en la interfaz del usurio
   st.header("Unir PDF")                      # Agrega un encabezado en la insterfaz de usuario
   st.subheader("Adjuntar pdfs para unir")    # Agrega un subencabezado en la insterfaz de usuario

# Crea un area para que el usuario carge  varios archivos PDF
   pdf_adjuntos = st.file_uploader(label="",accept_multiple_files=True)

#Crea un boton para "Unir PDFs"
   unir = st.button(label="Unir PDFs")

#--triger

   if unir: 
      # Comienzaun bloque condicional si se hace clic en el boton "Unir PDFs"
      if len(pdf_adjuntos) <= 1:
         st.warning("Debes adjuntar más de un PDF") #Muestra una advertencia si se cargaron menos de dos archivos PDF
      else:
           #Inicia un bloque de codigo si se cargaron al menos dos archivos PDF
         unir_pdfs(output_pdf, pdf_adjuntos) #Combina los archivos PDF cargados y guarda el resultado en output_pdf
         st.success("Desde aqui puede descargar el PDF Final") #Muestra un mensaje de exito en la interfaz de usuario
         with open(output_pdf, 'rb') as file:
              pdf_data = file.read() #Abre  el archivo PDF final combinado en modo lectura binaria

              #Muestra un boton de descarga para que el usuario pueda descargar el PDF final combinado 
              st.download_button(label="Descargar PDF final", data=pdf_data, file_name="pdf_final.pdf") 
              st.balloons()

if selected == "Cuenta":
   #st.image(imagen_usuario, caption="")
   #st.subheaderheader("Cuenta", divider=True)        # Muestra un encabezado en la interfaz
   #st.text("En esta sección podras ver los datos de tu cuenta")   

   col1, col2 = st.columns([1,1])
   with col1:
        st.image(imagen_usuario, caption="", width = 80)
   with col2:
        st.subheader("Cuenta")
        st.write('En esta sección podras ver los datos de tu cuenta')
        st.write('')
        st.write('Tu email es:')
        st.write('Para cancelar tu suscripcion, haz clik:')



                   