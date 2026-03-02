from django import forms
from .models import Artwork, ArtworkComment


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ["title", "author_name", "description", "image", "tags"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class ArtworkCommentForm(forms.ModelForm):
    class Meta:
        model = ArtworkComment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Напишите комментарий…",
                    "style": (
                        "width:100%; padding:12px; border-radius:14px; "
                        "border:1px solid rgba(15,23,42,.12); "
                        "background: rgba(255,255,255,.75);"
                    ),
                }
            )
        }