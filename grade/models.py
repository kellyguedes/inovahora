from django.db import models
from django.utils import timezone

#Todas as linhas começando com from ou import são linhas que adicionam alguns pedaços de outros arquivos.
#Então ao invés de copiar e colar as mesmas coisas em cada arquivo, podemos incluir algumas partes com from... import...
#class Post(models.Model): - esta linha define o nosso modelo (é um objeto).
#class é uma palavra-chave especial que indica que estamos definindo um objeto.
#Post é o nome do nosso modelo, podemos lhe dar um nome diferente (mas é preciso evitar os espaços em branco e caracteres especiais). Sempre comece um nome de classe com uma letra maiúscula.
#models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados
#title, text, created_date,published_date e author
#models.CharField - assim é como você define um texto com um número limitado de caracteres.
#models.TextField - este é para textos longos, sem um limite. Será ideal para um conteúdo de post de blog?
#models.DateTimeField - este é uma data e hora.
#models.ForeignKey - este é um link para outro modelo
#def publish(self):? Ele é exatamente o nosso método publish. significa que se trata de um função/método. publish é o nome do método
#Métodos muitas vezes retornam (return) algo. Há um exemplo disso no método __str__. Nesse cenário, quando chamamos __str__() receberemos um texto (string), com um título do Post.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
