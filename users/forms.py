from PIL import Image

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'gender', 'bio')


class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(label=_('Photo'),
                             help_text=_('JPG, GIF or PNG. Max size of 1 MB.'))

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        try:
            main, sub = photo.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'jpg', 'gif', 'png']):
                raise forms.ValidationError(_("Please use a JPEG, GIF or PNG image."))
            if len(photo) > 1024000:
                raise forms.ValidationError(_("Please select a image that is less than 1MB."))
        except AttributeError:
            raise forms.ValidationError(_("Please select a image."))
        return photo

    def save(self, commit=True):
        user = super(PhotoForm, self).save(commit)

        image = Image.open(user.photo)
        size = (200, 200)

        (pw, ph) = image.size
        (nw, nh) = size

        if (pw, ph) != (nw, nh):
            pr = float(pw / ph)
            nr = float(nw / nh)

            if pr > nr:
                # photo aspect is wider than destination ratio
                tw = int(round(nh * pr))
                image = image.resize((tw, nh), Image.ANTIALIAS)
                l = int(round((tw - nw) / 2.0))
                image = image.crop((l, 0, l + nw, nh))
            elif pr < nr:
                # photo aspect is taller than destination ratio
                th = int(round(nw / pr))
                image = image.resize((nw, th), Image.ANTIALIAS)
                t = int(round((th - nh) / 2.0))
                image = image.crop((0, t, nw, t + nh))
            else:
                # photo aspect matches the destination ratio
                image = image.resize(size, Image.ANTIALIAS)
            image.save(user.photo.path, quality=90)
        return user

    class Meta:
        model = User
        fields = ('photo',)
