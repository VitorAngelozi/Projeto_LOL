from django.urls import path
from .views import Homepage, Clipezudos, DescricaoClipezudo

app_name = 'filme'
urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('clipezudos/', Clipezudos.as_view(), name='clipezudos'),
    path('clipezudos/<int:pk>', DescricaoClipezudo.as_view(), name='detalhes_clipezudos'),
]