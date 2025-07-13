from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Transaction
from django.db.models import Q
from datetime import datetime
from collections import defaultdict
import csv
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Filtering logic
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if category and category != 'All':
        transactions = transactions.filter(category=category)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    # Searching logic
    search_query = request.GET.get('search')

    if search_query:
        transactions = transactions.filter(description__icontains=search_query)

    # Balance summary
    total_income = sum(t.amount for t in transactions if t.amount > 0)
    total_expense = sum(abs(t.amount) for t in transactions if t.amount < 0)
    balance = total_income - total_expense

    # Chart data (only for expenses)
    category_totals = defaultdict(float)
    for txn in transactions:
        if txn.amount < 0:
            category_totals[txn.category] += abs(txn.amount)

    chart_labels = list(category_totals.keys())
    chart_data = list(category_totals.values())

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'selected_category': category or 'All',
        'start_date': start_date or '',
        'end_date': end_date or '',
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }

    return render(request, 'tracker/home.html', context)



@login_required
def add_transaction(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        description = request.POST['description']
        category = request.POST['category']
        Transaction.objects.create(user=request.user, amount=amount, description=description, category=category)
        return redirect('home')
    return render(request, 'tracker/add_transaction.html')

@login_required
def edit_transaction(request, pk):
    txn = get_object_or_404(Transaction, pk=pk, user=request.user)  # ✅ User check added

    if request.method == "POST":
        txn.amount = request.POST['amount']
        txn.description = request.POST['description']
        txn.category = request.POST['category']
        txn.save()
        return redirect('home')

    return render(request, 'tracker/edit_transaction.html', {'txn': txn})


@login_required
def delete_transaction(request, txn_id):
    txn = get_object_or_404(Transaction, id=txn_id, user=request.user)  # ✅ User check
    txn.delete()
    return redirect('home')


def export_transactions_csv(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Apply same filters
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if category and category != 'All':
        transactions = transactions.filter(category=category)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    # Prepare CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Description', 'Category', 'Amount'])

    for txn in transactions:
        writer.writerow([txn.date.strftime('%Y-%m-%d %H:%M'), txn.description, txn.category, txn.amount])

    return response


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created and logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "There was an error creating your account.")
    else:
        form = SignUpForm()
    return render(request, 'tracker/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # 🔐 Handle Remember Me
            if not request.POST.get('remember'):
                request.session.set_expiry(0)  # Browser close = logout
            else:
                request.session.set_expiry(1209600)  # 2 weeks

            messages.success(request, "Successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
