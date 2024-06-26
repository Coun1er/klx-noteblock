class Settings:
    # Выбор сети в которой будем работать: opBNB, BNB, Manta
    network = "tBNB"

    # Торговые пары на которых будем торговать. Если пар больше 1, то на каждый трейд пара берется рандомно.
    trading_pairs = ["ETH-USDT", "BTC-USDT"]

    # В какую сторону вставать в позицию, если указаны обе стороны, то каждый раз берется рандомно.
    trading_positions_type = ["LONG", "SHORT"]

    # Сколько спим между трейдами.
    sl_between_trades = [10, 20]

    # Сколько спим внутри трейда между открытием и закрытием позиции.
    sl_inside_trades = [30, 60]

    # Плечё - минимальное = 2, максимальное = 100.
    leverage = 10

    # Процент от баланса который будет использоваться для фарминга.
    margin_percent = 0.2

    # Сумма usdt при которой фарминг остановится, минимум = 10.
    min_balance = 10


settings = Settings()
