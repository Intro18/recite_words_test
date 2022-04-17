from django import forms
from django.forms import widgets
from .models import JapWord, VerbConjugation


class JapWordForm(forms.ModelForm):
    # 1.单词
    text = forms.CharField(label="单词", max_length=20, required=True)
    # 2.平仮名
    hiragana = forms.CharField(label="平仮名", max_length=20, required=True)
    # 3.单词类型
    classes = forms.MultipleChoiceField(label="单词类型",
                                        # initial=[2, ],
                                        choices=((1, '动词'),
                                                 (2, '一类形容词'),
                                                 (3, "二类形容词"),
                                                 (4, '名词'),
                                                 (5, '代词'),
                                                 (6, '数词'),
                                                 (7, '副词'),
                                                 (8, '连体词'),
                                                 (9, '连词'),
                                                 (10, '感叹词'),
                                                 (11, '助词'),
                                                 (12, '助动词')),
                                        # widget=widgets.CheckboxSelectMultiple
                                        )
    # 4.单词意思
    meaning = forms.CharField(label="单词意思", max_length=30, required=False)
    # 5.对应英语
    en_text = forms.CharField(label="对应英语", max_length=20, required=False)
    # 6.备注
    comments = forms.CharField(label="备注", max_length=200, required=False, widget=forms.Textarea)

    class Meta:
        model = JapWord
        fields = ['text', 'hiragana', 'classes', 'meaning', 'en_text', 'comments']
    #     labels = {'text': '单词',
    #               'hiragana': '平仮名',
    #               'classes': '单词类型',
    #               'meaning': '单词意思',
    #               'en_text': '对应英语',
    #               'comments': '备注'}


class VerbConjugationForm(forms.ModelForm):
    class Meta:
        model = VerbConjugation
        fields = ['polite',
                  'te_form',
                  'past',
                  'negative',
                  'imperative',
                  'volitional',
                  'conditional',
                  'potential',
                  'passive',
                  'causative']
        labels = {'polite': 'ます形',
                  'te_form': 'て形',
                  'past': 'た形',
                  'negative': '未然形',
                  'imperative': '命令形',
                  'volitional': '意志形',
                  'conditional': 'ば形',
                  'potential': '可能形',
                  'passive': '被動形',
                  'causative': '使役形'}


class JapWordClassesForm(forms.Form):
    classes = forms.MultipleChoiceField(label="单词类型",
                                        # initial=[2, ],
                                        choices=((1, '动词'),
                                                 (2, '一类形容词'),
                                                 (3, "二类形容词"),
                                                 (4, '名词'),
                                                 (5, '代词'),
                                                 (6, '数词'),
                                                 (7, '副词'),
                                                 (8, '连体词'),
                                                 (9, '连词'),
                                                 (10, '感叹词'),
                                                 (11, '助词'),
                                                 (12, '助动词')),
                                        # widget=widgets.CheckboxSelectMultiple
                                        )