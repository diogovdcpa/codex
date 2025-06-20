# Flask Tailwind Application

This repository provides a minimal fullstack application template using **Flask**, **Tailwind CSS**, **SQLite** and **SQLAlchemy** as the ORM.

## Project structure
```
app/
  __init__.py       - Application factory and database setup
  models.py         - SQLAlchemy models
  routes.py         - Application routes
  templates/
    base.html       - Base template with Tailwind
    index.html      - Home page example
  static/           - Static assets
config.py           - Configuration (SQLite database path)
manage.py           - Run the application
requirements.txt    - Python dependencies
```

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python manage.py
   ```
3. Open `http://localhost:5000` in your browser.

Tailwind CSS is included via CDN in `templates/base.html`. Adjust as needed for production setups.
