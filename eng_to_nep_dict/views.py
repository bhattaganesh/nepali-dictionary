from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
from bs4 import BeautifulSoup as bs

def index(request):
    if request.method == 'POST':
        word = request.POST['word']
        if len(word):
            payload = {'q': word}
            req = requests.get('https://www.englishnepalidictionary.com/', params=payload).text
            # print(dir(req))
            soup = bs(req, 'lxml')
            result = soup.find('div', class_='search-result').h3.text
            # print(result)
            return render(request, 'index.html',{'result': result, 'word': word})

        else:
            messages.error(request, 'Please, invalid wold.')
            return redirect(request.META.get("HTTP_REFERER"))
    return render(request, 'index.html')