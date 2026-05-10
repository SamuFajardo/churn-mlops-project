# Proyecto MLOps - Predicción de Churn

## Alumno
Samuel Anibal Fajardo Reinoso
Alejandro Vergara
Marlene Jimenez
Manuel Resquin

## Materia
Laboratorio de Minería de Datos

## Objetivo del proyecto
El objetivo del proyecto es desarrollar una solución de Machine Learning
capaz de predecir el abandono de clientes (Customer Churn)
para una empresa de suscripción digital.

## Dataset utilizado
IBM Telco Customer Churn Dataset.

## Tecnologías utilizadas
- Python
- Jupyter Notebook
- Pandas
- Scikit-learn
- MLflow
- Joblib
- DVC
- Git

## Estructura del proyecto

```text
data/
models/
notebooks/
reports/
tests/
README.md
requirements.txt
## Reproducibilidad

El proyecto utiliza:

- Git y GitHub para versionado de código
- MLflow para tracking de experimentos
- DVC para versionado de datasets
- requirements.txt para reproducibilidad
  del entorno

## Modelos evaluados

- Logistic Regression
- Random Forest

## Métricas utilizadas

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC