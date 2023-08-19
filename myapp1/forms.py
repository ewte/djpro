from django import forms

class Comment(forms.Form):
    #name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    #email = forms.EmailField(label="Ваш Email", max_length=100, required=True)
    message = forms.CharField(label="Сообщение", widget=forms.Textarea, required=True)



class Registration(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    email = forms.EmailField(label="Ваш Email", max_length=100, required=True)
    


class AddForm(forms.Form):
    pole = forms.CharField(label='Name', max_length=100, required=True)

    