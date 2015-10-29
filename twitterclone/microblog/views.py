from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
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
        my_profile, created = Profile.objects.get_or_create(user = self.request.user)
        following_profile_list = list(my_profile.following.all())
        following_profile_list.append(my_profile)
        return Post.objects.filter(profile__in = following_profile_list)

class CreatePostView(CreateView):
    model = Post
    fields = ['body']

    def get_success_url(self):
        #return reverse('microblog:profiledetail', args=[Profile.objects.filter(user = self.request.user)[0].id])
        return reverse('microblog:myfeed')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.profile, created = Profile.objects.get_or_create(user=self.request.user)
        post.save()
        return super(CreatePostView, self).form_valid(form)

class FollowFormView(SingleObjectMixin, View):
    model = Profile

    def post(self, request, *args, **kwargs):
        try:
            my_profile = request.user.profile_set.all()[0]
        except Profile.DoesNotExist:
            my_profile = Profile(bio = '', user = request.user)
            my_profile.save()
        my_profile.following.add(self.get_object())
        my_profile.save()
        return HttpResponseRedirect(reverse('microblog:followsuccess', args = (self.get_object().pk, )))

class FollowSuccessView(DetailView):
    model = Profile
    template_name = 'microblog/follow_success.html'

class CreateProfileView(CreateView):
    model = Profile
    fields = ['bio', 'profile_picture', 'following']

    def get_success_url(self):
        return reverse('microblog:profiledetail', args = (self.request.user.id, ))

    def form_valid(self, form):
        profile = Profile()
        profile.bio = form.cleaned_data['bio']
        profile.profile_picture = form.cleaned_data['profile_picture']
        profile.following = form.cleaned_data['following']
        profile.save()

        return super(CreateProfileView, self).form_valid(form)

class UpdateProfileView(UpdateView):
    model = Profile
    fields = ['bio', 'profile_picture', 'following']

    def get_success_url(self):
        return reverse('microblog:profiledetail', args = (self.get_object().pk, ))
#class ProfileFormView(SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView):
    #model = Profile
    #fields = ['bio', 'profile_picture']
    #template_name = 'microblog/profile_edit.



#       my_profile = self.request.user.profile_set.all()[0]		Does not work because sometimes
#									there is not a profile, and you
#                                                                       are requesting one. Use one of the two below instead.
#       my_profile, created = Profile.objects.get_or_create(user = self.request.user)
#
#
#       try:
#           my_profile = request.user.profile_set.all()[0]
#       except Profile.DoesNotExist:
#           my_profile = Profile(bio = '', user = request.user
#       my_profile.following.add(self.get_object())
#       my_profile.save()
