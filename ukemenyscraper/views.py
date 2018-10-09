from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from ukemenyscraper.scraper import simple_get
from bs4 import BeautifulSoup 
from datetime import * 

class Recipe:
  title = None
  url = None
  description = None


# Create your views here.
#def uke_meny(request):
    #return render(request, 'ukemenyscraper/uke_meny.html', {})
def ukensmatprat(request):
  raw_html = simple_get("https://www.matprat.no/artikler/middagstips/ukemeny-uke-412018/")
  html = BeautifulSoup(raw_html, 'html.parser')
  table = html.find("div", {"class":"rich-text"}).findAll('p')

  recipes = []
  for recipe_index in range(0, len(table), 3):
    recipe = Recipe()

    title = table[recipe_index]

    if not (title and title.a):
      break

    recipe.title = title.a.get('title')
    recipe.url = title.a.get('href')

    description = table[recipe_index+2]
    recipe.description = description.get_text()
    recipes.append(recipe)

  print(recipes)

  template = loader.get_template('ukemenyscraper/uke_meny.html')

  return HttpResponse(template.render({'recipes': recipes}, request))
