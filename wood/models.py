from django.db import models


class WoodMenu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, auto_created=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        # if self.parent:
        #     return f"{self.parent.get_absolute_url()}{self.slug}/"
        return f"/menu/{self.slug}/"            
    
    def __str__(self):
        return self.title
    
class Wood(models.Model):
    title = models.CharField(max_length=255)
    menu = models.ForeignKey(WoodMenu, on_delete=models.CASCADE, related_name='items')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['menu', 'id']

    def get_children(self):
        return Wood.objects.filter(parent=self)
    
    def __str__(self):
        return f"{self.menu.title} - {self.title}"
