from django.db import models
from django.utils import timezone
#criando as categorias de filme
LISTA_CATEGORIAS = (
    ('WORLDS', 'WORLDS'),
    ('KDA','KDA'),
    ('TRUE DAMAGE', 'True Damage'),
    ('PENTAKILL', 'Pentakill'),
    ('HEARTSTEEL', 'Heartsteel'),
)

# Create your models here.
class Filme(models.Model):

    nome            = models.CharField(max_length = 100)
    thumb           = models.ImageField(upload_to = 'thumb_filmes')
    descricao       = models.TextField(max_length = 500)
    categoria       = models.CharField(max_length = 100, choices = LISTA_CATEGORIAS)
    data_criacao    = models.DateField(default = timezone.now)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    filme           = models.ForeignKey("Filme", related_name='musica_filme', on_delete=models.CASCADE)
    nome            = models.CharField(max_length = 100)
    video           = models.URLField()
    thumb           = models.ImageField(upload_to = 'thumb_filmes')
    descricao       = models.TextField(max_length = 500)
    data_criacao    = models.DateField(default = timezone.now)

    def __str__(self):
        return self.filme.nome + "-" + self.nome
