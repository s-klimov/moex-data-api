from decimal import Decimal

from pydantic import BaseModel


class FancyDecimal:
    """
    Класс валидатора, который переводит встроенный в словарь {num: ..., scale: ...} в человекочитаемое десятичное число
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: dict) -> Decimal:
        return v["num"] / (10 ** v["scale"])


class IntraDayNumericCandle(BaseModel):
    """Класс свечи с человекочитаемыми десятичными числами"""

    open: FancyDecimal
    close: FancyDecimal
    high: FancyDecimal
    low: FancyDecimal
    volume: int
    timestamp: str
