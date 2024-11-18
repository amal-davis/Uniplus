from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogCard, University, Course, Scholarship
from django.utils.text import slugify 


class UniversitySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return University.objects.all()

    def location(self, obj):
        return reverse('university_detail', args=[obj.id])  # URL pattern for universities

class CourseSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return reverse('course_detail', args=[obj.id])  # URL pattern for courses

class ScholarshipSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Scholarship.objects.all()

    def location(self, obj):
        generated_slug = slugify(obj.title)  # Generate slug based on the title
        return reverse('scholarship_detail', args=[obj.id, generated_slug])


class BlogSitemap(Sitemap):
    # Define frequency and priority
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return BlogCard.objects.all()

    def location(self, obj):
        generated_slug = slugify(obj.title)  # Generate slug dynamically
        return reverse('blog_detail', args=[obj.id, generated_slug])
