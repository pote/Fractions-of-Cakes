# -*- encoding: utf-8
"""
Modulo que define la aplicación principal que carga el Frame de la ventana,
inicializa la informacion de la aplicación y permite cambiar entre los
estados que manejan el Content.

"""
import logging
import gtk
from estados import Inicio


log = logging.getLogger(__name__)


class Application:
    """
    Singleton correspondiente a la aplicación principal.
    Contiene un diccionario que mantiene la información que sera utilizada por
    los distintos estados del juego.

    """
    def __init__(self):
        """
        Cargamos el xml que define la interfaz (el marco), asignamos los
        eventos, creamos y asignamos el primer estado del juego.

        """
        builder = gtk.Builder()
        builder.add_from_file("data/frame.glade")
        window = builder.get_object("window")
        self.content = builder.get_object("dummycontent")
        builder.connect_signals(self)

        self.info = dict()
        self.change_state(Inicio)
        window.show()


    def change_state(self, state_class):
        """
        Cambiamos el estado de la aplicación, modificamos Content.
       
        """
        parent = self.content.parent
        parent.remove(self.content)
        new_state = state_class(self)
        # del self.content
        self.content = new_state
        self.content.get_content().reparent(parent)


    def on_FRAME_destroy(self, userdata):
        gtk.main_quit()


    def run(self):
        gtk.main()


app = Application()        
