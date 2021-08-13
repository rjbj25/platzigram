from django.http import HttpResponse
from datetime import date, datetime


def hello_world(request):
    now = datetime.now().strftime('%d/%m/%Y')
    return HttpResponse(f'There is it at {str(now)}')


def hi(request):
    return HttpResponse('Hi')