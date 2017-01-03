from django.db import models

class OrganizationalUnit(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

class Cooperative(OrganizationalUnit):

    def __str__(self):
        return self.name

class Farmer(OrganizationalUnit):
    cooperatives = models.ManyToManyField(Cooperative, blank=True, related_name='farmers')

    def __str__(self):
        return self.name

class Distributor(OrganizationalUnit):

    def __str__(self):
        return self.name
