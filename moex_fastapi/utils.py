import os
from datetime import datetime as dt, timedelta
from stockstats import wrap
from typing import List, Mapping, Callable, Any

import pandas as pd

from finam_trade_api import Client
from finam_trade_api.candles import (
    IntraDayCandlesRequestModel,
    IntraDayInterval,
    IntraDayCandle,
    DayCandlesRequestModel,
    DayInterval,
)

MOEX_ACCESS_TOKEN = os.getenv("moex_access_token")


async def get_hourly_candles(board: str, code: str) -> List[IntraDayCandle]:
    hours = 24 * 7

    client = Client(MOEX_ACCESS_TOKEN)
    interval_from = (dt.now() - timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M:%S")
    params = IntraDayCandlesRequestModel(
        securityBoard=board,
        securityCode=code,
        timeFrame=IntraDayInterval.H1,
        intervalFrom=interval_from,
        count=hours,
    )
    return await client.candles.get_in_day_candles(params)


class NumberCandle:

    def __init__(self, candle: IntraDayCandle):
        self.__candle = candle

    def to_json(self) -> Mapping:
        get_number: Callable[[Any, Any], float | Any] = lambda num, scale: num / (10**scale)

        return {
            "high": get_number(self.__candle.high.num, self.__candle.high.scale),
            "low": get_number(self.__candle.low.num, self.__candle.low.scale),
            "timestamp": self.__candle.timestamp,
        }


async def get_days_candles(board: str, code: str):

    days = 180

    client = Client(MOEX_ACCESS_TOKEN)
    interval_from = (dt.now() - timedelta(days=days)).date().strftime("%Y-%m-%d")
    params = DayCandlesRequestModel(
        securityBoard=board,
        securityCode=code,
        timeFrame=DayInterval.D1,
        intervalFrom=interval_from,
        count=days,
    )
    return await client.candles.get_day_candles(params)


async def calculate_rsi_14(candles) -> [str, float]:

    df = pd.DataFrame(
        [
            (
                candle.date,
                candle.high.num / (10**candle.high.scale),
                candle.low.num / (10**candle.low.scale),
                candle.open.num / (10**candle.open.scale),
                candle.close.num / (10**candle.close.scale),
                candle.volume,
            )
            for candle in candles
            if candle.date != dt.today().strftime("%Y-%m-%d")
        ],
        columns=["date", "high", "low", "open", "close", "volume"],
    )
    rsi = wrap(df)["rsi_14"]

    return rsi.index[-1], rsi.iloc[-1]
