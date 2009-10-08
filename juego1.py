import logging
import cairo
from torta import Torta


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

MAXLEVEL = 5
IMAGE = {
    "start": cairo.ImageSurface.create_from_png("start.png"),
    "background": cairo.ImageSurface.create_from_png("background.png"),
    "completed": cairo.ImageSurface.create_from_png("completed.png"),
    "failed": cairo.ImageSurface.create_from_png("failed.png"),
    "win": cairo.ImageSurface.create_from_png("win.png"),
    "gameover": cairo.ImageSurface.create_from_png("gameover.png"),
}


class JuegoModo1:
    def __init__(self):
        log.debug("init - JuegoModo1")
        self.change_state(Inicio(self))
        self.vidas = 5
        self.nivel = 1


    def change_state(self, state):
        self.state = state


    def draw(self, widget, event):
        cr = widget.window.cairo_create()
        self.state.draw(cr)


    def update(self, widget, event):
        if self.state.update(widget, event):
            self.draw(widget, event)


    def check(self, widget, event):
        if isinstance(self.state, Jugar):
            self.state.check(widget, event)

            
class Inicio:
    """
    Mostramos pantalla de inicio y esperamos a que el usuario pulse el raton
    para comenzar el juego.

    """
    def __init__(self, juego):
        self.juego = juego


    def update(self, widget, event):
        self.juego.change_state(Jugar(self.juego))
        self.juego.draw(widget, event)


    def draw(self, cairo_surface):
        log.debug("draw - INICIO")
        cairo_surface.set_source_surface(IMAGE["start"], 0, 0)
        cairo_surface.paint()
    

class Jugar:
    """
    Obtenemos los click's del usuario y esperamos por el resultado del juego.

    """
    def __init__(self, juego):
        self.juego = juego
        self.torta = Torta([3, 5], [100, 100], 80)


    def update(self, widget, event):
        """
        Verifica donde se pulso en el area del usuario y pasa a la torta.

        """
        log.debug("update - Jugar")
        pos = event.get_coords()
        if self.torta.select(pos):
            log.debug("> torta")
            return True
        return False


    def check(self, widget, event):
        """
        Cambia de estado tomando en cuenta los trozos seleccionados.

        """
        log.debug("check - Jugar")
        if self.torta.check():
            self.juego.change_state(Gana(self.juego))
            self.juego.draw(widget, event)
        else:
            self.juego.change_state(Pierde(self.juego))
            self.juego.draw(widget, event)


    def draw(self, cairo_surface):
        """
        Dibujamos la torta.

        """
        log.debug("draw - JUGAR")
        cairo_surface.set_source_surface(IMAGE["background"], 0, 0)
        cairo_surface.paint()
        self.torta.draw(cairo_surface)


class Gana:
    """
    Mostramos pantalla de felicitacion y avanzamos al siguiente nivel.

    """
    def __init__(self, juego):
        self.juego = juego


    def update(self, widget, event):
        """
        """
        self.juego.nivel += 1
        if self.juego.nivel == MAXLEVEL:
            self.juego.change_state(Win(self.juego))
            self.juego.draw(widget, event)
        else:
            self.juego.change_state(Jugar(self.juego))
            self.juego.draw(widget, event)


    def draw(self, cairo_surface):
        """
        Dibujamos felicitacion.

        """
        log.debug("draw - Gana")
        cairo_surface.set_source_surface(IMAGE["completed"], 0, 0)
        cairo_surface.paint()


class Pierde:
    """
    Mostramos pantalla de error. Volvemos al siguiente nivel.

    """
    def __init__(self, juego):
        self.juego = juego


    def update(self, widget, event):
        """
        Quita una vida. Si quedan reinicia el juego sino se va al game over.

        """
        self.juego.vidas -= 1
        if self.juego.vidas == 0:
            self.juego.change_state(GameOver(self.juego))
            self.juego.draw(widget, event)
        else:
            self.juego.change_state(Jugar(self.juego))
            self.juego.draw(widget, event)


    def draw(self, cairo_surface):
        """
        Dibuja pantalla de error.

        """
        log.debug("draw - Pierde")
        cairo_surface.set_source_surface(IMAGE["failed"], 0, 0)
        cairo_surface.paint()


class GameOver:
    """
    El jugador pierde por vidas.

    """
    def __init__(self, juego):
        self.juego = juego


    def update(self, widget, event):
        """
        No hace nada.

        """
        pass


    def draw(self, cairo_surface):
        """
        Dibuja game over.

        """
        log.debug("draw - GameOver")
        cairo_surface.set_source_surface(IMAGE["gameover"], 0, 0)
        cairo_surface.paint()


class Win:
    """
    El jugador llega al final del juego.

    """
    def __init__(self, juego):
        self.juego = juego


    def update(self, widget, event):
        """
        No hace nada.

        """
        pass


    def draw(self, cairo_surface):
        """
        Dibuja felicitacion.

        """
        log.debug("draw - Win")
        cairo_surface.set_source_surface(IMAGE["win"], 0, 0)
        cairo_surface.paint()
