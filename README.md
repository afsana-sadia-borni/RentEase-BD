<div align="center">

  <h1>🏠 RentEase BD</h1>
  <p><strong>A Next-Gen, Modern & Seamless Property Rental Management Solution for Bangladesh</strong></p>

  [![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
  [![PostgreSQL](https://img.shields.io/badge/Neon-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://neon.tech/)
  [![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
  [![Render](https://img.shields.io/badge/Render-Hosted-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://rentease-bd.onrender.com)

  <br />

  ### 🌐 **Live Website Link:** [https://rentease-bd.onrender.com](https://rentease-bd.onrender.com)

</div>

---

## 🌟 Overview

**RentEase BD** is a powerful full-stack Django platform engineered specifically to streamline property rentals across Bangladesh. It connects property owners (Landlords) with tenants, removing traditional hassles by offering dynamic listings, budget/location filtering, instant booking workflows, interactive maps, and cloud image management.

---

## 🔥 Key Features

* **👥 Role-Based Access:** Distinct interfaces and capabilities for **Tenants** and **Landlords/Owners**.
* **🏡 Dynamic Listings:** Add, edit, and delete properties with custom descriptions, prices, and high-res photos.
* **📍 Interactive Location Maps:** Geolocation integration using latitude & longitude for precise spot identification.
* **🔍 Smart Search & Filters:** Find rentals quickly by searching location keywords and applying maximum budget constraints.
* **📅 Booking Management:** Prevent duplicate booking requests with real-time status updates.
* **💳 Payment Simulation:** Simulated checkout and dummy payment portal for confirming rental bookings.
* **⭐ User Reviews & Ratings:** Verified feedback system to maintain trust between landlords and tenants.
* **🐘 Centralized Database:** Connected to **Neon PostgreSQL** serverless cloud database for reliable, scalable production storage.
* **☁️ Cloud Media Storage:** Integrated with **Cloudinary** for fast and persistent property image hosting.

---

## 🛠️ Tech Stack & Architecture

| Category | Technology / Tool Used |
| :--- | :--- |
| **Live Web App** | [https://rentease-bd.onrender.com](https://rentease-bd.onrender.com) |
| **GitHub Repository** | `afsana-sadia-borni/RentEaseBD` |
| **Backend Framework** | Python / Django |
| **Frontend UI** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Cloud Database** | **Neon Tech (PostgreSQL)** |
| **Media Hosting** | Cloudinary API |
| **Production Hosting** | Render (WSGI + Gunicorn) |

---

## 🚀 Local Installation & Setup

### 1️⃣ Clone Repo & Navigate
```bash
git clone [https://github.com/afsana-sadia-borni/RentEaseBD.git](https://github.com/afsana-sadia-borni/RentEaseBD.git)
cd RentEaseBD
2️⃣ Create Virtual Environment
Bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
Bash
pip install -r requirements.txt

4️⃣ Set Up Environment Variables (.env)
Create a .env file in the root directory:

Code snippet
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@ep-example.neon.tech/neondb
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

5️⃣ Migrate Database & Run
Bash
python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.
