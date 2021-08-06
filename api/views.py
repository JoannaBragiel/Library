from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Publication_API


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/api_book_list/',
        'Detail View':'/api_book_detail/<int:pk>/',
        'Create':'/api_book_create/',
        'Update':'/api_book_update/<int:pk>/',
        'Delete':'/api_book_delete/<int:pk>/',
    }

    return Response(api_urls, template_name='api/rest_page.html')


@api_view(['GET'])
def api_book_list(request):
    api_book = Publication_API.objects.all()
    serializer = BookSerializer(api_book, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_book_detail(request, pk):
    api_book = Publication_API.objects.get(id=pk)
    serializer = BookSerializer(api_book, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def api_book_create(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def api_book_update(request, pk):
    api_book = Publication_API.objects.get(id=pk)
    serializer = BookSerializer(instance=api_book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def api_book_delete(request, pk):
    api_book = Publication_API.objects.get(id=pk)
    api_book.delete()

    return Response('Item succsesfully delete!')