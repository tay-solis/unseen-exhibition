from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=256)
    # image = models.ImageField(blank=False)
    description = models.CharField(max_length=256, blank=True)
    url = models.URLField(max_length=256, blank=True)
    photo = models.ImageField(blank=False)

    def response_num(self):
        return self.comments.all().count()

    def featured_response(self):
        return self.comments.filter(featured=True).first()

    def __str__(self):
        return self.name


class Response(models.Model):
    photo = models.ForeignKey(
        "Photo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="comments"
    )
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    # image = models.ImageField(blank=False)
    email = models.EmailField(max_length=256, blank=True)
    response = models.CharField(
        max_length=75,
        blank=False,
        help_text="Max. 75 Characters"
    )
    consent_to_share = models.BooleanField(
        blank=True,
        help_text="Consent to OSF to use response in social media."
    )
    featured = models.BooleanField(
        blank=True,
        help_text="Featured comments will have special styling."
    )

    @property
    def display_name(self):
        return "{} {}.".format(self.first_name, self.last_name[0])
