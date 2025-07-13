# 💰 Expense Tracker - Django Project

A personal expense tracking system built with Django that allows users to register, log in, and manage their own income and expense transactions. All features are user-specific and wrapped in a sleek, responsive UI.

---

## 📌 Overview

This Django project allows users to:
- Register, login, logout securely
- Track income and expenses
- Filter transactions by date and category
- Search by description
- View total income, expenses, and balance
- Export filtered data to CSV
- Visualize data with charts
- Toggle light/dark mode with theme persistence

---

## 🔧 Features

- ✅ User Authentication (Signup/Login/Logout)
- ✅ Remember Me checkbox
- ✅ Toast messages on success/error (login, signup, logout)
- ✅ Per-user data (each user only sees their own transactions)  
- ✅ Add / Edit / Delete transactions
- ✅ Filter by category and date range
- ✅ Search by description
- ✅ Export to CSV
- ✅ Chart.js pie chart of expenses by category
- ✅ Auto-dismissing toast messages (Login / Logout / Actions)
- ✅ Fully responsive UI (Bootstrap 5)
- ✅ Dark Mode Toggle (persisted using localStorage)
- ✅ Styled forms (login, signup, add/edit transaction)

---

## 🛠 Tech Stack

- Django (Python)
- SQLite (default DB)
- HTML + Bootstrap 5
- Chart.js (for visualizing expenses)
- JavaScript (localStorage, theme toggle, toasts)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip
- Virtualenv (recommended)

---

### Installation

```bash
# Clone the repo
git clone https://github.com/MuazamAbbas/expense-tracker.git
cd expense-tracker

# Setup virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver

# Open in browser
http://127.0.0.1:8000/


📁 Folder Structure
expense_tracker/
├── expense_tracker/          # Django project (settings, urls)
├── tracker/                  # App (models, views, templates)
│   ├── templates/tracker/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── static/                   # (optional) static assets
├── manage.py
├── requirements.txt

🔐 Authentication Flow
Sign Up page (/signup)

Login page (/login)

Only logged-in users can access the dashboard (transactions)

Each user can only access their own transactions

📤 Export CSV
Filter your transactions (by category/date), and click Export CSV to download your data instantly.


🌗 Dark Mode
Toggle between Light and Dark mode.
Theme preference is saved using localStorage and applies globally:

-> Home page

-> Add Transaction

-> Edit Transaction

-> Login / Signup



🔔 Toast Messages
All success/error actions like login, logout, signup, and transaction updates trigger toast alerts with auto-dismiss after 3 seconds.

🔍 Search
You can search your transactions by description.
Search is case-insensitive and works alongside filters.
“Reset” button clears all filters.

📊 Chart Summary
Expense transactions are visualized in a pie chart by category using Chart.js.

🧪 Test Accounts
You can register a new user or log in with a superuser.

📄 License
This project is open-source and available under the MIT License.

👤 Author
Muazam Abbas
GitHub: MuazamAbbas