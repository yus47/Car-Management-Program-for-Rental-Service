from tabulate import tabulate
import regex as re
from .input import *
from .read import *
from .tabel import *

def input_angka(prompt):
    while True:
        angka = input(prompt)
        if angka.isdigit():
            return int(angka)
        else:
            print("Mohon masukkan angka yang benar!")

def create_admin(): #OK
    global car_id, car_data
    while True:
      ketemu = False
      plat_mobil = input_plate("Masukkan plat mobil baru yang telah dibeli: ")
      tipa = ""
      new_car = []
      for i in car_id:
          if plat_mobil == i["plate"]:
              print("Plat mobil sudah terdaftar!")
              y = input_yes_no("Apakah Anda ingin mengganti plat yang diinput? (y/n): ")
              if y == 'y':
                  ketemu = True
              elif y == 'n':
                  return
      if ketemu == False:
         break
    if plat_mobil != '':
        while True:
            print("Tipe mobil 1: Honde Alfard")
            print("Tipe mobil 2: Kujang Anova")
            print("Tipe mobil 3: Dahaksu Gaya")
            print("Tipe mobil 4: Coyota Fortuna")
            print("Tipe mobil 5: CNY 5x Series")
            tipe = input_angka("Masukkan tipe mobil yang ingin ditambah: ")
            if tipe in range(1,6):
                if tipe == 1:
                    tipa = "Honde Alfard"
                    tipe -=1
                elif tipe == 2:
                    tipa = "Kujang Anova"
                    tipe -=1
                elif tipe == 3:
                    tipa = "Dahaksu Gaya"
                    tipe -=1
                elif tipe == 4:
                    tipa = "Coyota Fortuna"
                    tipe -=1
                elif tipe == 5:
                    tipa = "CNY 5x Series"
                    tipe -=1
                break
            else:
                print("Masukkan tipe mobil yang benar!")
        tahun = input_angka("Masukkan tahun perilisan mobil: ")
        if tahun in list(range(2015, 2025)):
            new_car = [{"plate" : plat_mobil, "car_type" : tipa, "tahun": tahun, "available": 0, "deployed": 0, "on maintenance": 1, "last rented": ""}]
            car_id.extend(new_car)
            car_data[tipe]["total"] += 1
            car_data[tipe]["on maintenance"] +=1
            print("Data telah ditambahkan! Mohon masukkan mobil ke bengkel terlebih dahulu.")
            read_admin(new_car)
        else:
            print("Mobil tidak sesuai kebijakan, tidak dapat ditambahkan.")

