# 🛒 E-Commerce API – Django Rest Framework

This is a backend API for an e-commerce application built using **Django Rest Framework**, **JWT authentication**, **PostgreSQL**, and planned support for **Redis** and **Django Channels**. It supports core functionalities such as user registration, product and category management, and order handling.

> ⚠️ **Note:** Caching (Redis) and WebSocket-based notifications (Django Channels) are currently in progress.

---

## 🚀 Features

- ✅ User registration & JWT authentication
- ✅ Product & category CRUD operations
- ✅ Order creation and management
- ✅ Pagination for product listing
- ✅ Admin panel for backend management

---

## 📂 Project Structure

```
E-Commerce/
├── api/                # Core app logic (models, views, serializers)
├── ecommerce/          # Project settings
├── media/              # Uploaded files
├── static/             # Static assets
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Tech Stack

- **Framework:** Django, Django REST Framework
- **Auth:** JWT (SimpleJWT)
- **Database:** PostgreSQL
- **Upcoming:** Redis, Django Channels
- **Language:** Python

---

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/KushagraMahalwal/E-Commerce.git
cd E-Commerce
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

| Method | Endpoint           | Description                 |
|--------|--------------------|-----------------------------|
| POST   | `/api/register/`   | Register new user           |
| POST   | `/api/token/`      | Obtain JWT token            |
| GET/POST | `/api/products/` | List or create products     |
| GET/POST | `/api/categories/`| List or create categories  |
| GET/POST | `/api/orders/`   | Create/view orders          |

> Use tools like **Postman** or **cURL** to test these endpoints.

---

## 🔐 Authentication

This project uses JWT authentication via `djangorestframework-simplejwt`.

Add the following header to authenticate API requests:

```
Authorization: Bearer <your_access_token>
```

---

## 🛠 Future Enhancements

- [ ] Redis-based caching for product listing
- [ ] Real-time WebSocket updates for order status
- [ ] Docker support
- [ ] Swagger/OpenAPI documentation

---

## 👨‍💻 Author

**Kushagra Mahalwal**  
📧 [mahalwalkushagra@gmail.com](mailto:mahalwalkushagra@gmail.com)  
🔗 [GitHub Profile](https://github.com/KushagraMahalwal)

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use it for personal or commercial purposes.
