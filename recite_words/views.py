from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import JapWordForm, VerbConjugationForm, JapWordClassesForm
from .models import JapWord, VerbConjugation, JapWordClasses
from django.core.paginator import Paginator
from django.db.models import Count


def index(request):
    """记单词的主页"""
    return render(request, 'recite_words/index.html')


def jap_words_classes(request):
    """显示所有单词类型"""
    __classes = JapWordClasses.objects.values("id", "class_name").annotate(class_count=Count("japword__classes"))
    context = {'jap_words_classes': __classes}
    return render(request, 'recite_words/jap_words_classes.html', context)


def jap_word(request, jap_word_id):
    """显示单个单词及其所有条目"""
    __jap_word = JapWord.objects.get(id=jap_word_id)
    #因为结果可能为空，所以不能用get方法，要用filter方法
    verb_conjugation = VerbConjugation.objects.filter(id=jap_word_id)
    context = {'jap_word': __jap_word, 'verb_conjugation': verb_conjugation}
    return render(request, 'recite_words/jap_word.html', context)


def jap_words(request, page_num, classes_num):
    """显示所有单词"""
    current_num = page_num
    __jap_words = JapWord.objects.filter(classes_id=classes_num).order_by('id')
    __word_classes = JapWordClasses.objects.get(id=classes_num)
    paginator = Paginator(__jap_words, 10)
    page = paginator.page(current_num)

    if paginator.num_pages > 11:
        # 当前页码的后5页数超过最大页码时，显示最后10项
        if current_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        # 当前页码的前5页数为负数时，显示开始的10项
        elif current_num - 5 < 1:
            page_range = range(1, 12)
        else:
            # 显示左5页到右5页的页码
            page_range = range(current_num - 5, current_num + 5 + 1)
    # 小于11页时显示所有页码
    else:
        page_range = paginator.page_range

    context = {"page": page, "paginator": paginator, "current_num": current_num,
               "page_range": page_range, "word_classes": __word_classes}  # {}是字典数据类型(映射类型)
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
