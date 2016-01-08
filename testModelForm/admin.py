from django.contrib import admin

# Register your models here.
from models import TestData
admin.site.register(TestData)

from models import Book
admin.site.register(Book)


from models import FieldTest
admin.site.register(FieldTest)
