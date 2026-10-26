def analyze_phases(phase_loads):
    """
    Вычисляет суммарные нагрузки фаз.
    """
    return {phase: sum(values) for phase, values in phase_loads.items()}


def detect_imbalance(phase_loads, max_diff=15.0):
    """
    Находит максимальное расхождение средних токов.
    Возвращает кортеж (is_imbalanced, max_diff).
    """
    averages = {
        phase: sum(values) / len(values)
        for phase, values in phase_loads.items()
    }

    difference = max(averages.values()) - min(averages.values())
    is_imbalanced = difference > max_diff

    return is_imbalanced, difference


def get_last_n_samples(phase_loads, n=5):
    """
    Формирует словарь с n последними измерениями с помощью срезов [-n:].
    """
    return {
        phase: values[-n:]
        for phase, values in phase_loads.items()
    }


if __name__ == '__main__':
    test_loads = {
        'A': [110, 115, 120, 118],
        'B': [95, 98, 92, 96],
        'C': [140, 145, 150, 148]
    }
    print(analyze_phases(test_loads))
    print(detect_imbalance(test_loads))
    print(get_last_n_samples(test_loads, n=3))