from django.db import models
from django.urls import reverse
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name='Category')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, verbose_name='News category')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


# id - int
# title - varchar (CharField)
# content - varchar
# created_at - datetime (DateField)
# updated_at - datetime
# photo - image
# is_published - bool