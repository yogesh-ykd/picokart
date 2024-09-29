from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(max_length=255, unique=True)
    trending = models.BooleanField(default=False)
    recommendations = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    buying_links = models.JSONField(blank=True, null=True)
    description = models.TextField()
    specifications = models.JSONField(blank=True, null=True)
    product_slug = models.CharField(max_length=500, unique=True)
    product_image = models.JSONField(blank=True, null=True)
    asin_code = models.CharField(max_length=255, blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    trending = models.BooleanField(default=False)
    region = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField()
    review_text = models.TextField()
    review_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} star review by {self.product.name}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    html = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    seo_tags = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Affiliate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    affiliate_url = models.URLField()
    source = models.CharField(max_length=255, choices=[('Amazon', 'Amazon'), ('Other', 'Other')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.source} affiliate link"