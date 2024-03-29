
from django.urls import path
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve

from bboard import settings
from main.views import index, other_page, BBLoginView, testBS, profile, \
    BBLogoutView, ChangeUserInfoView, BBPasswordChangeView, \
    RegisterUserView, RegisterDoneView, user_activate, DeleteUserView, \
    by_rubric, detail, profile_bb_detail, profile_bb_add, profile_bb_change, \
    profile_bb_delete

app_name = 'main'
urlpatterns = [
    path('new/<int:rubric_pk>/<int:pk>/', detail, name='novelty'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/register/activate/<str:sign>/',
         user_activate, name='register_activate'),
    path('accounts/register/done/',
         RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/',
         RegisterUserView.as_view(), name='register'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('bs/', testBS, name='bootstrap'),
    path('accounts/profile/delete/',
         DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/',
         ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/change/<int:pk>/',
         profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/',
         profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/add/',
         profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/<int:pk>/',
         profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/',
         BBPasswordChangeView.as_view(), name='password_change'),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
