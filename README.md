# Shoe Hub

A full-stack e-commerce web application built with Django and PostgreSQL.

Shoe Hub provides a complete online shopping experience including product browsing, product search, user authentication, shopping cart management, checkout, stock management, and order tracking.

## Live Demo

https://ecommerce-shoehub.onrender.com

---

## Features

- 🛍️ Browse products
- 🔎 Search products by name
- 📦 View product details
- 📊 Product stock management
- 🛒 Add products to cart
- ➕ Increase and decrease cart quantities
- 🗑️ Remove products from cart
- 👤 User registration
- 🔐 User login and logout
- 💳 Checkout and demo payment flow
- 📋 Order confirmation
- 📦 Order history
- 🔎 View individual order details
- 🏪 Django admin panel
- 🖼️ Product image uploads
- 📱 Responsive user interface
- 🗄️ PostgreSQL database
- 🚀 Production deployment on Render

---

## Tech Stack

### Backend

- Python
- Django
- Gunicorn

### Frontend

- HTML5
- CSS3
- Django Templates

### Database

- PostgreSQL
- Django ORM

### Tools & Deployment

- Git
- GitHub
- Render
- VS Code

---

## Project Structure

```text
Ecommerce/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── products/
│   ├── migrations/
│   ├── static/
│   │   └── products/
│   ├── templates/
│   │   └── products/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── products/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Application Flow

```text
Home
  │
  ▼
Products
  │
  ├── Search Products
  │
  ▼
Product Details
  │
  ▼
Add to Cart
  │
  ▼
Shopping Cart
  │
  ▼
Login / Register
  │
  ▼
Checkout
  │
  ▼
Demo Payment
  │
  ▼
Order Confirmation
  │
  ▼
My Orders
```

---

## Database Models

The application uses Django's ORM with PostgreSQL in production.

### Product

Stores:

- Product name
- Description
- Price
- Stock
- Product image
- Creation date

### Cart

Represents a shopping cart.

### CartItem

Stores:

- Product
- Quantity
- Cart relationship

### Order

Stores:

- Customer information
- Shipping information
- Order total
- Payment status
- Payment information
- Order creation date

### OrderItem

Stores:

- Product
- Quantity
- Price
- Order relationship

### User

Uses Django's built-in authentication system.

---

## Authentication

Shoe Hub uses Django's built-in authentication system for:

- User registration
- User login
- User logout
- Protected checkout
- User-specific orders
- User-specific order details

---

## Checkout & Payment

The project currently uses a **demo payment flow** for testing the complete e-commerce order lifecycle.

During checkout, the application:

1. Validates the cart
2. Checks product stock
3. Collects shipping information
4. Creates an order
5. Creates order items
6. Updates product stock
7. Clears the cart
8. Displays the order confirmation

---

## Django Admin

The Django admin panel allows administrators to manage application data including products and orders.

Admin URL:

```text
/admin/
```

---

## Deployment

The application is deployed using:

- **Render Web Service** — Django application
- **Render PostgreSQL** — production database
- **Gunicorn** — WSGI application server

Static files are collected using Django's `collectstatic` command.

---

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/hithainali/Ecommerce-shoehub.git
cd Ecommerce-shoehub
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv env
```

Activate it:

```powershell
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Environment Variables

Production configuration uses environment variables.

Example:

```text
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
```

Do not commit `.env` files or secret credentials to GitHub.

---


## 👨‍💻 Author

**Hithain Ali**

GitHub:

https://github.com/hithainali

---

