from django.db import models

# Create your models here.
# modelop del registro de usuarios
class Usuarios(models.Model):
    nombre = models.CharField('nombre',max_length=30, null=False, blank=False)
    apellido = models.CharField('apellido',max_length=30, null=False, blank=False)
    email = models.EmailField('email', max_length=254, null=False, blank=False)
    direccion = models.CharField('direccion',max_length=100, null=False, blank=False)
    identificacion = models.PositiveIntegerField('identificacion', null=False, blank=False, unique=True)
    telefono = models.BigIntegerField('telefono', null=False, blank=False)
    objects = models.Manager()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']


# datos de la empresa
class Empresa(models.Model):
    """Model definition for Empresa."""
    nombre = models.CharField('nombre',max_length=30, null=False, blank=False)
    direccion = models.CharField('direccion',max_length=100, null=False, blank=False)
    ciudad = models.CharField('ciudad', max_length=100, null=False, blank=False)
    telefono = models.BigIntegerField('telefono', null=False, blank=False)
    email = models.EmailField('email', max_length=254, null=False, blank=False)
    paginaweb = models.URLField('paginaweb', max_length=200, null=False, blank=False)
    mision = models.TextField('mision', null=False, blank=False)
    vision = models.TextField('vision', null=False, blank=False)
    objetivos = models.TextField('objetivos', null=False, blank=False)
    objects = models.Manager()
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Empresa."""
        db_table = ''
        managed = True
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        """Unicode representation of Empresa."""
        return self.nombre


class Cliente(models.Model):
    """Model definition for Cliente."""
    nombre = models.CharField('nombre',max_length=30, null=False, blank=False)
    apellido = models.CharField('apellido',max_length=30, null=False, blank=False)
    identificacion = models.PositiveIntegerField('identificacion', null=False, blank=False, unique=True)
    direccion = models.CharField('direccion',max_length=100, null=False, blank=False)
    telefono = models.BigIntegerField('telefono', null=False, blank=False)
    email = models.EmailField('email', max_length=254, null=False, blank=False)
    objects = models.Manager()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Cliente."""
        db_table = ''
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return self.nombre


class Proveedor(models.Model):
    """Model definition for Proveedor."""
    razon_social = models.CharField('razon social',max_length=30, null=False, blank=False)
    direccion = models.CharField('direccion',max_length=100, null=False, blank=False)
    nit_cif = models.PositiveIntegerField('NIT/CIF', null=False, blank=False, unique=True)
    telefono = models.BigIntegerField('telefono', null=False, blank=False)
    persona_contacto = models.CharField('persona de contacto',max_length=30, null=False, blank=False)
    actividad_economica = models.CharField('actividad economica',max_length=100, null=False, blank=False)
    paginaweb = models.URLField('paginaweb', max_length=200, null=False, blank=False)
    email = models.EmailField('email', max_length=254, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=False, blank=False)
    fax = models.BigIntegerField('fax', null=False, blank=False)
    objects = models.Manager()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Proveedor."""
        db_table = ''
        managed = True
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedors'

    def __str__(self):
        """Unicode representation of Proveedor."""
        return self.razon_social


class Empleado(models.Model):
    """Model definition for Empleado."""
    nombre = models.CharField('nombre',max_length=30, null=False, blank=False)
    apellido = models.CharField('apellido',max_length=30, null=False, blank=False)
    identificacion = models.PositiveIntegerField('identificacion', null=False, blank=False, unique=True)
    direccion = models.CharField('direccion',max_length=100, null=False, blank=False)
    telefono = models.BigIntegerField('telefono', null=False, blank=False)
    email = models.EmailField('email', max_length=254, null=False, blank=False)
    birtday = models.DateField('cumpleaños',auto_now=False, auto_now_add=False)
    objects = models.Manager()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Empleado."""
        db_table = ''
        managed = True
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return "%s %s" % (self.nombre, self.apellido)


class Horalaborada(models.Model):
    """Model definition for Horalaborada."""
    horainicio = models.TimeField('hora de inicio',auto_now=False, auto_now_add=False)
    horafinal = models.TimeField('hora de finalizacion', auto_now=False, auto_now_add=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    objects = models.Manager()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Horalaborada."""
        db_table = ''
        managed = True
        verbose_name = 'Horalaborada'
        verbose_name_plural = 'Horalaboradas'

    def __str__(self):
        """Unicode representation of Horalaborada."""
        pass
