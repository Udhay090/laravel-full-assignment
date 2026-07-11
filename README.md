# Laravel Assignment

Laravel app with login page, a Selenium script that automates the login form, and a calendar page served through Laravel.

## Structure
- `main-laravel/` — Laravel app (login system + calendar route)
- `selenium-script/` — Python script that auto-fills the login form
- `template-html/` — original HTML calendar template (source for the calendar route)

## Setup

```bash
cd main-laravel
composer install
cp .env.example .env
# set DB credentials in .env
php artisan key:generate
mysql -u root -p -e "CREATE DATABASE myad"
mysql -u root -p myad < db/db.sql
php artisan serve
```

Add to `/etc/hosts`:

**Login page:** `http://da.adlynk.in:8000/login`
**Calendar page:** `http://da.adlynk.in:8000/html-page`

## Automate the login

```bash
cd selenium-script
pip install selenium
python3 login_test.py
```

Opens the login page, fills email + password with dummy values, submits, and exits.
