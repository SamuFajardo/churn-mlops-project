from typing import Literal

from pydantic import BaseModel


class CustomerData(BaseModel):

    tenure_months: int
    monthly_charge: float
    total_charges: float
    support_tickets: int
    late_payments: int
    avg_monthly_usage_gb: float

    contract_type: Literal[
        "mensual",
        "anual",
        "bianual"
    ]

    payment_method: Literal[
        "transferencia",
        "debito",
        "efectivo",
        "credito"
    ]

    internet_service: Literal[
        "cable",
        "fibra",
        "movil",
        "ninguno"
    ]

    has_streaming: str

    has_security_pack: str

    num_products: int

    region: Literal[
        "centro",
        "norte",
        "oeste",
        "sur"
    ]

    customer_age: int

    is_promo: str