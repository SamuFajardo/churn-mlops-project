from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


# =========================
# HOME
# =========================

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["mensaje"] == "API funcionando correctamente"


# =========================
# HEALTH
# =========================

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert "status" in response.json()

    assert "model_loaded" in response.json()


# =========================
# PREDICT OK
# =========================

def test_predict():

    payload = {

        "tenure_months": 12,
        "monthly_charge": 1500,
        "total_charges": 18000,
        "support_tickets": 2,
        "late_payments": 0,
        "avg_monthly_usage_gb": 120,
        "contract_type": "mensual",
        "payment_method": "credito",
        "internet_service": "fibra",
        "has_streaming": "si",
        "has_security_pack": "no",
        "num_products": 2,
        "region": "norte",
        "customer_age": 35,
        "is_promo": "no"

    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    assert "prediccion" in response.json()

    assert "probabilidad" in response.json()


# =========================
# PREDICT ERROR
# =========================

def test_predict_invalid_data():

    payload = {

        "tenure_months": 12

    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422