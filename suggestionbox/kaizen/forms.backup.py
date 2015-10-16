from django import forms

class CommentForm(forms.Form):
    person = forms.CharField(max_length=200, label="Name")
    comment_text = forms.CharField(widget=forms.Textarea, label="comment")
    idea_id = forms.IntegerField(widget=forms.HiddenInput)
