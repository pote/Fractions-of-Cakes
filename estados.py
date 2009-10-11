# -*- encoding: utf-8
"""
Mantenemos los distintos estados de la aplicación.

class State:
    def __init__(self):
        debe retornar el contenido que se pondra en CONTENT. 

"""
import logging
import gtk
import cairo


log = logging.getLogger(__name__)
IMAGE = {
    "start": cairo.ImageSurface.create_from_png("data/start.png"),
    "background": cairo.ImageSurface.create_from_png("data/background.png"),
    "completed": cairo.ImageSurface.create_from_png("data/completed.png"),
    "failed": cairo.ImageSurface.create_from_png("data/failed.png"),
    "win": cairo.ImageSurface.create_from_png("data/win.png"),
    "gameover": cairo.ImageSurface.create_from_png("data/gameover.png"),
}


class Inicio:
    def __init__(self, state):
        builder = gtk.Builder()
        builder.add_from_file("data/state_inicio.glade")
        builder.connect_signals(self)
        self.content = builder.get_object("window").child
        self.state = state
        

    def get_content(self):
        """
        Devuelve el widget que colocaremos en content_container.

        """
        log.debug("gtk: %s", self.content)
        return self.content


    def dibujar(self):
        cr = self.content.window.cairo_create()
        cr.set_source_surface(IMAGE["start"], 0, 0)
        cr.paint()


    def on_drawingarea_button_press_event(self, widget, event):
        #log.debug("-> cambiar estado a Jugar")
        self.state.change_state(Fin)


    def on_drawingarea_expose_event(self, widget, event):
        self.dibujar()


class Fin:
    def __init__(self, state):
        builder = gtk.Builder()
        builder.add_from_file("data/state_inicio.glade")
        builder.connect_signals(self)
        self.content = builder.get_object("window").child
        

    def get_content(self):
        """
        Devuelve el widget que colocaremos en content_container.

        """
        log.debug("gtk: %s", self.content)
        return self.content


    def dibujar(self):
        cr = self.content.window.cairo_create()
        cr.set_source_surface(IMAGE["win"], 0, 0)
        cr.paint()


    def on_drawingarea_button_press_event(self, widget, event):
        log.debug("-> cambiar estado a Jugar")


    def on_drawingarea_expose_event(self, widget, event):
        self.dibujar()
