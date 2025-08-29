# Phimart E-commerce Project

Phimart is a full-featured e-commerce platform with RESTful APIs built using Django REST Framework. It supports user authentication, product and category management, shopping carts, orders, and admin dashboards.

---

## Table of Contents

- [Features](#features)  
- [API Endpoints](#api-endpoints)  
- [Models](#models)  
- [Installation](#installation)  
- [Usage](#usage)  
- [License](#license)  

---

## Features

- User registration, login, and JWT authentication  
- Product and category CRUD operations  
- Shopping cart management with add/update/delete items  
- Order placement and status management  
- User profile management  
- Admin dashboard endpoints for platform metrics  

---

## API Endpoints Overview

### 1. Authentication

| Method | Endpoint             | Description                     |
|--------|----------------------|---------------------------------|
| POST   | `/auth/register/`    | Register a new user             |
| POST   | `/auth/login/`       | User login, get JWT token       |
| POST   | `/auth/logout/`      | Log out current user            |
| POST   | `/auth/token/refresh/` | Refresh JWT token              |

### 2. Categories

| Method | Endpoint                | Description                    |
|--------|-------------------------|--------------------------------|
| GET    | `/api/categories/`      | List all categories            |
| GET    | `/api/categories/<id>/` | Retrieve a specific category   |
| POST   | `/api/categories/`      | Create category (Admin only)   |
| PUT    | `/api/categories/<id>/` | Update a category              |
| DELETE | `/api/categories/<id>/` | Delete a category              |

### 3. Products

| Method | Endpoint                | Description                                |
|--------|-------------------------|--------------------------------------------|
| GET    | `/api/products/`        | List all products                          |
| GET    | `/api/products/<id>/`   | Retrieve a specific product                |
| GET    | `/api/products/?search=`| Search products by name or description    |
| GET    | `/api/products/?category=` | Filter products by category             |
| POST   | `/api/products/`        | Create a product (Admin only)              |
| PUT    | `/api/products/<id>/`   | Update product (Admin only)                 |
| DELETE | `/api/products/<id>/`   | Delete product (Admin only)                 |

### 4. Shopping Cart

| Method  | Endpoint                         | Description               |
|---------|---------------------------------|---------------------------|
| POST    | `/api/carts/`                   | Create a cart             |
| GET     | `/api/carts/<cart_id>/`         | Retrieve a cart           |
| DELETE  | `/api/carts/<cart_id>/`         | Delete a cart             |
| POST    | `/api/carts/<cart_id>/items/`  | Add item to cart          |
| PATCH   | `/api/carts/<cart_id>/items/<item_id>/` | Update cart item   |
| DELETE  | `/api/carts/<cart_id>/items/<item_id>/` | Remove item from cart |

### 5. Orders

| Method | Endpoint                 | Description                          |
|--------|--------------------------|------------------------------------|
| GET    | `/api/orders/`           | List user’s orders                  |
| GET    | `/api/orders/<id>/`      | Retrieve order details              |
| POST   | `/api/orders/`           | Place a new order                   |
| PUT    | `/api/orders/<id>/status/` | Update order status (Admin only) |
| DELETE | `/api/orders/<id>/`      | Cancel an order                    |

### 6. User Profile

| Method | Endpoint          | Description                 |
|--------|-------------------|-----------------------------|
| GET    | `/api/profile/`   | Retrieve logged-in user profile |
| PUT    | `/api/profile/`   | Update user profile          |

### 7. Dashboard (Admin)

| Method | Endpoint                     | Description                      |
|--------|------------------------------|----------------------------------|
| GET    | `/api/dashboard/total-users/` | Get total registered users      |
| GET    | `/api/dashboard/total-orders/`| Get total orders placed          |
| GET    | `/api/dashboard/total-products/` | Get total products available  |

---

## Models

### User
- `id`: Primary Key  
- `first_name`: CharField  
- `last_name`: CharField  
- `email`: EmailField (unique)  
- `address`: TextField (optional)  
- `phone_number`: CharField (optional)  
- `password`: Hashed password  

### Category
- `id`: Primary Key  
- `name`: CharField  
- `description`: TextField (optional)  
- One-to-many with Product  

### Product
- `id`: Primary Key  
- `name`: CharField  
- `description`: TextField  
- `price`: DecimalField  
- `stock`: IntegerField  
- `image`: ImageField (optional)  
- `category`: ForeignKey(Category)  
- `created_at`: DateTimeField  
- `updated_at`: DateTimeField  

### Cart
- `id`: Primary Key  
- `user`: OneToOneField(User)  
- `created_at`: DateTimeField  

### CartItem
- `id`: Primary Key  
- `cart`: ForeignKey(Cart)  
- `product`: ForeignKey(Product)  
- `quantity`: IntegerField  

### Order
- `id`: Primary Key  
- `user`: ForeignKey(User)  
- `status`: CharField (Pending, Shipped, Delivered)  
- `total_price`: DecimalField  
- `created_at`: DateTimeField  
- `updated_at`: DateTimeField  

### OrderItem
- `id`: Primary Key  
- `order`: ForeignKey(Order)  
- `product`: ForeignKey(Product)  
- `quantity`: IntegerField  
- `price`: DecimalField (price at purchase)  

---

## Getting Started With The Project

### API Documentation
Swagger documentation is available at:

[http://127.0.0.1:8000/swagger/](https://phimart-kappa.vercel.app/swagger/)

Redoc documentation is available at:

http://127.0.0.1:8000//swagger/

### Environmental Variables
Create a `.env` file in the root directory and add the follwong:
````

````

### Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/Moniruzzaman-Shawon/Phimart.git
   cd Phimart
   ````
2. Create and activate a virtual environment
````
python -m venv .env # To create virual environment

.\.env\Scripts\Activate # Windows PowerShell

source .env/bin/activate # macOS/Linux
````
3. Install dependencies
````
pip install -r requirements.txt
````
4. Run migrations

````
python manage.py migrate
````
5. Create superuser (optional)
````
python manage.py createsuperuser
````
6. Start development server
````
python manage.py runserver
````


## Usage
Access the API at http://localhost:8000/api/

Use an API client like Postman or the DRF browsable API to interact with endpoints

Use JWT tokens to authenticate protected endpoints


## License
MIT License © 2025 Moniruzzaman Shawon
