from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
import re
import requests
import json

from .models import *
from .forms import OrderForm
# from .parser import values

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def index(request):
    cats = Categories.objects.all()
    context = {
        'cats': cats
    }
    return render(request, 'nanostroi/index.html', context=context)


def get_marks_list(request, category_slug):
    marks = Mark.objects.filter(cats__slug=category_slug)
    template_name = 'nanostroi/mark.html'

    context = {
        'marks': marks,

    }
    return render(request, template_name, context=context)


def get_series_list(request, mark_slug):
    series = Series.objects.filter(marks__slug=mark_slug)
    template_name = 'nanostroi/ser.html'
    context = {
        'series': series,
    }
    return render(request, template_name, context=context)


def get_cond_list(request, ser_slug):
    conds = Cond.objects.filter(series__slug=ser_slug)
    template_name = 'nanostroi/cond.html'
    context = {
        'conds': conds,
    }
    return render(request, template_name, context=context)


def get_price(cond):
    CREDENTIALS_FILE = 'credent/creds.json'
    spreadsheet_id = cond.provider

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    c = cond.price_cell  # ячейка в прайсе
    d = f'ДЛЯ ЗАЛИВКИ!{c}'  # название листа и номер ячейки в прайсе
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=d,
        majorDimension='ROWS'
    ).execute()
    cellValues = values.get('values')  # значение из прайса получаем в двумерном массиве
    # print('cV ', cellValues)
    value = cellValues[0][0]  # достаем значения из массива
    # print('val ', value)
    val = re.findall(r'\d+', value)  # убираем из значения в ячейке пробелы и другие знаки, оставляем цифры
    if len(val) > 1:
        v = val[0] + val[1]
        cost = int(v)
    else:
        v = val[0]
        cost = int(v)
    cost += round((cost * cond.discount) / 100)
    print('cost1 ', cost)
    return cost


def get_nbrb_cost(cost):
    r = requests.get(f'https://www.nbrb.by/api/exrates/rates/usd?parammode=2')
    total_base = json.loads(r.content)
    result = cost * total_base["Cur_OfficialRate"]
    result = round(result)
    return result


def get_cond(request, cond_slug):
    cond = Cond.objects.get(slug=cond_slug)
    template_name = 'nanostroi/order.html'
    cost = get_price(cond)  # получаем из гугл-таблицы стоимость в валюте
    result = get_nbrb_cost(cost)  # берем курс нб и получаем стоимость в руб
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(conder=cond, name=form.data['name'], phone=form.data['phone'])  # создаем заказ
            print('ok')
            return redirect('confirm')
    # else:
    #     form = OrderForm()

    context = {
        'cond': cond,
        'result': result,
        'form': form
    }
    return render(request, template_name, context=context)


def order_confirm(request):
    template_name = 'nanostroi/orderview.html'
    # form = OrderForm(request.POST)
    # if form.is_valid():
    #     Order.objects.create(conder=cond, name=form.data['name'], phone=form.data['phone'], result=result)
    #     print('ok')
    #     return redirect('hello')
    return render(request, template_name)