from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название раздела')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)


class Mark(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Марка кондиционера')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='image/')
    cats = models.ForeignKey(Categories, on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)


class Series(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Серия кондиционера')
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='image/')
    marks = models.ForeignKey(Mark, on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)


class Cond(models.Model):

    ELITE = '17Wp4QmlaSk65Z1x_irI_KqHFzmYkEhfWxFQafTPXgKQ'
    MAG_COLD = '1mNxqsxE_AkvzWcFBcnzyYGNf6AXl1MXhQRI0H0etL4Y'

    PROVIDER_CHOICES = [
        (ELITE, 'Элитхолод'),
        (MAG_COLD, 'Магазин холода'),
    ]

    name = models.CharField(max_length=255, unique=True, verbose_name='Модель кондиционера')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    description = models.TextField(verbose_name="Описание")
    provider = models.CharField(max_length=64, choices=PROVIDER_CHOICES, db_index=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='image/')
    series = models.ForeignKey(Series, on_delete=models.PROTECT, db_index=True)
    price_cell = models.CharField(max_length=10, verbose_name='Ячейка с ценой в прайсе', null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    phone = PhoneNumberField(null=False, help_text='Введите номер телефона')
    name = models.CharField(max_length=16, verbose_name='Имя заказчика', help_text='Ваше имя')
    conder = models.ForeignKey(Cond, on_delete=models.CASCADE)
    result = models.FloatField(default=0, verbose_name='Стоимость')
    datecreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.conder)
