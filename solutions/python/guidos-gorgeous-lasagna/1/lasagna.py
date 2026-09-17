EXPECTED_BAKE_TIME = 40    # tempo total de forno, em minutos


def bake_time_remaining(elapsed_bake_time):
    """Calcula quanto tempo ainda falta para a lasanha assar.

    Args:
        elapsed_bake_time: minutos que a lasanha já passou no forno.

    Returns:
        minutos restantes até completar o tempo esperado.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calcula o tempo de preparo da lasanha.

    Cada camada leva 2 minutos.

    Args:
        number_of_layers: quantidade de camadas da lasanha.

    Returns:
        tempo total de preparo, em minutos.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula o tempo total gasto (preparo + forno).

    Args:
        number_of_layers: quantidade de camadas da lasanha.
        elapsed_bake_time: minutos que a lasanha já passou no forno.

    Returns:
        soma do tempo de preparo com o tempo já no forno, em minutos.
    """
    total = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total


# Testes rápidos
print(bake_time_remaining(30))                    # 10
print(preparation_time_in_minutes(3))             # 6
print(elapsed_time_in_minutes(3, 20))             # 26
    