from datetime import timezone

from faker import Factory as FakerFactory
from finam_trade_api.candles import IntraDayCandle, Decimal

faker = FakerFactory.create()

MIN_NUM, MAX_NUM = 1_000, 10_000
MIN_SCALE, MAX_SCALE = 0, 2


class IntraDayCandleFixture:
    """Фикстура внутридневных часовых баров"""

    def __init__(self):
        self.__candle = IntraDayCandle(
            open=self.__get_random_decimal(),
            close=self.__get_random_decimal(),
            high=self.__get_random_decimal(),
            low=self.__get_random_decimal(),
            volume=self.__get_random_int(),
            timestamp=self.__get_random_datetime(),
        )

    @staticmethod
    def __get_random_decimal() -> Decimal:
        return Decimal(num=faker.random_int(MIN_NUM, MAX_NUM), scale=faker.random_int(MIN_SCALE, MAX_SCALE))

    @staticmethod
    def __get_random_int() -> int:
        return faker.random_int(MIN_NUM, MAX_NUM)

    @staticmethod
    def __get_random_datetime() -> str:
        # FIXME время каждого бара должно быть в формате HH:00:00Z
        return faker.date_time(tzinfo=timezone.utc).isoformat()

    @property
    def candle(self):
        return self.__candle
