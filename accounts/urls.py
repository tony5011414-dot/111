from django.urls import path
from django.http import JsonResponse

def placeholder(request):
    return JsonResponse({'detail': 'accounts endpoints placeholder'})

urlpatterns = [
    path('', placeholder),
]
