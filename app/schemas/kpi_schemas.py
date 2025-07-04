from pydantic import BaseModel

#Pydantic permet de définir des schémas de données en utilisant des classes Python.
# Cela va permettre d'alimenter Swwagger et de valider les données entrantes et sortantes de l'API.

class TotalCoursesResponse(BaseModel):
    total_courses: int


class AvgDistanceResponse(BaseModel):
    avg_distance: float


class TotalAmountResponse(BaseModel):
    total_amount: float


class AvgTipResponse(BaseModel):
    avg_tip: float


class PaymentTypeDistributionResponse(BaseModel):
    payment_type_distribution: dict[str, int]


class TotalPassengersResponse(BaseModel):
    total_passengers: int


class AvgPassengersResponse(BaseModel):
    avg_passengers: float


class Top5PickupLocationsResponse(BaseModel):
    top5_pickup_locations: list[dict[str, int]]


class TotalCongestionSurchargeResponse(BaseModel):
    total_congestion_surcharge: float


class RidesPerDayResponse(BaseModel):
    rides_per_day: dict[str, int]


class RidesPerMonthResponse(BaseModel):
    rides_per_month: dict[str, int]


class TipPercentageResponse(BaseModel):
    tip_percentage: float
