from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name="أسم الخدمة")
    description = models.TextField(
        max_length=500, blank=True, verbose_name="وصف الخدمة")
    short_description = models.TextField(
        max_length=250, blank=True, verbose_name="وصف مختصر للخدمة")
    image = models.ImageField(upload_to='services/',
                              verbose_name='صورة الخدمة ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "الخدمات"


SERVICE_TYPE = [
    ("private",
     "الفيلات الخاصة "),
    ("educational", "الجامعات والمدارس"),
    ("companies", "الشركات"),
    ("malls", "المولات و المحلات")
]


class Project(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(
        upload_to='projects/', verbose_name='الصورة الرئيسة للمشروع')
    slug = models.SlugField(max_length=50, allow_unicode=True, unique=True)
    description = models.CharField(
        max_length=250,  blank=True, verbose_name='وصف المشروع')
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE)
    image1 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image2 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image3 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image4 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image5 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image6 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image7 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image8 = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title


class Request(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20)
    info = models.TextField(max_length=250)
    time = models.DateTimeField(auto_now_add=True)
    service_type = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(max_length=250, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
