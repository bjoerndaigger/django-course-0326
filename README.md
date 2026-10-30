# Django Demo

Minimal Django project with a hello world endpoint.

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

Open http://127.0.0.1:8000/hello/ in your browser.
