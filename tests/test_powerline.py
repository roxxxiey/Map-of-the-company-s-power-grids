import pytest
from django.urls import reverse
from django.utils.timezone import now
from powerline_app.models import PowerLine


@pytest.mark.django_db
class TestPowerLineModel:
    def test_create_powerline(self):
        """Тест создания объекта PowerLine"""
        powerline = PowerLine.objects.create(
            name="Test Line",
            voltage="medium",
            condition="Good",
            last_service_date=now().date(),
            coordinates={"lat": 56.4933, "lon": 85.0113},
        )
        assert PowerLine.objects.count() == 1
        assert powerline.name == "Test Line"
        assert powerline.voltage == "medium"

    def test_voltage_choices(self):
        """Тест недопустимого значения voltage"""
        with pytest.raises(ValueError):
            PowerLine.objects.create(
                name="Invalid Voltage Line",
                voltage="invalid_value",
                condition="Bad",
                last_service_date=now().date(),
                coordinates={"lat": 56.4933, "lon": 85.0113},
            )


@pytest.mark.django_db
class TestPowerLineViews:
    def test_powerline_map_view(self, client):
        """Тест представления powerline_map"""
        PowerLine.objects.create(
            name="Test Line",
            voltage="high",
            condition="Good",
            last_service_date=now().date(),
            coordinates={"lat": 56.4933, "lon": 85.0113},
        )
        url = reverse("powerline_map")
        response = client.get(url)
        assert response.status_code == 200
        assert "Test Line" in response.content.decode()

    def test_about_view(self, client):
        """Тест представления about"""
        url = reverse("about")
        response = client.get(url)
        assert response.status_code == 200
        assert "О проекте" in response.content.decode()


@pytest.mark.django_db
class TestPowerLineURLs:
    def test_urls(self, client):
        """Проверка доступности URL-ов"""
        urls = [reverse("powerline_map"), reverse("about")]
        for url in urls:
            response = client.get(url)
            assert response.status_code == 200
