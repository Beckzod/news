from django.urls import path
from .views import news_list, news_detail, ContactView, notFoundView, aboutView, HomePageView, LocalNewsView, ForeignNewsView, EconomyNewsView, SocietyNewsView, TechnologyNewsView, SportNewsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("news/", news_list, name="news_list"),
    path("local-news/", LocalNewsView.as_view(), name="local_page"),
    path("foreign-news/", ForeignNewsView.as_view(), name="foreign_page"),
    path("economy-news/", EconomyNewsView.as_view(), name="economy_page"),
    path("society-news/", SocietyNewsView.as_view(), name="society_page"),
    path("technology-news/", TechnologyNewsView.as_view(), name="technology_page"),
    path("contact/", ContactView.as_view(), name="contact_page"),
    path("not_found/", notFoundView, name="404_page"),
    path("about/", aboutView, name="about_page"),
    path("sport-news/", SportNewsView.as_view(), name="sport_page"),
    path("<slug:news>/", news_detail, name="news_detail_page"),

]
