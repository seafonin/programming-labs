import sys
from variant3_mod import *

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    loads = {
        'A': [110, 115, 120, 118],
        'B': [95, 98, 92, 96],
        'C': [140, 145, 150, 148]
    }

    totals = analyze_phases(loads)
    is_imbalanced, max_diff = detect_imbalance(loads, max_diff=15.0)
    last_n = get_last_n_samples(loads, n=n)

    print("=== МОНИТОРИНГ ТРЕХФАЗНОЙ СЕТИ ===")
    print(f"Суммарные токи фаз: А={totals['A']}А, "
          f"В={totals['B']}А, С={totals['C']}А")

    status = "ДА" if is_imbalanced else "НЕТ"
    print(f"Перекос фаз: {status} "
          f"(макс. расхождение: {max_diff:.2f} А)")

    print(f"Свежие замеры (срез [-{n}:]): {last_n}")

if __name__ == '__main__':
    main()