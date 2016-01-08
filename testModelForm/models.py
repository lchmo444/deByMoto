from django.db import models
from datetime import date

class TestData(models.Model):

    LEVELS = [(x,str(x)) for x in range(1, 17)]

    dName         = models.CharField(max_length=30,     default='data_name')
    dDescription  = models.CharField(max_length=300,    default='data_description')
    dLevel        = models.IntegerField(choices=LEVELS, default=11)
    dDate         = models.DateField(auto_now=False,    default=date.today)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.dName



class Book(models.Model):

    bName        = models.CharField(max_length=30,  default='book_name')
    bPrice       = models.IntegerField(default='12000')
    bAuthor      = models.CharField(max_length=30,  default='ABC')
    bReleaseDate = models.DateField(auto_now=False, default=date.today)
    bISBN        = models.CharField(max_length=30,  default='ISBN')


import uuid

class FieldTest(models.Model):

    #fAutoField = models.AutoField
    fBigIntegerField            = models.BigIntegerField(default=1)
    fBooleanField               = models.BooleanField(default=True)
    fCharField                  = models.CharField(default='charField', max_length=30)
    fCommaSeparatedIntegerField = models.CommaSeparatedIntegerField(default="1,2,3,4,5,6,7,8,9", max_length=30)
    fDateField                  = models.DateField(auto_now=False,    default=date.today)
    fDateTimeField              = models.DateTimeField(auto_now=False, auto_now_add=False)
    fDecimalField               = models.DecimalField(default=1.7321, decimal_places=4, max_digits=10)
    fEmailField                 = models.EmailField(default="email@example.com")
    fFloatField                 = models.FloatField(default=1.7321)
    fIntegerField               = models.IntegerField(default=10)
    fGenericIPAddressField      = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, default=None)
    fNullBooleanField           = models.NullBooleanField(default=True)
    fPositiveIntegerField       = models.PositiveIntegerField(default=100)
    fPositiveSmallIntegerField  = models.PositiveSmallIntegerField(default=50)
    fSlugField                  = models.SlugField(max_length=30, default='slug')
    fSmallIntegerField          = models.SmallIntegerField(default=-50)
    fTextField                  = models.TextField(default="text text text text text text text")
    fURLField                   = models.URLField(max_length=200, default='http://localhost')

    #fFileField                  = models.FileField(upload_to="media/")
    #fFilePathField              = models.FilePathField(path="")
    #fImageField
    #fDurationField              = models.DurationField()
    #fTimeField                  = models.TimeField(blank=True)
    #fUUIDField                  = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)





