from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View,
)
from django.views.generic.detail import SingleObjectMixin
from .models import Post
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse

# Create your views here.


# def home(request):
#     return render(request, "home.html", {})
class HomeView(ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-post_date')
    template_name = "home.html"
    ordering = ["-post_date"]
    paginate_by = 3


class PostDisplay(DetailView):
    model = Post
    template_name = "article_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "add_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("article-detail", kwargs={"pk": post.pk}) + "#comments"
