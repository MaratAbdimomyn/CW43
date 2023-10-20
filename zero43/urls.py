from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', UserList.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup')
]
