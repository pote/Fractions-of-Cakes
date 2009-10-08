#!/usr/bin/env python
import logging
import gtk
from juego1 import JuegoModo1


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Fracciones:
    def __init__(self):
        self.modo = JuegoModo1()

        builder = gtk.Builder()
        builder.add_from_file("fracciones.xml")
        builder.connect_signals(self)
        window = builder.get_object("window")
        window.show()
        self.drawingarea = builder.get_object("drawingarea")


    def on_window_destroy(self, userdata):
        gtk.main_quit()


    def on_drawingarea_expose_event(self, widget, event):
        self.modo.draw(widget, event)


    def on_drawingarea_button_press_event(self, widget, event):
        self.modo.update(widget, event)


    def on_button_clicked(self, widget):
        log.debug("on_button_clicked")
        self.modo.check(self.drawingarea, None)


if __name__ == "__main__":
    app = Fracciones()
    gtk.main()
