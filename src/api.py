from fastapi import FastAPI
from fastapi.responses import JSONResponse

import joblib
import pandas as pd
import logging

from pathlib import Path

from src.schema import CustomerData
from prometheus_fastapi_instrumentator import Instrumentator

# =========================
# LOGGING
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# =========================
# APP
# =========================

app = FastAPI()

# =========================
# PROMETHEUS
# =========================

Instrumentator().instrument(app).expose(app)

# =========================
# RUTAS
# =========================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR.parent / "models" / "model.pkl"

# =========================
# LOAD MODEL
# =========================

try:

    model = joblib.load(MODEL_PATH)

    logger.info("Modelo cargado correctamente.")

except Exception as e:

    model = None

    logger.error(f"No fue posible cargar el modelo: {e}")

# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "mensaje": "API funcionando correctamente"
    }

# =========================
# HEALTH
# =========================

@app.get("/health")
def health():

    return {

        "status": "ok",

        "model_loaded": model is not None

    }

# =========================
# PREDICT
# =========================

@app.post("/predict")
def predict(data: CustomerData):

    try:

        if model is None:

            return JSONResponse(

                status_code=500,

                content={

                    "error": "El modelo no se encuentra cargado."

                }

            )

        input_data = data.model_dump()

        # =========================
        # MAPEO SI/NO
        # =========================

        binary_map = {

            "si": 1,
            "yes": 1,
            "no": 0

        }

        binary_columns = [

            "has_streaming",
            "has_security_pack",
            "is_promo"

        ]

        for col in binary_columns:

            input_data[col] = binary_map.get(
                str(input_data[col]).lower(),
                input_data[col]
            )

        # =========================
        # DATAFRAME
        # =========================

        input_df = pd.DataFrame([
            input_data
        ])

        # =========================
        # PREDICT
        # =========================

        prediction = model.predict(
            input_df
        )[0]

        probability = model.predict_proba(
            input_df
        )[0][1]

        logger.info("Predicción realizada correctamente.")

        return {

            "prediccion": int(prediction),

            "probabilidad": float(probability),

            "riesgo": "ALTO" if prediction == 1 else "BAJO"

        }

    except Exception as e:

        logger.error(f"Error durante la predicción: {e}")

        return JSONResponse(

            status_code=500,

            content={

                "error": str(e)

            }

        )