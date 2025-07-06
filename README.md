# 💰 Expense Tracker - Django Project

A complete expense tracking web application built with Django. It helps users manage income and expenses with ease. Includes features like filtering, charts, dark mode, CSV export, and more.

---

## 📌 Overview

This Django project allows users to:
- Track income and expenses
- Filter transactions by date and category
- Search by description
- View summary statistics
- Export to CSV
- Toggle dark/light themes

---

## 🔧 Features

- ✅ Add / Edit / Delete transactions
- ✅ Filter by category and date range
- ✅ Search by description
- ✅ Export to CSV
- ✅ Pie chart by category (Chart.js)
- ✅ Responsive design with Bootstrap
- ✅ Persistent Dark Mode (via localStorage)

---

## 🛠 Tech Stack

- Django (Python)
- SQLite (default DB)
- HTML + Bootstrap 5
- Chart.js (for graphs)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip
- Virtualenv (recommended)

### Installation

```bash
# Clone the repo
git clone https://github.com/MuazamAbbas/expense-tracker.git
cd expense-tracker

# Setup virtual environment
python -m venv venv
venv\\Scripts\\activate    # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver


Visit: http://127.0.0.1:8000/

# 🗃 Folder Structure
expense_tracker/
├── expense_tracker/          # Settings & URLs
├── tracker/                  # App with templates, models, views, etc.
│   ├── templates/tracker/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── manage.py
├── requirements.txt


# 📤 Export CSV
Filter your transactions and download them in .csv format with one click.

#🌗 Dark Mode
Dark mode toggle persists using localStorage. It applies across:

Home

Add Transaction

Edit Transaction

# 🔍 Search
You can search transactions by description (case-insensitive). “Reset” button clears filters and search term.

#📄 License
This project is open-source and available under the MIT License.

# 👤 Author
Muazam Abbas
GitHub: MuazamAbbas