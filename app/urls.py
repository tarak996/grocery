from django.urls import path
from . import views

app_name = "app"

urlpatterns = [

    # User pages
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.contact, name="contact"),
    path("all-products/", views.AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", views.ProductDetailView.as_view(), name="productdetail"),
    path("add-to-cart-<int:pro_id>/", views.AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", views.MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", views.ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", views.EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("register/",views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", views.CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", views.CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", views.CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", views.CustomerOrderDetailView.as_view(),name="customerorderdetail"),
    #path("search/", views.SearchView.as_view(), name="search"),
    path('pay/',views.razorpay,name='pay'),
    
    path('pay/success',views.success,name='success'),
    # Admin pages
    path("admin-login/", views.AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", views.AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", views.AdminOrderDetailView.as_view(),name="adminorderdetail"),
    path("admin-all-orders/", views.AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change/",views.AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),
    path("admin-product/list/", views.AdminProductListView.as_view(),name="adminproductlist"),
    path("admin-users/list/", views.AdminUserListView.as_view(),name="adminuserlist"),
    path("admin-product/add/", views.AdminProductCreateView.as_view(),name="adminproductcreate"),
    path('delete/<int:id>/', views.DeleteView.as_view(),name='delete'),
    path('userdelete/<int:id>/', views.DeleteUserView.as_view(),name='userdelete'),
    path('adminfeedback/',views.adminfeedback,name='adminfeedback')
]
