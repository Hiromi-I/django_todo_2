from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    title = models.CharField("タイトル", max_length=100)
    description = models.TextField("詳細")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_complete = models.BooleanField("完了済み")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return f"[{self.author}] {self.title}"
