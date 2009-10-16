# -*- coding: utf-8 -*-
import logging


log = logging.getLogger(__name__)


class BaseState(object):
    """ tareas comunes a todos los estados """

    def __init__(self, appmanager):
        super(BaseState, self).__init__()

        self._appmanager = appmanager
        # cuando BaseState se instancia desde una clase heredada self.__class__ es esa clase y no BaseState
        # esto nos permite usar la clase misma como llave en el diccionario
        self.state_info = appmanager.state_info[self.__class__] if self.__class__ in appmanager.state_info else {}


    def change_state(self, new_state):
        self._appmanager.state_info[self.__class__] = self.state_info
        self._appmanager.change_state(new_state)
