from django.db import models

class Post(models.Model):
    heading = models.CharField(max_length=50, verbose_name='Заголовок', help_text='Введите заголовок')
    description = models.TextField('Введите содержимое поста')
    image = models.ImageField(upload_to='blog/photo', blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    publication = models.BooleanField()
    views_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров', default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пост'

    def str(self):
        return f'{self.heading}'
