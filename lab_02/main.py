def check_hydro_pressure(p_list, max_p=25.0):
    max_pressure = 0
    for pressure in p_list:
        if pressure < 0:
            continue
        if pressure > max_pressure:
            max_pressure = pressure
    if max_pressure > max_p:
        status = "Опасно!"
    else:
        status = "Безопасно"
    print(f"Максимальное давление: {max_pressure}")
    print(f"Статус: {status}")
    return status
p_list = [12.5, 18.3, -2.0, 27.1, -11.4]
check_hydro_pressure(p_list)