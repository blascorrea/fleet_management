
# Fleet management

Este módulo gestiona los vehículos de los contactos

___
Explicar en qué archivo se debe definir el modelo (models) y los conceptos de herencia
de models.Model.

* Debido al patrón de diseño que utiliza Odoo (MVC) es recomendable seguir con la práctica de poner los modelos en la carpeta models
* Se puede heredar de la clase models.Model de las siguientes formas:
    * Herencia clásica, cuyo propósito es extender o modificar atributos y métodos del modelo padre
    * Herencia delegada, lo cual consite en delegar parte del comportamiento del modelo relacionado, en este caso se crea una tabla con un campo relacionado al modelo principal.
    * Herencia por prototipo, cuyo propósito es heredar todos los atributos y métodos del modelo relacionado creando una tabla con todas las columnas del modelo principal
