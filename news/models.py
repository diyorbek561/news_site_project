from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "DRAFT"
        PUBLISHED = "PB", "PUBLISHED"

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        ordering = ['-created_time']

    def save(self,*args,**kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'post'
            slug = base_slug
            count = 1
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{count}"
                count+=1
            self.slug=slug
        if 'update_fields' in kwargs and kwargs ['update_fields']:
            kwargs['update_fields']=set(kwargs['update_fields']) | {'slug'}
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)




    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})