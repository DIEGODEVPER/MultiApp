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

import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from bs4 import BeautifulSoup
import re  #para tokenizar en vez de nltk en la nube
import nltk #tokenizador de idiomas, pero depende de instalacion de punkt
from nltk.corpus import stopwords

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

#---FROMT---
#--Pantalla inicial
st.set_page_config(page_title="DIFODS25", page_icon="", layout="centered")
st.title("Propuesta para MINEDU - DIFODS")
st.write("###")

#--Navigation Menu--
selected = option_menu(
    menu_title= None,
    options= ["Home","Video/audio a texto","Extraer texto de audio","Sentimiento de imagen", "Sentimiento de texto","Cuenta"],
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
imagen_usuario = ("assets/Programador.JPG")



if selected == "Home":
   #st.image("assets/welcome.jpg") #No me cuadro
   st.image(Imagen_welcome, caption="", use_column_width=True)
   st.write("###")
   st.write("Esperamos disfrutes de nuestro producto.")
   st.write("En esta app podras:")
   st.write("- Video/Audios a texto (Nuevo ingreso):star:")
   st.write("- Transcribir texto de audio (Nuevo ingreso):star:")
   st.write("- Sentimiento de una imagen proximamente:heavy_check_mark:")
   st.write("- Sentimiento de un texto proximamente:heavy_check_mark:")
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
   st.success("Elabora por: Diego Salas")
   
   
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
   """
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
      """
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
                model = whisper.load_model("small") #("mediun") # base")small
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

if selected == "Sentimiento de imagen": #"Eliminar Fondo":
    st.write("Muchas gracias, este modulo se esta trabajando")

if selected == "Sentimiento de texto":  #"Unir PDFs":

    # -----------------------------------------------
    # CONFIGURACIÓN DE LA INTERFAZ
    # -----------------------------------------------
    # st.set_page_config(page_title="Análisis Semántico Bicentenario", layout="wide") #En lo cal lo puedo llamar mas de una vez en cloude no.
    st.title("📊 Análisis Semántico y de Sentimiento")
    st.markdown("""
    Esta plataforma analiza los textos escritos por formadores en el marco del programa **Escuelas Bicentenario**, 
    identificando patrones semánticos, tono emocional y generando reportes por docente.
    """)

    # -----------------------------------------------
    # CARGA DEL ARCHIVO EXCEL
    # -----------------------------------------------
    uploaded_file = st.file_uploader("📁 Cargar archivo Excel del protocolo", type=["xlsx"])

    # ✅ Verificamos si el usuario cargó un archivo
    if uploaded_file:
        # ✅ Leemos el archivo Excel y forzamos que la columna USUARIO_DOCUMENTO sea tipo string
        df = pd.read_excel(uploaded_file, dtype={'USUARIO_DOCUMENTO': str})

        # ✅ Normalizamos los nombres de las columnas (elimina espacios extra)
        df.columns = [col.strip() for col in df.columns]

        # ✅ Filtrar solo los que asistieron (Asistió AP 1 = 1)
        if 'Asistió AP 1.' in df.columns:
            df = df[df['Asistió AP 1'] == 1]

        # ✅ Lista fija de campos semánticos que queremos permitir en el selector
        semantic_fields = [
            "AP1 FORTALEZA 1",
            "AP1 MEJORA 1",
            "AP2 FORTALEZA 1",
            "AP2 MEJORA 1"
        ]

        # ✅ Filtramos la lista para incluir solo los campos que existen en el archivo cargado
        available_fields = [field for field in semantic_fields if field in df.columns]

        # ✅ Creamos un selector dinámico para que el usuario elija uno o varios campos
        selected_fields = st.multiselect(
            "Selecciona los campos para análisis semántico",
            options=available_fields,
            default=available_fields[:1]  # Si hay al menos un campo, selecciona el primero
        )

        # -----------------------------------------------
        # PROCESAMIENTO POR DOCENTE (EXCLUYENDO TEXTOS VACÍOS)
        # -----------------------------------------------
        resultados = []
        for index, row in df.iterrows():
            # ✅ Unimos el texto de los campos seleccionados en una sola cadena
            textos = ' '.join([str(row[field]) for field in selected_fields if pd.notna(row[field])])

            # ✅ Solo procesar si hay texto (evita filas vacías)
            if textos.strip():
                blob = TextBlob(textos)
                sentimiento = blob.sentiment.polarity  # Rango: -1 (negativo) a +1 (positivo)

                # ✅ Guardamos los resultados en un diccionario para cada docente
                resultados.append({
                    'DNI_DOCENTE': row.get('USUARIO_DOCUMENTO', f'Docente_{index}'),
                    'Asistió AP 1': row.get('Asistió AP 1.', 0),
                    'Texto_Analizado': textos,
                    'Sentimiento': sentimiento
                })

        # ✅ Convertimos la lista de resultados en un DataFrame para mostrar y exportar
        report_df = pd.DataFrame(resultados)

        # -----------------------------------------------
        # AGREGAR COLUMNA DE VALORACIÓN CATEGÓRICA
        # -----------------------------------------------
        def clasificar_valoracion(sentimiento):
            if pd.isna(sentimiento):
                return "Sin análisis"
            elif sentimiento > 0.1:
                return "Positivo"
            elif sentimiento < -0.1:
                return "Negativo"
            else:
                return "Neutro"

        if not report_df.empty:
            report_df['Valoración'] = report_df['Sentimiento'].apply(clasificar_valoracion)

            # -----------------------------------------------
            # VISUALIZACIÓN DE RESULTADOS POR DOCENTE
            # -----------------------------------------------
            st.subheader("📋 Reporte por Docente")
            st.dataframe(report_df)

            # -----------------------------------------------
            # DESCARGA DEL REPORTE EN EXCEL
            # -----------------------------------------------
            report_df['DNI_DOCENTE'] = report_df['DNI_DOCENTE'].astype(str)  # ✅ Convertimos DNI a texto
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                report_df.to_excel(writer, index=False, sheet_name='Reporte')
                workbook = writer.book
                worksheet = writer.sheets['Reporte']
                text_format = workbook.add_format({'num_format': '@'})  # ✅ Formato texto
                dni_col_index = report_df.columns.get_loc('DNI_DOCENTE')
                for row_num, value in enumerate(report_df['DNI_DOCENTE'], start=1):
                    worksheet.write_string(row_num, dni_col_index, value, text_format)
            output.seek(0)

            # ✅ Generamos el nombre dinámico del archivo según los campos seleccionados
            if selected_fields:
                campos_nombre = "_".join([field.replace(" ", "_") for field in selected_fields])
                file_name = f"reporte_docentes_{campos_nombre}.xlsx"
            else:
                file_name = "reporte_docentes.xlsx"

            # ✅ Botón de descarga
            st.download_button(
                label="📥 Descargar reporte en Excel",
                data=output,
                file_name=file_name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            # -----------------------------------------------
            # ☁️ NUBE DE PALABRAS GLOBAL (LIMPIA)
            # -----------------------------------------------
            st.subheader("☁️ Nube de Palabras Global")
            all_text = ' '.join(report_df['Texto_Analizado'].dropna().tolist()).lower()
            all_text = BeautifulSoup(all_text, "html.parser").get_text()  # ✅ Eliminar etiquetas HTML
            all_text = re.sub(r'[^a-záéíóúüñ\s]', '', all_text)  # ✅ Eliminar caracteres especiales
            words = re.findall(r'\b\w+\b', all_text)
            stop_words = set(stopwords.words('spanish'))
            custom_stopwords = {"br", "uso", "etc", "actividade"}  # ✅ Lista personalizada
            stop_words.update(custom_stopwords)
            filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
            cleaned_text = ' '.join(filtered_words)
            wordcloud = WordCloud(width=1000, height=500, background_color='white').generate(cleaned_text)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)

            # -----------------------------------------------
            # DISTRIBUCIÓN DE SENTIMIENTOS
            # -----------------------------------------------
            st.subheader("📈 Distribución de Sentimientos")
            fig2, ax2 = plt.subplots()
            sns.histplot(report_df['Sentimiento'].dropna(), bins=20, kde=True, ax=ax2, color='skyblue')
            ax2.set_title("Distribución de Sentimientos por Docente")
            ax2.set_xlabel("Valor de Sentimiento (-1 = Negativo, +1 = Positivo)")
            st.pyplot(fig2)

            # -----------------------------------------------
            # MÉTRICAS EJECUTIVAS
            # -----------------------------------------------
            st.subheader("📊 Métricas Generales")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Promedio de Sentimiento", f"{report_df['Sentimiento'].mean():.2f}")
            col2.metric("Docentes con Sentimiento Positivo", f"{(report_df['Valoración'] == 'Positivo').sum()}")
            col3.metric("Docentes con Sentimiento Negativo", f"{(report_df['Valoración'] == 'Negativo').sum()}")
            col4.metric("Docentes con Sentimiento Neutro", f"{(report_df['Valoración'] == 'Neutro').sum()}")

            # -----------------------------------------------
            # CIERRE
            # -----------------------------------------------
            st.markdown("""
            ---
            ✅ Este análisis permite identificar patrones de percepción sobre el desempeño docente, 
            facilitando la toma de decisiones estratégicas en el acompañamiento pedagógico.
            """)
        else:
            st.warning("No hay docentes con texto analizado en los campos seleccionados.")

if selected == "Cuenta":
   #st.image(imagen_usuario, caption="")
   #st.subheaderheader("Cuenta", divider=True)        # Muestra un encabezado en la interfaz
   #st.text("En esta sección podras ver los datos de tu cuenta")   

   col1, col2 = st.columns([1,1])
   with col1:
        st.image(imagen_usuario, caption="", width = 400)
   with col2:
        st.subheader("Diego Salas")
        st.write('******************')
        st.write('')
        st.write('email es: diegofiis10@gmail.com')
        st.write('celular es: 920187327')
        #st.write('Para cancelar tu suscripcion, haz clik: Proximamente')



                   
