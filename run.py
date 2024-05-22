
from tabulate import tabulate
import regex as re
from caps1 import *


def main():
  print('''
Pusing Car Rental Control System
Silahkan login terlebih dahulu :)
    ''')
  login = input_login()
  if login == 0:
    return 0
  while True:
    print(f'''
Admin Logging In: {login}
Apa yang ingin Anda lakukan?
1. Melihat data mobil
2. Menambahkan mobil baru
3. Mengubah data mobil
4. Menghapus data mobil
0. Keluar
    ''')
    menu = inputmain("Silakan masukkan angka sesuai kebutuhan Anda: ")
    if menu == 0:
      break
    if menu == 1:
      print("Data apa yang ingin Anda lihat?\n1. Data kumulatif\n2. Daftar mobil\n0. Keluar")
      menu1 = input_angka("Silakan masukkan angka sesuai kebutuhan Anda: ")
      if menu1 == 1:
        read_admin(car_data)
        print("\nApakah Anda ingin melihat daftar mobil yang lebih detail?")
        y = input_yes_no("Ke daftar mobil? (y/n): ")
        if y == 'y':
          menu1 = 2
        elif y == 'n':
          pass
      if menu1 == 2:
        read_admin(car_id)
        print("Apakah Anda ingin mengfilter data? (y/n)")
        yes = input_yes_no("Masukkan pilihan Anda (y/n)")
        if yes == "y":
          read_filter_admin()
        elif yes == "n":
          pass
    if menu == 2:
      create_admin()
    if menu == 3:
      update_admin()
    if menu == 4:
      del_admin()
    print("Apakah Anda ingin melakukan hal lain? (y/n)")
    yes = input_yes_no("Masukkan pilihan Anda (y/n): ")
    if yes == "n":
      break
    else:
      continue

main()