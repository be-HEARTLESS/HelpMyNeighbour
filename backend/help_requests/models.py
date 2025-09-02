from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class HelpRequest(models.Model):
    """Model for help requests"""

    # Request categories
    CATEGORY_CHOICES = [
        ('daily_help', 'Daily Help'),
        ('transport', 'Transport'),
        ('emergency', 'Emergency'),
        ('resources', 'Resources'),
        ('learning', 'Learning'),
        ('other', 'Other'),
    ]

    # Urgency levels
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
    ]

    # Status choices
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    # Basic information
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='normal')

    # Location information
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # Relationships
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='help_requests')
    assigned_helper = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_requests')

    # Status and timestamps
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    # Additional fields
    estimated_duration = models.DurationField(blank=True, null=True)
    reward_points = models.PositiveIntegerField(default=0)
    is_public = models.BooleanField(default=True)

    # Images/attachments
    images = models.JSONField(default=list, blank=True)  # Store image URLs

    class Meta:
        verbose_name = _('Help Request')
        verbose_name_plural = _('Help Requests')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.requester.username}"

    def mark_completed(self):
        """Mark the request as completed"""
        from django.utils import timezone
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.save()

        # Update helper's rating if applicable
        if self.assigned_helper:
            # This would typically be called after user provides rating
            pass


class HelpRequestResponse(models.Model):
    """Model for responses/offers to help requests"""

    help_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, related_name='responses')
    helper = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='help_responses')

    message = models.TextField(blank=True, null=True)
    offered_at = models.DateTimeField(auto_now_add=True)

    # Response status
    is_accepted = models.BooleanField(default=False)
    accepted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('Help Request Response')
        verbose_name_plural = _('Help Request Responses')
        unique_together = ['help_request', 'helper']
        ordering = ['-offered_at']

    def __str__(self):
        return f"Response by {self.helper.username} to {self.help_request.title}"


class Rating(models.Model):
    """Model for ratings after help completion"""

    help_request = models.OneToOneField(HelpRequest, on_delete=models.CASCADE, related_name='rating')
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='given_ratings')
    rated_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_ratings')

    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')
        unique_together = ['help_request', 'rater']
        ordering = ['-created_at']

    def __str__(self):
        return f"Rating {self.rating} by {self.rater.username} for {self.rated_user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the rated user's average rating
        self.rated_user.update_rating(self.rating)
