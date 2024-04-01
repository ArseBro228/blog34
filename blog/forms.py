from django import forms
from .models import Post, Tag, Photo
from multiupload.fields import MultiImageField


class PostForm(forms.ModelForm):
    # photos = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags", ]
        exclude = ('published_date', 'comments', 'user')

    def save(self, commit=True):
        # photo_ids = []
        # for photo in self.cleaned_data['photos']:
        #     photo_ids.append(Photo.objects.create(image=photo))
        instance = super().save(commit)
        # instance.photo_set.add(self.cleaned_data['photos'])
        return instance
