# Lisans Anahtarı Doğrulama Sistemi

## Genel Bakış
Bu proje, kullanıcının **anakart seri numarasına** dayalı olarak lisans anahtarını doğrulayan bir **lisans anahtarı doğrulama sistemi**dir. Sistem, lisans anahtarının geçerliliğini **MongoDB** üzerinde sorgulayarak periyodik olarak kontrol eder. Eğer anahtar süresi dolmuş veya geçersizse, program otomatik olarak kapanır.

## Özellikler
- **MongoDB** ile lisans anahtarı doğrulama.
- `threading.Timer` kullanarak **periyodik anahtar kontrolü**.
- Yetkisiz veya süresi dolmuş anahtarlar için **güvenli program kapatma mekanizması**.
- **Global stop event** ile çalışan **tüm thread'leri sonlandırma**.
- **Hata yönetimi** ve **MongoDB bağlantısının yeniden kurulması**.

## Gereksinimler
- **Python 3.13.2**
- **MongoDB**
- **Gerekli Kütüphaneler**: `pymongo`, `wmi`, `threading`, `time`, `os`

## Kurulum ve Kullanım
1. Depoyu klonlayın:
   ```sh
   git clone https://github.com/Leo4Bey/basic-lisance-system.git
2. Modülleri Yükleyin:
   ```sh
   pip install pymongo wmi threading time os
3. Çalıştırın:
   ```sh
   python main.py
--------------------------------------------------------------------------------------

# License Key Validation System

## Overview
This project is a **license key validation system** that verifies a user's license key based on their motherboard's serial number. The system periodically checks the license key's validity by querying a **MongoDB** database. If the key is expired or invalid, the application automatically stops.

## Features
- License key verification via MongoDB.
- Periodic key validation using `threading.Timer`.
- Secure shutdown mechanism for unauthorized or expired keys.
- Multi-threaded execution with a **global stop event** to terminate all running threads.
- Error handling and MongoDB connection recovery.

## Requirements
- **Python 3.13.2**
- **MongoDB**
- **Required Libraries**: `pymongo`, `wmi`, `threading`, `time`, `os`

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/Leo4Bey/basic-lisance-system.git
2. Install Modules:
   ```sh
   pip install pymongo wmi threading time os
3. Run:
   ```sh
   python main.py
