from django import forms

class CommentForm(forms.Form):
    name     = forms.CharField(max_length=200, label="Your name")
    comment  = forms.CharField(widget=forms.Textarea, max_length=1000, label="Your comment")
    post_id  = forms.IntegerField(widget=forms.HiddenInput)
