from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoHomeView.as_view(), name='home'),  
    path('message/', MessageView.as_view(), name='message'),
    path('error/', ErrorView.as_view(), name='error'),
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('profile/detail/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('verify/<int:pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    
    path('todo/create', TodoCreateView.as_view(), name='create_todo'),
    path('todo/detail/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
]
