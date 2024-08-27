from django.shortcuts import render

# Create your views here.
details=[['anandhi','sharma','anu@gmail.com','anu']]

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')


def success(request):
    f = request.POST.get('fn')
    l = request.POST.get('ln')
    
    if request.method=='POST':
        id=request.POST.get('lid')
        pas=request.POST.get('lpd')
        # form_data=request.POST
        count=0
        for i in details:
            if i[2]==id and i[3]==pas:
                count+=1
                return render(request, 'success.html',{f: i[0], l: i[1]})

        if count==0:
            return render(request,'login.html', {'err':'Invalid Email or Password'})

def create(request):
    f = request.POST.get('fn')
    l = request.POST.get('ln')
    id = request.POST.get('sid')
    pas1 = request.POST.get('spd')
    pas2 = request.POST.get('spd1')

    count=0
    for i in details:
        if i[2]==id:
            count+=1
            break
        if count==1:
            return render( request,'signup.html',msg='Email ID already exists !')
        if pas1==pas2:        
                x=[f,l,id,pas1]
                # x.append(f)
                # x.append(l)
                # x.append(id)
                # x.append(pas1)
                details.append(x)
                return render(request,'create.html', {f:f, l:l })
        else:
            return render( request,'signup.html',{'msg':'Create valid password !',f:f,l:l,id:id})
