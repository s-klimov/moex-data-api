from typing import Annotated

from fastapi import FastAPI, Query

from utils import (
    get_hourly_candles,
    NumberCandle,
    get_days_candles,
    calculate_rsi_14,
)

app = FastAPI()


@app.get("/api/candles/")
async def get_candles(
    board: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[A-Z]+$")] = ...,
    code: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[[A-Z]|\d]+$")] = ...,
):
    *_, prev_bar, last_bar, _ = await get_hourly_candles(board=board, code=code)
    return {
        "prev_bar": NumberCandle(prev_bar).to_json(),
        "last_bar": NumberCandle(last_bar).to_json(),
    }


@app.get("/api/rsi/")
async def get_rsi(
    board: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[A-Z]+$")] = ...,
    code: Annotated[str, Query(min_length=3, max_length=50, pattern=r"^[[A-Z]|\d]+$")] = ...,
):
    candles = await get_days_candles(board, code)
    date, rsi_14 = await calculate_rsi_14(candles)
    return {"date": date, "rsi_14": rsi_14}
