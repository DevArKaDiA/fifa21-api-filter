from rest_framework import status
from django.http import HttpResponse
import os



class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        apiKey = os.getenv('API_KEY')
        if apiKey != None:
            if not('x-api-key' in request.headers and request.headers['x-api-key'] == str(apiKey)):
                return HttpResponse({'Unauthorized': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        response = self.get_response(request)        

        # Code to be executed for each request/response after
        # the view is called.

        return response