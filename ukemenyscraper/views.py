from django.shortcuts import render
from django.http import HttpResponse
from ukemenyscraper.scraper import simple_get
from bs4 import BeautifulSoup 
from datetime import * 

# Create your views here.
#def uke_meny(request):
    #return render(request, 'ukemenyscraper/uke_meny.html', {})
def ukensmatprat(request):
  raw_html = simple_get("https://www.matprat.no/artikler/middagstips/ukemeny-uke-412018/")
  html = BeautifulSoup(raw_html, 'html.parser')
  table = html.find("div", {"class":"rich-text"}).findAll('p')
  #table_text = ''
  #for p in table:
    #table_text = p.findAll(text = True)
    #html_table = "<html><body> %s</body></html>" % table_text
  return HttpResponse(table)



