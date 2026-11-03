# Django Demo

Minimal Django project with a small JSON API: a hello world endpoint and a book endpoint.

## Setup

```bash
git clone https://github.com/bjoerndaigger/django-course-0326.git
cd django-course-0326

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

The server runs at http://127.0.0.1:8000/.

## API Endpoints

| Method | URL             | Description                  |
| ------ | --------------- | ---------------------------- |
| GET    | `/hello/`       | Returns a hello world message |
| GET    | `/books/`       | Returns a list of all books  |
| GET    | `/books/<id>/`  | Returns a single book by ID  |

Example:

```bash
curl http://127.0.0.1:8000/hello/
# {"message": "Hello World"}
```

### Book model

| Field          | Type      |
| -------------- | --------- |
| `title`        | string (max. 200) |
| `author`       | string (max. 100) |
| `pages`        | integer   |
| `published`    | date      |
| `is_available` | boolean (default: `True`) |

Books can be added via the Django admin (`/admin/`). Create an admin user first:

```bash
python manage.py createsuperuser
```

## Project Structure

```
core/              Project settings and root URL configuration
my_app/
├── models.py      Book model
├── admin.py       Admin configuration
└── api/
    ├── urls.py    API routes
    └── views.py   API views
```
