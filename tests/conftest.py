import pytest

from finam_trade_api.candles import IntraDayCandle, Decimal


@pytest.fixture(scope="module")
def intra_day_candles():
    yield [
        IntraDayCandle(
            open=Decimal(num=7935, scale=2),
            close=Decimal(num=7931, scale=2),
            high=Decimal(num=7938, scale=2),
            low=Decimal(num=7916, scale=2),
            volume=5949,
            timestamp="2024-02-07T06:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7932, scale=2),
            close=Decimal(num=794, scale=1),
            high=Decimal(num=7942, scale=2),
            low=Decimal(num=7919, scale=2),
            volume=14372,
            timestamp="2024-02-07T07:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7941, scale=2),
            close=Decimal(num=7965, scale=2),
            high=Decimal(num=7974, scale=2),
            low=Decimal(num=7939, scale=2),
            volume=25898,
            timestamp="2024-02-07T08:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7964, scale=2),
            close=Decimal(num=7992, scale=2),
            high=Decimal(num=7994, scale=2),
            low=Decimal(num=7955, scale=2),
            volume=29831,
            timestamp="2024-02-07T09:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7992, scale=2),
            close=Decimal(num=7989, scale=2),
            high=Decimal(num=7998, scale=2),
            low=Decimal(num=7978, scale=2),
            volume=16577,
            timestamp="2024-02-07T10:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7987, scale=2),
            close=Decimal(num=7988, scale=2),
            high=Decimal(num=7999, scale=2),
            low=Decimal(num=7972, scale=2),
            volume=21600,
            timestamp="2024-02-07T11:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7987, scale=2),
            close=Decimal(num=7983, scale=2),
            high=Decimal(num=7995, scale=2),
            low=Decimal(num=7979, scale=2),
            volume=6374,
            timestamp="2024-02-07T12:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7982, scale=2),
            close=Decimal(num=7978, scale=2),
            high=Decimal(num=7992, scale=2),
            low=Decimal(num=7962, scale=2),
            volume=14719,
            timestamp="2024-02-07T13:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7978, scale=2),
            close=Decimal(num=7958, scale=2),
            high=Decimal(num=7994, scale=2),
            low=Decimal(num=7955, scale=2),
            volume=22792,
            timestamp="2024-02-07T14:00:00Z",
        ),
        IntraDayCandle(
            open=Decimal(num=7958, scale=2),
            close=Decimal(num=7982, scale=2),
            high=Decimal(num=8002, scale=2),
            low=Decimal(num=7956, scale=2),
            volume=29530,
            timestamp="2024-02-07T15:00:00Z",
        ),
    ]
