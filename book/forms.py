from django import forms
from book.models import Book



class CategoryForm(forms.Form):

    name = forms.CharField(max_length=50,label="عنوان",widget=forms.TextInput(attrs={"class": "form-control mt-2"}),)
    description = forms.CharField(max_length=255,label="توضیحات",widget=forms.Textarea(attrs={"class": "form-control mt-2"}),)

class AhtorForms(forms.Form):
    fname = forms.CharField(max_length=50, label='نام',widget=forms.TextInput(attrs={"class": "form-control mt-2"}))
    lname = forms.CharField(max_length=50,label='نام خانوادگی',widget=forms.TextInput(attrs={"class": "form-control mt-2"}))
    birthdate = forms.DateField(label='تاریخ تولد',widget=forms.TextInput(attrs={"class": "form-control mt-2"}))
    bio = forms.CharField(max_length=250,label='بیوگرافی',widget=forms.TextInput(attrs={"class": "form-control mt-2"}))



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "category",
            "pages",
            "kholase",
            "cover",
        ]      
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "author": forms.Select(attrs={"class": "form-control mt-2"}),
            "category": forms.Select(attrs={"class": "form-control mt-2"}),
            "pages": forms.NumberInput(attrs={"class": "form-control mt-2"}),
            "cover": forms.FileInput(attrs={"class": "form-control mt-2"}),
            "summary": forms.Textarea(attrs={"class": "form-control mt-2"}),
        }