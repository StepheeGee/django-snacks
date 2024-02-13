from django.urls import path
from .views import home, about

app_name = 'snacks'  # This is used by the {% url %} template tag to reference the correct URL pattern

urlpatterns = [
    path('', home, name='home'),      # Maps to the home view
    path('about/', about, name='about'),  # Maps to the about view
  
]
