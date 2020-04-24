from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Django")

def sorry(request):
    params = {
        'title':'Hello There!',
        'msg':'現在サイトが混みあっております。\n時間を空けてアクセスして頂きますようお願い申し上げます。',
    }
    return render(request, 'next/sorry.html', params)