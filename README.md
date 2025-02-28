# Amazon Django Project

## 📌 Overview
The **Amazon Django Project** is a web-based e-commerce platform built using Django, designed to replicate the core functionalities of an online shopping site like Amazon. It allows users to browse products, add them to their cart, make purchases, and manage their accounts efficiently.

## 🚀 Features
### 🔹 User Authentication
- User signup, login, and logout functionality.
- Secure password hashing and reset option.

### 🔹 Product Management
- Dynamic product listings with detailed descriptions and pricing.
- Categorized product search and filtering.

### 🔹 Shopping Cart & Checkout
- Add, update, and remove products from the cart.
- Secure checkout process with order summary.

### 🔹 Order Management
- Order tracking and history for users.
- Admin dashboard for order processing.

### 🔹 Payment Integration
- Seamless integration with payment gateways.

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL / SQLite
- **Authentication:** Django Authentication System

## 📂 Project Structure
```
Amazon_Django_Project/
│── amazon/                # Main Django App
│── static/                # Static files (CSS, JS, Images)
│── templates/             # HTML Templates
│── media/                 # Uploaded media files
│── db.sqlite3             # Database file (if using SQLite)
│── manage.py              # Django management script
│── requirements.txt       # Dependencies list
└── README.md              # Project documentation
```

## 🔧 Setup & Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/AmoghShukla/Amazon_Django_Project.git
   cd Amazon_Django_Project
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin panel access):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```sh
   python manage.py runserver
   ```
   Access the project at: `http://127.0.0.1:8000/`

## 🔑 Admin Panel
- URL: `http://127.0.0.1:8000/admin/`
- Use the superuser credentials created in step 5 to log in.

## 📜 License
This project is open-source and available under the MIT License.

---
💡 *Feel free to contribute and enhance the project! Fork, star, and submit a PR.* 🚀
