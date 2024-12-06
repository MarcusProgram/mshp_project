from django.shortcuts import render

def index_page(request):
    context = {
        'course_name': 'Курс "Промышленное программирование"',
        'author_name': 'Константин',
        'page_count': 1,
    }
    return render(request, 'index.html', context)
