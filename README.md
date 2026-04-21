#  Library Management System API

A RESTful API built with **Django REST Framework** for managing a library — including books, user accounts, and borrowing records. Authentication is handled via **JWT tokens**, and API documentation is available via **Swagger/ReDoc**.

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **API Docs:** Swagger UI & ReDoc (via `drf-yasg`)
- **Filtering:** `django-filters`

---

##  Project Structure

```
Library_management/
├── library/          # Core project settings & root URLs
├── accounts/         # User registration, custom User model, permissions
├── books/            # Book CRUD, pagination, serializers
└── borrow/           # Borrow/return logic, borrow history
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd library
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

This API uses **JWT (JSON Web Tokens)**. Tokens must be included in the `Authorization` header as:

```
Authorization: Bearer <access_token>
```

| Token Type     | Lifetime  |
|----------------|-----------|
| Access Token   | 30 minutes |
| Refresh Token  | 7 days    |

---

## 🔗 API Endpoints

### Auth

| Method | Endpoint               | Description              | Access |
|--------|------------------------|--------------------------|--------|
| POST   | `/api/login/`          | Obtain JWT tokens        | Public |
| POST   | `/api/token/refresh/`  | Refresh access token     | Public |

### Accounts

| Method | Endpoint                | Description       | Access |
|--------|-------------------------|-------------------|--------|
| POST   | `/api/accounts/register/` | Register new user | Public |

### Books

| Method | Endpoint          | Description            | Access           |
|--------|-------------------|------------------------|------------------|
| GET    | `/api/books/`     | List all books         | Authenticated    |
| POST   | `/api/books/`     | Add a new book         | Admin only       |
| GET    | `/api/books/{id}/`| Retrieve a book        | Authenticated    |
| PUT    | `/api/books/{id}/`| Update a book          | Admin only       |
| PATCH  | `/api/books/{id}/`| Partially update a book| Admin only       |
| DELETE | `/api/books/{id}/`| Delete a book          | Admin only       |

**Query Parameters:**
- `search=` — search by title, author, or genre
- `author=`, `genre=`, `is_available=` — filter results
- `ordering=title` or `ordering=author` — sort results
- `page=`, `page_size=` (max 50)

### Borrow

| Method | Endpoint              | Description                   | Access      |
|--------|-----------------------|-------------------------------|-------------|
| GET    | `/api/borrow/`        | List available books to borrow| Member only |
| POST   | `/api/borrow/`        | Borrow a book                 | Member only |
| POST   | `/api/borrow/return/` | Return a borrowed book        | Member only |
| GET    | `/api/borrow/history/`| View all borrow records       | Admin only  |

**Borrow POST body:**
```json
{ "book_id": 1 }
```

**History Query Parameters:**
- `status=borrowed` or `status=returned`
- `due_date=YYYY-MM-DD`
- `user=<user_id>`
- `search=<username or book title>`
- `page=`, `page_size=` (max 20)

---

## 👥 User Roles

| Role     | Capabilities                                               |
|----------|------------------------------------------------------------|
| `member` | Browse books, borrow books, return books                   |
| `admin`  | All member capabilities + full book CRUD + borrow history  |

New users default to the `member` role. Admins can be created via Django's admin panel or `createsuperuser`.

---

##  API Documentation

Interactive docs are available once the server is running:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

##  Data Models

### User
- Extends Django's `AbstractUser`
- Additional field: `role` (`admin` or `member`)

### Book
| Field          | Type        | Description              |
|----------------|-------------|--------------------------|
| `title`        | CharField   | Book title               |
| `author`       | CharField   | Author name              |
| `genre`        | CharField   | Genre                    |
| `book_no`      | CharField   | Unique book identifier   |
| `is_available` | BooleanField| Availability status      |

### BorrowRecord
| Field         | Type      | Description                       |
|---------------|-----------|-----------------------------------|
| `user`        | FK → User | Borrowing user                    |
| `book`        | FK → Book | Borrowed book                     |
| `borrow_date` | DateField | Auto-set on creation              |
| `due_date`    | DateField | Set to 7 days after borrow date   |
| `return_date` | DateField | Set when book is returned         |
| `status`      | CharField | `borrowed` or `returned`          |