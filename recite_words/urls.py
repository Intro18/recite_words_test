from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('jap_words_classes/', views.jap_words_classes, name='jap_words_classes'),
    path('jap_words/<int:page_num>/<int:classes_num>', views.jap_words, name='jap_words'),
    #path('jap_words/page<int:num>/', views.jap_words, name='jap_words'),
    path('jap_word/<int:jap_word_id>', views.jap_word, name='jap_word'),
    path('new_jap_word/', views.new_jap_word, name='new_jap_word'),
    path('new_verb_conjugation/<int:jap_word_id>', views.new_verb_conjugation, name='new_verb_conjugation'),
]
