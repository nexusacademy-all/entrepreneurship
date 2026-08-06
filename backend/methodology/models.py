from django.db import models


class MethodologySection(models.Model):
    SECTION_VISION = 'vision'
    SECTION_PHILOSOPHY = 'philosophy'
    SECTION_POSITIONING = 'positioning'
    SECTION_ASSETS = 'assets'
    SECTION_PRINCIPLES = 'principles'
    SECTION_CHOICES = [
        (SECTION_VISION, 'Vision'),
        (SECTION_PHILOSOPHY, 'Philosophy'),
        (SECTION_POSITIONING, 'Positioning'),
        (SECTION_ASSETS, 'Assets'),
        (SECTION_PRINCIPLES, 'Principles'),
    ]

    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    featured_image = models.ImageField(upload_to='methodology/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"
