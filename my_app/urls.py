from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('books', BookViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('library/', TemplateView.as_view(template_name='library.html'), name='library'),
]