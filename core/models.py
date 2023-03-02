from django.db import models

class Fabricante(models.Model):
    fabricante = models.CharField(max_length=30, verbose_name='Fabricante')

    def __str__(self):
        return self.fabricante

    class Meta:
        verbose_name_plural = 'Fabricantes'
        
class Tipo(models.Model):
    tipo = models.CharField(max_length=30, verbose_name='Tipo de veículo')

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name_plural = 'Tipos de veículos'

class Categoria(models.Model):
    categoria = models.CharField(max_length=30, verbose_name='Categoria')
    id_tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING, verbose_name='Tipo de Veículo')

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name_plural = 'Categorias'   

class Veiculo(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING, verbose_name='Tipo de Veículo')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.DO_NOTHING, verbose_name='Fabricante')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoria')

    nome = models.CharField(max_length=70, verbose_name='Nome')
    modelo = models.CharField(max_length=20, verbose_name='Modelo')
    motor = models.CharField(max_length=30, verbose_name='Motor')
    cor = models.CharField(max_length=15, verbose_name='Cor')
    ano = models.IntegerField(default=2022, verbose_name='Ano')
    placa = models.CharField(max_length=12, verbose_name='Placa')
    km = models.IntegerField(default=0, blank=True, null=True, verbose_name='KM')
    cambio = models.CharField(max_length=30, verbose_name='Câmbio')
    combustivel = models.CharField(max_length=30, verbose_name='Combustível')
    portas = models.IntegerField(default=0, blank=True, null=True, verbose_name='Portas')

    opcionais = models.TextField(blank=True, null=True, verbose_name='Opcionais')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Preco')
    
    choices_estado = (('N', 'Novo'),('S', 'Seminovo'),('U', 'Usado'))
    estado = models.CharField(max_length=1, choices=choices_estado)
    
    choices_status = (('D', 'Disponível'),('V', 'Vendido'))
    status = models.CharField(max_length=1, choices=choices_status, default=('D', 'Disponível'))
    vizualizacoes = models.IntegerField(default=0, verbose_name='Vizualizações')
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Veículos'

class VeiculoImage(models.Model):
    foto = models.ImageField(upload_to='fotos_veiculos', blank=True, null=True, verbose_name='Fotos do veículo')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veículo')
    def __str__(self):
        return self.veiculo.nome
    
    
