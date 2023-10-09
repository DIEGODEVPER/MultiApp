import streamlit as st    # Importar la biblioteca Streamlit para crear la interfaz
from PIL import Image     # Importa la clase Image de la biblioteca PIL (Python Imaging Library)
from rembg import remove  # Importa la funcion 'remove' del paquete 'rembg' para quitar fondos de imagen
import io                 # Importa la biblioteca 'io' para trabajar con datos en memoria
import os                 # Importa la biblioteca 'os' para realizar operaciones con el sistema operativo


Imagen = Image.open(r"C:\Users\dgsalas\Desarrollos_Python\yt-automation-master\assets\camaro_remove.jpg") # Creo la variable para almacenar la ruta de imagen a mostrar para el usuario

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

st.image(Imagen, caption="")               # Muestra una imagen en la interfaz de usuario
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

    os.remove("processed_image.png") # Elimina el archivo temporal de la imagen procesada del sistema operativo          
    



