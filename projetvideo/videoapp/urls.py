from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path
from .views import *
from . import views


router = DefaultRouter()
router.register('Module', ModuleViewSet, base_name='Module')
router.register('User_module', User_moduleViewSet, base_name='User_module')
router.register('Categorie', CategorieViewSet, base_name='Categorie')
# router.register('Video', VideoViewSet, base_name='video')
# path('postRegister', views.register, name='register'),
# path('postLogin', views.Login, name='Login'),
router.register('User', UserViewSet, base_name='user')

urlpatterns = [
    path("VideosListe/", VideosListe.as_view(), name="videos_liste"),
    path("", acc, name="acc"),
    path('connexionUser',registerUser,name='connexionUser'),
    path('loginUser',loginUser,name='loginUser'),
    path("Videos/<int:pk>/", VideoDetail.as_view(), name="video_detail"),
    # path("", acc, name="acc"),
    path("connexion/", login, name="login"),
    path("inscription", register, name="register"),
    path("category/<int:id_cat>/", cat, name="cat"),
    path("video/<int:id_video>/", acc, name="acc"),
]

urlpatterns += router.urls