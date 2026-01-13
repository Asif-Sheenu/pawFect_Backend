from django.urls import path
from .views import ProductAddView,ProductfetchView,ProductUpdateView,OrderEditView,OrderListView,AdminDashboardView,AdminUserListView,AdminUserBlockView

urlpatterns= [
    path ('viewproduct/', ProductfetchView.as_view(),name="viewProduct"),
    path ('addproduct/', ProductAddView.as_view(),name="addProduct"),
    path ('editproduct/<int:pk>/', ProductUpdateView.as_view(),name="editProduct"),
   

    path('orders/',OrderListView.as_view(),name = "list_orders"),
    path('ordersedit/<int:pk>/',OrderEditView.as_view(),name = "list_orders"),


    path('dashboard/', AdminDashboardView.as_view()),


    path('users/', AdminUserListView.as_view(),name='admin-users'),
    path('userblock/<int:pk>/', AdminUserBlockView.as_view(),name='admin-userblock'),

]