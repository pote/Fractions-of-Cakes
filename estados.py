# -*- coding: utf-8 -*-
import logging
import gtk
import cairo


log = logging.getLogger(__name__)


class BaseState(object):
    """ tareas comunes a todos los estados """

    def __init__(self, appmanager):
        super(BaseState, self).__init__()
        self._appmanager = appmanager
        print self.__class__


class Inicio(BaseState):
    """
    Clase de inicio.

    """
    template = "inicio.glade"


    def __init__(self, appmanager):
        super(Inicio, self).__init__(appmanager)


    def on_buttonjugar_clicked(self, widget):
        log.debug("-> cambiar estado a Start")
        self._appmanager.change_state(Start(self._appmanager))


class Start(BaseState):
    """
    Clase para probar las transiciones.

    """
    template = "win.glade"


    def __init__(self, appmanager):
        super(Start, self).__init__(appmanager)
        self.image = cairo.ImageSurface.create_from_png("data/start.png")


    def on_drawingarea_button_press_event(self, widget, event):
        #log.debug("-> cambiar estado a Fin")
        #self._appmanager.change_state(Fin(self._appmanager))
        self._appmanager.change_state(Juego(self._appmanager))


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()


class Juego(BaseState):
    """
    Clase que dibuja la torta.

    """
    template = "juego.glade"


    def __init__(self, appmanager):
        super(Juego, self).__init__(appmanager)
        # Aqui tenemos que cargar en la segunda posicion del contenedor vbox
        # una clase torta en este caso.
        # Si fuera otro tipo de juego estariamos cargando un grid que
        # contendria X clases torta.


    def on_drawingarea_button_press_event(self, widget, event):
        log.debug("-> cambiar estado a Fin")
        self._appmanager.change_state(Fin(self._appmanager))


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()


    def on_button_clicked(self, widget):
        log.debug("-> cambiar estado a Start")
        self._appmanager.change_state(Fin(self._appmanager))


class Fin(BaseState):
    """
    Clase para probar las transiciones.

    """
    template = "win.glade"


    def __init__(self, appmanager):
        super(Fin, self).__init__(appmanager)
        self.image = cairo.ImageSurface.create_from_png("data/win.png")


    def on_drawingarea_button_press_event(self, widget, event):
        log.debug("-> cambiar estado a Start")
        self._appmanager.change_state(Start(self._appmanager))


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()
