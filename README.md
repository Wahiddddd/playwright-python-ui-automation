# SauceDemo Web Automation Testing 🧪

[![Playwright Tests](https://github.com/Wahiddddd/playwright-python-ui-automation/actions/workflows/playwright.yml/badge.svg)](https://github.com/Wahiddddd/playwright-python-ui-automation/actions/workflows/playwright.yml)
![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-1.40%2B-green.svg)
![Pytest](https://img.shields.io/badge/pytest-9.0%2B-orange.svg)

Repository ini berisi skrip automated testing End-to-End (E2E) untuk aplikasi web [SauceDemo](https://www.saucedemo.com/) menggunakan **Python**, **Playwright**, dan **Pytest** dengan menerapkan desain arsitektur **Page Object Model (POM)** serta integrasi **Continuous Integration (CI/CD)** via **GitHub Actions**.

---

## 🚀 Tech Stack

- **Language:** Python 3.13+
- **Test Framework:** [pytest](https://docs.pytest.org/)
- **Automation Engine:** [Playwright for Python](https://playwright.dev/python/)
- **Reporting:** [pytest-html](https://pytest-html.readthedocs.io/)
- **Debugging & Tracing:** Playwright Trace Viewer
- **CI/CD:** [GitHub Actions](https://github.com/features/actions)
- **Architecture Pattern:** Page Object Model (POM)

---

## 📁 Struktur Direktori

```text
saucedemo_automation/
├── .github/
│   └── workflows/
│       └── playwright.yml          # Pipeline CI/CD GitHub Actions
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
├── conftest.py                     # Setup Playwright, Tracing, Auto-screenshot & CI Config
├── requirements.txt                # Dependensi library Python
├── .gitignore                      # File & folder yang diabaikan Git
└── README.md                       # Dokumentasi proyek
```

---

## ⚙️ Fitur & Kemampuan Pengujian

- [x] **Page Object Model (POM):** Struktur kode rapi, modular, dan mudah di-maintain.
- [x] **Authentication Flow:** Pengujian login positif dan negatif menggunakan `@pytest.mark.parametrize`.
- [x] **E2E Shopping Flow:** Dari memilih produk, keranjang, checkout form, overview, hingga transaksi selesai.
- [x] **Automated Failure Screenshot:** Otomatis mengambil screenshot layar penuh ketika test case gagal dan langsung menyematkannya ke dalam laporan HTML (Base64).
- [x] **Smart Trace Viewer (`retain-on-failure`):** Merekam timeline aksi, snapshot DOM, dan network log jika terjadi kegagalan tanpa membebani disk pada test yang passed.
- [x] **Adaptive Headless/Headed Mode:** Otomatis berjalan dalam mode *headed* (terlihat) saat run lokal, dan beralih ke *headless* saat berjalan di pipeline CI (GitHub Actions).
- [x] **CI/CD GitHub Actions:** Pengujian dijalankan otomatis di Ubuntu Linux setiap ada `push` atau `pull_request` ke branch `main`/`master`, lengkap dengan upload artefak laporan HTML, screenshot, dan trace.

---

## 🛠️ Panduan Instalasi & Menjalankan Tes (Lokal)

### 1. Clone Repository

```bash
git clone https://github.com/Wahiddddd/playwright-python-ui-automation.git
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

### 4. Install Browser Chromium Playwright

```bash
playwright install chromium
```

---

## 🧪 Cara Menjalankan Tes

### 1. Menjalankan Seluruh Tes (Default: Headed di Lokal)
```bash
pytest
```

### 2. Menjalankan Tes Tertentu (Contoh: Login saja)
```bash
pytest tests/test_login.py -v
```

### 3. Menjalankan dalam Mode Headless di Lokal
Bila ingin menjalankan test di lokal tanpa membuka jendela browser:

**Windows (PowerShell):**
```powershell
$env:HEADLESS="true"; pytest
```

**Linux / macOS:**
```bash
HEADLESS=true pytest
```

### 4. Menjalankan Tes dan Menghasilkan Laporan HTML
```bash
pytest --html=reports/report.html --self-contained-html
```
*Laporan pengujian akan tersimpan di `reports/report.html` lengkap dengan screenshot jika ada pengujian yang gagal.*

### 5. Membuka Playwright Trace Viewer (Debugging Kegagalan)
Jika terdapat pengujian yang gagal, file trace `.zip` akan otomatis tersimpan di folder `traces/`. Buka rekaman trace interaktif dengan perintah:
```bash
playwright show-trace traces/<nama_file_trace>.zip
```

---

## 🔄 Integrasi CI/CD (GitHub Actions)

Project ini telah dikonfigurasi dengan workflow GitHub Actions pada file [`.github/workflows/playwright.yml`](.github/workflows/playwright.yml).

### Apa yang Dilakukan Pipeline CI?
1. **Trigger:** Otomatis aktif saat ada `push` atau `pull request` ke branch `main` / `master`, atau melalui pemicu manual (*workflow_dispatch*).
2. **Environment:** Menjalankan runner `ubuntu-latest` dengan Python 3.13 dan browser Chromium Playwright berserta dependensi sistemnya.
3. **Execution:** Menjalankan seluruh test suite secara otomatis dalam mode *headless*.
4. **Artifacts Upload:**
   - **`pytest-html-report`**: Selalu diunggah agar tim dapat mengunduh dan melihat laporan hasil run.
   - **`failure-screenshots`**: Diunggah otomatis bila ada test yang gagal.
   - **`failure-traces`**: Diunggah otomatis bila ada test yang gagal untuk kebutuhan investigasi mendalam di Trace Viewer.
