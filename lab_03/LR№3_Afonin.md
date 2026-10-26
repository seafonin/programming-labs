# Отчет по лабораторной работе №3
## по дисциплине «Программирование на языке Python»

**Проверил:** доц., к.н Ситников Д.В.  
**Разработал:** Студент гр. УТС-251т Афонин С.А.  

---

## Ход работы

### Задание
**Вариант 3. Балансировка трехфазной электросети цеха.**  
Разработать пользовательский модуль `variant3_mod.py` для вычисления суммарных нагрузок фаз, поиска максимального расхождения средних токов и формирования срезов последних измерений. В главном скрипте `main.py` реализовать динамическое чтение параметров из командной строки `sys.argv`.

### Решение

#### Код модуля `variant3_mod.py`:
```python
def analyze_phases(phase_loads):
    return {phase: sum(values) for phase, values in phase_loads.items()}

def detect_imbalance(phase_loads, max_diff=15.0):
    averages = {phase: sum(values) / len(values) for phase, values in phase_loads.items()}
    difference = max(averages.values()) - min(averages.values())
    is_imbalanced = difference > max_diff
    return is_imbalanced, difference

def get_last_n_samples(phase_loads, n=5):
    return {phase: values[-n:] for phase, values in phase_loads.items()}
```

#### Код главного скрипта `main.py`:
```python
import sys
from variant3_mod import analyze_phases, detect_imbalance, get_last_n_samples

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    loads = {
        'A':,
        'B':,
        'C': [140, 145, 150, 148]
    }
    totals = analyze_phases(loads)
    is_imbalanced, max_diff = detect_imbalance(loads, max_diff=15.0)
    last_n = get_last_n_samples(loads, n=n)
    
    print("=== МОНИТОРИНГ ТРЕХФАЗНОЙ СЕТИ ===")
    print(f"Суммарные токи фаз: А={totals['A']}А, В={totals['B']}А, С={totals['C']}А")
    status = "ДА" if is_imbalanced else "НЕТ"
    print(f"Перекос фаз: {status} (макс. расхождение: {max_diff:.2f} А)")
    print(f"Свежие замеры (срез [-{n}:]): {last_n}")

if __name__ == '__main__':
    main()
```

**Вывод программы в консоль:**
```text
=== МОНИТОРИНГ ТРЕХФАЗНОЙ СЕТИ ===
Суммарные токи фаз: А=463А, В=381А, С=583А
Перекос фаз: ДА (макс. расхождение: 50.50 А)
Свежие замеры (срез [-3:]): {'A':, 'B':, 'C':}
```

---

## Вывод
В ходе выполнения работы изучены принципы модульной архитектуры в Python, правила применения системного модуля `sys` и списка аргументов `sys.argv`. Закреплены практические навыки работы со списками, кортежами, ассоциативными словарями и синтаксисом срезов с отрицательными индексами.
