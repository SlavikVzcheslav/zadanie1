temperature = int(input("Какая будет температура?(в градусах) "))
# is_rainy = int(input("Какая будет температура?(в градусах)"))
# is_raining_healvy =  int(input("Какая будет температура?(в градусах)"))
if temperature < 30 and temperature > 20:
    is_rainy = int(input("Будут осадки, нажмите 1, если да; в противном случае 0 "))
    if is_rainy == 0:
        print("Футболка и шорты")
    else:
        print("Футболка и шорты и дождевик")
else:
    if temperature > 0:
        is_rainy = int(input("Будут осадки, нажмите 1, если да; в противном случае 0 "))
        if is_rainy == 0:
            print("Пальто")
        else:
            is_raining_healvy =  int(input("Будут сильные осадки, нажмите 1, если да; в противном случае 0"))
            if is_raining_healvy == 0:
                print("Пальто и дождевик")
            else:
                print("Пальто, резиновые сапоги и зонт")
    else:
        print("Пуховик")