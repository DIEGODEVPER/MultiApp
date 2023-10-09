import streamlit as st #importo la libreria de STREAMLIT
import PyPDF2          #importo la libreria PyPDF2 para trabajar con archivos pdfs
from PIL import Image
''' Ejecutar STREAMLIT
Desarrollado por Diego Salas
 streamlit run unir_pdfs.py
'''

'''Importar librerias
pip install streamlit #varias veces porque necesito que se actualicen varias librerias
'''
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

imagen = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\combine-pdf.png")


st.image(imagen, caption = "") #("assets/combine-pdf.png")         # Muestra una imagen en la interfaz del usurio
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