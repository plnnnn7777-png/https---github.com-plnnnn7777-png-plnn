from django.db import models


class Service(models.Model):
    """Beauty salon service with basic marketing details."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "title"]

    def __str__(self) -> str:
        return self.title
