from django.shortcuts import render
import datetime

# Create your views here.

def dateInfo(request):

    date = datetime.datetime.now()
    name = 'Sonu'
    h = int(date.strftime('%H'))
    greet = ''
    
    if h < 12:
        greet = 'Good Morning!'
    elif h < 16:
        greet = "Good Afternoon"
    elif h < 22:
        greet = "Godd Evening"
    else:
        greet = 'Good Night'

    dict = {

        'name' : name,
        'greet' : greet,
        'date' : date
    }

    return render(request, 'testAppTemplates/index.html', context=dict)
