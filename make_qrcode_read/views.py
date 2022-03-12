from django.shortcuts import render
from django.http import FileResponse
import qrcode

# Create your views here.

def home(request):
    if request.method=='POST':
        url = request.POST['url']
        generate_qr_code(url=url)
        print(generate_qr_code(url=url))
        # return render(request, 'result.html')
    return render(request, 'home.html')

def generate_qr_code(url):
    img = qrcode.make(url)
    img.save('static/img/qr_code.png')
    return 'static/img/qr_code.png'
    
    # return img
