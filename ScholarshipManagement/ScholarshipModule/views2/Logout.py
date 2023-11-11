from django.shortcuts import redirect
from django.contrib.auth import logout

def signOut(request):
    
    logout(request)
    return redirect('/')