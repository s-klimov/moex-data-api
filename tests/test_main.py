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
            "close": intra_day_candles[-3].close.num / 10 ** intra_day_candles[-3].close.scale,
            "high": intra_day_candles[-3].high.num / 10 ** intra_day_candles[-3].high.scale,
            "low": intra_day_candles[-3].low.num / 10 ** intra_day_candles[-3].low.scale,
            "open": intra_day_candles[-3].open.num / 10 ** intra_day_candles[-3].open.scale,
            "timestamp": intra_day_candles[-3].timestamp,
            "volume": intra_day_candles[-3].volume,
        },
        "last_bar": {
            "close": intra_day_candles[-2].close.num / 10 ** intra_day_candles[-2].close.scale,
            "high": intra_day_candles[-2].high.num / 10 ** intra_day_candles[-2].high.scale,
            "low": intra_day_candles[-2].low.num / 10 ** intra_day_candles[-2].low.scale,
            "open": intra_day_candles[-2].open.num / 10 ** intra_day_candles[-2].open.scale,
            "timestamp": intra_day_candles[-2].timestamp,
            "volume": intra_day_candles[-2].volume,
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
