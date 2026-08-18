# Shoe Hub

A full-stack e-commerce web application built with Django. Shoe Hub demonstrates the core functionality of an online shopping platform, including product browsing, search, authentication, cart management, checkout, stock management, and order tracking.

> **Note:** This is a portfolio/demo project. Payments are simulated and no real transactions are processed.


## Features

- User registration and login
- Product listing and product details
- Product search
- Shopping cart
- Add, remove, and update cart quantities
- Stock availability validation
- Checkout with shipping information
- Simulated payment flow
- Automatic order creation after successful payment
- Automatic stock reduction after purchase
- Order confirmation
- My Orders page
- Individual order details
- Responsive user interface
- Django admin support for managing products and orders


## Tech Stack

### Backend
- Python
- Django
- PostgreSQL

### Frontend
- HTML
- CSS
- Django Templates

### Tools
- Git
- GitHub
- VS Code

## Project Structure

```text
Ecommerce/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   ├── templates/
│   │   └── products/
│   ├── static/
│   │   └── products/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── run_local_https.py
├── .gitignore
└── README.md


## Database

The application uses **PostgreSQL** as its database.

Database configuration is handled through environment variables.


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hithainali/Ecommerce-shoehub.git
cd Ecommerce-shoehub
```

### 2. Create a virtual environment

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Make sure PostgreSQL is installed and running.

Configure the database settings in `config/settings.py`.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.