from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from django.db.models import Q
from datetime import datetime
from collections import defaultdict
import csv
from django.http import HttpResponse

# Create your views here.
def home(request):
    transactions = Transaction.objects.all().order_by('-date')

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




def add_transaction(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        description = request.POST['description']
        category = request.POST['category']
        Transaction.objects.create(amount=amount, description=description, category=category)
        return redirect('home')
    return render(request, 'tracker/add_transaction.html')


def edit_transaction(request, pk):
    txn = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        txn.amount = request.POST['amount']
        txn.description = request.POST['description']
        txn.category = request.POST['category']
        txn.save()
        return redirect('home')

    return render(request, 'tracker/edit_transaction.html', {'txn': txn})


def delete_transaction(request, txn_id):
    txn = get_object_or_404(Transaction, id=txn_id)
    txn.delete()
    return redirect('home')

def export_transactions_csv(request):
    transactions = Transaction.objects.all().order_by('-date')

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