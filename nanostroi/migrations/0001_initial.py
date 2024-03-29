# Generated by Django 4.2.7 on 2024-01-02 17:00

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название раздела')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Модель кондиционера')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('provider', models.CharField(choices=[('17Wp4QmlaSk65Z1x_irI_KqHFzmYkEhfWxFQafTPXgKQ', 'Элитхолод'), ('1mNxqsxE_AkvzWcFBcnzyYGNf6AXl1MXhQRI0H0etL4Y', 'Магазин холода')], db_index=True, max_length=64, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('price_cell', models.CharField(max_length=10, null=True, verbose_name='Ячейка с ценой в прайсе')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Марка кондиционера')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nanostroi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Серия кондиционера')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('marks', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nanostroi.mark')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите номер телефона', max_length=128, region=None)),
                ('name', models.CharField(help_text='Ваше имя', max_length=16, verbose_name='Имя заказчика')),
                ('result', models.FloatField(default=0, verbose_name='Стоимость')),
                ('datecreation', models.DateTimeField(auto_now_add=True)),
                ('conder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nanostroi.cond')),
            ],
        ),
        migrations.AddField(
            model_name='cond',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nanostroi.series'),
        ),
    ]
