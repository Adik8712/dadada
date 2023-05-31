from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='post/', verbose_name="Изображение")
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True,
         verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"{self.title} | {self.created_at}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"





# [
#     (image='image.url', title="Item"),
#     (image='image.url', title="Item"),
#     (image='image.url', title="Item"),
#     (image='image.url', title="Item"),
#     (image='image.url', title="Item"),
#     (image='image.url', title="Item"),
# ]


# # {% for i in context %}
# # {{ i.title }}
# # {% endfor %}