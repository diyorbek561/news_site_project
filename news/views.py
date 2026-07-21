
from django.views.generic import CreateView,DeleteView,DetailView,ListView,UpdateView
from .models import News

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import  redirect
from .forms import CommentForm
class NewsListView(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = News.objects.all()
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            queryset = queryset.filter(title__icontains = query)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        return queryset


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        from .models import Category
        context['categories']=Category.objects.all()
        return context




class NewsCreateView(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'CRUD/post_create.html'
    success_url = reverse_lazy('home')
    fields = ['title','content','image','category','slug','status']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsDetailView(DetailView):
    model = News
    template_name = 'CRUD/post_read.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'object'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=self.request.user
            comment.post = self.object
            comment.save()
        return redirect('post_detail',slug = self.object.slug)





class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = News
    template_name = 'CRUD/post_delete.html'
    success_url = reverse_lazy('home')
    def get_queryset(self):
        return News.objects.filter(author=self.request.user)

    slug_field = 'slug'
    slug_url_kwarg = 'slug'
class NewsUpdateView(UpdateView):
    model = News
    template_name = 'CRUD/post_update.html'
    fields = ['title','content','image','category']
    success_url = reverse_lazy('home')
    def get_queryset(self):
        return News.objects.filter(author=self.request.user)

    slug_field = 'slug'
    slug_url_kwarg = 'slug'