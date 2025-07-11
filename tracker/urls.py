from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:txn_id>/', views.delete_transaction, name='delete_transaction'),
    path('export-csv/', views.export_transactions_csv, name='export_csv'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
