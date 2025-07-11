# 💰 Expense Tracker - Django Project

A full-featured personal expense tracking web app built with Django. Users can manage income and expenses, view insights, toggle dark/light mode, and get real-time feedback using modern UI elements.

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
- ✅ Add / Edit / Delete transactions
- ✅ Filter by category and date range
- ✅ Search by description
- ✅ Export to CSV
- ✅ Pie chart by category (Chart.js)
- ✅ Responsive Bootstrap UI
- ✅ Dark Mode Toggle (persisted using localStorage)
- ✅ Styled forms (login, signup, add/edit transaction)

---

## 🛠 Tech Stack

- Django (Python)
- SQLite (default DB)
- HTML + Bootstrap 5
- Chart.js (for graphs)
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
User feedback is shown using toast alerts on:

-> Successful login, signup, logout

-> Form errors (like invalid credentials)

Toasts auto-dismiss and are styled according to status (success/danger).

🔍 Search
You can search your transactions by description.
Search is case-insensitive and works alongside filters.
“Reset” button clears all filters.


📄 License
This project is open-source and available under the MIT License.

👤 Author
Muazam Abbas
GitHub: MuazamAbbas