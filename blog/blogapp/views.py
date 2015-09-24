from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Post, Comment, Category
from .forms import CommentForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blogapp/index.html'
    model = Post
    
    def get_queryset(self):
        # This is the SQL way to return the five most recently published posts.
        # SELECT * from blogapp_post ORDER BY pub_date DESC LIMIT 5
        # This is the Python way to do it.
        return Post.objects.order_by('-pub_date')[:5]

class PostDetailView(generic.DetailView):
#   template_name = 'blogapp/detail.html'
    model = Post

    def get_context_data(self, *args, **kwargs):
    #    context = super(PostDetail, self).get_context_data()
    #    context.update({"comment_list": self.get_object().comment_set.all()})
    #   context.update({"comment_list": Comment.objects.filter(post_pk = self.kwargs.get('pk'))})
    #    return context;
        context = super(PostDetailView, self).get_context_data()
        context["form"] = CommentForm(initial={'post_id': self.object.pk})
        return context;

class PostCommentFormView(generic.detail.SingleObjectMixin, generic.FormView):
    form_class = CommentForm
    model = Post
    success_url = reverse_lazy('blogapp:comment_success')

    def form_valid(self, form):

        comment = Comment()
        comment.post = get_object_or_404(Post, pk=form.cleaned_data["post_id"])
        comment.person = form.cleaned_data["name"]
        comment.comment_text = form.cleaned_data["comment"]
        comment.save()
        return super(PostCommentFormView, self).form_valid(form)

class CategoryDetailView(generic.DetailView):
        model = Category
        # query set

class CategoryDetailView(generic.DetailView):
    model = Category
    # query set
