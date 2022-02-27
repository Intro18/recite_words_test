from django.db import models


class JapWord(models.Model):
    """日语单词"""
    # 1.单词
    text = models.CharField(max_length=20)
    # 2.单词类型
    classes = models.CharField(max_length=2)
    # 3.单词意思
    meaning = models.CharField(max_length=30)
    # 4.对应英语
    en_text = models.CharField(max_length=20)
    # 5.追加时间
    date_added = models.DateTimeField(auto_now_add=True)


class EnWord(models.Model):
    """英语单词"""
    # 1.单词
    text = models.CharField(max_length=20)
    # 2.单词类型
    classes = models.CharField(max_length=2)
    # 3.单词意思
    meaning = models.CharField(max_length=30)
    # 4.追加时间
    date_added = models.DateTimeField(auto_now_add=True)


class VerbConjugation(models.Model):
    """动词变形表"""
    # 1.单词
    jap_word = models.ForeignKey(JapWord, on_delete=models.DO_NOTHING)
    # 2.ます形
    polite = models.CharField(max_length=20)
    # 3.て形
    te_form = models.CharField(max_length=20)
    # 4.た形
    past = models.CharField(max_length=20)
    # 5.未然形
    negative = models.CharField(max_length=20)
    # 6.命令形
    imperative = models.CharField(max_length=20)
    # 7.意志形
    volitional = models.CharField(max_length=20)
    # 8.ば形
    conditional = models.CharField(max_length=20)
    # 9.可能形
    potential = models.CharField(max_length=20)
    # 10.被動形
    passive = models.CharField(max_length=20)
    # 11.使役形
    causative = models.CharField(max_length=20)
