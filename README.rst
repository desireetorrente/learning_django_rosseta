Learning Django-rosetta
=======================

Este es un repositorio para aprende sobre Django.rosetta y
probarla como posible aplicación en un proyecto de Django 3.1

Traducción Django
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://docs.djangoproject.com/en/3.1/topics/i18n/translation/

Django traduce las string que le indicas en el código y crea unos
archivos de texto plano (`.po <https://docs.djangoproject.com/en/3.1/topics/i18n/#term-message-file>`_) con las cadenas
a traducir donde, los traductores pueden escribir cadenas traducidas.
Una vez estos archivos están rellenos con las traducciones, tienen que ser compilados.

Traducción estandar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para decir que string queremos traducir hay que usar la función ``get_text()``.

.. code-block:: python

    from django.http import HttpResponse

    from django.utils.translation import gettext as _

    def traducciones_list(request):
        output = _('Bienvenido a las traducciones')

        return HttpResponse(output)


Traducción Lazy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es importante saber cuando usar el modo lazy y el "normal".
En este caso usamos la función ``gettext_lazy()``.
El modo lazy lo que nos proporciona es que se traduce la string cuando y solo cuando
es usada como por ejemplo en una template y sin embargo, el modo "normal" se ejecuta
cuando es llamada la función, da igual si se usa o no la string.

Info: https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#lazy-translations


Crear los archivos de traducción
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**1. Crear el path donde van a ir los archivos de traducción:**
- Crear una carpeta locale para guardar los archivos .po
- Configurar en setting.py este path, por ejemplo:

.. code-block:: python

   # Build paths inside the project like this: BASE_DIR / 'subdir'.
   BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
   LOCALE_PATHS = [str(BASE_DIR / "locale")]

**2. Crear los messages files:**

de => especificación del idioma.

``django-admin makemessages -l de``

**3. Explicaicón rápida del archivo .po**
* msgid: es la string a traducir que está puesta en el código. NO cambiar
* msgstr: espacio reservado para poner la traducción.

**4. Compilar los archivos .po**
``django-admin compilemessages``
Esto convierte los archivos .po en .mo y la traducción está lista para usarse.


.. note::
    Este proyecto tiene el layout por defecto de Django pero no es
    el deseable.
    Además se ha creado el folder docs con Sphinx.
