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
styczeń1_spłata = (1 + (inflacja_styczeń1 + oprocentowanie) / 1200) * kwota_pożyczki - kwota_raty
luty1_spłata = (1 + (inflacja_luty1 + oprocentowanie) / 1200) * styczeń1_spłata - kwota_raty
marzec1_spłata = (1 + (inflacja_marzec1 + oprocentowanie) / 1200) * luty1_spłata - kwota_raty
kwiecień1_spłata = (1 + (inflacja_kwiecień1 + oprocentowanie) / 1200) * marzec1_spłata - kwota_raty
maj1_spłata = (1 + (inflacja_maj1 + oprocentowanie) / 1200) * kwiecień1_spłata - kwota_raty
czerwiec1_spłata = (1 + (inflacja_czerwiec1 + oprocentowanie) / 1200) * maj1_spłata - kwota_raty
lipiec1_spłata = (1 + (inflacja_lipiec1 + oprocentowanie) / 1200) * czerwiec1_spłata - kwota_raty
sierpień1_spłata = (1 + (inflacja_sierpień1 + oprocentowanie) / 1200) * lipiec1_spłata - kwota_raty
wrzesień1_spłata = (1 + (inflacja_wrzesień1 + oprocentowanie) / 1200) * sierpień1_spłata - kwota_raty
październik1_spłata = (1 + (inflacja_październik1 + oprocentowanie) / 1200) * wrzesień1_spłata - kwota_raty
listopad1_spłata = (1 + (inflacja_listopad1 + oprocentowanie) / 1200) * październik1_spłata - kwota_raty
grudzień1_spłata = (1 + (inflacja_grudzień1 + oprocentowanie) / 1200) * listopad1_spłata - kwota_raty
styczeń2_spłata = (1 + (inflacja_styczeń2 + oprocentowanie) / 1200) * grudzień1_spłata - kwota_raty
luty2_spłata = (1 + (inflacja_luty2 + oprocentowanie) / 1200) * styczeń2_spłata - kwota_raty
marzec2_spłata = (1 + (inflacja_marzec2 + oprocentowanie) / 1200) * luty2_spłata - kwota_raty
kwiecień2_spłata = (1 + (inflacja_kwiecień2 + oprocentowanie) / 1200) * marzec2_spłata - kwota_raty
maj2_spłata = (1 + (inflacja_maj2 + oprocentowanie) / 1200) * kwiecień2_spłata - kwota_raty
czerwiec2_spłata = (1 + (inflacja_czerwiec2 + oprocentowanie) / 1200) * maj2_spłata - kwota_raty
lipiec2_spłata = (1 + (inflacja_lipiec2 + oprocentowanie) / 1200) * czerwiec2_spłata - kwota_raty
sierpień2_spłata = (1 + (inflacja_sierpień2 + oprocentowanie) / 1200) * lipiec2_spłata - kwota_raty
wrzesień2_spłata = (1 + (inflacja_wrzesień2 + oprocentowanie) / 1200) * sierpień2_spłata - kwota_raty
październik2_spłata = (1 + (inflacja_październik2 + oprocentowanie) / 1200) * wrzesień2_spłata - kwota_raty
listopad2_spłata = (1 + (inflacja_listopad2 + oprocentowanie) / 1200) * październik2_spłata - kwota_raty
grudzień2_spłata = (1 + (inflacja_grudzień2 + oprocentowanie) / 1200) * listopad2_spłata - kwota_raty
print(f'Styczeń 1. roku: Twoja pozostała kwota kredytu to {styczeń1_spłata}, to {kwota_pożyczki - styczeń1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Luty 1. roku: Twoja pozostała kwota kredytu to {luty1_spłata}, to {styczeń1_spłata - luty1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Marzec 1. roku: Twoja pozostała kwota kredytu to {marzec1_spłata}, to {luty1_spłata - marzec1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Kwiecień 1. roku: Twoja pozostała kwota kredytu to {kwiecień1_spłata}, to {marzec1_spłata - kwiecień1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Maj 1. roku: Twoja pozostała kwota kredytu to {maj1_spłata}, to {kwiecień1_spłata - maj1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Czerwiec 1. roku: Twoja pozostała kwota kredytu to {czerwiec1_spłata}, to {maj1_spłata - czerwiec1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Lipiec 1. roku: Twoja pozostała kwota kredytu to {lipiec1_spłata}, to {czerwiec1_spłata - lipiec1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Sierpień 1. roku: Twoja pozostała kwota kredytu to {sierpień1_spłata}, to {lipiec1_spłata - sierpień1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Wrzesień 1. roku: Twoja pozostała kwota kredytu to {wrzesień1_spłata}, to {sierpień1_spłata - wrzesień1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Październik 1. roku: Twoja pozostała kwota kredytu to {październik1_spłata}, to {wrzesień1_spłata - październik1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Listopad 1. roku: Twoja pozostała kwota kredytu to {listopad1_spłata}, to {październik1_spłata - listopad1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Grudzień 1. roku: Twoja pozostała kwota kredytu to {grudzień1_spłata}, to {listopad1_spłata - grudzień1_spłata} mniej niż w poprzednim miesiącu. \n'
f'Styczeń 2. roku: Twoja pozostała kwota kredytu to {styczeń2_spłata}, to {grudzień1_spłata - styczeń2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Luty 2. roku: Twoja pozostała kwota kredytu to {luty2_spłata}, to {styczeń2_spłata - luty2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Marzec 2. roku: Twoja pozostała kwota kredytu to {marzec2_spłata}, to {luty2_spłata - marzec2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Kwiecień 2. roku: Twoja pozostała kwota kredytu to {kwiecień2_spłata}, to {marzec2_spłata - kwiecień2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Maj 2. roku: Twoja pozostała kwota kredytu to {maj2_spłata}, to {kwiecień2_spłata - maj2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Czerwiec 2. roku: Twoja pozostała kwota kredytu to {czerwiec2_spłata}, to {maj2_spłata - czerwiec2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Lipiec 2. roku: Twoja pozostała kwota kredytu to {lipiec2_spłata}, to {czerwiec2_spłata - lipiec2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Sierpień 2. roku: Twoja pozostała kwota kredytu to {sierpień2_spłata}, to {lipiec2_spłata - sierpień2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Wrzesień 2. roku: Twoja pozostała kwota kredytu to {wrzesień2_spłata}, to {sierpień2_spłata - wrzesień2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Październik 2. roku: Twoja pozostała kwota kredytu to {październik2_spłata}, to {wrzesień2_spłata - październik2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Listopad 2. roku: Twoja pozostała kwota kredytu to {listopad2_spłata}, to {październik2_spłata - listopad2_spłata} mniej niż w poprzednim miesiącu. \n'
f'Grudzień 2. roku: Twoja pozostała kwota kredytu to {grudzień2_spłata}, to {listopad2_spłata - grudzień2_spłata} mniej niż w poprzednim miesiącu.')
