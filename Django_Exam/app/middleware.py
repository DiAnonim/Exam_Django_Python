from django.shortcuts import render

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return self.get_response(request)
            return render(request, 'error.html')
        return self.get_response(request)