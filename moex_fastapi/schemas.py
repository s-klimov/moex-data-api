from decimal import Decimal

from pydantic import BaseModel, validator, Field


class IntraDayNumericCandle(BaseModel):
    """Информация о баре"""

    open: Decimal = Field(description="Цена открытия")
    close: Decimal = Field(description="Цена закрытия")
    high: Decimal = Field(description="Максимум цены")
    low: Decimal = Field(description="Минимум цены")
    volume: int = Field(description="Объем сделок")
    timestamp: str = Field(description="Дата и время бара")

    @validator("open", "close", "high", "low", pre=True)
    def validate_decimal(cls, v: dict):
        return v["num"] / (10 ** v["scale"])


class TwoLastCandles(BaseModel):
    """Два последних завершенных бара"""

    prev_bar: IntraDayNumericCandle = Field(description="Предпоследний бар")
    last_bar: IntraDayNumericCandle = Field(description="Последний бар")


class RsiValue(BaseModel):
    """Значение индекса относительной силы RSI"""

    date: str = Field(description="Дата торгового дня")
    rsi_14: float = Field(description="Значение индекса относительной силы RSI за последние 14 дней")
