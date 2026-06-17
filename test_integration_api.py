import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_list_bens():
    """Verifica se a listagem de bens retorna status 200."""
    response = client.get("/api/v1/bem/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_api_report_excel():
    """Verifica se o endpoint de exportação Excel funciona."""
    response = client.get("/api/v1/relatorio/exportar?formato=xlsx")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

def test_api_report_pdf():
    """Verifica se o endpoint de exportação PDF funciona."""
    response = client.get("/api/v1/relatorio/exportar?formato=pdf")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"

def test_api_stats_categoria():
    """Verifica o formato das estatísticas por categoria."""
    response = client.get("/api/v1/bem/stats/categoria")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert len(data[0]) == 2 # [nome, total]

def test_api_stats_status():
    """Verifica o formato das estatísticas por status."""
    response = client.get("/api/v1/bem/stats/status")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert len(data[0]) == 2 # [status, total]
