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