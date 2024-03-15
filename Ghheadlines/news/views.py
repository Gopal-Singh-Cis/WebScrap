from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views import View
from bs4 import BeautifulSoup
from django.views.generic.base import TemplateView, RedirectView 
from .models import ArticleData
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from django.views.generic.detail import DetailView
from django.utils import timezone
from datetime import timedelta

class Home(View):
    def get(self,request):
        article_queryset = ArticleData.objects.all().order_by('-date').values()
        return render(request,"article_list.html",{"article_data":article_queryset})
    
class ArticleFilter(View):
    def post(self,request,*argv, **kwargs):
        form_data = request.POST.get("search")
        article_queryset = ArticleData.objects.filter(title__icontains=form_data).order_by('-date')
        return render(request,"article_list.html",{"article_data":article_queryset})
    
class ArticleFilterByDate(View):
    def get(self,request,parameter):
        today = timezone.now().date()
        if parameter == 'today':
            start_date = today
            end_date = today + timedelta(days=1)
        elif parameter == 'yesterday':
            start_date = today - timedelta(days=1)
            end_date = today
        elif parameter == 'this-month':
            start_date = today.replace(day=1)
            next_month = today.replace(day=28) + timedelta(days=4)
            end_date = next_month - timedelta(days=next_month.day)
        
        article_queryset = ArticleData.objects.filter(date__range=(start_date, end_date)).order_by('-date')
        return render(request,"article_list.html",{"article_data":article_queryset})
    
class ArticleWithSource(View):
    def get(self,request,article_source):
        article_queryset = ArticleData.objects.filter(article_source = article_source).order_by('-date')
        return render(request,"article_list.html",{"article_data":article_queryset})

class ArticleView(DetailView):
        model = ArticleData
        context_object_name = "article"
        template_name = "article_detail_page.html"


def scrape_website1(request):
    try:
        url = 'https://www.myjoyonline.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Scraping article titles
        for div in soup.find_all('div', class_='home-post-list-title'):
        # Find the <a> tag inside the <div>
            a_tag = div.find('a')
            if a_tag:
                # Extract the URL from the href attribute of the <a> tag
                article_url = a_tag['href']
                # Extract the title from the text content of the <a> tag
                article_title = a_tag.text.strip()
                # Optionally, follow the URL and fetch additional details  position-relative share-this-item-show img-holder 
                response = requests.get(article_url)
                if response.status_code == 200:
                    # Parse the linked page content
                    linked_page_soup = BeautifulSoup(response.content, 'html.parser')

                    div_tag = linked_page_soup.find('div', class_='article-meta').find('div')   
                    article_date_str = div_tag.text.strip()
                    article_date = datetime.strptime(article_date_str, '%d %B %Y %I:%M%p').strftime('%Y-%m-%d %H:%M:%S')

                    img_tag = linked_page_soup.find('div', class_='img-holder').find('a').find('img')
                    article_image = img_tag['data-src']

                    for div in linked_page_soup.find_all('div', class_='article-text'): 
                        p_tags = div.find_all('p')
                        p_text_list = [ p_tag.text.strip() for p_tag in p_tags]
                        article_content = ''.join(p_text_list)

            ArticleData.objects.get_or_create(
                title = article_title,
                image = article_image,
                date = article_date,
                content = article_content,
                article_source = 'myjoyonline'
            )
        return JsonResponse({'status': 'success', 'message': 'Scraping completed successfully'})
    
    except requests.RequestException as e:
        return JsonResponse({'status': 'error', 'message': 'Request failed: {}'.format(str(e))})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'An error occurred: {}'.format(str(e))})

def scrape_website2(request):
    try:
        url = 'https://thebftonline.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Scraping article titles
        for div in soup.find_all('div', class_='td-module-thumb'):
        # Find the <a> tag inside the <div>
            a_tag = div.find('a')
            if a_tag:
                # Extract the URL from the href attribute of the <a> tag
                article_url = a_tag['href']
                # Extract the title from the text content of the <a> tag
                article_title = a_tag['title']
                # Optionally, follow the URL and fetch additional details  position-relative share-this-item-show img-holder 
                response = requests.get(article_url)
                if response.status_code == 200:
                    # Parse the linked page content
                    linked_page_soup = BeautifulSoup(response.content, 'html.parser')

                    div_tag = linked_page_soup.find('div', class_='td-module-meta-info').find('time')   
                    article_date = div_tag['datetime']

                    img_tag = linked_page_soup.find('div', class_='td-post-featured-image').find('a').find('img')
                    article_image = img_tag['data-src']

                    for div in linked_page_soup.find_all('div', class_='td-post-content'): 
                        p_tags = div.find_all('p')
                        p_text_list = [ p_tag.text.strip() for p_tag in p_tags]
                        article_content = ''.join(p_text_list)

            ArticleData.objects.get_or_create(
                title = article_title,
                image = article_image,
                date = article_date,
                content = article_content,
                article_source = 'thebftonline'
            )
            return JsonResponse({'status': 'success', 'message': 'Scraping completed successfully'})
    
    except requests.RequestException as e:
        return JsonResponse({'status': 'error', 'message': 'Request failed: {}'.format(str(e))})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'An error occurred: {}'.format(str(e))})