import random

barang = []

# Class Transaction
class Transaction():
  """ Create class transaction for customer"""
  id = str(random.uniform(1,100))
  transaction_id = "TRX-" + id
  def __init__(self, name):
    self.name = name

# Create Transaction
def Create_transaction():
  """ Function to create name and random id for customer"""
  name = input("Selamat Datang, masukkan nama customer: \n")
  trx = Transaction(name)
  trx = trx.transaction_id
  msg = print(f"Customer {name}, dengan id {trx} telah dibuat")
  transaction_menu()

# Add Item
def add():
  """ Function to add single item """
  nama = input("Masukkan nama barang : \n")
  
  while True:
    try:
      jumlah = float(input("Masukkan jumlah barang : \n"))
      if isinstance(jumlah, int) or isinstance(jumlah, float):
        break
    except ValueError:
      print('masukkan dalam tipe numerik')

  while True:
    try:
      harga = float(input("Masukkan Harga Satuan : \n"))
      if isinstance(harga, int) or isinstance(harga, float):
        break
    except ValueError:
      print('masukkan dalam tipe numerik')

  harga_total = jumlah*harga
  barang.append([nama, jumlah, harga, harga_total])
  return barang

# Add Item Menu
def add_item():
  """ Function add item on menu/ to loop add function"""
  belanja = True
  while belanja == True:
    add()
    while True:
      ask = input("Tambahkan barang lagi ? (Y/n)")
      if ask in ('n','N','no','No'):
        belanja = False
        break
      elif ask in ('Y','y','Yes','yes'):
        belanja = True
        break
      else:
        print('please give a proper input')

# Update Item
def update():
  """ To insert updated data on item"""
  nama = input("Masukkan nama barang update: \n")
  
  while True:
    try:
      jumlah = float(input("Masukkan jumlah barang update : \n"))
      if isinstance(jumlah, int) or isinstance(jumlah, float):
        break
    except ValueError:
      print('masukkan dalam tipe numerik')

  while True:
    try:
      harga = float(input("Masukkan Harga Satuan update: \n"))
      if isinstance(harga, int) or isinstance(harga, float):
        break
    except ValueError:
      print('masukkan dalam tipe numerik')

  harga_total = jumlah*harga
  barang.append([nama, jumlah, harga, harga_total])
  return barang

# Update Item Menu
def update_item():
  """ To check which item to update"""
  print(barang)
  nama = input("Masukkan nama barang yang ingin di ubah : \n")

  for x in barang:
      if nama in x[0]:
        while True:
          print(x)
          ask = input("Anda yakin ingin mengupdate entry ini ? (Y/n/cancel)")
          if ask in ('n','N','no','No'):
            update_item()
          elif ask in ('Y','y','Yes','yes'):
            barang.remove(x)
            update()
            print('Entry Berhasil Di Update')
            transaction_menu()
          elif ask == 'cancel':
            transaction_menu()
          else:
            print('please give a proper input')
      else:
        continue

  return barang

# Delete Item Menu
def delete_item():
  """ Function on delete item """
  print(barang)
  hapus = str(input("Masukkan nama barang yang ingin di hapus : \n"))

  for x in barang:
    if hapus in x[0]:
      while True:
        ask = input("Anda yakin ingin menghapus entry ini ? (Y/n/cancel)")
        if ask in ('n','N','no','No'):
          delete_item()
        elif ask in ('Y','y','Yes','yes'):
          barang.remove(x)
          print('Entry Berhasil Dihapus')
          transaction_menu()
        elif ask == 'cancel':
          transaction_menu()
        else:
          print('please give a proper input')

  print('nama barang tidak di temukan')
  delete_item()

# Check Item
def check_cart():
  """ Check Item on cart """
  total = sum(x[-1] for x in barang)
  total = print(f"Jumlah yang harus di bayarkan : Rp. {total}")
  print('Daftar Barang belanjaan')
  print(barang)

# Reset Transaction
def reset_transaction():
  """ Function to reset Transaction, empty the cart"""
  while True:
    ask = input('Anda Yakin ingin mereset semua transaksi: (Y/n)')
    if ask in ('n','N','no','No'):
      transaction_menu()
    elif ask in ('Y','y','Yes','yes'):
      barang.clear()
      print('Semua Transaksi berhasil di hapus')
      transaction_menu()
    else:
      print('please give a proper input')

# Promo
def promo():
  """Function to check total transaction, and it's promo"""
  total = sum(x[-1] for x in barang)
  disc = "0%"
  if total > 200000:
    disc = "5%"
    total = 0.95 * total
  elif total > 300000:
    disc = "8%"
    total = 0.92 * total
  elif total > 500000:
    disc = "10%"
    total = 0.90 * total

  return total, disc

# CheckOut
def checkout():
  """ Function to sum all transaction and final review before paying"""
  check_cart()
  total = promo()
  print(f'Jumlah diskon yang di dapatkan adalah {total[1]}')
  print(f'Jumlah yang harus di bayarkan adalah {total[0]} (Sudah termasuk diskon)')
  while True:
    ask = input('Apa anda sudah yakin dengan semua barang belanja anda ? (Y/n)')
    if ask in ('n','N','no','No'):
      transaction_menu()
    elif ask in ('Y','y','Yes','yes'):
      print('Transaksi berhasil')
      main_menu()
    else:
      print('please give a proper input')

# Main Menu
def main_menu():
  """ Main menu """
  print("Welcome to Main Menu")
  print("1. Create Transaction | 2. Exit Program")
  while True:
    user = input("Please Select the menu")
    if user == '2':
      return print("Thank you for using this program")
      break
    elif user == '1':
      Create_transaction()
    else:
      print('please give a proper input')
  sys.exit()
  
# Transaction Menu
def transaction_menu():
  """" Transaction on each user"""
  while True:
    print("Transaction Menu")
    print("1. Add Item \n2. Update Item \n3. Delete Item \n4. Check Item \n5. Reset Item \n6. Checkout \n7. To Main Menu")
    user = input("Please Select the menu")
    if user == '1':
      add_item()
    elif user == '2':
      update_item()
    elif user == '3':
      delete_item()
    elif user == '4':
      check_cart()
    elif user == '5':
      reset_transaction()
    elif user == '6':
      checkout()
    elif user == '7':
      main_menu()
      exit()
    else:
      print('please give a proper input')