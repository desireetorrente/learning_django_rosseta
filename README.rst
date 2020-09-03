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



Traducción Lazy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es importante saber cuando usar el modo lazy y el "normal".
En este caso usamos la función ``gettext_lazy()``.
El modo lazy lo que nos proporciona es que se traduce la string cuando y solo cuando
es usada como por ejemplo en una template y sin embargo, el modo "normal" se ejecuta
cuando es llamada la función, da igual si se usa o no la string.

https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#lazy-translations

.. note::
    Este proyecto tiene el layout por defecto de Django pero no es
    el deseable.
