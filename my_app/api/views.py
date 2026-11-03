from django.http import JsonResponse
from my_app.models import Book


def hello_world(request):
    return JsonResponse({"message": "Hello World"})


def book_list(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)


def book_detail(request, book_id):
    book = Book.objects.values().get(id=book_id)
    return JsonResponse(book)
