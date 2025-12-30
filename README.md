Event Management System

A full-stack web application for managing events, tasks, and staff attendance, built with **Django REST Framework** (backend) and **React** (frontend). Features JWT authentication for secure login and role-based access.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Create, update, and delete events
- Assign tasks to users
- Track task completion
- Record attendance for staff per event
- JWT-based authentication
- React frontend with protected routes

---

## Tech Stack

**Backend:**

- Django 5.x  
- Django REST Framework  
- Simple JWT for authentication  
- SQLite (development) / PostgreSQL (production-ready)

**Frontend:**

- React.js  
- Material-UI (for components)  
- Chart.js (for dashboard charts)  
- Axios (API requests)  

---

## Project Structure

backend/
├── accounts/ # User model & authentication
├── events/ # Event, Task, Attendance apps
├── manage.py
└── db.sqlite3

frontend/
├── src/
│ ├── pages/ # Dashboard, Login, etc.
│ ├── components/ # Reusable components
│ └── api.js # Axios API setup
└── public/

yaml
Copy code

---

## Installation

### Backend

1. Clone the repository:
```bash
git clone https://github.com/banumariwan/event-management-system.git
cd event-management-system/backend
Create a virtual environment:

bash
Copy code
python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Run the server:

bash
Copy code
python manage.py runserver
Frontend
Navigate to frontend folder:

bash
Copy code
cd ../frontend
Install dependencies:

bash
Copy code
npm install
Start the development server:

bash
Copy code
npm start
The app will run at: http://localhost:3000

Usage
Go to http://127.0.0.1:8000/admin to manage events, tasks, and attendance.

Use the React frontend to log in and view the dashboard.

Dashboard includes:

Event statistics

Task progress

Attendance overview

API Endpoints
Auth:

POST /api/login/ → Obtain JWT token

POST /api/refresh/ → Refresh token

Events:

GET /api/events/ → List all events

POST /api/events/ → Create a new event

Tasks:

GET /api/tasks/ → List all tasks

POST /api/tasks/ → Create a task

Attendance:

GET /api/attendances/ → List all attendance records

POST /api/attendances/ → Add attendance

(All endpoints require JWT token in headers except login.)

Contributing
Fork the repository

Create a branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add feature')

Push to the branch (git push origin feature/YourFeature)

Open a Pull Request

License
This project is licensed under the MIT License.
See LICENSE for details.
