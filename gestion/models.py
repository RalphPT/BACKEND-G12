from django.db import models

# https://docs.djangoproject.com/en/4.2/ref/models/fields/
class Categoria(models.Model):
    # EL id se puede crear o no crear( es obligatorio a nivel de bd) pero si no lo declaramos DJANGO igual lo creara en bd
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=False, unique=True)
    estante = models.TextField()
    piso = models.TextField()

    class Meta:
        #https://docs.djangoproject.com/en/4.2/ref/models/options/
        # sirve para pasar metadata o informacion a la clase de la cual estamos heredando
        db_table = 'categorias'
        # estante       piso
        #   A            1
        #   A            2 (OK)
        #   B            1 (OK)
        #   A            1 (ERROR)
        unique_together =['estante', 'piso']

        # estante       piso
        #   ...
        # nombre        piso
        # 'TERROR'      1
        # 'TERROR'      2 (OK)
        # 'TERROR       1 (ERROR)

        # nombre    id      piso
        # 'TERROR'  1       1
        # 'TERROR'  2       2 (OK)
        # 'TERROR'  1       2 (OK)
        # 'TERROR'  1       1 (ERROR)
        #unique_together = [['estante', 'piso'], ['nombre', 'piso'], ['nombre', 'id', 'piso']]

class Libro(models.Model):
    # no coloco el ID porque django lo creara automaticamente
    titulo = models.TextField(null=False)
    fechaPublicacion = models.DateField(db_column='a-b')
    unidades = models.IntegerField(default=0)
    sinopsis = models.TextField()
    # on_delete > sirve para indicar que va a suceder cuando se intente eliminar una categoria
    # CASACADE > eliminara la categoria y luego todos sus libros
    # PROTECT > evitara la eliminicacion de la categoria mientras que tenga libros
    #SETE NULL > eliminara la categoria y a los libros les cambiara el valor a NULL en la bd
    # SET_DEFAULT > eliminara la categoria y cambiara el valor a un valor por defecto colocado en el parametro DEFAULT
    # DO_NOTHING > elimina la categoria y no cambia el valor de la categoria a la cual pertenece el libro, NO SE RECOMIENDA UTILIZAR ESTO porque genera mala integracion de datos
    categoria = models.ForeignKey(to=Categoria, db_column='categoria_id', related_name='libros', on_delete=models.CASCADE)

    class Meta:
        db_table = 'libros'

class Autor(models.Model):
    ...
    # nombre tiene que ser not null,
    nombre = models.TextField(null=False, unique=True)
    # nacionalidad tiene que ser texto
    nacionalidad = models.TextField()
    # foto ImageField
    foto = models.ImageField()
    # el nombre y nacionalidad no se pueden repetir
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['nombre', 'nacionalidad'], name='unique_autor')
    #     ]
    # https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
    #Relacion de muchos a muchos y esto creara la tabla puente, pivote o detalle
    libros = models.ManyToManyField(to=Libro)
    class Meta:
        db_table = 'autores'
        unique_together = ['nombre', 'nacionalidad']

