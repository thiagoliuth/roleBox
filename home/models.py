from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Categoria(models.Model):
    class CategoriaType(models.TextChoices):
        MUSICA = 'musica', 'Música'
        TEATRO = 'teatro', 'Teatro'
        DANCA = 'danca', 'Dança'
        CULINARIA = 'culinaria', 'Culinária'
        ESPORTE = 'esporte', 'Esporte'
        ARTE = 'arte', 'Arte'
        FESTA = 'festa', 'Festa'
        RAVE = 'rave', 'Rave'
        
    tipo = models.CharField(max_length=20, choices=CategoriaType.choices)

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return self.get_tipo_display()


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.get_full_name() or self.username


class InteracaoRole(models.Model):
    class InteractionType(models.TextChoices):
        LIKE = 'like', 'Like'
        DISLIKE = 'dislike', 'Dislike'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=InteractionType.choices)
    interacted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role"],
                name="unique_user_role_interaction"
            )
        ]

class Role(models.Model):
    idRole = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    dataRole = models.DateField()
    horarioRole = models.TimeField()
    siglaEstado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=80)
    bairro = models.CharField(max_length=80)
    rua = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="roles"
    )
    votosPositivos = models.IntegerField(default=0)
    votosNegativos = models.IntegerField(default=0)
    mediaClassificacao = models.FloatField(default=0.0)
    ehPago = models.BooleanField(default=False)
    ehPublico = models.BooleanField(default=True)
    linkSite = models.URLField(blank=True, null=True)
    linkInstagram = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="roles"
    )


class RoleImage(models.Model):
    image = models.ImageField(upload_to='role_images/')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_images')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]
        constraints = [
            models.UniqueConstraint(
                fields=["image", "role"],
                name="unique_image_role"
            )
        ]

    def __str__(self):
        return f"Imagem de {self.role.nome}"
    
class Mensagem(models.Model):
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField()
    autor = models.CharField(max_length=80, default='Anônimo')
    criada_em = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mensagens"
    )


    class Meta:
        ordering = ['-criada_em']

    def __str__(self):
        return self.titulo

