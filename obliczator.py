# coding=UTF-8

import colorama
import time
colorama.init()

while True:
  print('\n')
  print('\033[36m'+'OBLICZATOR'+'\033[39m')
  time.sleep(2)
  print('aby obliczyć pole trójkąta wpisz 1')
  time.sleep(0.25)
  print('aby obliczyć pole trapezu wpisz 2')
  time.sleep(0.25)
  print('aby obliczyć pole koła wpisz 3')
  time.sleep(0.25)
  WYBOR = input('TWÓJ WYBÓR: ')
  if int(WYBOR) == 1:
    print('wybrałeś/wybrałaś obliczator pola trójkąta')
    time.sleep(2)
    print('\033[31m' + 'wczytywanie kodów atomowych...' + '\033[39m')
    time.sleep(3)
    a = input('podaj bok: ')
    time.sleep(0.5)
    h = input('podaj wysokość: ')
    wynik = int(a) * int(h) / 2
    time.sleep(2)
    print('wynik: ''\033[32m' + str(wynik) + '\033[39m')
    time.sleep(1)
    print('czy chcesz zamknąć program? [t/n]')
    time.sleep(0.5)
    zamykanie_1 = input()
    if zamykanie_1 == 't':
      break
    elif zamykanie_1 == 'n':
      continue
    else:
          print('nie to miałes napisac ale ok (zamykam)')
          break
  elif int(WYBOR) == 2:
    print('wybraleś/wybralaś obliczator pola trapezu')
    time.sleep(2)
    print('\033[31m' + 'wczytywanie kodow atomowych...' + '\033[39m')
    time.sleep(3)
    a2 = input('podaj pierwsza podstawe: ')
    time.sleep(0.5)
    b2 = input('podaj drugą podstawe: ')
    time.sleep(0.5)
    h2 = input('podaj wysokosc: ')
    wynik2 = (int(a2) + int(b2)) * int(h2) / 2
    time.sleep(2)
    print('wynik: ''\033[32m' + str(wynik2) + '\033[39m')
    time.sleep(1)
    print('czy chcesz zamknąć program? [t/n]')
    time.sleep(0.5)
    zamykanie_2 = input()
    if zamykanie_2 == 't':
      break
    elif zamykanie_2 == 'n':
      continue
    else:
      print('nie to miałeś napisać ale ok (zamykam)')
      break
  elif int(WYBOR) == 3:
    print('wybrales/wybralas obliczator pola kola')
    time.sleep(2)
    print('\033[31m' + 'wczytywanie kodow atomowych...' + '\033[39m')
    time.sleep(3)
    r = input('podaj promien: ')
    wynik3 = 3.14 * int(r)**2
    time.sleep(2)
    print('wynik: ' + '\033[32m' + str(wynik3) + '\033[39m')
    time.sleep(1)
    print('czy chcesz zamknac program? [t/n]')
    time.sleep(0.5)
    zamykanie_3 = input()
    if zamykanie_3 == "t":
      break
    elif zamykanie_3 == "n":
      continue
    else:
      print('nie to miales napisac ale ok (zamykam)')
      break
