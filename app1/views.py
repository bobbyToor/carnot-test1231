import json
from django.http import HttpResponse,  HttpResponseNotFound, HttpResponseServerError, JsonResponse
from django.shortcuts import render
from app1.models import Book, School, Student
from app1.services.student import create, search, data_by_id


def index(request):
    return HttpResponse("Hello, world")


def student_data(request, id):
    try:

        response = data_by_id(id)
        return JsonResponse(response)

    except Student.DoesNotExist:
        return HttpResponseNotFound('Not found')
    except Exception as e:
        return HttpResponseServerError(json.dumps({'error': e.args}))


def student(request):

    try:
        # student search
        if request.method == 'GET':
            search_by = request.GET.get('search_by', None)
            key = request.GET.get('key', None)

            response = search(search_by, key)
            return JsonResponse(response, safe=False)

        # student create
        if request.method == 'POST':
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            email = request.POST.get('email', None)
            gender = request.POST.get('gender', None)
            school_id = request.POST.get('school_id', None)
            book_id = request.POST.get('book_id', None)

            response = create(first_name, last_name, email,
                              gender, school_id, book_id)

            return JsonResponse(response, safe=False)

    except Student.DoesNotExist:
        return HttpResponseNotFound('Not found')
    except Exception as e:
        return HttpResponseServerError(json.dumps({'error': e.args}))


def student_search_page(request):
    return render(request, 'search.html')


def student_create_page(request):
    # get all schools and books data for selection
    schools = School.objects.all()
    books = Book.objects.all()

    data = {
        'schools': [{'id': s.id, 'name': s.name} for s in schools],
        'books': [{'id': b.id, 'name': b.title} for b in books],
    }

    return render(request, 'student_create.html', data)
