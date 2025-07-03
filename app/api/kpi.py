from fastapi import APIRouter

# Créé objet router utilisé dans main et kpi.py
router = APIRouter()

# --- MOCK KPI ROUTES ---


@router.get("/total_courses")
def total_courses():
    """Mock: Nombre total de courses"""
    return {"total_courses": 12345}


@router.get("/avg_distance")
def avg_distance():
    """Mock: Distance moyenne d’une course"""
    return {"avg_distance": 3.7}


@router.get("/total_amount")
def total_amount():
    """Mock: Montant total des courses"""
    return {"total_amount": 456789.12}


@router.get("/avg_tip")
def avg_tip():
    """Mock: Montant moyen des pourboires"""
    return {"avg_tip": 2.15}


@router.get("/payment_type_distribution")
def payment_type_distribution():
    """Mock: Répartition des types de paiement"""
    return {"payment_type_distribution": {"1": 8000, "2": 3000, "3": 500}}


@router.get("/total_passengers")
def total_passengers():
    """Mock: Nombre total de passagers"""
    return {"total_passengers": 25000}


@router.get("/avg_passengers")
def avg_passengers():
    """Mock: Nombre moyen de passagers par course"""
    return {"avg_passengers": 1.7}


@router.get("/top5_pickup_locations")
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


@router.get("/total_congestion_surcharge")
def total_congestion_surcharge():
    """Mock: Montant total des surcharges de congestion"""
    return {"total_congestion_surcharge": 12345.67}


@router.get("/rides_per_day")
def rides_per_day():
    """Mock: Nombre de courses par jour"""
    return {"rides_per_day": {"2025-07-01": 500, "2025-07-02": 600}}


@router.get("/rides_per_month")
def rides_per_month():
    """Mock: Nombre de courses par mois"""
    return {"rides_per_month": {"2025-06": 12000, "2025-07": 13000}}


@router.get("/tip_percentage")
def tip_percentage():
    """Mock: Pourcentage de courses avec pourboire"""
    return {"tip_percentage": 62.5}


# --- FIN MOCK KPI ---

# Pour passer en mode réel, il suffira de remplacer le contenu de chaque fonction par une requête SQL.
