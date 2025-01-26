# 🛠️ Fb-Token Converter 🚀
![Fb-Token Logo](https://github.com/user-attachments/assets/7c230760-9495-4e7e-bc53-f832032fc95d)
![GitHub](https://img.shields.io/badge/Version-4.0.0-blue)
![GitHub](https://img.shields.io/badge/License-MIT-green)
![GitHub](https://img.shields.io/badge/Python-3.7%2B-yellow)

Alat ini dirancang untuk mengonversi **cookies Facebook** menjadi **EAAB Access Token** yang dapat digunakan untuk mengakses API Instagram dan Graph Facebook. Alat ini masih berfungsi dengan baik hingga tahun 2023 dan dapat digunakan untuk berbagai keperluan pengembangan aplikasi.

## 🌟 Fitur Utama
- **Konversi Cookies ke Token**: Mengubah cookies Facebook menjadi EAAB Access Token.
- **Akses Graph API**: Token yang dihasilkan dapat digunakan untuk mengakses `graph.facebook.com` dengan cakupan yang luas.
- **Cakupan Token**:
  - `business_management`
  - `publish_actions`
  - `manage_pages`
  - `publish_pages`
  - `ads_management`
  - `email`
  - `public_profile`
 
## 🛠️ Instalasi
```bash
apt update -y && apt upgrade -y
pkg install git python-pip
git clone https://github.com/RozhakXD/Fb-Token.git
cd "Fb-Token"
pip install -r requirements.txt
python Run.py "Your Facebook Cookies!"
```

## 📝 Contoh Penggunaan
**Masukkan**:
```
python Run.py "datr=S1pQZyc0VPvzB_L2jvSnE3ZW; sb=S1pQZzx-fI4ooSCbf7EjEej3; ps_l=1; ps_n=1; dpr=1.5; wd=1272x594; c_user=4; fr=1TTwJtJJF8hFqLvak.AWX_7ICXau7XMfduyiKv_E3tO3I.BnlL21..AAA.0.0.BnlL21.AWXKlJLfPUY; xs=; presence="
```
**Keluaran**:
```
[Info] Token Ditemukan: EAABwzLixnjYBO1KcAecmZBNa5tmTo4TIPSkLfhkIOeuyr2ndSlSRgn3qkRluQDRYLWkEcETE2pqZBAPvnizIl2xEId3udOaCIPbzzvgDXNXZA1hqiawk0tp4KCr0V7XGDd3sFHaq2MkE294ca968BFDpZBsofixrZCISmgtJ8Wtw86Y0R1mFZCDH8Mli6ScWd7uYoZD
```

## ⚙️ Persyaratan
- **Python 3.x**: Pastikan Python 3.x sudah terinstal di sistem Anda.
- **Modul Python**:
  - `requests`
  - `re`
  - `sys`
 
## ⚠️ Catatan Penting
- **Penggunaan Bertanggung Jawab**: Alat ini hanya untuk tujuan pengembangan dan pembelajaran. Pastikan Anda mematuhi kebijakan dan aturan yang berlaku dari Facebook dan Instagram.
- **Keamanan**: Jangan pernah membagikan cookies atau token Anda kepada pihak yang tidak terpercaya.

## 📜 Lisensi
Alat ini dirilis di bawah lisensi MIT. Anda bebas menggunakan, memodifikasi, dan mendistribusikan alat ini sesuai dengan ketentuan lisensi.
