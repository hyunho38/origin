from django.http import JsonResponse
from django.views import views

class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200);
        result ={
            'data': data,
            'message': message,
        }
    return JsonResponse(result, status)
