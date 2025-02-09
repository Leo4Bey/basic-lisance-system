import wmi
import pymongo
import time
import threading
import os

url = "" # Mongo URL sadece okuma izni verilecek

client = pymongo.MongoClient(url)
db = client.zenith

key_input = input("Key'inizi giriniz...")

def get_motherboard_serial():
    try:
        c = wmi.WMI()
        for board in c.Win32_BaseBoard():
            return board.SerialNumber
    except Exception as e:
        return f"Hata: {e}"

motherboard_serial = get_motherboard_serial()

def check_key(key):
    threading.Timer(5, lambda: check_key(key_input)).start()
    try:
        filtre = {
            "bot_key": key,
            "motherboard_serial": motherboard_serial
        }
        if db.deneme.count_documents(filtre) != 0:
            document = db.deneme.find_one(filtre)
            deadline = document.get("deadline")
            current_timestamp = int(time.time())
            if current_timestamp > deadline:
                print(f"Current: {current_timestamp}")
                print(f"deadline: {deadline}")
                print("Key'in süresi doldu!\nPROGRAM SONLANDIRILDI")
                os._exit(0)
            else:
                print("Sorun yok")
        else:
            print("Geçersiz key ya da yetkisiz erişim!\nPROGRAM SONLANDIRILDI")
            os._exit(0)
    except Exception as e:
        return f"Hata: {e}"
    
check_key(key_input)