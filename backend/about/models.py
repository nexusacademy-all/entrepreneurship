from django.db import models


class AboutSection(models.Model):
    SECTION_STORY = 'story'
    SECTION_MISSION = 'mission'
    SECTION_VISION = 'vision'
    SECTION_VALUES = 'values'
    SECTION_TEAM = 'team'
    SECTION_CHOICES = [
        (SECTION_STORY, 'Story'),
        (SECTION_MISSION, 'Mission'),
        (SECTION_VISION, 'Vision'),
        (SECTION_VALUES, 'Values'),
        (SECTION_TEAM, 'Team'),
    ]

    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"


class Founder(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='founder/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"


class TimelineEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    image = models.ImageField(upload_to='timeline/', blank=True, null=True)
    is_milestone = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['event_date', 'order']

    def __str__(self):
        return f"{self.title} - {self.event_date}"
