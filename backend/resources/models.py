from django.db import models
from django.utils.text import slugify


class Resource(models.Model):
    FILE_TYPE_PDF = 'pdf'
    FILE_TYPE_DOC = 'doc'
    FILE_TYPE_XLS = 'xls'
    FILE_TYPE_PPT = 'ppt'
    FILE_TYPE_ZIP = 'zip'
    FILE_TYPE_OTHER = 'other'
    FILE_TYPE_CHOICES = [
        (FILE_TYPE_PDF, 'PDF'),
        (FILE_TYPE_DOC, 'DOC'),
        (FILE_TYPE_XLS, 'XLS'),
        (FILE_TYPE_PPT, 'PPT'),
        (FILE_TYPE_ZIP, 'ZIP'),
        (FILE_TYPE_OTHER, 'Other'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES, default=FILE_TYPE_OTHER)
    download_count = models.PositiveIntegerField(default=0)
    is_free = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
