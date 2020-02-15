from django.shortcuts import render

# Create your views here.
def authoritylogin(request):
    if request.method == "POST":
        username = request.POST.get('username')   
        password = request.POST.get('password')
        user  = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)

        else:
            return HttpResponse("invalid Credentials")
        return HttpResponse("Tdfndkdgx")
    

    return render(request, "Authority/authoritylogin.html")