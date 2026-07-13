import os
import pandas as pd

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# ==========================
# RUTAS
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "churn_sintetico.csv")

REPORTS_DIR = os.path.join(BASE_DIR, "reports")

REPORT_PATH = os.path.join(REPORTS_DIR, "evidently_report.html")

# ==========================
# CREAR CARPETA
# ==========================

os.makedirs(REPORTS_DIR, exist_ok=True)

# ==========================
# CARGAR DATASET
# ==========================

df = pd.read_csv(DATA_PATH)

# ==========================
# SIMULAR DRIFT
# ==========================

reference_data = df.copy()

current_data = df.copy()

# Cambiamos algunos valores para simular cambios en producción
current_data["monthly_charge"] = current_data["monthly_charge"] * 1.15

current_data["avg_monthly_usage_gb"] = (
    current_data["avg_monthly_usage_gb"] * 0.85
)

# ==========================
# REPORTE
# ==========================

report = Report(

    metrics=[

        DataDriftPreset()

    ]

)

report.run(

    reference_data=reference_data,

    current_data=current_data

)

report.save_html(REPORT_PATH)

print("Reporte generado correctamente.")

print(REPORT_PATH)