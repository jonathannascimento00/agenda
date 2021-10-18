from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    #campo usuario = chave estrangeira do Model de Users do django
    #são passados 2 parâmetros para o models.ForeignKey:
    #o primeiro é a classe no qual está o registro primário
    #o segundo é a definição do que acontece quando um registro da primeira classe é deletado

    class Meta:
        db_table = 'evento' #informo que a minha tabela vai ter nome "evento"

    def __str__(self):
        return self.titulo #vai aparecer o nome do título do evento