from django.urls import path
from django.http import JsonResponse

def placeholder(request):
    return JsonResponse({'detail': 'categories endpoints placeholder'})

urlpatterns = [
    path('', placeholder),
]
