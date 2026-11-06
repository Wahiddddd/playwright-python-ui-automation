# SauceDemo Web Automation Testing 🧪

Repository ini berisi skrip automated testing End-to-End (E2E) untuk aplikasi web [SauceDemo](https://www.saucedemo.com/) menggunakan **Python**, **Playwright**, dan **Pytest** dengan menerapkan desain pola **Page Object Model (POM)**.

> 📌 **Catatan Progres:** Proyek ini masih dalam tahap pengembangan aktif (*Work in Progress* / WIP).

---

## 🚀 Tech Stack

- **Language:** Python 3.13+
- **Test Framework:** [pytest](https://docs.pytest.org/)
- **Automation Tool:** [Playwright for Python](https://playwright.dev/python/)
- **Reporting:** [pytest-html](https://pytest-html.readthedocs.io/)
- **Pattern:** Page Object Model (POM)

---

## 📁 Struktur Direktori

```text
saucedemo_automation/
├── pages/                          # Page Object Model (POM) classes
│   ├── login_page.py               # Interaksi & locator halaman Login
│   ├── inventory_page.py           # Interaksi halaman Product Inventory
│   ├── cart_page.py                # Interaksi halaman Keranjang Belanja
│   ├── checkout_page.py            # Interaksi halaman Form Checkout (Info Pembeli)
│   ├── checkout_overview_page.py   # Interaksi halaman Ringkasan Checkout
│   └── complete_page.py            # Interaksi halaman Checkout Selesai
├── tests/                          # Test Suites / Skenario Pengujian
│   ├── test_login.py               # Pengujian Login (Data-driven / Parametrized)
│   ├── test_inventory.py           # Pengujian Halaman Katalog Produk
│   ├── test_cart.py                # Pengujian Keranjang
│   ├── test_checkout.py            # Pengujian Form Checkout
│   ├── test_checkout_overview.py   # Pengujian Ringkasan Checkout
│   └── test_complete.py            # Pengujian Konfirmasi Order Selesai
├── conftest.py                     # Setup fixture Playwright & Hook Screenshot on Failure
├── requirements.txt                # Daftar dependensi library Python
├── .gitignore                      # Daftar file yang diabaikan oleh Git
└── README.md                       # Dokumentasi proyek
```

---

## ⚙️ Fitur Pengujian yang Dicakup

- [x] **Authentication:** Pengujian login positif dan negatif menggunakan `@pytest.mark.parametrize`.
- [x] **Inventory Page:** Verifikasi daftar produk dan navigasi katalog.
- [x] **Shopping Cart:** Menambahkan dan memvalidasi item di keranjang.
- [x] **Checkout Step One:** Pengisian data pembeli (First Name, Last Name, Postal Code).
- [x] **Checkout Overview:** Validasi item dan ringkasan pembayaran.
- [x] **Checkout Complete:** Verifikasi transaksi sukses (*Thank you for your order!*).
- [x] **Automatic Failure Screenshot:** Pengambilan screenshot otomatis jika ada test case yang gagal, langsung disematkan ke dalam laporan HTML (Base64).

---

## 🛠️ Panduan Instalasi & Menjalankan Tes

### 1. Clone Repository

```bash
git clone <URL_REPO_GITHUB_ANDA>
cd saucedemo_automation
```

### 2. Buat & Aktifkan Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Install Browser Driver Playwright

```bash
playwright install chromium
```

---

## 🧪 Cara Menjalankan Tes

### Menjalankan Seluruh Skenario Tes
```bash
pytest
```

### Menjalankan Tes Tertentu (Contoh: Login saja)
```bash
pytest tests/test_login.py
```

### Menjalankan Tes dan Menghasilkan Laporan HTML
```bash
pytest --html=reports/report.html --self-contained-html
```
*Laporan pengujian akan tersimpan di dalam folder `reports/report.html` beserta screenshot bila ada tes yang gagal.*

