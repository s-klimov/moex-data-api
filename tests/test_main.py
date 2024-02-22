from fastapi.testclient import TestClient
from finam_trade_api.candles import CandlesClient

from main import app


client = TestClient(app)


fixture_day_candles = {}


def test_read_main(monkeypatch, intra_day_candles):
    async def mockreturn(*_):
        return intra_day_candles

    monkeypatch.setattr(CandlesClient, "get_in_day_candles", mockreturn)

    response = client.get("/api/candles/?board=FUT&code=BRH4")
    assert response.status_code == 200
    assert response.json() == {
        "prev_bar": {"high": 79.92, "low": 79.62, "timestamp": "2024-02-07T13:00:00Z"},
        "last_bar": {"high": 79.94, "low": 79.55, "timestamp": "2024-02-07T14:00:00Z"},
    }
