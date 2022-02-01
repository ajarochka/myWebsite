from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='', null=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='News category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title
# id - int
# title - varchar (CharField)
# content - varchar
# created_at - datetime (DateField)
# updated_at - datetime
# photo - image
# is_published - bool