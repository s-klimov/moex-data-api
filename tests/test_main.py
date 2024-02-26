import pytest
from finam_trade_api.candles import CandlesClient


@pytest.mark.parametrize("route", ["/api/candles/"])
def test_get_candles(client, route, monkeypatch, intra_day_candles):
    """Тестируем ендпойнт /api/candles/"""

    async def mockreturn(*_):
        return intra_day_candles

    monkeypatch.setattr(CandlesClient, "get_in_day_candles", mockreturn)

    response = client.get(route, params={"board": "FUT", "code": "BRH4"})
    assert response.status_code == 200
    assert response.json() == {
        "prev_bar": {
            "close": 79.78,
            "high": 79.92,
            "low": 79.62,
            "open": 79.82,
            "timestamp": "2024-02-07T13:00:00Z",
            "volume": 14719,
        },
        "last_bar": {
            "close": 79.58,
            "high": 79.94,
            "low": 79.55,
            "open": 79.78,
            "timestamp": "2024-02-07T14:00:00Z",
            "volume": 22792,
        },
    }


@pytest.mark.parametrize("route", ["/api/rsi/"])
def test_get_rsi(client, route, monkeypatch, daily_candles):
    """Тестируем ендпойнт /api/rsi/"""

    async def mockreturn(*_):
        return daily_candles

    monkeypatch.setattr(CandlesClient, "get_day_candles", mockreturn)

    response = client.get(route, params={"board": "TQBR", "code": "LKOH"})
    assert response.status_code == 200
    assert response.json() == {"date": "2024-02-22", "rsi_14": 45.141565255351416}
