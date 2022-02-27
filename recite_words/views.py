from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import JapWordForm, VerbConjugationForm
from .models import JapWord, VerbConjugation


def index(request):
    """记单词的主页"""
    return render(request, 'recite_words/index.html')


def jap_word(request, jap_word_id):
    """显示单个单词及其所有条目"""
    __jap_word = JapWord.objects.get(id=jap_word_id)
    verb_conjugation = VerbConjugation.objects.get(id=jap_word_id)
    context = {'jap_word': __jap_word, 'verb_conjugation': verb_conjugation}
    return render(request, 'recite_words/jap_word.html', context)


def jap_words(request):
    """显示所有单词"""
    __jap_words = JapWord.objects.order_by('date_added')
    context = {'jap_words': __jap_words}  # {}是字典数据类型(映射类型)
    return render(request, 'recite_words/jap_words.html', context)


def new_jap_word(request):
    """添加新单词"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = JapWordForm()
    else:
        # post提交的数据，对数据进行处理
        form = JapWordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recite_words:jap_words'))

    context = {'form': form}
    return render(request, 'recite_words/new_jap_word.html', context)


def new_verb_conjugation(request, jap_word_id):
    """添加动词变形的新条目"""
    __jap_word = JapWord.objects.get(id=jap_word_id)

    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = VerbConjugationForm()
    else:
        # post提交的数据，对数据进行处理
        form = VerbConjugationForm(data=request.POST)
        if form.is_valid():
            __verb_conjugation = form.save(commit=False)
            __verb_conjugation.jap_word = __jap_word
            __verb_conjugation.save()
            return HttpResponseRedirect(reverse('recite_words:jap_word', args=[jap_word_id]))

    context = {'jap_word': __jap_word, 'form': form}
    return render(request, 'recite_words/new_verb_conjugation.html', context)
