from django.urls import path
from .views import *
from .views2 import *
from rest_framework_simplejwt.views import TokenRefreshView


# urlpatterns = [
#     path('get-blog/<id>/', get_blog, name='get_blog'),
#     path('',home, name='home'),
#     path('login/', login_page, name='login'),
#     path('register/', register_page, name='register'),
#     path('all-blogs/', all_blogs, name='all_blogs'),
#     path('create-blog/', create_blog, name='create_blog'),
#     path('update-blog/<id>/', update_blog, name='update_blog'),
#     path('delete-blog/<id>/', delete_blog, name='delete_blog'),
#     path('logout/', logout_page, name='logout'),
# ]

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('blogs/', BlogView.as_view()),
    path('category/<int:pk>', DetailedCategoryView.as_view()),
    path('blogs/<int:pk>', DetailedBlogView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]