import circle
import square
import triangle

FIGS = {
    'circle': {'module': circle, 'params': 1},
    'square': {'module': square, 'params': 1},
    'triangle': {'module': triangle, 'params': 3}
}

FUNCS = ['perimeter', 'area']


def calc(fig, func, size):
    if fig not in FIGS:
        raise ValueError(
            f"Фигура '{fig}' недоступна. Доступные фигуры: "
            f"{list(FIGS.keys())}"
        )
    if func not in FUNCS:
        raise ValueError(
            f"Функция '{func}' недоступна. Доступные функции: {FUNCS}"
        )

    module = FIGS[fig]['module']
    func_to_call = getattr(module, func)

    expected_params = FIGS[fig]['params']
    if len(size) != expected_params:
        raise ValueError(
            f"Для фигуры '{fig}' требуется {expected_params} параметр(ов), но "
            f"было передано {len(size)}"
        )

    result = func_to_call(*size)
    print(
        f'{func.capitalize()} of {fig} with size(s) {size} is {result}'
    )
    return result
