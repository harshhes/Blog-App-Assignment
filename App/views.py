# from django.shortcuts import redirect, render
# from .models import *
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from .forms import *
# from django.contrib.auth.decorators import login_required


# def home(request):
#     context = {'blogs': Blog.objects.all()}
#     return render(request, 'home.html',context)

# def login_page(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user_obj = User.objects.filter(username=username)

#         if not user_obj.exists():
#             messages.success(request, 'User not Found!!')
#             return redirect('/login/')
        
#         user_obj = authenticate(username=username, password=password)

#         if not user_obj:
#             messages.success(request, "Invalid Credentials")
#             return redirect('/login/')

#         login(request, user_obj)
#         return redirect('/')


#     return render(request, 'login_page.html')

# def logout_page(request):
#     logout(request)
#     return redirect('/')

# def register_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user_obj = User.objects.filter(username=username)

#         if user_obj.exists():
#             messages.success(request, 'This username is taken')
#             return redirect('/register/')

#         user_obj = User.objects.filter(email=email)

#         if user_obj.exists():
#             messages.success(request, 'This email is taken')
#             return redirect('/register/')

#         user_obj = User(username=username, email=email)
#         user_obj.set_password(password)
#         user_obj.save()
#         messages.success(request, 'Your account is created')
        
#         return redirect('/login/')


#     return render(request, 'register_page.html')

# @login_required(login_url='/login/')
# def all_blogs(request):
#     context = {'blogs': Blog.objects.filter(author=request.user)}

#     return render(request, 'all_blogs.html', context)

# @login_required(login_url='/login/')
# def create_blog(request):
#     context = {'form': BlogForm, 'categories': Category.objects.all()}
#     if request.method == "POST":
#         form = BlogForm(request.POST)
#         category = request.POST.get('category')
#         title = request.POST.get('title')
#         banner_image = request.FILES.get('banner')
        
#         if form.is_valid():
#             content = form.cleaned_data['content']

#             Blog.objects.create(
#                 title = title,
#                 content = content,
#                 category = Category.objects.get(id= category),
#                 author = request.user,
#                 banner_image = banner_image
#             )
#             messages.success(request, "Blog created!")
#             return redirect('/create-blog/')

#         # else:
#         #     messages.success(request, "Invalid Credentials")
#         #     return redirect('/create-blog/')

#     return render(request, 'create_blog.html', context)

# @login_required(login_url='/login/')
# def update_blog(request, id):
#     context = {'categories': Category.objects.all()}
#     try:
#         if request.method == "POST":
#             form = BlogForm(request.POST)
#             category = request.POST.get('category')
#             title = request.POST.get('title')
#             banner_image = request.FILES.get('banner')
#             if form.is_valid():
#                 content = form.cleaned_data['content']
#                 blog_obj = Blog.objects.get(id=id)
#                 blog_obj.title = title

#                 blog_obj.content = content
#                 blog_obj.category = Category.objects.get(id = category)

#                 if banner_image:
#                     blog_obj.banner_image = banner_image

#                 blog_obj.save()
#                 messages.success(request, "Blog updated")

#                 return redirect('/create-blog/')
       
#         blog_obj = Blog.objects.get(id=id)
#         if blog_obj.author != request.user:
#             return redirect('/')

#         initial_dict =  {'content': blog_obj.content}
#         form = BlogForm(initial = initial_dict)
#         context['form'] = form
#         context['blog_obj'] = blog_obj
          
#     except Exception as e:
#         print(e)

#     return render(request, 'update_blog.html', context)

# @login_required(login_url='/login/')
# def delete_blog(request, id):
#     blog_obj = Blog.objects.get(id=id)

#     if blog_obj.author != request.user:
#         return redirect('/')

#     blog_obj.delete()
#     return redirect('/all-blogs/')


# def get_blog(request, id):
#     context = {}
#     try:
#         blog_obj = Blog.objects.get(id=id)
#         context['blog'] = blog_obj
#         category_obj = Category.objects.get(id=id)
#         context['category'] = category_obj
#     except Exception as e:
#         print(e)
#     return render(request, 'detail_blog.html', context)

