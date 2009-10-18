# -*- coding: utf-8 -*-
import logging
import cairo
from estados.basestate import BaseState


log = logging.getLogger(__name__)


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
        self.change_state("Start")


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()
