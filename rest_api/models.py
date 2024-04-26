from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# ARTICLE MODEL
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

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

# PRODUCT DESIGN MODEL

class ProductModel(models.Model):
    title = models.CharField(
        verbose_name='Product Title',
        max_length=256,
        null=False,
        blank=False
    )

    image = models.ImageField(
        verbose_name='Product Image',
        upload_to='products/',
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class TextModel(models.Model):
    title = models.CharField(
        verbose_name='Design Title',
        max_length=256,
        null=False,
        blank=False
    )

    identifier = models.CharField(
        verbose_name='Design Identifier',
        max_length=256,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Text Design'
        verbose_name_plural = 'Text Designs'

class DesignTextModel(models.Model):
    text = models.ForeignKey(TextModel, on_delete=models.CASCADE)

    context = models.CharField(
        verbose_name='Design Context',
        max_length=256,
        null=False,
        blank=False,
        default='BRANDNAME'
    )

    x_coor = models.FloatField(
        verbose_name='Design X Coordinate',
        null=False,
        blank=False,
        default=1.0
    )

    y_coor = models.FloatField(
        verbose_name='Design Y Coordinate',
        null=False,
        blank=False,
        default=1.0
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class DesignImageModel(models.Model):
    image = models.ImageField(
        verbose_name='Design Image',
        upload_to='design_images/',
        null=False,
        blank=False
    )

    x_coor = models.FloatField(
        verbose_name='Design Image X Coordinate',
        null=False,
        blank=False,
        default=1.0
    )

    y_coor = models.FloatField(
        verbose_name='Design Image Y Coordinate',
        null=False,
        blank=False,
        default=1.0
    )

    class Meta:
        verbose_name = 'Design Image'
        verbose_name_plural = 'Design Images'

class DesignModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE)

    texts = models.ManyToManyField(DesignTextModel)

    images = models.ManyToManyField(DesignImageModel)

    created_at = models.DateTimeField(
        verbose_name='Created At',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated At',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'