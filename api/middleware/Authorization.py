from django.http import HttpResponse
from api.models.Login import Login


class HeaderValidationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code that is executed in each request before the view is called

        response = self.get_response(request)

        # Code that is executed in each request after the view is called
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if(request.META.get('HTTP_AUTHORIZATION') == None):

            return HttpResponse('Nenhum token foi informado', status=201)

        try:
            login = Login.objects.get(token=request.META.get('HTTP_AUTHORIZATION'))
        except:
            return HttpResponse('Token inválido', status=201)


         
        
