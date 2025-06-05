# pages/disclaimer.py
import streamlit as st
logo_image = "images/logo.png"
st.logo(logo_image,size='large')

st.title("\u26a0\ufe0f Aviso legal / Disclaimer")
st.markdown("""
Esta aplicación es un proyecto personal realizado por curiosidad y con fines informativos.

- Los datos han sido recopilados manualmente desde internet (etiquetas, fichas técnicas, sitios web oficiales).
- No se garantiza la exactitud, actualidad o veracidad de los valores.
- El uso de esta app es completamente bajo la **responsabilidad del usuario**.
- La app **no representa ninguna empresa ni institución oficial**.
- Si tienes sugerencias / ideas / tips: ¡coméntamelos! O si quieres que añada marcas específicas. 

Disfrútala con criterio 🙂
""")

st.sidebar.success("Selecciona una pestaña arriba.")

st.sidebar.markdown('CoffeeWater permite visualizar, comparar y mezclar aguas utilizadas en preparación de café, en función de su alcalinidad y dureza. Puedes elegir dos marcas (ciudad, embotellada, comercial o oficial), definir la proporción de mezcla y ver dónde cae la combinación respecto a la zona ideal SCA.')
# add the logo small