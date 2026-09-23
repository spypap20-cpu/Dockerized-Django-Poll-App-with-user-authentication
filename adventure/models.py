from django.db import models

class Story(models.Model):
    story_text = models.TextField()
    is_start = models.BooleanField(default=False)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.title


class Choice(models.Model):
    current_scene = models.ForeignKey(Story, on_delete=models.CASCADE)
    choice_text = models.TextField()
    next_scene = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='previous_choices')

    def __str__(self):
        return self.choice_text


