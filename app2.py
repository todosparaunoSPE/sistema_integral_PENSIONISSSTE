# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 09:19:53 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import os



# Configuración inicial
st.set_page_config(page_title="AFORE PENSIONISSSTE - Sistema de Agentes Inteligentes", layout="wide")


# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("Sistema Integral de Agentes Inteligentes para AFORE PENSIONISSSTE")


st.sidebar.title("Sistema Integral de Agentes Inteligentes para AFORE PENSIONISSSTE")
st.sidebar.write("Desarrollado por: **Javier Horacio Pérez Ricárdez**")


# Cargar datos desde CSV (en un caso real, estos archivos estarían en un directorio 'data/')
@st.cache_data
def load_data():
    # Crear datos simulados si no existen
    if not os.path.exists('afiliados.csv'):
        afiliados = pd.DataFrame({
            'id': range(1, 11),
            'nombre': ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Luis Ramírez',
                       'Sofía Díaz', 'Jorge Cruz', 'Patricia Ruiz', 'Fernando Vázquez', 'Adriana Soto'],
            'edad': [45, 38, 52, 29, 60, 41, 35, 48, 55, 33],
            'salario': [25000, 32000, 18000, 28000, 15000, 38000, 42000, 29000, 21000, 35000],
            'años_cotizacion': [15, 10, 28, 5, 35, 18, 12, 22, 30, 8],
            'estado_civil': ['Casado', 'Soltero', 'Casado', 'Soltero', 'Casado', 'Divorciado', 'Soltero',
                            'Casado', 'Casado', 'Soltero'],
            'hijos': [2, 0, 3, 0, 1, 2, 0, 3, 2, 1],
            'escolaridad': ['Universidad']*7 + ['Preparatoria']*3,
            'riesgo_pension_insuficiente': ['Medio', 'Bajo', 'Alto', 'Bajo', 'Alto', 'Medio', 'Bajo', 'Medio', 'Alto', 'Bajo'],
            'fondo_actual': ['Balanceado', 'Crecimiento', 'Conservador', 'Crecimiento', 'Conservador',
                            'Balanceado', 'Crecimiento', 'Balanceado', 'Conservador', 'Crecimiento']
        })
        afiliados.to_csv('afiliados.csv', index=False)

    if not os.path.exists('proyecciones_pensiones.csv'):
        proyecciones = pd.DataFrame({
            'id': range(1, 11),
            'edad_jubilacion': [65]*10,
            'pension_proyectada_base': [12500, 18000, 8500, 22000, 7000, 16000, 24000, 13500, 9000, 19500],
            'pension_optimista': [14500, 21000, 9500, 25000, 8000, 18500, 27500, 15500, 10500, 22500],
            'pension_pesimista': [10500, 15000, 7500, 19000, 6000, 13500, 20500, 11500, 7500, 16500],
            'recomendacion_aportacion': [
                "Aumentar 2000 mensuales", "Mantener aportación", "Aumentar 3000 mensuales",
                "Mantener aportación", "Aumentar 2500 mensuales", "Aumentar 1000 mensuales",
                "Mantener aportación", "Aumentar 1500 mensuales", "Aumentar 3000 mensuales",
                "Mantener aportación"
            ]
        })
        proyecciones.to_csv('proyecciones_pensiones.csv', index=False)

    if not os.path.exists('fondos_inversion.csv'):
        fondos = pd.DataFrame({
            'fondo': ['Conservador', 'Balanceado', 'Crecimiento'],
            'rendimiento_anual': [4.5, 6.8, 8.2],
            'riesgo': ['Bajo', 'Medio', 'Alto'],
            'comision': [0.8, 1.2, 1.5],
            'perfil_recomendado': ['Jubilación cercana', 'Jubilación media', 'Jubilación lejana'],
            'rentabilidad_5años': [24.6, 39.1, 48.3]
        })
        fondos.to_csv('fondos_inversion.csv', index=False)

    if not os.path.exists('transacciones.csv'):
        transactions = pd.DataFrame({
            'id_afiliado': [1,1,2,3,4,5,6,7,8,9],
            'fecha': ['2024-01-15', '2024-02-18', '2024-01-20', '2024-01-10', '2024-02-05',
                     '2024-01-22', '2024-02-28', '2024-01-30', '2024-02-12', '2024-01-08'],
            'monto': [2500, 2500, 1500, 1000, 3000, 800, 2000, 1800, 1200, 900],
            'tipo': ['Aportación']*10,
            'concepto': ['Voluntaria']*10
        })
        transactions.to_csv('transacciones.csv', index=False)

    # Cargar los archivos
    afiliados = pd.read_csv('afiliados.csv')
    proyecciones = pd.read_csv('proyecciones_pensiones.csv')
    fondos = pd.read_csv('fondos_inversion.csv')
    transacciones = pd.read_csv('transacciones.csv')

    # Convertir fechas
    transacciones['fecha'] = pd.to_datetime(transacciones['fecha'])

    # Unir datos de afiliados con proyecciones
    datos_completos = pd.merge(afiliados, proyecciones, on='id')
    return datos_completos, fondos, transacciones

