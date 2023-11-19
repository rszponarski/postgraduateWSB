# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających w centrum
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
centrum = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
krzyki = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma zbiorów ->              |
# cześć wspólna zbiorów   ->   &
# różnica zbiorów  ->          -
# różnica symetryczna  ->      ^

# ile osob chorowalo w ostatnim roku w centrum
print(f'Chorzy w ostatnim roku w centrum to {chorzy_rok & centrum}')
print(f'Liczba chorych w ostatnim roku: {len(chorzy_rok & centrum)}')

# Kazdy kto chorowal w ostatnim miesiacu musial byc w bazie danych za rok
# Sprawdzmy:
if len(chorzy_rok & centrum) == 0:
    print("Jest ok")
else:
    print("Blad w danych")
    print(f'{chorzy_miesiac - chorzy_rok}')
print(krzyki)
if len(centrum & krzyki) > 0:
    print("error")
    print(f'{centrum & krzyki} niewlasciwy pesel')
    krzyki -= krzyki & centrum
    print(krzyki)