from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', UserList.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('verify/<int:user_pk>/<str:token>', VerifyEmailView.as_view(), name='verify'),
    path('positive/', Positive.as_view(), name='positive'),
    path('negative/', Negative.as_view(), name='negative'),
]
