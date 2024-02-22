# Получаем статистику торговой площадки ММВБ (moex)
API получения информации о барах и индексе относительной силы для проведения технического анализа

## Приступая к работе

Следуя этим инструкциям, вы получите копию проекта, которая будет запущена на вашем локальном компьютере для целей разработки и тестирования. Примечания о том, как развернуть проект в действующей системе, см. в разделе Развертывание.

### Предпосылки

Клонируйте проект на локальный компьютер

```commandline
git clone https://github.com/s-klimov/moex-data-api.git
```

Для работы сервиса у вас должны быть установлены:
* python версии 3.10 и выше
* poetry версии 1.4.x 

### Развертывание

1. Установите зависимости
```commandline
poetry install
```
2. Активируйте локальное окружение
```commandline
poetry shell
```
4. Переименуйте файл .env.dist в .env и заполните его параметрами подключения.  

Назначение параметров:
* moex_access_token -- токен для доступа к API биржи. Достаточно токена с правами только на получения данных.

Пример:  
* moex_access_token=CGHP06mYARoQqbS-zCtGuKilWljdqILPOW4ZhBOUK1z0

## Запуск проекта

### Запустите сервер
> Проект запускается из папки moex_fastapi
```commandline
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

### Выполните тестирование
> Модульные тесты запускаются из корневой папки проекта  
```commandline
pytest -v -p no:warnings
```

## Используемый стек

* [fastapi](https://fastapi.tiangolo.com/) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
* [finam-trade-api](https://pypi.org/project/finam-trade-api/) - Асинхронный REST-клиент для API Finam
* [poetry](https://python-poetry.org/docs/) - Dependency Management

## Авторы

* **Sergei Klimov** - [repos](https://github.com/s-klimov/)

## Лицензия

Проект разработан под лицензией MIT - см. [LICENSE](LICENSE) файл для подробного изучения.

## Благодарности

* Автору идеи - моей супруге Анне!
* Автору пакета [finam-trade-api](https://pypi.org/project/finam-trade-api/) - [Boyara](https://github.com/DBoyara/FinamTradeApiPy/commits?author=DBoyara)
