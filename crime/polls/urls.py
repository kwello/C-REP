from django.urls import path
from django.contrib import admin

from polls import views

urlpatterns = [
 path('',views.open),
 #path('thankyou/', polls_views.responseform),

#path('', admin.site.urls),
]
