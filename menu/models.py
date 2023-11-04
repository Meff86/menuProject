from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=True, blank=True)
    named_url = models.CharField(max_length=100, null=True, blank=True)
    menu_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
