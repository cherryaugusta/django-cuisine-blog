# Django Cuisine Blog

A production-oriented Django web application showcasing professional backend architecture, class-based views, pagination, canonical URLs, and Git workflow discipline.

---

## Overview

This project demonstrates clean Django architecture and production-ready structuring practices suitable for backend engineering portfolios.

---

## Core Features

- Function-Based View (FBV)
- Class-Based Views (CBV)
- Pagination
- Canonical URLs
- Custom model manager
- Media file handling
- Namespaced URL configuration
- Secure settings configuration
- Structured Git commit history

---

## Architecture Highlights

- Separation of concerns
- DRY template inheritance
- Custom `PublishedManager`
- `get_absolute_url()` canonical routing
- Modular URL namespacing
- Static and media best practices

---

## Installation

```
git clone https://github.com/cherryaugusta/django-cuisine-blog.git
cd django-cuisine-blog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Access:
```
http://127.0.0.1:8000/cuisine/
```
---

## Project Structure
```
config/        # Core project configuration
cuisine/       # Application logic
static/        # Static assets
media/         # Uploaded media
```

---

## Git Strategy
•	Atomic commits
•	Architectural progression
•	Clean repository structure
•	Professional .gitignore

---

## Educational & Portfolio Disclaimer
This project is created strictly for educational purposes and professional portfolio demonstration.
It is not intended for commercial deployment without additional production hardening.

---

## License
MIT License
