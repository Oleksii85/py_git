def money(ovoci, cina, kg):
    for ovoci, cina, kg in zip(ovoci, cina, kg):
        print("Витрати на овочі", ovoci, cina * kg, "грн")


money(["картопля", "цибуля", "морква", "буряк"], [12, 40, 55, 35], [2, 1, 0.4, 0.5])