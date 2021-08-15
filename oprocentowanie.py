#formuła na wysokość kredytu (1 + (inflacja.miesiąc + oprocentowanie) / 1200) * pozostała.kwota - stała.kwota.raty
#z terminala: wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację), kwota raty
kwota_pożyczki = float(input('Wprowadź początkową kwotę pożyczki: '))
oprocentowanie = float(input('Wprowadź wartość oprocentowania pożyczki (w skali roku): '))
kwota_raty = float(input('Wprowadź kwotę stałej raty miesięcznej: '))
#wartości inflacji w każdym miesiącu
inflacja_styczeń1 = 1.59282448436825
inflacja_luty1 = -0.453509101198007
inflacja_marzec1 = 2.32467171712441
inflacja_kwiecień1 = 1.26125440724877
inflacja_maj1 = 1.78252628571251
inflacja_czerwiec1 = 2.32938454145522
inflacja_lipiec1 = 1.50222984223283
inflacja_sierpień1 = 1.78252628571251
inflacja_wrzesień1 = 2.32884899407637
inflacja_październik1 = 0.616921348207244
inflacja_listopad1 = 2.35229588637833
inflacja_grudzień1 = 0.337779545187098
inflacja_styczeń2 = 1.57703524727525
inflacja_luty2 = -0.292781442607648
inflacja_marzec2 = 2.48619659017508
inflacja_kwiecień2 = 0.267110317834564
inflacja_maj2 = 1.41795267229799
inflacja_czerwiec2 = 1.05424326726375
inflacja_lipiec2 = 1.4805201044812
inflacja_sierpień2 = 1.57703524727525
inflacja_wrzesień2 = -0.0774206903147018
inflacja_październik2 = 1.16573339872354
inflacja_listopad2 = -0.404186717638335
inflacja_grudzień2 = 1.49970852083123
