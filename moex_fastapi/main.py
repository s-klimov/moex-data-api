from typing import Annotated

from fastapi import FastAPI, Query

from schemas import (
    TwoLastCandles,
    RsiValue,
)
from services import (
    get_hourly_candles,
    get_days_candles,
    calculate_rsi_14,
)

app = FastAPI()


@app.get("/api/candles/", response_model=TwoLastCandles)
async def get_candles(
    board: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[A-Z]+$", description="Код площадки")] = ...,
    code: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[[A-Z]|\d]+$", description="Тикер")] = ...,
):
    """Возвращает информацию по двум последним завершенным барам."""

    *_, prev_bar, last_bar, _ = await get_hourly_candles(board=board, code=code)
    return dict(
        prev_bar=prev_bar.dict(),
        last_bar=last_bar.dict(),
    )


@app.get("/api/rsi/", response_model=RsiValue)
async def get_rsi(
    board: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[A-Z]+$", description="Код площадки")] = ...,
    code: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[[A-Z]|\d]+$", description="Тикер")] = ...,
):
    """Возвращает значение индекса относительной силы RSI за прошедший торговый день."""

    candles = await get_days_candles(board, code)
    date, rsi_14 = await calculate_rsi_14(candles)
    return dict(
        date=date,
        rsi_14=rsi_14,
    )
