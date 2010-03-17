# -*- coding: utf-8 -*-
from sugar.activity.activity import Activity, ActivityToolbox
from application import ApplicationManager

class FraccionesActivity(Activity):
    """ Clase principal cuando la aplicacion corre como actividad dentro de Sugar """
    def __init__(self, handle, *args, **kwargs):
        super(FraccionesActivity, self).__init__(handle, *args, **kwargs)

        self.gamename = "Fracciones"

        # barra de herramientas de Sugar
        toolbox = ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # conectar maquina de estados principal
        self.application_manager = ApplicationManager(self)
