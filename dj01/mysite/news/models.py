from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='News Title')
    content = models.TextField(blank=True, verbose_name='News content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of last edit')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Active')

    def __str__(self):
        return f'<{self.title}>'


    class Meta:
        verbose_name = '\'News\''
        verbose_name_plural = 'News'
        ordering = ['-created_at']