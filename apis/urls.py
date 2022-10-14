from django.urls import path
from django.urls.conf import include
from apis.views import *

from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView


app_name='apis'

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    
    path('user/',ListUser.as_view(), name='user'),
    path('user/<int:pk>/',DetailUser.as_view()),
    
    path('employee/',ListEmployee.as_view(), name='employee'),
    path('employee/<int:pk>/',DetailEmployee.as_view()),
    
    path('appel_offre/',ListAppel_offre.as_view(), name='appel_offre'),
    path('appel_offre/<int:pk>/',DetailListAppel_offre.as_view()),
    
    path('passation/',ListAvis_passation.as_view(), name='passation'),
    path('passation/<int:pk>/',DetailAvis_passation.as_view()),
    
    path('passassion/',ListPassassion.as_view(), name='PAS'),
    path('passassion/<int:pk>/',DetailPassassion.as_view()),
    
    path('contrat/',ListContrat.as_view(), name='contrat'),
    path('contrat/<int:pk>/',DetailContrat.as_view()),
    
    path('comptabilite/',ListComptabilite.as_view(), name='compta'),
    path('comptabilite/<int:pk>/',DetailComptabilite.as_view()),

    path('compta/',ListCompta.as_view(), name='comptabilite'),
    path('compta/<int:pk>/',DetailCompta.as_view()),
    
    path('conge/',ListConge.as_view(), name='conge'),
    path('conge/<int:pk>/',DetailConge.as_view()),
    
    path('ordre_mission',ListOrdre_mission.as_view(), name='ordre_mission'),
    path('ordre_mission/<int:pk>/',DetailOrdre_mission.as_view()),
    
    path('documents/',ListDocuments.as_view(), name='documents'),
    path('documents/<int:pk>/',DetailDocuments.as_view()),
    
    path('courrier/',ListCourrier.as_view(), name='courrier'),
    path('courrier/<int:pk>/',DetailCourrier.as_view()),
    
    path('loginclient/', loginclient, name='loginclient'),

    path('updatepassassion/<int:id>/',updatepassassion,name='updatepassassion'),

    path('updatecompta/<int:id>/',updatecompta,name='updatecompta'),
    path('stat/',stat,name='stat'),
    
    
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]