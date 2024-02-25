from typing import Annotated

from fastapi import FastAPI, Query

from schemas import IntraDayNumericCandle
from services import (
    get_hourly_candles,
    get_days_candles,
    calculate_rsi_14,
)

app = FastAPI()


@app.get("/api/candles/")  # TODO Добавить аннотация для возвращаемого типа в response
async def get_candles(
    board: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[A-Z]+$", description="Код площадки")] = ...,
    code: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[[A-Z]|\d]+$", description="Тикер")] = ...,
):
    """Возвращает информацию по двум последним завершенным свечам."""

    *_, prev_bar, last_bar, _ = await get_hourly_candles(board=board, code=code)
    return {
        "prev_bar": IntraDayNumericCandle(**prev_bar.dict()).dict(),
        "last_bar": IntraDayNumericCandle(**last_bar.dict()).dict(),
    }


@app.get("/api/rsi/")  # TODO Добавить аннотация для возвращаемого типа в response
async def get_rsi(
    board: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[A-Z]+$", description="Код площадки")] = ...,
    code: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[[A-Z]|\d]+$", description="Тикер")] = ...,
):
    """Возвращает значение индекса относительной силы RSI за прошедший торговый день."""

    candles = await get_days_candles(board, code)
    date, rsi_14 = await calculate_rsi_14(candles)
    return {"date": date, "rsi_14": rsi_14}
