# -*- coding: utf-8 -*-
import logging
import cairo
from estados.basestate import BaseState


log = logging.getLogger(__name__)


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
        #self.change_state("Fin")
        self.change_state("Juego")


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()
