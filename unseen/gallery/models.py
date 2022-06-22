from django.db import models
from django.urls import reverse
from django.forms import TextInput, Textarea, CheckboxInput, ModelForm

from autoslug import AutoSlugField
from orderable.models import Orderable


class Photo(Orderable):
    name = models.CharField(max_length=256, unique=True)
    # image = models.ImageField(blank=False)
    description = models.CharField(max_length=256, blank=True)
    photo = models.ImageField(blank=False)
    slug = AutoSlugField(populate_from='name')

    def get_next_photo(self):
        if Photo.objects.all().count() > 1:
            if self.sort_order < Photo.objects.all().count() - 1:
                return Photo.objects.get(sort_order=self.sort_order + 1)
            else:
                return Photo.objects.get(sort_order=0)
        else:
            return None

    def get_previous_photo(self):
        if Photo.objects.all().count() > 1: 
            if self.sort_order - 1 > 0:
                return Photo.objects.get(sort_order=self.sort_order - 1)
            else:
                return Photo.objects.get(sort_order=Photo.objects.all().count() - 1)
    
    def get_previous_photo_convo_url(self):
        return self.get_previous_photo().get_conversation_url()

    def get_next_photo_convo_url(self):
        return self.get_next_photo().get_conversation_url()

    def get_previous_photo_slug(self):
        return self.get_previous_photo().slug

    def get_next_photo_slug(self):
        return self.get_next_photo().slug

    def response_num(self):
        return self.comments.all().count()

    def featured_response(self):
        return self.comments.filter(featured=True).last()

    def get_absolute_url(self):
        return reverse("conversation", args=[self.slug])

    def get_conversation_url(self):
        return '/gallery/{}/conversation/'.format(self.slug)

    def get_comments(self):
        return self.comments.all().order_by('-featured')
        
    def __unicode__(self):
        return self.name

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

    def __str__(self):
        return "'{}' —{} | response to {}".format(self.response, self.display_name, self.photo.name)


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['first_name', 'last_name', 'email',
                  'response', 'consent_to_share', ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'photo-convo__input  photo-convo__input--names'}),
            'last_name': TextInput(attrs={'class': 'photo-convo__input photo-convo__input--names'}),
            'email': TextInput(attrs={'class': 'photo-convo__input'}),
            'response': Textarea(attrs={'rows':2, 'cols':20, 'class': 'photo-convo__input photo-convo__input--response'}),
            'consent_to_share': CheckboxInput({'class': 'photo-convo__input photo-convo__input--consent'}),
        }
        help_texts = {
            'consent_to_share': 'I grant OSF permission to share this response on social media. \
                Your quote will be shared along with other audience responses and will appear with a \
                first name and last initial: -- “Quote” - Liz, L.',
        }
