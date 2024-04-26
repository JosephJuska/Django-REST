from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(
        verbose_name='Article Title',
        max_length=256,
        null=False,
        blank=False
    )

    content = models.TextField(
        verbose_name='Article Content',
        blank=False,
        null=False
    )

    banner = models.ImageField(
        verbose_name='Article Banner',
        upload_to='banners/',
        null=False,
        blank=False
    )

    created_at = models.DateField(
        verbose_name='Article Creation Date',
        auto_now_add=True
    )

    updated_at = models.DateField(
        verbose_name='Article Update Date',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'