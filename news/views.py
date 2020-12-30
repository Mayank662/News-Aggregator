from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import headline

def scrape(request):
    url = "https://timesofindia.indiatimes.com/briefs"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    brief = []
    s = 0
    for row in soup.find_all('div', attrs = {'class' : 'brief_box'}):
        brief.append(row)		
    for row in brief:
        if(s >= 10):
            break
        else:
            try:
                title = row.h2.text
                link = row.find('a')['href']
                img = row.find('div', attrs = {'class' : 'posrel'}).find('img')['src']
                headline_obj = headline()
                headline_obj.title = title
                headline_obj.url = 'https://timesofindia.indiatimes.com/'+link
                headline_obj.image = img
                s = s+1
                headline_obj.save()
            except:
                pass
        
    return redirect("../")

def news_list(request):
    headlines = headline.objects.all()
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)