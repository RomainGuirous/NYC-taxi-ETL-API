from fastapi import APIRouter
from app.schemas.kpi_schemas import (
    TotalCoursesResponse,
    AvgDistanceResponse,
    TotalAmountResponse,
    AvgTipResponse,
    PaymentTypeDistributionResponse,
    TotalPassengersResponse,
    AvgPassengersResponse,
    Top5PickupLocationsResponse,
    TotalCongestionSurchargeResponse,
    RidesPerDayResponse,
    RidesPerMonthResponse,
    TipPercentageResponse,
)

# Créé objet router utilisé dans main et kpi.py
router = APIRouter()

# --- MOCK KPI ROUTES ---


@router.get("/total_courses", response_model=TotalCoursesResponse)
def total_courses():
    """Mock: Nombre total de courses"""
    return {"total_courses": 12345}


@router.get("/avg_distance", response_model=AvgDistanceResponse)
def avg_distance():
    """Mock: Distance moyenne d’une course"""
    return {"avg_distance": 3.7}


@router.get("/total_amount", response_model=TotalAmountResponse)
def total_amount():
    """Mock: Montant total des courses"""
    return {"total_amount": 456789.12}


@router.get("/avg_tip", response_model=AvgTipResponse)
def avg_tip():
    """Mock: Montant moyen des pourboires"""
    return {"avg_tip": 2.15}


@router.get(
    "/payment_type_distribution", response_model=PaymentTypeDistributionResponse
)
def payment_type_distribution():
    """Mock: Répartition des types de paiement"""
    return {"payment_type_distribution": {"1": 8000, "2": 3000, "3": 500}}


@router.get("/total_passengers", response_model=TotalPassengersResponse)
def total_passengers():
    """Mock: Nombre total de passagers"""
    return {"total_passengers": 25000}


@router.get("/avg_passengers", response_model=AvgPassengersResponse)
def avg_passengers():
    """Mock: Nombre moyen de passagers par course"""
    return {"avg_passengers": 1.7}


@router.get("/top5_pickup_locations", response_model=Top5PickupLocationsResponse)
def top5_pickup_locations():
    """Mock: Top 5 des lieux de prise en charge"""
    return {
        "top5_pickup_locations": [
            {"pickup_location_id": 101, "count": 1200},
            {"pickup_location_id": 102, "count": 1100},
            {"pickup_location_id": 103, "count": 900},
            {"pickup_location_id": 104, "count": 850},
            {"pickup_location_id": 105, "count": 800},
        ]
    }


@router.get(
    "/total_congestion_surcharge", response_model=TotalCongestionSurchargeResponse
)
def total_congestion_surcharge():
    """Mock: Montant total des surcharges de congestion"""
    return {"total_congestion_surcharge": 12345.67}


@router.get("/rides_per_day", response_model=RidesPerDayResponse)
def rides_per_day():
    """Mock: Nombre de courses par jour"""
    return {"rides_per_day": {"2025-07-01": 500, "2025-07-02": 600}}


@router.get("/rides_per_month", response_model=RidesPerMonthResponse)
def rides_per_month():
    """Mock: Nombre de courses par mois"""
    return {"rides_per_month": {"2025-06": 12000, "2025-07": 13000}}


@router.get("/tip_percentage", response_model=TipPercentageResponse)
def tip_percentage():
    """Mock: Pourcentage de courses avec pourboire"""
    return {"tip_percentage": 62.5}


# --- FIN MOCK KPI ---

# Pour passer en mode réel, il suffira de remplacer le contenu de chaque fonction par une requête SQL.
