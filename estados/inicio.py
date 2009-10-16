# -*- coding: utf-8 -*-
import logging
from estados.basestate import BaseState


log = logging.getLogger(__name__)


class Inicio(BaseState):
    """
    Clase de inicio.

    """
    template = "inicio.glade"


    def __init__(self, appmanager):
        super(Inicio, self).__init__(appmanager)


    def on_buttonjugar_clicked(self, widget):
        log.debug("-> cambiar estado a Start")
        self.change_state("Start")
