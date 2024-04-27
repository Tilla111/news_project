from django.urls import path
from .views import news_list,ContactPageView,errorPageView,HomePageView,single_page,LocalPageView,\
    TechnologyPageView,SportPageView,ForeignPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('all/', news_list, name='all_news_list'),
    path('local_1/', LocalPageView.as_view(), name='local_news_page'),
    path('technology/', TechnologyPageView.as_view(), name='technology_news_page'),
    path('sport/', SportPageView.as_view(), name='sport_news_page'),
    path('foreign/', ForeignPageView.as_view(), name='foreign_news_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404 error/', errorPageView, name='error_page'),
    path('<slug:news>/', single_page, name='single_page'),

]