# %%
def update_admin(): #OK
    global car_data, car_id
    plat_mobil = input_plate("Masukkan plat mobil yang ingin Anda ubah informasinya: ")
    for i in car_id:
        if plat_mobil == i['plate']:
            print("Mobil ditemukan!")
            listi = [i]
            read_admin(listi)
            tipee = car_tipefunc(i)
            print("\nInformasi apa yang ingin Anda ubah?\n\
                1. Ganti nomor pelat\n\
                2. Status penyewaan mobil\n\
                3. Ubah tanggal terakhir mobil disewa\n\
                0. Cancel")
            while True:
              menu = input_angka("Masukkan angka sesuai dengan pilihan")
              if menu == 1:
                  while True:
                    plat = input_plate("Masukkan plat mobil yang baru: ")
                    for j in car_id:
                      if plat == j['plate']:
                        print("Plat sudah terpakai oleh mobil lain, cek input!")
                        y = input_yes_no("Apakah Anda ingin mengganti plat yang diinput? (y/n): ")
                        if y == 'y':
                          update_admin()
                        elif y == 'n':
                          return None
                    break
                  i['plate'] = plat
                  print("Data sudah diupdate!")
                  read_admin(listi)
                  return None
                  exit
              elif menu == 2:
                print("Pilih status baru: ")
                if i['available'] == 0:
                  print("1. Available")
                if i['deployed'] == 0:
                  print("2. Deployed")
                if i['on maintenance'] == 0:
                  print("3. On Maintenance")
                print("0. Cancel")
                while True:
                  menu2 = input_angka("Masukkan status baru: ")
                  if menu2 == 1 and i['available'] == 1:
                    print("Masukkan pilihan yang tepat!")
                  elif menu2 == 2 and i['deployed'] == 1:
                    print("Masukkan pilihan yang tepat!")
                  elif menu2 == 3 and i['on maintenance'] == 1:
                    print("Masukkan pilihan yang tepat!")
                  elif menu2 == 0:
                    print("Perubahan dibatalkan")
                    y = input_yes_no("Apakah Anda ingin mengganti plat yang diinput? (y/n): ")
                    if y == 'y':
                      update_admin()
                    elif y == 'n':
                      return None
                  elif menu2 not in [1,2,3]:
                    print("Masukkan pilihan yang tepat!")
                  else:
                    if menu2 == 1:
                      i['available'] = 1
                      car_data[tipee]['available'] += 1
                      if i['deployed'] == 1:
                        i['last rented'] = input_tgl_str("Masukkan tanggal terakhir mobil dirental (mungkin hari ini): ")
                        car_data[tipee]['deployed'] -= 1
                      if i['on maintenance'] == 1:
                        car_data[tipee]['on maintenance'] -= 1
                      i['deployed'] = 0
                      i['on maintenance'] = 0
                      print("Data sudah diupdate!")
                      read_admin(listi)
                      return None
                    elif menu2 == 2:
                      if i['available'] == 1:
                        car_data[tipee]['available'] -= 1
                      if i['on maintenance'] == 1:
                        car_data[tipee]['on maintenance'] -= 1
                      i['available'] = 0
                      i['deployed'] = 1
                      i['on maintenance'] = 0
                      i['last rented'] = ""
                      print("Data sudah diupdate!")
                      read_admin(listi)
                      return None
                    elif menu2 == 3:
                      if i['available'] == 1:
                        car_data[tipee]['available'] -= 1
                      i['available'] = 0
                      if i['deployed'] == 1:
                        i['last rented'] = input_tgl_str("Masukkan tanggal terakhir mobil dirental (mungkin hari ini): ")
                        car_data[tipee]['deployed'] -= 1
                      i['deployed'] = 0
                      i['on maintenance'] = 1
                      print("Data sudah diupdate!")
                      read_admin(listi)
                      return None
              elif menu == 3:
                tgl_str = input_tgl_str("Masukkan tanggal last rented yang baru: ")
                i['last rented'] = tgl_str
                read_admin(listi)
                return None
              elif menu == 0:
                print("Perubahan dibatalkan")
                y = input_yes_no("Apakah Anda ingin mengganti plat yang diinput? (y/n): ")
                if y == 'y':
                  update_admin()
                elif y == 'n':
                  return None
              else:
                 print("Pilihan yang dimasukkan tidak sesuai, silakan input ulang")
    print("Mobil tidak ditemukan")
    y = input_yes_no("Apakah Anda ingin mengganti plat yang diinput? (y/n): ")
    if y == 'y':
        update_admin()
    elif y == 'n':
        return None
    
def del_admin(): #OK
  global car_id, car_data, car_past
  plat_mobil = input_plate("Masukkan plat mobil yang ingin Anda hapus datanya: ")
  for i in car_id:
    if plat_mobil == i['plate']:
      print("Mobil ditemukan")
      listi = [i]
      read_admin(listi)
      tipee = car_tipefunc(i)
      yn = input_yes_no("Apakah Anda yakin akan menghapus data mobil? (y/n): ")
      if yn == 'y':
        car_data[tipee]['total'] -= 1
        if i['available'] == 1:
          car_data[tipee]['available'] -= 1
        if i['deployed'] == 1:
          car_data[tipee]['deployed'] -= 1
        if i['on maintenance'] == 1:
          car_data[tipee]['on maintenance'] -= 1
          del listi[0]['available']
          del listi[0]['deployed']
          del listi[0]['on maintenance']
        reason = input_kata('Masukkan alasan mobil dihapus datanya secara singkat: ')
        listi[0]['reason'] = reason
        car_id.remove(i)
        car_past.extend(listi)
        print('Data mobil sudah dihapus.')
        return None
      else:
        return None
  print("Mobil tidak ditemukan, cek ulang input")
  y = input_yes_no("Apakah Anda ingin mengganti plat yang diinput? (y/n): ")
  if y == 'y':
    del_admin()
  elif y == 'n':
    return None
  
