from django.shortcuts import render, redirect
from django.http import HttpResponse
from myprofile.models import *
import json
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def home_page(request):
    current_user = request.user.id
    print(current_user)
    response_data = {
        'h_content':'Welcome to the Breakfast Club',
        'para_home':'Signup and become a Member',
        'home_anchor':'/login'
    }
    return render(request, 'home.html', response_data)

def error(request):
    current_user = request.user.id
    print(current_user)
    response_data = {
        'h_content':'All you have to do is register to become a member',
        'para_home':'Signup and become a Member',
        'home_anchor':'/register'
    }
    return render(request, 'error.html', response_data)    

def contact_us(request):
    some_data_to_dump = {'client_data':200}
    data =json.dumps(some_data_to_dump)
    return HttpResponse(data, content_type='application/json')

def form_submission(request):
    if request.method == "GET":
        current_user = request.user.id
        print(current_user)
        return render(request, 'form.html')
    if request.method =="POST":
        user_file = request.FILES['u_image']
        client_info_data = client_info(
            client_name = request.POST.get("u_name"),
            client_age = request.POST.get("u_age"),
            client_city = request.POST.get("u_city"),
            client_food = request.POST.get("u_food"),
            client_phone = request.POST.get("u_phone"),
            client_image = user_file.name,
            client_id = request.user.id,
        ) 


        client_info_data.save()
        destination_folder = r"C:\Users\aaron\Documents\MAJOR_PROJECTS\Django_projects\Chrome\members\myprofile\static\images/" + user_file.name
        with open(destination_folder, 'wb+') as destination_file:
            for chunk in user_file.chunks():
                destination_file.write(chunk)
                all_user_data = client_info.objects.all().values()
                last_id = client_info.objects.latest('client_id')
                data_to_be_sent = {
        'user_list' : list(all_user_data),
        'last_id' : last_id,
    }
        return render(request, 'form_success.html', data_to_be_sent)
    


def users_list(request):
    all_user_data = client_info.objects.all().values()
    last_id = client_info.objects.latest('client_id')
    data_to_be_sent = {
        'users_list' : list(all_user_data),
        'last_id' : last_id,
    }
    return render(request, 'users_list.html', data_to_be_sent)





def profile(request, id):
    user_data = client_info.objects.filter(id=id).values()
    return render(request, 'profile.html', {'user_list': list(user_data)})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("r_password")
        if password == repeat_password:
            user = User.objects.create_user(username = username, password = password)
            return redirect('login/')
        else:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})




# def UserProfile(request, id):
#         if request.method == 'GET':
#           user_data = client_info.objects.filter(id=id).values()
#         if request.method == 'POST':
#           userprofile_form = UserProfileForm(request.POST if request.POST else None, instance = client_info.objects.get(user=request.client_id))
#           if form.is_valid():
#               form.save()     
#               return redirect('profile')  

#         return render(request, 'user_edit.html', context={'userprofile_form': userprofile_form, 'client_info': user_data})





# def userEdit(request, user_id):
#     user = get_object_or_404(Question, pk=user_id)
#     if request.method == "GET":
#         form = UserEditForm(initial=model_to_dict(user))
#         return render(request, 'myprofile/user_edit.html', {'form':form)
#     elif request.method == "POST":
#         form = UserEditForm(request.POST, instance=user)
#         if form.is_valid():
#              form.save()
#              return HttpResponseRedirect(reverse('user_profile', kwargs={'uid':user.id}))
#         else:
#              return HttpResponseRedirect(reverse('some_fail_loc'))        