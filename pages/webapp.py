# pages/app_main.py
import streamlit as st
import plotly.graph_objects as go


lang = st.sidebar.selectbox("Idioma / Language", ["Español", "English"])

textos = {
    "Español": {
        "title": "💧 Composición del agua para preparar café",
        "select1": "Selecciona Agua 1",
        "select2": "Selecciona Agua 2",
        "ratio": "Proporción de Agua 1 (%)",
        "mezcla": "🧪 Mezcla",
        "alk": "Alcalinidad",
        "hard": "Dureza",
        "zone": "Zona ideal SCA"
    },
    "English": {
        "title": "💧 Water Composition for Coffee Brewing",
        "select1": "Select Water 1",
        "select2": "Select Water 2",
        "ratio": "Ratio of Water 1 (%)",
        "mezcla": "🧪 Mix",
        "alk": "Alkalinity",
        "hard": "Hardness",
        "zone": "SCA Ideal Zone"
    }
}

etiquetas = {
    "Español": {"Ciudad": "Ciudad", "Embotellada": "Embotellada", "Comercial": "Comercial", "Oficial": "Oficial"},
    "English": {"Ciudad": "City", "Embotellada": "Bottled", "Comercial": "Commercial", "Oficial": "Official"}
}

def etiquetar(dic, grupo):
    return {f"{grupo}: {k}": v for k, v in dic.items()}

ciudades = {'Madrid': {'alkalinity': 4.1, 'hardness': 13}}
embotelladas = {
    'Lanjaron': {'alkalinity': 88.56, 'hardness': 118.99},
    'Bezoya': {'alkalinity': 4.1, 'hardness': 8.63},
    'Solan de Cabras': {'alkalinity': 232.88, 'hardness': 253.46},
    'Teleno': {'alkalinity': 12.55, 'hardness': 13.74},
    'Aquarel': {'alkalinity': 112.34, 'hardness': 122.54},
    'Cabreiroa': {'alkalinity': 136.94, 'hardness': 25.63},
    'Aquafina': {'alkalinity': 13.94, 'hardness': 13.20},
    'VilaDrau': {'alkalinity': 93.48, 'hardness': 88.47},
    'Auchan': {'alkalinity': 190.24, 'hardness': 39.75},
    'Font Natura': {'alkalinity': 161.54, 'hardness': 57.4},
    'Sierra Cazorla': {'alkalinity': 335.13, 'hardness': 395.35}
}
comercial = {'Third Wave': {'alkalinity': 30, 'hardness': 50}}
oficial = {'SCAA': {'alkalinity': 40, 'hardness': 68}}

all_waters = {
    **etiquetar(ciudades, etiquetas[lang]["Ciudad"]),
    **etiquetar(embotelladas, etiquetas[lang]["Embotellada"]),
    **etiquetar(comercial, etiquetas[lang]["Comercial"]),
    **etiquetar(oficial, etiquetas[lang]["Oficial"])
}

st.title(textos[lang]["title"])
agua1 = st.selectbox(textos[lang]["select1"], list(all_waters.keys()), index=0)
agua2 = st.selectbox(textos[lang]["select2"], list(all_waters.keys()), index=1)
ratio = st.slider(textos[lang]["ratio"], 0, 100, 50)

r1 = ratio / 100
r2 = 1 - r1
mix = {
    'alkalinity': all_waters[agua1]['alkalinity'] * r1 + all_waters[agua2]['alkalinity'] * r2,
    'hardness': all_waters[agua1]['hardness'] * r1 + all_waters[agua2]['hardness'] * r2
}

st.markdown(f"### {textos[lang]['mezcla']}: {agua1} ({r1:.2f}) + {agua2} ({r2:.2f})")
st.write(f"**{textos[lang]['alk']}:** {mix['alkalinity']:.2f} ppm as CaCO₃")
st.write(f"**{textos[lang]['hard']}:** {mix['hardness']:.2f} ppm as CaCO₃")

fig = go.Figure()
for name, data in all_waters.items():
    fig.add_trace(go.Scatter(
        x=[data['alkalinity']],
        y=[data['hardness']],
        mode='markers+text',
        text=[name],
        textposition='top center',
        marker=dict(size=10)
    ))
fig.add_trace(go.Scatter(
    x=[mix['alkalinity']],
    y=[mix['hardness']],
    mode='markers+text',
    text=[f"{agua1} + {agua2}"],
    textposition="bottom center",
    marker=dict(size=12, color='purple', symbol='x')
))
fig.add_shape(type="rect", x0=40, y0=50, x1=75, y1=175,
                fillcolor="lightgreen", opacity=0.3, layer="below", line_width=0)
fig.add_annotation(x=42, y=160, text=textos[lang]['zone'], showarrow=False,
                    font=dict(size=12, color="green"))
fig.update_layout(
    xaxis_title="Alkalinity (ppm as CaCO₃)",
    yaxis_title="Total Hardness (ppm as CaCO₃)",
    xaxis=dict(range=[0, 360]),
    yaxis=dict(range=[0, 420]),
    height=650
)
st.plotly_chart(fig, use_container_width=True)