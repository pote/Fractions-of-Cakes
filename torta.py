# -*- encoding: utf-8
import math
from utils import draw_arc


class Torta:
    def __init__(self, fraction, pos, radius):
        """
        Creamos una torta de centro pos, radio radius y que corresponda a la
        fraccion fraction. El parametro fraction es una lista cuyo primer
        elemento es el numerador y el segundo el denominador de la fraccion.

        """
        self.M = fraction[0]
        self.N = fraction[1]
        self.center = pos
        self.radius = radius
        self.selected = [0] * self.N


    def select(self, pos):
        """
        Si pos esta dentro del area de la torta cambia el estado del trozo y 
        devuelve True, en caso contrario devuelve False.

        """
        x = pos[0] - self.center[0]
        y = pos[1] - self.center[1]
        if math.pow(x, 2) + math.pow(y, 2) > math.pow(self.radius, 2):
            return False
        angle = math.atan2(y, x)
        if angle < 0:
            angle += 2 * math.pi
        sector = angle * self.N / (2 * math.pi)
        index = int(math.floor(sector))
        self.selected[index] = 1 - self.selected[index]
        return True


    def check(self):
        """
        Devuelve True si esta seleccionada la cantidad de sectores
        correspondientes a la fraccion, False en caso contrario.

        """
        return sum(self.selected) == self.M


    def draw(self, cairo_drawing_area):
        """
        Dibuja la torta.

        """
        for i in xrange(self.N):
            angle_start = 2 * math.pi * i / self.N
            angle_end = 2 * math.pi * (i + 1) / self.N
            if self.selected[i]:
                fg = (1.0, 1.0, 0.0)
                bg = (0.0, 1.0, 1.0)
            else:
                fg = (1.0, 0.0, 0.0)
                bg = (0.0, 1.0, 0.0)
            draw_arc(cairo_drawing_area, fg, bg, self.center[0], self.center[1],
                self.radius, angle_start, angle_end)       
