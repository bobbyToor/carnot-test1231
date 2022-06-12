from unicodedata import name
from django.core.management.base import BaseCommand
import datetime
import xlrd
from app1.models import Book, School, Student

from carnot.settings import SAMPLE_DATA_FILEPATH


class Command(BaseCommand):
    help = 'Creates sample data to play with'

    def handle(self, *args, **options):
        self.populate_data()

    def populate_data(self):

        self.stdout.write(self.style.NOTICE(
            '--Populating sample data--'))

        # clear all data first
        School.objects.all().delete()
        Book.objects.all().delete()
        Student.objects.all().delete()

        workbook = xlrd.open_workbook(SAMPLE_DATA_FILEPATH)

        # insert schools
        school_sheet = workbook.sheet_by_index(1)
        schools = []

        for row in range(1, school_sheet.nrows):

            school = School()

            school.region = school_sheet.cell_value(row, 0)
            school.name = school_sheet.cell_value(row, 1)
            school.email = school_sheet.cell_value(row, 2)
            school.principal = school_sheet.cell_value(row, 3)
            school.phone = school_sheet.cell_value(row, 4)
            school.address = school_sheet.cell_value(row, 5)

            schools.append(school)

        School.objects.bulk_create(schools)

        # insert books
        book_sheet = workbook.sheet_by_index(2)
        books = []

        for row in range(1, book_sheet.nrows):

            book = Book()

            book.title = book_sheet.cell_value(row, 0)
            book.author_name = book_sheet.cell_value(row, 1)
            book.pages = book_sheet.cell_value(row, 3)

            date_value = book_sheet.cell_value(row, 2)
            if date_value:
                date_formatted = datetime.datetime(
                    *xlrd.xldate_as_tuple(date_value, workbook.datemode)).isoformat()
            else:
                date_formatted = ''

            book.publishing_date = date_formatted

            books.append(book)

        Book.objects.bulk_create(books)

        student_sheet = workbook.sheet_by_index(0)

        # insert students
        students = []

        for row in range(1, student_sheet.nrows):

            student = Student()

            student.first_name = student_sheet.cell_value(row, 1)
            student.last_name = student_sheet.cell_value(row, 2)
            student.email = student_sheet.cell_value(row, 3)
            student.gender = student_sheet.cell_value(row, 4)

            school_name = student_sheet.cell_value(row, 5)
            school = School.objects.filter(name=school_name).first()
            student.school = school

            book_title = student_sheet.cell_value(row, 6)
            book = Book.objects.filter(title=book_title).first()
            student.book = book

            students.append(student)

        Student.objects.bulk_create(students)

        self.stdout.write(self.style.SUCCESS(
            '--Sample data inserted--\n'))
