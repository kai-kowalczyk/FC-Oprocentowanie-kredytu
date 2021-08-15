#formuła na wysokość kredytu (1 + (inflacja.miesiąc + oprocentowanie) / 1200) * pozostała.kwota - stała.kwota.raty
#z terminala: wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację), kwota raty
kwota_pożyczki = float(input('Wprowadź początkową kwotę pożyczki: '))
oprocentowanie = float(input('Wprowadź wartość oprocentowania pożyczki: '))
kwota_raty = float(input('Wprowadź kwotę stałej raty miesięcznej: '))
