from tabulate import tabulate
import regex as re
from .edit import *
from .read import *
from .tabel import *

credential = [{"alpha@admin" : "1234abcd"}, #OK
              {"bravo@admin" : "gueadminbos"},
              {"charlie@admin" : "password"}]

def input_login(): #OK
  global credential
  username = input("Masukkan username Anda ")
  password = input("Masukkan password: ")
  for i in credential:
    esc = 0
    for key, value in i.items():
      if username == key and password == value:
        esc = 1
        return username.replace("@admin", "")
  if esc == 0:
    print("Username atau Password Anda Salah!")
    y = input_yes_no("Apakah Anda ingin mencoba login kembali? (y/n): ")
    if y == 'y':
      input_login()
    elif y == 'n':
      return 0

def input_plate(prompt): #OK
    import regex as re
    while True:
        plate = input(prompt)
        plate = plate.replace(" ", '').upper()
        if re.fullmatch("B\d{3,4}(?:[A-Z]){2,3}", plate):
            return plate
        else:
            print("Masukkan plat Jakarta tanpa spasi!")

def input_angka(prompt):
    while True:
        angka = input(prompt)
        if angka.isdigit():
            return int(angka)
        else:
            print("Mohon masukkan angka yang benar!")

def input_kata(prompt): #OK
    while True:
        kata = input(prompt)
        if kata.replace(" ","").isalpha():
            return kata
        else:
            print("Mohon masukkan alfabet saja (case sensitive)!")

def input_tgl_str(prompt): #OK
    import regex as re
    while True:
        tgl = input(prompt)
        tgl = tgl.replace(" ", "").replace("/", "").replace("-","")
        if re.fullmatch("[2][0]\d{2}[01]\d[0123]\d", tgl):
            return tgl
        else:
            print("Mohon masukkan tanggal dengan format YYYYMMDD")

def input_yes_no(prompt): #OK
    while True:
        yesno = input(prompt)
        if yesno.lower() == 'y' or yesno.lower() == 'n':
            return yesno.lower()
        else:
            print("Masukkan 'y' jika yes atau 'n' jika no!")

def car_tipefunc(i):
  if i["car_type"] == "Honde Alfard":
    return 0
  elif i["car_type"] == "Kujang Anova":
    return 1
  elif i["car_type"] == "Dahaksu Gaya":
    return 2
  elif i["car_type"] == "Coyota Fortuna":
    return 3
  elif i["car_type"] == "CNY 5x Series":
    return 4
  
def inputmain(prompt):
  while True:
    choice = input_angka(prompt)
    if choice in [0,1,2,3,4]:
      return choice
    else:
      print("Mohon masukkan pilihan yang tersedia!")
