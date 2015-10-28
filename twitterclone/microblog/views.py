from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django import forms
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Profile, Post

# Create your views here.
class ListAllPosts(ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all().order_by('-pub_date')

class ProfileDetailView(DetailView):
    model = Profile

class MyFeedView(ListView):
    model = Post
    paginate_by = 10
    template_name = "microblog/myfeed.html"

    def get_queryset(self):
        my_profile = self.request.user.profile_set.all()[0]
        following_profile_list = list(my_profile.following.all())
        following_profile_list.append(my_profile)
        return Post.objects.filter(profile__in = following_profile_list)

class FollowFormView(SingleObjectMixin, View):
    model = Profile
    
    def post(self, request, *args, **kwargs):
        my_profile = request.user.profile_set.all()[0]
        my_profile.following.add(self.get_object())
        my_profile.save()
        #return HttpResponseRedirect(reverse('microblog:followsuccess'))

        #if request.is_ajax():
            #returnHttp

        return HttpResponseRedirect(reverse('microblog:followsuccess', args=(self.get_object().pk, )))

class FollowSuccessView(SingleObjectMixin, TemplateView):
    model = Profile
    template_name = 'microblog/follow_success.html'

class NewPostView(CreateView):
    model = Post
    fields = ['body']

    def get_success_url(self):
        return reverse('microblog:profiledetail', args=[Profile.objects.filter(user = self.request.user)[0].id])

    def form_valid(self, form):
        post = form.save(commit=False)
        post.profile = Profile.objects.filter(user = self.request.user)[0]
        return super(NewPostView, self).form_valid(form)






    
# class FollowFormView(FormView):
#     success_url = reverse_lazy('microblog:followsuccess')
# 
#     class FollowUserForm(forms.Form):
#         follow_user_id = forms.IntegerField(widget=forms.HiddenInput)
# 
#     form_class = FollowUserForm
# 
#     def form_valid(self, form):
#         self.user_id
