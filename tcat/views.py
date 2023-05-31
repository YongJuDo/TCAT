from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from .models import Tcat
from .forms import TcatForm
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import base64

# Create your views here.
def index_redirect(request):
    return redirect('tcat:index')

def index(request):
    # 인터파크 크롤링
    current_date = datetime.now().strftime("%Y%m%d")
    interpark_total_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=P&pCate=&pType=D&pDate={}'.format(current_date)
    interpark_total_res = requests.get(interpark_total_url)
    interpark_total_soup = BeautifulSoup(interpark_total_res.text, 'html.parser')

    # 종합
    interpark_total = []
    for item in interpark_total_soup.select('.rankingContent.detailBodyList')[:5]:
        link = item.select_one('.prdImg')['onclick']
        product_id = re.search(r"Go\('(\d+)'", link)
        if product_id:
            product_link = product_id.group(1)
        image = item.select_one('.prdImg img')['src']
        title = item.select_one('.prdInfo > a > b').text.strip()
        period = item.select_one('.prdDuration').text.strip()
        interpark_total.append({'product_link': product_link, 'title': title, 'image': image, 'period': period})

    # 스포츠
    interpark_sport_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=RK811&pCate=&pType=D&pDate={}'.format(current_date)
    interpark_sport_res = requests.get(interpark_sport_url)
    interpark_sport_soup = BeautifulSoup(interpark_sport_res.text, 'html.parser')
    
    interpark_sport = []
    for item in interpark_sport_soup.select('.rankingContent.detailBodyList')[:5]:
        link = item.select_one('.prdImg')['onclick']
        product_id = re.search(r"Go\('(\d+)'", link)
        if product_id:
            product_link = product_id.group(1)
        image = item.select_one('.prdImg img')['src']
        title = item.select_one('.prdInfo > a > b').text.strip()
        period = item.select_one('.prdDuration').text.strip()
        interpark_sport.append({'product_link': product_link, 'title': title, 'image': image, 'period': period})

    # 행사 / 전시
    interpark_exhibitions_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=01008&pCate=&pType=D&pDate={}'.format(current_date)
    interpark_exhibitions_res = requests.get(interpark_exhibitions_url)
    interpark_exhibitions_soup = BeautifulSoup(interpark_exhibitions_res.text, 'html.parser')
    
    interpark_exhibitions = []
    for item in interpark_exhibitions_soup.select('.rankingContent.detailBodyList')[:5]:
        link = item.select_one('.prdImg')['onclick']
        product_id = re.search(r"Go\('(\d+)'", link)
        if product_id:
            product_link = product_id.group(1)
        image = item.select_one('.prdImg img')['src']
        title = item.select_one('.prdInfo > a > b').text.strip()
        period = item.select_one('.prdDuration').text.strip()
        interpark_exhibitions.append({'product_link': product_link, 'title': title, 'image': image, 'period': period})


    context = {
        'interpark_total': interpark_total,
        'interpark_sport': interpark_sport,
        'interpark_exhibitions': interpark_exhibitions,
    }

    return render(request, 'tcat/index.html', context)


def detail(request, tcat_pk):
    tcat = Tcat.objects.get(pk=tcat_pk)
    context = {
        'tcat': tcat,
    }
    return render(request, 'tcat/detail.html', context)


def create(request):
    if request.method == 'POST':
        tcat_form = TcatForm(request.POST, request.FILES)

        if tcat_form.is_valid():
            tcat = tcat_form.save(commit=False)
            tcat.user = request.user
            tcat.save()

        if tcat.image:
            tcat.image_url = settings.MEDIA_URL + str(tcat.image)
            tcat.save()

            return redirect('tcat:detail', tcat.pk)
        
        else:
            return redirect('tcat:detail', tcat.pk)
    else:
        tcat_form = TcatForm()

    context = {
        'form': tcat_form,
    }

    return render(request, 'tcat/create.html', context)


def all_events(request):
    all_events = Tcat.objects.all()
    out = []
    for event in all_events:
        out.append({
            'date': event.date,
            'title': event.title,
            'image_url': event.image_url,
        })

    return JsonResponse(out, safe=False)

@csrf_exempt
def capture(request):
    data = request.POST.__getitem__('data')
    data = data[22:] #앞의 필요없는 부분 제거

    filename = 'calendar.png'
    img_path  = settings.MEDIA_ROOT+ '/'+ filename
    
    image = open(img_path, "wb")
    # `base64.b64decode()`를 통하여 디코딩을 하고 파일에 써준다.
    image.write(base64.b64decode(data))
    image.close()

    # filename을 json형식에 맞추어 response를 보내준다.
    answer = {'filename': filename}

    return JsonResponse(answer)


def kakao_image_search(request):
    query = request.GET.get('query')  # 검색할 쿼리 파라미터를 가져옵니다.
    REST_API_KEY = '8969178c6cfa4eeab6adcea83593d5aa'  # 위에서 얻은 REST API 키를 입력합니다.

    headers = {
        "Authorization": "KakaoAK {}".format(REST_API_KEY)
    }

    params = {
        "query": query
    }

    response = requests.get("https://dapi.kakao.com/v2/search/image", headers=headers, params=params)
    result = response.json()

    return JsonResponse(result)  # 검색 결과를 반환합니다.

def naver_image_search(request):
    query = request.GET.get('query')  # 검색할 쿼리 파라미터를 가져옵니다.
    CLIENT_ID = '6QiN42Ji89EyMmmQ685s'  # 네이버 개발자 센터에서 얻은 클라이언트 ID
    CLIENT_SECRET = 's39U1HlM5h'  # 네이버 개발자 센터에서 얻은 클라이언트 비밀키

    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }

    params = {
        "query": query,
        "display": 10,
        "start": 1,
        "sort": "sim"
    }

    response = requests.get("https://openapi.naver.com/v1/search/image", headers=headers, params=params)
    result = response.json()

    return JsonResponse(result)
