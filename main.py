print("Формула счастья")



#определяет уровень самооценки по мотивам формулы У.Джеймса

def formula_of_happiness(uspex, zhelaniye):
    while zhelaniye == 0:
        print("Вы достигли нирваны")
        break
    else:
        happiness = uspex/zhelaniye
        return happiness


print()
print("Оцените уровень достигнутого от 1 до 10")
uspex = input()
uspex = int(uspex)
print("Оцените уровень притязаний от 1 до 10")
zhelaniye = input()
zhelaniye = int(zhelaniye)

resultat = formula_of_happiness(uspex, zhelaniye)



if (resultat < 1):
    print("У вас завышенный уровень притязаний. Вы можете доситчь счастья, увеличивая свой успех либо отказываясь от своих притязаний.")
if (resultat > 1):
    print("У вас заниженный уровень притязаний. Вы можете доситчь счастья, увеличивая свои притязания.")
if (resultat == 1):
    print("У вас адекватная самооценка")
