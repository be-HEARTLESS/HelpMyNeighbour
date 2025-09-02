from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """Custom user model extending Django's AbstractUser"""

    # Additional fields for the help neighbor app
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Rating system
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_ratings = models.PositiveIntegerField(default=0)

    # Verification status
    is_verified = models.BooleanField(default=False)

    # Preferences
    is_available_for_help = models.BooleanField(default=True)
    preferred_help_categories = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"{self.username} ({self.email})"

    def update_rating(self, new_rating):
        """Update user's average rating"""
        total_score = (self.rating * self.total_ratings) + new_rating
        self.total_ratings += 1
        self.rating = total_score / self.total_ratings
        self.save()
