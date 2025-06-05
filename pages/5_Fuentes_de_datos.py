# pages/sources.py
import streamlit as st
logo_image = "images/logo.png"
st.logo(logo_image,size='large')
st.title("\U0001F4C4 Fuentes / Sources")
st.markdown("""
Enlaces a las fuentes de composición química de las aguas:

- Bezoya: [https://www.bezoya.es](https://www.bezoya.es)  
- Lanjaron: [https://www.lanjaron.es](https://www.lanjaron.es)  
- Cabreiroá: [https://www.cabreiroa.es](https://www.cabreiroa.es)  
- Solan de Cabras: [https://www.solandecabras.es](https://www.solandecabras.es)  
- Sierra Cazorla: [https://sierracazorla.com](https://sierracazorla.com)  
- Font Natura: info del etiquetado  
- Auchan: datos del etiquetado de botella  
- Aquafina: ficha técnica disponible online  
- Teleno: ficha mineral  
- Aquarel (Nestlé): [https://www.nestle-waters.com](https://www.nestle-waters.com)  
- VilaDrau: [https://www.fontvella.es/viladrau](https://www.fontvella.es/viladrau)
""")

st.sidebar.success("Selecciona una pestaña arriba.")

st.sidebar.markdown('CoffeeWater permite visualizar, comparar y mezclar aguas utilizadas en preparación de café, en función de su alcalinidad y dureza. Puedes elegir dos marcas (ciudad, embotellada, comercial o oficial), definir la proporción de mezcla y ver dónde cae la combinación respecto a la zona ideal SCA.')
# add the logo small