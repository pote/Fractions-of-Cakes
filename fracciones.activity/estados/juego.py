# -*- coding: utf-8 -*-
import logging
from estados.basestate import BaseState


log = logging.getLogger(__name__)


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
        self.change_state("Fin")


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_surface(self.image, 0, 0)
        cr.paint()


    def on_button_clicked(self, widget):
        log.debug("-> cambiar estado a Start")
        self.change_state("Fin")
