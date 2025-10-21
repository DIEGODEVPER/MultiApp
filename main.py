#---LIBRERIAS---

#---From principal
from streamlit_option_menu import option_menu
import time
#from st_paywall import add_auth  #pip install st-paywall
#---YT

##--audio-video a txt
#import speech_recognition  as sr
import moviepy.editor as mp
#from pydub import AudioSegment
import whisper
#from whisper.utils import Write_txt
#from pydub import AudioSegment
#------------------------
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
import os                 # Importa la biblioteca 'os' para realizar operaciones con el sistema operativo

from tempfile import NamedTemporaryFile



#---FROMT---
#--Pantalla inicial
st.set_page_config(page_title="DIFODS25", page_icon="", layout="centered")
st.title("Propuesta para MINEDU - DIFODS")
st.write("###")

#--Navigation Menu--
selected = option_menu(
    menu_title= None,
    options= ["Home","Video/audio a texto","Extraer texto de audio","Eliminar Fondo", "Unir PDFs","Cuenta"],
    icons=["house","caret-right-square-fill","body-text","camera","filetype-pdf","file-person"], # https://icons.getbootstrap.com/ #Me falta saber como importarlos
    orientation="horizontal",
)
#Abrir las imagenes --rutas relativas mejoradas

Imagen_welcome = ("assets/Bienvenidos.png") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
Imagen_Google  = ("assets/Logo_Minedu.png") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
Imagen_yt      = ("assets/logoyt.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
imagen_convertidor = ("assets/Convertidoratxt.png")
Imagen_camaro = ("assets/camaro_remove.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario
imagen_combine_pdf = ("assets/combine-pdf.png")
imagen_usuario = ("assets/Programador.jpg")



if selected == "Home":
   #st.image("assets/welcome.jpg") #No me cuadro
   st.image(Imagen_welcome, caption="", use_column_width=True)
   st.write("###")
   st.write("Esperamos disfrutes de nuestro producto.")
   st.write("En esta app podras:")
   st.write("- Video/Audios a texto :heavy_check_mark:")
   st.write("- Transcribir texto de audio (Nuevo ingreso):star:")
   st.write("- Sentimiento de una imagen :heavy_check_mark:")
   st.write("- Sentimiento de un texto :heavy_check_mark:")
   st.write("###")
   st.write("Te da la bienvenida el programador DGSR  🧑‍💻☕")

with st.sidebar:
   #st.image("assets/google.png")
   st.image(Imagen_Google, caption="")
   
   st.write("###")
   #st.warning("Esta App es totalmente gratuita, pero nos gustaria tener un apoyo economico de tu parte para poder continuar")
    st.warning("Esta aplicacion tiene la finalidad de ser usada como propuesta para el MINEDU - DIFODS")
    
   #pagar= st.button(Label = "Pagar suscripcion") # https://mpago.la/19tVAX9")
   #add_auth(required=True)
   #####################################
   #autenticacion + suscripcion
   #st.write("Pagar a:")
   #st.link_button(label = "Realizar mi aporte", url="https://link.mercadopago.com.pe/appmultiusosperu" )
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




if selected == "Video/audio a texto":
   '''
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
   
   if link_video == "":
        st.warning("Debes introducir un link")
   else:
        yt = YouTube(link_video)

        try:
            streams = yt.streams
        except pytube.exceptions.VideoUnavailable:
            st.write("Este video no esta disponible")
            disponible = False
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
                  #yt = YouTube(link_video)
                  extencion = 'mp4'         
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
                        extencion = 'mp3'
                        #video.download('./YT')
                        st.success("audio")
                     
               st.balloons()
               #with st.spinner('Descargando...'):
                  #time.sleep(5)
                  #st.success('Felicitaciones!') 

            with open(f"{video.title}.{extencion}", "rb") as f:  # Abro el archivo con la sentencia 'with'
               video_open = f.read() # Lee los datos de la imagen procesada
               ## Muestra un boton de descarga para que el usuario pueda descargar la imagen procesada
               st.download_button("Descargar video", data=video_open, file_name=f"{video.title}.{extencion}")



        else:
              st.exception("El video debe estar disponible para descargarlo")
      '''
    st.image(imagen_convertidor, caption="", width=200)
    st.header("Convertidor de audio/video a texto")

    uploaded_file = st.file_uploader("Sube tu archivo de audio o video", type=['mp3', 'wav', 'm4a', 'mp4', 'mov'])

    if uploaded_file is not None:
        st.write(f"Archivo cargado: {uploaded_file.name}")

        if uploaded_file.type.startswith("audio"):
            st.audio(uploaded_file)

        transcribir = st.button("Transcribir")

        if transcribir:
            try:
                st.success("Cargando modelo Whisper...")
                model = whisper.load_model("base")
                st.success("Modelo cargado correctamente")

                with NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_path = temp_file.name

                if uploaded_file.type.startswith("video"):
                    st.info("Extrayendo audio del video...")
                    audio_path = temp_path.replace(os.path.splitext(temp_path)[1], ".wav")
                    clip = mp.VideoFileClip(temp_path)
                    clip.audio.write_audiofile(audio_path)
                else:
                    audio_path = temp_path

                st.info("Transcribiendo...")
                result = model.transcribe(audio_path, language='es')
                st.success("Transcripción completada")

                st.text_area("Transcripción:", result["text"], height=300)
                st.download_button("Descargar transcripción", data=result["text"], file_name="transcripcion.txt")
                st.balloons()

            except Exception as e:
                st.error(f"Ocurrió un error: {str(e)}")
    else:
        st.info("Por favor, sube un archivo para comenzar.")

    st.write("Muchas gracias por usar el convertidor.")









if selected == "Extraer texto de audio":
   '''
   #---FRONT---
   
   #st.image("assets/logoyt.jpg")
   st.image(imagen_convertidor,caption="", width= 400)   #use_column_width=True cuando quiero que hagarre todo el ancho
   st.header("Convertidor de audio-video a texto")
   

   uploaded_file = st.file_uploader("File upload", type=['mp3','wav','m4a'])
   st.write(f"{uploaded_file.name}")
   
   st.audio(f"{uploaded_file.name}")
   
   
   
      
      #si fuera video - pasar de video a audio
      #clip = mp.VideoFileClip(filename= f"{uploaded_file.name}")

      #clip.audio.write_audiofile("extracted_audio.wav")

      #else:
         #audio =  st.audio(uploaded_file)
         #i=audio.save("extracted_audio.wav")
         #audio = AudioSegment.from_wav(file = f"{uploaded_file.name}")
         #audio.export('extracted_audio.wav', format = 'wav')
         #audio.export('extracted_audio', format = 'wav')
         #audio =  st.audio(uploaded_file)

         #with open('extracted_audio.wav','w') as f:
              #f.write(uploaded_file.getbuffer())
      
      #Modelo de Wisper
     
   model = whisper.load_model("base") # esta puede incrementarse y ser mas exacto
   st.text("Wisper Model Loaded")

   transcribir = st.button(label = "Transcribir") 
  
   if transcribir:
      if uploaded_file is not None:
         st.success("Transcribiendo audio")
         transciption = model.transcribe(uploaded_file.name)
         st.success("Transcripcion completeada")
         #st.text(transciption["text"])
         st.text_area("La transcripcion es:" , transciption["text"])
         
      else:
         st.error("Please upload an audio file")

   with open("transcripcion.txt", 'w', encoding = 'utf-8') as w:
       w.write(transciption["text"])
          #write_txt(result["text"], file = txt)
          #print(result["text"])

   with open("transcripcion.txt", 'r') as re:  
        txt = re.read()  
        st.download_button("Descargar transcripcion", data=txt, file_name="transcripcion.txt")

   st.balloons()
   




   st.write("Muchas gracias")
'''
    
   
   #--- FRONT ---
   st.image(imagen_convertidor, caption="", width=400)
   st.header("Convertidor de audio-video a texto")

   uploaded_file = st.file_uploader("File upload", type=['mp3', 'wav', 'm4a'])

   if uploaded_file is not None:
       st.write(f"Archivo subido: {uploaded_file.name}")

       # Detectar formato de audio
       if uploaded_file.name.endswith(".mp3"):
           audio_format = "audio/mp3"
       elif uploaded_file.name.endswith(".wav"):
           audio_format = "audio/wav"
       elif uploaded_file.name.endswith(".m4a"):
           audio_format = "audio/m4a"
       else:
           st.error("Formato no soportado.")
           audio_format = None

       # Reproducir audio
       if audio_format:
           st.audio(uploaded_file, format=audio_format)

           # Guardar archivo para transcripción
           audio_filename = "extracted_audio." + uploaded_file.name.split(".")[-1]
           with open(audio_filename, "wb") as f:
               f.write(uploaded_file.getbuffer())

           st.success("Audio guardado correctamente.")

           # Cargar modelo Whisper
           model = whisper.load_model("base")
           st.text("Modelo Whisper cargado")

           # Botón para transcribir
           transcribir = st.button(label="Transcribir")

           if transcribir:
               st.success("Transcribiendo audio...")
               transcription = model.transcribe(audio_filename)
               st.success("Transcripción completada")

               st.text_area("La transcripción es:", transcription["text"])

               # Guardar transcripción en archivo
               with open("transcripcion.txt", 'w', encoding='utf-8') as w:
                   w.write(transcription["text"])

               # Botón para descargar
               with open("transcripcion.txt", 'r', encoding='utf-8') as re:
                   txt = re.read()
                   st.download_button("Descargar transcripción", data=txt, file_name="transcripcion.txt")

               st.balloons()

   st.write("Muchas gracias")

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

   def unir_pdfs(output_path, documents):
       # Crea un objeto PdfMerger de PDF2 para combinar archivos PDF
       pdf_final = PyPDF2.PdfMerger()

       for document in documents:
           pdf_final.append(document) # Agrega cada documento PDF a la fusión.

       pdf_final.write(output_path) # Guarda el PDF combinado en la ruta de salida.


#---FROM---

   st.image(imagen_combine_pdf, caption = "") #("assets/combine-pdf.png")         # Muestra una imagen en la interfaz del usurio
   st.header("Unir PDF")                      # Agrega un encabezado en la insterfaz de usuario
   st.subheader("Adjuntar pdfs para unir")    # Agrega un subencabezado en la insterfaz de usuario

# Crea un area para que el usuario carge varios archivos PDF.
   pdf_adjuntos = st.file_uploader(label="",accept_multiple_files=True)

# Crea un boton para "Unir PDFs".
   unir = st.button(label="Unir PDFs")

#--triger

   if unir: 
      # Comienza un bloque condicional si se hace clic en el boton "Unir PDFs".
      if len(pdf_adjuntos) <= 1:
         st.warning("Debes adjuntar más de un PDF") #Muestra una advertencia si se cargaron menos de dos archivos PDF
      else:
         # Inicia un bloque de codigo si se cargaron al menos dos archivos PDF
         unir_pdfs(output_pdf, pdf_adjuntos) # Combina los archivos PDF cargados y guarda el resultado en output_pdf
         st.success("Desde aqui puede descargar el PDF Final") # Muestra un mensaje de exito en la interfaz de usuario
         with open(output_pdf, 'rb') as file:
              pdf_data = file.read() # Abre  el archivo PDF final combinado en modo lectura binaria

              # Muestra un boton de descarga para que el usuario pueda descargar el PDF final combinado 
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
        st.subheader("Cuenta Free")
        st.write('En esta sección podras ver los datos de tu cuenta')
        st.write('')
        st.write('Tu email es:')
        st.write('Para cancelar tu suscripcion, haz clik: Proximamente')



                   
