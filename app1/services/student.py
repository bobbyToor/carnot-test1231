from django.db.models import Q
from http.client import HTTPException
from app1.models import Book, School, Student


def data_by_id(id: int):
    student = Student.objects.get(id=id)

    return student_data_parse(student)


def search(search_by, key):

    if search_by == None or key == None:
        raise HTTPException('Empty args')

    if search_by not in ['id', 'name']:
        raise HTTPException('Unknown args')

    if search_by == 'id':
        if key.isdigit():
            students = Student.objects.filter(id=key)
        else:
            students = []

    if search_by == 'name':
        students = Student.objects.filter(Q(
            first_name__icontains=key) | Q(last_name__icontains=key))

    respone = [student_data_parse(s) for s in students]

    return respone


def create(first_name, last_name, email, gender, school_id, book_id):
    if not first_name:
        raise HTTPException('Empty first name')

    student = Student()

    student.first_name = first_name
    student.last_name = last_name
    student.email = email
    student.gender = gender

    school = School.objects.get(id=school_id)
    student.school = school

    book = Book.objects.get(id=book_id)
    student.book = book

    student.save()

    return student_data_parse(student)


def student_data_parse(student: Student):
    return {
        'full_name': student.first_name + ' ' + student.last_name,
        'email': student.email,
        'gender': student.gender,
        'school_name': student.school.name if student.school else None,
        'school_phone': student.school.phone if student.school else None,
        'books_read': student.book.title if student.book else None,
        'pages_read': student.book.pages if student.book else None
    }
