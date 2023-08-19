from django.db import models

class Articles(models.Model):
    post_autor = models.CharField('Автор', max_length=50, default='Unknown')
    post_autor_photo = models.CharField('Фото автора', max_length=250, default='Unknown')
    post_title = models.CharField('Заголовок', max_length=250, default='Unknown')
    post_photo = models.CharField('Картинка к статье', max_length=250, default='Unknown')
    post_category = models.CharField('Категория', max_length=250, default='Unknown')
    post_full_text = models.TextField('Статья', default='Unknown')
    post_date = models.DateTimeField('Дата публикации')
    post_viev = models.IntegerField('Просмотры', default=0)
    post_like = models.IntegerField('Лайки', default=0)
    post_comment = models.IntegerField('Комментарии', default=0)
    post_bookmark = models.IntegerField('Закладки', default=0)


    #def __str__(self):
        #return "Автор: {}\nФото автора: {}\nЗаголовок: {}\nКартинка к статье: {}\nКатегория: {}\nАнонс: {}\nСтатья: {}\nДата публикации: {}".format(
            #self.autor, self.autor_photo, self.post_title, self.post_photo, self.post_category, self.anons, self.full_text, self.date
        #)



# Create your models here.



class NewTab(models.Model):
    name = models.CharField('Name', max_length=50, default='Unknown')
    age = models.IntegerField('Age', default=0)

