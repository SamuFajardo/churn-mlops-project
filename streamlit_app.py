import os
import requests
import streamlit as st

# ======================================
# CONFIGURACIÓN
# ======================================

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

# ======================================
# TÍTULO
# ======================================

st.title("Predicción de Churn de Clientes")

# ======================================
# FORMULARIO
# ======================================

tenure = st.number_input(
    "Meses de antigüedad",
    min_value=0
)

monthly_charge = st.number_input(
    "Cargo mensual",
    min_value=0.0
)

total_charges = st.number_input(
    "Cargo total",
    min_value=0.0
)

support_tickets = st.number_input(
    "Tickets de soporte",
    min_value=0
)

late_payments = st.number_input(
    "Pagos atrasados",
    min_value=0
)

usage = st.number_input(
    "Uso promedio (GB)",
    min_value=0.0
)

contract_type = st.selectbox(
    "Tipo de contrato",
    ["mensual", "anual", "bianual"]
)

payment_method = st.selectbox(
    "Método de pago",
    ["transferencia", "debito", "efectivo", "credito"]
)

internet_service = st.selectbox(
    "Servicio de Internet",
    ["fibra", "cable", "movil", "ninguno"]
)

has_streaming = st.selectbox(
    "Streaming",
    ["si", "no"]
)

has_security_pack = st.selectbox(
    "Pack de seguridad",
    ["si", "no"]
)

num_products = st.number_input(
    "Cantidad de productos",
    min_value=1
)

region = st.selectbox(
    "Región",
    ["norte", "sur", "centro", "oeste"]
)

customer_age = st.number_input(
    "Edad",
    min_value=18
)

is_promo = st.selectbox(
    "Promoción",
    ["si", "no"]
)

# ======================================
# BOTÓN
# ======================================

if st.button("Predecir"):

    data = {
        "tenure_months": int(tenure),
        "monthly_charge": float(monthly_charge),
        "total_charges": float(total_charges),
        "support_tickets": int(support_tickets),
        "late_payments": int(late_payments),
        "avg_monthly_usage_gb": float(usage),
        "contract_type": contract_type,
        "payment_method": payment_method,
        "internet_service": internet_service,
        "has_streaming": has_streaming,
        "has_security_pack": has_security_pack,
        "num_products": int(num_products),
        "region": region,
        "customer_age": int(customer_age),
        "is_promo": is_promo
    }

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=data,
            timeout=10
        )

        # Si es el error 422, lo atajamos para que nos imprima exactamente qué campo falló
        if response.status_code == 422:
            st.error("🚨 FastAPI rechazó un dato. Detalle exacto del error:")
            st.json(response.json())
        else:
            # Si no es 422, que siga su curso normal
            response.raise_for_status()
            resultado = response.json()

            st.success("Predicción realizada correctamente")
            st.subheader("Resultado")
            st.json(resultado)

            if resultado["prediccion"] == 1:
                st.warning("⚠️ El cliente presenta ALTO riesgo de abandono.")
            else:
                st.success("✅ El cliente presenta BAJO riesgo de abandono.")

            st.metric("Probabilidad de Churn", f"{resultado['probabilidad']:.2%}")

    except requests.exceptions.Timeout:
        st.error("La API tardó demasiado en responder.")

    except requests.exceptions.ConnectionError:
        st.error("No fue posible conectar con la API.")

    except requests.exceptions.RequestException as e:
        st.error(f"Error general de conexión: {e}")