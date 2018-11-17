from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE 
    )
    title = models.CharField(
        max_length=200
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
    
    def __str__(self): #Definindo o titulo do post no painel admin
        return self.title