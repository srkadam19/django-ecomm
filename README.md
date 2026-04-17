# django-ecomm


Prerequisites
Python 3.10+
PostgreSQL 17
Git
Commands (in order)

# 1. Clone the project
git clone <your-repo-url>
cd django-admin

# 2. Install dependencies
pip install django djangorestframework psycopg2-binary Pillow

# 3. Start PostgreSQL & create database
pg_ctl -D "C:/Program Files/PostgreSQL/17/data" start
psql -U postgres -c "CREATE DATABASE ecommerce_db;"

# 4. Run migrations
python manage.py migrate

# 5. Seed sample data (18 products, 5 categories, admin user)
python manage.py seed_data

# 6. Run the server
python manage.py runserver
Then open http://127.0.0.1:8000/ in the browser.

Important: If the other laptop has a different PostgreSQL username/password, update ecommerce/settings.py:63-65 (USER and PASSWORD fields) before running migrate.

Admin login: admin / admin123

SSR