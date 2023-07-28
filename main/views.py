# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout

# def home(request):
#     return render(request, 'home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def signin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'signin.html', {'form': form})

# def signout(request):
#     logout(request)
#     return redirect('home')

# import json
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import SignUpform

# def home(request):
#     return render(request, 'home.html')

# @csrf_exempt
# def signup(request):
#     print(request.body)
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         username = data.get('username')
#         fname = data.get('fname')
#         lname = data.get('lname')
#         email = data.get('email')
#         pass1 = data.get('pass1')
#         pass2 = data.get('pass2')

#         if not username or not pass1 or not fname or not lname or not email or not pass1 or not pass2:
#             return JsonResponse({'error' : 'Please complete all the fields'}, status = 400)
        
#         if pass1 != pass2:
#             return JsonResponse({'error' : "Passwords don't match"}, status = 400)
        
#         if SignUpform.objects.filter(username = username).exists():
#             return JsonResponse({'error' : 'username already exists'}, status = 400)
        
#         user = SignUpform(username = username, password = pass1, email = email)
#         user.first_name = fname
#         user.last_name = lname
#         user.save()

#         return JsonResponse({'success' : 'Account has been successfully created'}, status = 201)

#     return render(request, 'signup.html')

# @csrf_exempt
# def signin(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         username = data.get('username')
#         pass1 = data.get('pass1')

#         if not username or pass1:
#             return JsonResponse({"error" : "Please complete all the fields"}, status = 400)
        
#         try:
#             user = SignUpform.objects.get(username = username)
#             if user.password == pass1:
#                 return JsonResponse({'success' : 'Successfully loged in'}, status = 201)
#             else:
#                 return JsonResponse({'error' : 'Username or Password is wrong'}, status = 401)
#         except SignUpform.DoesNotExist:
#             return JsonResponse({'error' : "User does not exist"}, status = 404)
        
#     return render(request, 'signin.html')

# def signout(request):
#     return redirect(request, 'home.html')

import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import SignUpform

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        #data = json.loads(request.body)
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if not username or not pass1 or not fname or not lname or not email or not pass1 or not pass2:
            return JsonResponse({'error': 'Please complete all the fields'}, status=400)
        
        if pass1 != pass2:
            return JsonResponse({'error': "Passwords don't match"}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        user = User.objects.create_user(username=username, password=pass1, email=email)
        user.first_name = fname
        user.last_name = lname
        user.save()

        # return JsonResponse({'success': 'Account has been successfully created'}, status=201)

        return redirect('home')

    return render(request, 'signup.html')

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        #data = json.loads(request.body)
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        if not username or not pass1:
            return JsonResponse({"error": "Please complete all the fields"}, status=400)
        
        user = User.objects.filter(username=username).first()
        if user and user.check_password(pass1):
            # return JsonResponse({'success': 'Successfully logged in'}, status=200)
            return redirect('auth')
        else:
            return JsonResponse({'error': 'Username or Password is wrong'}, status=401)
        
    return render(request, 'signin.html')

def auth(request):
    return render(request, 'auth.html')

def signout(request):
    return redirect('home')


# import json
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import logout
# from .models import SignUpform

# def home(request):
#     return render(request, 'home.html')

# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         if 'application/json' in request.content_type:
#             data = json.loads(request.body)
#             username = data.get('username')
#             fname = data.get('fname')
#             lname = data.get('lname')
#             email = data.get('email')
#             pass1 = data.get('pass1')
#             pass2 = data.get('pass2')

#             if not username or not pass1 or not fname or not lname or not email or not pass1 or not pass2:
#                 return JsonResponse({'error': 'Please complete all the fields'}, status=400)
            
#             if pass1 != pass2:
#                 return JsonResponse({'error': "Passwords don't match"}, status=400)
            
#             if User.objects.filter(username=username).exists():
#                 return JsonResponse({'error': 'Username already exists'}, status=400)
            
#             user = User.objects.create_user(username=username, password=pass1, email=email)
#             user.first_name = fname
#             user.last_name = lname
#             user.save()

#             #return JsonResponse({'success': 'Account has been successfully created'}, status=201)
#             return redirect('home')
        
        
#         # Regular Form Submission
#         else:
#             username = request.POST.get('username')
#             fname = request.POST.get('fname')
#             lname = request.POST.get('lname')
#             email = request.POST.get('email')
#             pass1 = request.POST.get('pass1')
#             pass2 = request.POST.get('pass2')

#             if not username or not pass1 or not fname or not lname or not email or not pass1 or not pass2:
#                 return JsonResponse({'error': 'Please complete all the fields'}, status=400)
            
#             if pass1 != pass2:
#                 return JsonResponse({'error': "Passwords don't match"}, status=400)
            
#             if User.objects.filter(username=username).exists():
#                 return JsonResponse({'error': 'Username already exists'}, status=400)
            
#             user = User.objects.create_user(username=username, password=pass1, email=email)
#             user.first_name = fname
#             user.last_name = lname
#             user.save()

#             # return JsonResponse({'success': 'Account has been successfully created'}, status=201)
#             return redirect('home')

#     return render(request, 'signup.html')

# @csrf_exempt
# def signin(request):
#     if request.method == 'POST':
#         if 'application/json' in request.content_type:
#             data = json.loads(request.body)
#             username = data.get('username')
#             pass1 = data.get('pass1')

#             if not username or not pass1:
#                 return JsonResponse({"error": "Please complete all the fields"}, status=400)
            
#             user = User.objects.filter(username=username).first()
#             if user and user.check_password(pass1):
#                 # return JsonResponse({'success': 'Successfully logged in'}, status=200)
#                 return redirect('auth')
#             else:
#                 return JsonResponse({'error': 'Username or Password is wrong'}, status=401)
        
#         # Regular Form Submission
#         else:
#             username = request.POST.get('username')
#             pass1 = request.POST.get('pass1')

#             if not username or not pass1:
#                 return JsonResponse({"error": "Please complete all the fields"}, status=400)
            
#             user = User.objects.filter(username=username).first()
#             if user and user.check_password(pass1):
#                 # return JsonResponse({'success': 'Successfully logged in'}, status=200)
#                 return redirect('auth')
#             else:
#                 return JsonResponse({'error': 'Username or Password is wrong'}, status=401)
        
#     return render(request, 'signin.html')

# def auth(request):
#     return render(request, 'auth.html')

# def signout(request):
#     logout(request)
#     return redirect('home')


        
