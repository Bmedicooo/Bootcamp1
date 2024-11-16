import streamlit as st  
from PIL import Image

st.set_page_config(page_title="OPTIMED MisteryIA", page_icon="🧬",layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Diseño/main.css")
email_address ="emailcontact@gmail.com"

#intro
with st.container():
    st.title("OPTIMED by MisteryIA")
    st.write("Análisis predictivo de Consultas de Medicina General en la Empresa Social del Estado Pasto Salud E.S.E")
    st.write(""""
             Maria Jose Ortiz \n Juan Diego Estupiñan \n Juan Guazaquillo \n Jair Bulla \n
             """)

# About us

with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("Empresa Social del Estado Pasto Salud E.S.E 🔍")
        st.write(
            """
            La Empresa Social del Estado Pasto Salud ESE se encuentra ubicada en el Municipio de Pasto.
            cuenta con una sede Administrativa además de una red de veintidós IPS organizadas en cuatro redes o zonas según su localización geográfica urbana o rural en el Municipio de Pasto. Red Norte, Red Sur, Red Oriente, Red Occidente.

            -Red Norte:
            Zona Urbana: Hospital Local Civil, Centro de Salud Primero de Mayo, Centro de Salud Pandiaco.
            Zona Rural: Centro de Salud Morasurco, Centro de Salud Buesaquillo.

            -Red Sur: 
            Zona Urbana: Hospital La Rosa, Centro de Salud El Progreso
            Zona Rural: Centro de Salud Catambuco, Centro de Salud Santa Barbara, Centro de Salud Gualmatan.

            -Red Oriente: 
            Zona Urbana: Hospital Santa Mónica, Centro de Salud El Rosario, Centro de Salud Oral Mis Kikes.
            Zona Rural: Centro de Salud Cabrera, Centro de Salud La Laguna, Centro de Salud El Encano.
            
            -Red Occidente: 
            Zona Urbana: Centro de Salud Tamasagra, Centro de Salud San Vicente.
            Zona Rural: Centro de Salud Genoy, Centro de Salud Obonuco, Centro de Salud Mapachico, Centro de Salud La Caldera.
            """
        )
    with right_column:
       image = Image.open("Logo1.png")
       st.write(", ")

with st.container():
    st.write("---")
    st.header("Modelos Predictivos")
    st.write("##")
    text_column,image_column = st.columns((1,2))
    with image_column:
        image = Image.open("")
        st.image(image, use_column_width=True)
    with text_column:
        st.write(
            """
            Modelado consulta de control o de seguimiento por medicina general
            """
        )

with st.container():
    st.write("---")
    st.header("Modelos Predictivos")
    st.write("##")
    text_column,image_column = st.columns((1,2))
    with image_column:
        image = Image.open("")
        st.image(image, use_column_width=True)
    with text_column:
        st.write(
            """
            Modelado consulta de primera vez por medicina general
            """
        )


with st.container():
    st.write("---")
    st.header("Modelos Predictivos")
    st.write("##")
    text_column,image_column = st.columns((1,2))
    with image_column:
        image = Image.open("")
        st.image(image, use_column_width=True)
    with text_column:
        st.write(
            """
            Modelado consulta de primera vez por medicina general RIAS
            """
        )

#Contactenos
with st.container():
    st.write("---")
    st.header("Dejanos tus comentarios!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Indroduzca su nombre" required>
        <input type="email" name="email" placeholder="Introduzca su email" required>
        <textarea name="message" placeholder="Introduzca su mensaje" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
         