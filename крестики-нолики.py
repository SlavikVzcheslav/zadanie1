print("Игра крестики-нолики")
hod = 0
massiv = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def vivod_massiv(m):
    print("  0 1 2")
    o = 0
    for row in m:
        print(str(o) + " ", end="")
        o = o + 1
        for i in row:
            print(i, end=" ")
        print()

def pobeda(m, p):
    # Горизонтали
    for i in m:
        if i[0] == p and i[1] == p and i[2] == p:
            return True
    # Вертикали
    for i in range(3):
        if m[0][i] == p and m[1][i] == p and m[2][i] == p:
            return True
    # Диагонали
    if m[0][0] == p and m[1][1] == p and m[2][2] == p:
        return True
    if m[0][2] == p and m[1][1] == p and m[2][0] == p:
        return True
    return False

vivod_massiv(massiv)

while True:
    hod += 1
    if hod % 2 == 0:
        player = "O"
    else:
        player = "X"
    print("Ходит игрок " + player)
    while True:
        gorizont = int(input("Горизонталь (0-2): "))
        vertikal = int(input("Вертикаль (0-2): "))
        if massiv[vertikal][gorizont] == ".":
            massiv[vertikal][gorizont] = player
            break
        else:
            print("Там уже занято")

    vivod_massiv(massiv)

    if pobeda(massiv, player):
        print("Победа игрока " + player)
        break
    if hod == 9:
        print("Ничья!")
        break
