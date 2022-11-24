from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет! Едем дальше!')


def second_page(request):
    return HttpResponse('А это вторая страница!')  # ! добавлен
