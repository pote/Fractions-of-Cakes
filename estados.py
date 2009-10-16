# -*- coding: utf-8 -*-
import logging
import gtk
import cairo


log = logging.getLogger(__name__)


class Inicio(object):
    """
    Clase de inicio.

    """
    template = "inicio.glade"


    def __init__(self, state):
        self._state = state


    def on_buttonjugar_clicked(self, widget): #, event):
        log.debug("-> cambiar estado a Start")
        self._state.change_state(Start(self._state))


class Start(object):
    """
    Clase para probar las transiciones.

    """
    template = "win.glade"


    def __init__(self, state):
        self._state = state
        self.image = cairo.ImageSurface.create_from_png("data/start.png")


    def on_drawingarea_button_press_event(self, widget, event):
        log.debug("-> cambiar estado a Fin")
        self._state.change_state(Fin(self._state))


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()


class Fin(object):
    """
    Clase para probar las transiciones.

    """
    template = "win.glade"


    def __init__(self, state):
        self._state = state
        self.image = cairo.ImageSurface.create_from_png("data/win.png")


    def on_drawingarea_button_press_event(self, widget, event):
        log.debug("-> cambiar estado a Start")
        self._state.change_state(Start(self._state))


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()
