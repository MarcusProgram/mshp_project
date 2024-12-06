from django.shortcuts import render
from datetime import datetime
def index_page(request):
    context = {
        'course_name': 'Курс "Промышленное программирование"',
        'author_name': 'Константин',
        'page_count': 2,
    }
    return render(request, 'index.html', context)


def time_page(request):
    now = datetime.now()
    context = {
        'course_name': 'Курс "Промышленное программирование"',
        'current_date': now.strftime('%d.%m.%Y'),
        'current_time': now.strftime('%H:%M:%S'),
    }
    return render(request, 'time.html', context)


def calc_page(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        a = 0
        b = 0

    result = a + b

    context = {
        'course_name': 'Курс "Промышленное программирование"',
        'first_number': a,
        'second_number': b,
        'sum_result': result,
    }
    return render(request, 'calc.html', context)