# Cargar datos
df_afiliados, df_fondos, df_transacciones = load_data()

# Menú principal
menu = st.sidebar.selectbox("Módulos del Sistema", [
    "Dashboard General",
    "Agentes de Predicción de Pensiones",
    "Agentes de Asesoría Financiera",
    "Agentes de Gestión de Inversiones",
    "Agentes de Análisis de Comportamiento",
    "Agentes de Supervisión de Riesgos"
])

# Contenido según selección del menú
if menu == "Dashboard General":
    st.header("Dashboard General - Visión Integral")

    # Métricas clave
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Afiliados", len(df_afiliados))
    with col2:
        st.metric("Pensión Promedio Proyectada", f"${df_afiliados['pension_proyectada_base'].mean():.2f}")
    with col3:
        riesgo_alto = len(df_afiliados[df_afiliados['riesgo_pension_insuficiente'] == 'Alto'])
        st.metric("Afiliados con Riesgo Alto", f"{riesgo_alto} ({riesgo_alto/len(df_afiliados)*100:.1f}%)")

    # Gráficos
    st.subheader("Distribución de Pensiones Proyectadas")
    fig = px.histogram(df_afiliados, x='pension_proyectada_base', nbins=10,
                      title="Distribución de Pensiones Proyectadas",
                      labels={'pension_proyectada_base': 'Pensión mensual proyectada ($)'})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Distribución por Tipo de Fondo de Inversión")
    fig = px.pie(df_afiliados, names='fondo_actual', title="Afiliados por Tipo de Fondo")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Resumen de Datos de Afiliados")
    st.dataframe(df_afiliados)

elif menu == "Agentes de Predicción de Pensiones":
    st.header("Agentes de Predicción de Pensiones")
    st.markdown("""
    **Funciones principales:**
    - Predicción dinámica de pensiones futuras
    - Identificación de afiliados con pensiones insuficientes
    - Adaptación de proyecciones según condiciones económicas
    """)
    
    st.subheader("Proyecciones Actuales de los Afiliados")
    st.dataframe(df_afiliados[['id', 'nombre', 'edad', 'años_cotizacion', 'pension_proyectada_base',
                             'riesgo_pension_insuficiente', 'recomendacion_aportacion']])

    st.subheader("Simulador de Proyección de Pensión")
    with st.form("simulador_pension"):
        col1, col2 = st.columns(2)
        with col1:
            edad = st.slider("Edad actual", 25, 65, 40)
            salario = st.number_input("Salario mensual actual ($)", 10000, 100000, 25000)
            años_cotizacion = st.slider("Años de cotización", 1, 40, 10)
        with col2:
            aportacion_voluntaria = st.number_input("Aportación voluntaria mensual ($)", 0, 10000, 1000)
            tasa_crecimiento = st.slider("Tasa de crecimiento salarial anual estimada (%)", 0.0, 10.0, 3.5)
            edad_jubilacion = st.slider("Edad de jubilación planeada", 60, 75, 65)
        
        submitted = st.form_submit_button("Calcular Proyección")
    
    if submitted:
        años_restantes = edad_jubilacion - edad
        
        # Cálculo simplificado para demostración
        pension_base = (salario * años_cotizacion * 0.05)
        pension_aportaciones = (aportacion_voluntaria * 12 * años_restantes * 1.03)
        pension_proyectada = (pension_base + pension_aportaciones) * (1 + (tasa_crecimiento/100 * años_restantes))
        
        st.success(f"**Pensión mensual proyectada:** ${pension_proyectada:.2f}")
        
        if pension_proyectada < salario * 0.4:
            st.warning(" ▲ **Riesgo de pensión insuficiente detectado**")
            st.markdown("""
            **Recomendaciones del agente:**
            - Incrementar aportaciones voluntarias
            - Considerar extender años de cotización
            - Revisar estrategia de inversión del fondo
            """)
        
        # Gráfico de proyección
        años = list(range(edad, edad_jubilacion + 1))
        proyeccion = [pension_base * (1 + (tasa_crecimiento/100 * (x - edad))) + 
                     (aportacion_voluntaria * 12 * (x - edad) * 1.03) for x in años]
        
        fig = px.line(x=años, y=proyeccion, title="Proyección de Pensión",
                     labels={'x': 'Edad', 'y': 'Pensión mensual proyectada ($)'})
        st.plotly_chart(fig, use_container_width=True)

