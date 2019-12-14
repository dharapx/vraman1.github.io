from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    # dest1 = Destination(1, 'KOLKATA', 'THE CITY OF JOY', 800, 'kolkata.jpg', True)
    # dest2 = Destination(2, 'DELHI', 'THE CAPITAL OF INDIA', 900, 'delhi.jpg', False)
    # dest3 = Destination(3, 'MUMBAI', 'CITY THAT NEVER SLEEPS', 1200, 'mumbai.jpg', False)
    # dest_list = [dest1, dest2, dest3]
    # return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})
    dest_list = Destination.objects.all()
    return render(request, 'index.html', {'dest_list': dest_list})
