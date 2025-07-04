from fastapi.testclient import TestClient
from app.main import app  # importe ton app FastAPI

client = TestClient(app)

def test_total_courses():
    response = client.get("/kpi/total_courses")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "total_courses" in data, "La clé 'total_courses' est absente de la réponse"
    assert isinstance(data["total_courses"], int), "Le résultat retourné n'est pas un int"

def test_avg_distance():
    response = client.get("/kpi/avg_distance")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "avg_distance" in data, "La clé 'avg_distance' est absente de la réponse"
    assert isinstance(data["avg_distance"], float), "Le résultat retourné n'est pas un float"

def test_total_amount():
    response = client.get("/kpi/total_amount")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "total_amount" in data, "La clé 'total_amount' est absente de la réponse"
    assert isinstance(data["total_amount"], float), "Le résultat retourné n'est pas un float"

def test_avg_tip():
    response = client.get("/kpi/avg_tip")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "avg_tip" in data, "La clé 'avg_tip' est absente de la réponse"
    assert isinstance(data["avg_tip"], float), "Le résultat retourné n'est pas un float"

def test_payment_type_distribution():
    response = client.get("/kpi/payment_type_distribution")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "payment_type_distribution" in data, "La clé 'payment_type_distribution' est absente de la réponse"
    assert isinstance(data["payment_type_distribution"], dict), "Le résultat retourné n'est pas un JSON"

def test_total_passengers():
    response = client.get("/kpi/total_passengers")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "total_passengers" in data, "La clé 'total_passengers' est absente de la réponse"
    assert isinstance(data["total_passengers"], int), "Le résultat retourné n'est pas un int"

def test_avg_passengers():
    response = client.get("/kpi/avg_passengers")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "avg_passengers" in data, "La clé 'avg_passengers' est absente de la réponse"
    assert isinstance(data["avg_passengers"], float), "Le résultat retourné n'est pas un float"

def test_top5_pickup_locations():
    response = client.get("/kpi/top5_pickup_locations")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "top5_pickup_locations" in data, "La clé 'top5_pickup_locations' est absente de la réponse"
    assert isinstance(data["top5_pickup_locations"], list), "Le résultat retourné n'est pas une liste"
    for item in data["top5_pickup_locations"]:
        assert isinstance(item, dict), "Un élément n'est pas un dictionnaire"
        assert "pickup_location_id" in item, "La clé 'pickup_location_id' est absente de la réponse (dans la liste de dictionnaires)"
        assert "count" in item, "La clé 'count' est absente de la réponse (dans la liste de dictionnaires)"
        assert isinstance(item["pickup_location_id"], int)
        assert isinstance(item["count"], int)

def test_total_congestion_surcharge():
    response = client.get("/kpi/total_congestion_surcharge")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "total_congestion_surcharge" in data, "La clé 'total_congestion_surcharge' est absente de la réponse"
    assert isinstance(data["total_congestion_surcharge"], float), "Le résultat retourné n'est pas un float"

def test_rides_per_day():
    response = client.get("/kpi/rides_per_day")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "rides_per_day" in data, "La clé 'rides_per_day' est absente de la réponse"
    assert isinstance(data["rides_per_day"], dict), "Le résultat retourné n'est pas un JSON"

def test_rides_per_month():
    response = client.get("/kpi/rides_per_month")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "rides_per_month" in data, "La clé 'rides_per_month' est absente de la réponse"
    assert isinstance(data["rides_per_month"], dict), "Le résultat retourné n'est pas un JSON"

def test_tip_percentage():
    response = client.get("/kpi/tip_percentage")
    assert response.status_code == 200, "La route ne retourne pas un code 200"
    data = response.json()
    assert "tip_percentage" in data, "La clé 'tip_percentage' est absente de la réponse"
    assert isinstance(data["tip_percentage"], float), "Le résultat retourné n'est pas un float"


#Pour lancer tests, lancer dans la racine du projet en terminal:
# pytest