elif menu == "Agentes de Asesoría Financiera":
    st.header("Agentes de Asesoría Financiera Personalizada")
    st.markdown("""
    **Funciones principales:**
    - Asesoría personalizada basada en perfil financiero
    - Recomendaciones sobre aportaciones voluntarias
    - Información sobre fondos más adecuados
    """)
    
    st.subheader("Seleccione un Afiliado para Análisis")
    afiliado_id = st.selectbox("Afiliado", df_afiliados['id'])
    afiliado = df_afiliados[df_afiliados['id'] == afiliado_id].iloc[0]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nombre", afiliado["nombre"])
        st.metric("Edad", afiliado["edad"])
        st.metric("Años de cotización", afiliado['años_cotizacion'])
        st.metric("Fondo actual", afiliado['fondo_actual'])
    with col2:
        st.metric("Salario", f"${afiliado['salario']:.2f}")
        st.metric("Pensión proyectada", f"${afiliado['pension_proyectada_base']:.2f}")
        st.metric("Riesgo de pensión insuficiente", afiliado['riesgo_pension_insuficiente'])
        st.metric("Recomendación aportación", afiliado['recomendacion_aportacion'])
    
    st.subheader("Recomendaciones Personalizadas")
    if afiliado['riesgo_pension_insuficiente'] == 'Alto':
        st.warning("""
        **Análisis del agente:** Alto riesgo de pensión insuficiente detectado
        
        **Recomendaciones:**
        1. Incrementar aportaciones voluntarias según sugerencia
        2. Considerar cambiar al fondo de inversión más adecuado
        3. Evaluar opciones de jubilación tardía
        """)
    elif afiliado['riesgo_pension_insuficiente'] == 'Medio':
        st.info("""
        **Análisis del agente:** Riesgo moderado de pensión insuficiente
        
        **Recomendaciones:**
        1. Seguir recomendación de incremento de aportaciones
        2. Revisar adecuación del fondo actual
        3. Monitorear cambios en situación laboral
        """)
    else:
        st.success("""
        **Análisis del agente:** Buen nivel de pensión proyectada
        
        **Recomendaciones:**
        1. Mantener estrategia actual
        2. Considerar diversificación de inversiones
        3. Revisar proyecciones periódicamente
        """)
    
    st.subheader("Historial de Aportaciones")
    transacciones_afiliado = df_transacciones[df_transacciones['id_afiliado'] == afiliado_id]
    
    if not transacciones_afiliado.empty:
        fig = px.bar(transacciones_afiliado, x='fecha', y='monto',
                    title=f"Aportaciones voluntarias de {afiliado['nombre']}",
                    labels={'monto': 'Monto ($)', 'fecha': 'Fecha'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No se encontraron aportaciones voluntarias registradas para este afiliado.")
    
    st.subheader("Opciones de Fondos de Inversión")
    st.dataframe(df_fondos)

elif menu == "Agentes de Gestión de Inversiones":
    st.header("Agentes de Gestión de Inversiones y Fondos")
    st.markdown("""
    **Funciones principales:**
    - Optimización de la asignación de fondos
    - Ajuste dinámico de carteras
    - Supervisión de rentabilidad y riesgo
    """)
    
    st.subheader("Rendimiento de Fondos de Inversión")
    fig = px.bar(df_fondos, x='fondo', y='rendimiento_anual',
                title='Rendimiento Anual Esperado por Tipo de Fondo',
                labels={'rendimiento_anual': 'Rendimiento (%)', 'fondo': 'Tipo de Fondo'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Distribución Actual de Afiliados por Fondos")
    distribucion_fondos = df_afiliados['fondo_actual'].value_counts().reset_index()
    distribucion_fondos.columns = ['Fondo', 'Cantidad de Afiliados']
    fig = px.pie(distribucion_fondos, names='Fondo', values='Cantidad de Afiliados',
                title="Distribución de Afiliados por Tipo de Fondo")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Simulador de Cambio de Fondo")
    with st.form("simulador_fondo"):
        afiliado_id = st.selectbox("Seleccione afiliado", df_afiliados['id'])
        fondo_actual = df_afiliados[df_afiliados['id'] == afiliado_id]['fondo_actual'].values[0]
        st.write(f"Fondo actual: **{fondo_actual}**")
        nuevo_fondo = st.selectbox("Seleccione nuevo fondo", df_fondos['fondo'])
        submitted = st.form_submit_button("Simular Cambio")
    
    if submitted:
        fondo_info = df_fondos[df_fondos['fondo'] == nuevo_fondo].iloc[0]
        st.success(f"**Proyección con fondo {nuevo_fondo}:**")
        st.write(f"- Rendimiento anual esperado: {fondo_info['rendimiento_anual']}%")
        st.write(f"- Nivel de riesgo: {fondo_info['riesgo']}")
        st.write(f"- Comisión anual: {fondo_info['comision']}%")
        st.write(f"- Perfil recomendado: {fondo_info['perfil_recomendado']}")
        
        afiliado = df_afiliados[df_afiliados['id'] == afiliado_id].iloc[0]
        años_restantes = 65 - afiliado['edad']
        
        if años_restantes < 10 and nuevo_fondo == 'Crecimiento':
            st.warning(" ▲ Este fondo puede no ser adecuado para perfiles cercanos a la jubilación")
        elif años_restantes > 20 and nuevo_fondo == 'Conservador':
            st.warning(" ▲ Este fondo puede ofrecer rendimientos insuficientes para horizontes largos")

elif menu == "Agentes de Análisis de Comportamiento":
    st.header("Agentes de Análisis de Comportamiento de los Afiliados")
    st.markdown("""
    **Funciones principales:**
    - Identificar patrones en decisiones financieras
    - Proponer cambios en estrategias de ahorro
    - Prevenir deserción de afiliados
    """)
    
    st.subheader("Patrones de Aportaciones Voluntarias")
    transacciones_analisis = df_transacciones.merge(df_afiliados[['id', 'nombre', 'edad', 'salario']],
                                                  left_on='id_afiliado', right_on='id')
    fig = px.scatter(transacciones_analisis, x='salario', y='monto', color='edad',
                    title="Relación entre Salario y Aportaciones Voluntarias",
                    labels={'salario': 'Salario ($)', 'monto': 'Aportación ($)', 'edad': 'Edad'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Frecuencia de Aportaciones por Afiliado")
    frecuencia_aportaciones = transacciones_analisis.groupby(['id_afiliado', 'nombre']).size().reset_index(name='aportaciones')
    fig = px.bar(frecuencia_aportaciones, x='nombre', y='aportaciones',
                title="Número de Aportaciones por Afiliado",
                labels={'aportaciones': 'Número de aportaciones', 'nombre': 'Afiliado'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Recomendaciones de Comportamiento")
    st.markdown("""
    **Hallazgos del agente de análisis:**
    - Los afiliados con mayores salarios tienden a realizar aportaciones más consistentes
    - Los afiliados mayores de 50 años muestran menor frecuencia de aportaciones voluntarias
    - Se detectaron 3 afiliados sin aportaciones voluntarias en los últimos 6 meses
    
    **Recomendaciones:**
    1. Implementar campaña de concientización para afiliados mayores de 50 años
    2. Crear programa de recordatorios automatizados para aportaciones
    3. Contactar a afiliados inactivos en aportaciones voluntarias
    """)


#################################

elif menu == "Agentes de Supervisión de Riesgos":
    st.header("Agentes de Supervisión de Riesgos y Cumplimiento Normativo")
    st.markdown("""
    **Funciones principales:**
    - Supervisión de conformidad normativa
    - Detección de irregularidades
    - Identificación de riesgos financieros
    """)
    
    st.subheader("Alertas de Riesgo Detectadas")
    alertas = [
        {"tipo": "Pensión insuficiente", "afiliados": 3, "severidad": "Alta"},
        {"tipo": "Fondo inadecuado para edad", "afiliados": 2, "severidad": "Media"},
        {"tipo": "Sin aportaciones recientes", "afiliados": 4, "severidad": "Baja"},
        {"tipo": "Cambios bruscos en salario", "afiliados": 1, "severidad": "Media"}
    ]
    df_alertas = pd.DataFrame(alertas)
    st.dataframe(df_alertas)
    
    st.subheader("Afiliados con Mayor Riesgo")
    df_riesgo = df_afiliados[df_afiliados['riesgo_pension_insuficiente'] == 'Alto'][['id', 'nombre', 'edad', 'pension_proyectada_base']]
    st.dataframe(df_riesgo)
    
    st.subheader("Simulación de Pruebas de Cumplimiento")
    with st.form("prueba_cumplimiento"):
        prueba = st.selectbox("Seleccione prueba a ejecutar", [
            "Verificación de fondos adecuados por edad",
            "Detección de pensiones insuficientes",
            "Identificación de aportaciones atípicas"
        ])
        submitted = st.form_submit_button("Ejecutar Prueba")
    
    if submitted:
        if prueba == "Verificación de fondos adecuados por edad":
            # Afiliados mayores de 55 en fondos de crecimiento (riesgo alto)
            # O menores de 40 en fondos conservadores (oportunidad perdida)
            inadecuados = df_afiliados[
                ((df_afiliados['edad'] > 55) & (df_afiliados['fondo_actual'] == 'Crecimiento')) |
                ((df_afiliados['edad'] < 40) & (df_afiliados['fondo_actual'] == 'Conservador'))
            ]
            
            if not inadecuados.empty:
                st.warning(f"Se encontraron {len(inadecuados)} afiliados con fondos potencialmente inadecuados para su edad")
                st.dataframe(inadecuados[['id', 'nombre', 'edad', 'fondo_actual', 'riesgo_pension_insuficiente']])
            else:
                st.success("Todos los afiliados tienen fondos adecuados para su edad")
        
        elif prueba == "Detección de pensiones insuficientes":
            # Pensiones proyectadas menores al 40% del salario actual
            insuficientes = df_afiliados[
                df_afiliados['pension_proyectada_base'] < (df_afiliados['salario'] * 0.4)
            ]
            
            if not insuficientes.empty:
                st.warning(f"Se encontraron {len(insuficientes)} afiliados con pensiones proyectadas insuficientes")
                # Mostrar columna adicional con el porcentaje pensión/salario
                insuficientes['%_pension_salario'] = (insuficientes['pension_proyectada_base'] / insuficientes['salario'] * 100).round(1)
                st.dataframe(insuficientes[['id', 'nombre', 'salario', 'pension_proyectada_base', '%_pension_salario', 'recomendacion_aportacion']])
            else:
                st.success("No se detectaron pensiones insuficientes en los registros actuales")
        
        elif prueba == "Identificación de aportaciones atípicas":
            # Calcular estadísticas de aportaciones
            stats_aportaciones = df_transacciones.groupby('id_afiliado')['monto'].agg(['mean', 'std']).reset_index()
            
            # Unir con datos de afiliados
            transacciones_analisis = df_transacciones.merge(stats_aportaciones, on='id_afiliado')
            transacciones_analisis = transacciones_analisis.merge(df_afiliados[['id', 'nombre']], left_on='id_afiliado', right_on='id')
            
            # Identificar transacciones atípicas (monto > media + 2*std)
            transacciones_analisis['atipica'] = transacciones_analisis['monto'] > (transacciones_analisis['mean'] + 2 * transacciones_analisis['std'])
            atipicas = transacciones_analisis[transacciones_analisis['atipica']]
            
            if not atipicas.empty:
                st.warning(f"Se detectaron {len(atipicas)} aportaciones atípicas")
                st.dataframe(atipicas[['nombre', 'fecha', 'monto', 'mean', 'std']].rename(
                    columns={'mean': 'Promedio', 'std': 'Desviación', 'monto': 'Monto'}))
            else:
                st.success("No se detectaron aportaciones atípicas en los registros actuales")

# Pie de página
st.markdown("---")
st.markdown("**AFORE PENSIONISSSTE** - Sistema Integral de Agentes Inteligentes - © 2025")
