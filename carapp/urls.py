from django.urls import path
from . import views

urlpatterns=[
  
      path('',views.login,name='login_page'),
      path('login_page',views.loginnew),
      path('accounts_page',views.accounts,name="accounts_page"),
      path('signup_page',views.signup,name='signup_page'),
      path('home_page',views.home,name='home_page'),
      path('rent_page',views.rent,name='rent_page'),
      path('mechanic_page',views.mechanic,name='mechanic_page'),
      path('home_page',views.loginnew,name='home_page'),
      path('manager_page',views.manager,name='manager_page'),
      path('book_page',views.book,name='book_page'),
      path('rent',views.rentnext,name='rent'),
      path('your_page',views.your,name='your_page'),
      path('rent_car',views.rent,name='rent_car'),
      path('addcar_page',views.addpage,name='addcar_page'),
      path('new',views.add,name='new')
]