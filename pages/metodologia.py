# pages/sources.py
import streamlit as st

st.title("\U0001F4C4 Metodologia")
st.markdown("""
Para estimar la **alcalinidad** y la **dureza** del agua utilizada en café, se parte de su **composición química**, en particular de los minerales disueltos expresados en mg/L. Los cálculos se basan en la siguiente metodología:

### \U0001F4DD Dureza Total (GH)
La dureza total está relacionada principalmente con la concentración de **calcio (Ca²⁺)** y **magnesio (Mg²⁺)**. Se calcula como:

**Dureza (en mg/L como CaCO₃) = (Ca²⁺ × 2.5) + (Mg²⁺ × 4.1)**

Esta fórmula proviene de la equivalencia en peso molecular con el carbonato cálcico (CaCO₃), que se usa como estándar.

### \U0001F4DD Alcalinidad (KH)
La alcalinidad refleja la capacidad del agua para neutralizar ácidos, y está principalmente asociada a la presencia de **bicarbonatos (HCO₃⁻)**. Se calcula como:

**Alcalinidad (en mg/L como CaCO₃) = HCO₃⁻ × 0.82**

Esta relación asume que todos los HCO₃⁻ provienen de carbonatos y bicarbonatos equivalentes a CaCO₃.

""")