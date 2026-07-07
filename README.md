# Proyecto MLOps - Predicción de Churn de Clientes

## Equipo de Trabajo (Alumnos)
- Samuel Aníbal Fajardo Reinoso
- Alejandro Vergara
- Marlene Jimenez

**Materia:** Laboratorio de Minería de Datos

---

## Objetivo del Proyecto
El objetivo del proyecto es desarrollar e implementar una solución integral de Machine Learning Operations (MLOps) capaz de predecir el abandono de clientes (Customer Churn) para una empresa de suscripción digital. El sistema abarca desde el entrenamiento del modelo hasta su despliegue en producción mediante contenedores, con monitoreo continuo y una interfaz gráfica de usuario.

## Dataset Utilizado
**IBM Telco Customer Churn Dataset.**

---

## Tecnologías Utilizadas

**Modelado y Experimentación:**
- Python, Pandas, Scikit-learn, Joblib
- MLflow (Tracking de experimentos)
- DVC (Versionado de datasets)
- Jupyter Notebook

**Despliegue e Ingeniería de Software:**
- FastAPI (API RESTful)
- Pydantic (Validación estricta de datos)
- Streamlit (Interfaz Gráfica / Frontend)
- Pytest (Pruebas unitarias y de integración)

**Infraestructura y Monitoreo:**
- Docker & Docker Compose (Contenerización y Orquestación)
- Prometheus & Grafana (Monitoreo de métricas en tiempo real)
- Git & GitHub (Control de versiones)

---

## Arquitectura del Sistema

El despliegue local sigue una arquitectura de microservicios comunicados en una red interna de Docker:

[Usuario/Cliente] ➔ (Puerto 8501) ➔ [GUI Streamlit] ➔ (Red interna HTTP) ➔ [API FastAPI] ➔ [Modelo .pkl]
                                                                        ↘
                                                                   [Prometheus/Grafana]

---

##  Instrucciones de Despliegue (Reproducibilidad)

Para levantar el proyecto completo de manera local, solo es necesario contar con Docker y Docker Compose instalados.

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/SamuFajardo/churn-mlops-project.git](https://github.com/SamuFajardo/churn-mlops-project.git)
   cd churn-mlops-project
