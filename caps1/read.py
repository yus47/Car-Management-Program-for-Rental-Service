from tabulate import tabulate
import regex as re
from .edit import *
from .input import *
from .tabel import *
def input_angka(prompt):
    while True:
        angka = input(prompt)
        if angka.isdigit():
            return int(angka)
        else:
            print("Mohon masukkan angka yang benar!")

def read_admin(table): #OK
    print(tabulate(table, headers = 'keys', tablefmt = "pretty"))

def read_filter_admin():
  while True:
    print("Filter apa yang ingin Anda gunakan?\n1. Tipe mobil\n2. Status mobil")
    filtera = input_angka("Masukkan angka sesuai pilihan: ")
    carlist = []
    carlistprint = []
    cardictprint ={}
    if filtera == 1:
      print("Daftar Tipe Mobil:\n1. Honde Alfard\n2. Kujang Anova\n3. Dahaksu Gaya\n4. Coyota Fortuna\n5. CNY 5x Series")
      while True:
        filterb = input_angka("Masukkan angka sesuai pilihan: ")
        if filterb == 1:
          cartipe = "Honde Alfard"
          break
        elif filterb == 2:
          cartipe = "Kujang Anova"
          break
        elif filterb == 3:
          cartipe = "Dahaksu Gaya"
          break
        elif filterb == 4:
          cartipe = "Coyota Fortuna"
          break
        elif filterb == 5:
          cartipe = "CNY 5x Series"
          break
        else:
          print("Mohon masukkan angka sesuai tipe mobil yang tersedia")
      carlist = [i for i in car_id if i["car_type"] == cartipe]
      carlist = sorted(carlist, key = lambda x : x['last rented'])
      read_admin(carlist)
      return None
    elif filtera == 2:
      print("Status apa yang ingin Anda cari?\n1. Available\n2. Deployed\n3. On Maintenance")
      filterc = input_angka("Masukkan angka sesuai pilihan: ")
      if filterc == 1:
        carlist = [i for i in car_id if i["available"] == 1]
        carlist = sorted(carlist, key = lambda x : x['last rented'])
        for car in carlist:
          for key, value in car.items():
            if key not in ['available', 'deployed', 'on maintenance']:
              cardictprint[key] = value
          carlistprint.append(cardictprint)
          cardictprint = {}
        print("List mobil yang available")
        read_admin(carlistprint)
        return None
      elif filterc == 2:
        carlist = [i for i in car_id if i["deployed"] == 1]
        for car in carlist:
          for key, value in car.items():
            if key not in ['available', 'deployed', 'on maintenance', 'last rented']:
              cardictprint[key] = value
          carlistprint.append(cardictprint)
          cardictprint = {}
        print("List mobil yang deployed")
        read_admin(carlistprint)    
        return None
      elif filterc  == 3:
        carlist = [i for i in car_id if i["on maintenance"] == 1]
        carlist = sorted(carlist, key = lambda x : x['last rented'])
        for car in carlist:
          for key, value in car.items():
            if key not in ['available', 'deployed', 'on maintenance']:
              cardictprint[key] = value
          carlistprint.append(cardictprint)
          cardictprint = {}
        print("List mobil yang on maintenance")
        read_admin(carlistprint)
        return None
    else:
      print("Mohon masukkan angka sesuai pilihan")
