# pages/about.py
import streamlit as st
logo_image = "images/logo.png"
st.logo(logo_image,size='large')
st.sidebar.success("Selecciona una pestaña arriba.")

st.sidebar.markdown('CoffeeWater permite visualizar, comparar y mezclar aguas utilizadas en preparación de café, en función de su alcalinidad y dureza. Puedes elegir dos marcas (ciudad, embotellada, comercial o oficial), definir la proporción de mezcla y ver dónde cae la combinación respecto a la zona ideal SCA.')
# add the logo small
st.title("\u2139\ufe0f Sobre esta página")
st.markdown("""
Esta aplicación permite visualizar, comparar y mezclar aguas utilizadas en preparación de café, en función de su alcalinidad y dureza.

Puedes elegir dos marcas (ciudad, embotellada, comercial o oficial), definir la proporción de mezcla y ver dónde cae la combinación respecto a la zona ideal SCA.
""")
    
st.title("👤 Sobre mí")
st.markdown("""
Soy Bart Ortiz (@thebooort), postdoc en Machine learning.

Esta app es un experimento personal: si la encuentras útil, puedes usarla, modificarla o compartirla libremente (CC BY).
Si la usas para alguna cosa o haces tu propia version, me haría ilusión que me lo dijeses por alguna red social!

Para mejoras, ideas o sugerencias: 
- [GitHub Repo](https://github.com/thebooort/mezcla-aguas)
- o escríbeme por donde encuentres :)
[Mis redes sociales](https://linktr.ee/bartortiz)

""")
