#!/usr/bin/env python
# -*- encoding: utf8 -*-
"""
La torta es una imagen redonda en un archivo de 500x500 pixeles.
Tiene un borde de 30 pixeles.

Pasado a coordenadas mundiales el radio es: (500-2*30)/(2*500) = 0.44

"""
import os, sys
import math
import gtk
import cairo


WIDTH = 500
HEIGHT = 500
RADIUS = 220
WRADIUS = 0.44


class Cake(gtk.DrawingArea):
    """Widget que dibuja una torta y permite seleccionar trozos de ella"""

    def __init__(self, subdivisions, *args, **kwargs):
        # constructor de la clase base
        gtk.DrawingArea.__init__(self, *args, **kwargs)
        # Carga imagenes
        self.image_bg = cairo.ImageSurface.create_from_png(os.path.join("data", "bg.png"))
        self.image_fg = cairo.ImageSurface.create_from_png(os.path.join("data", "fg.png"))
        # inicializa estado interno (se dibuja en el metodo expose)
        self.reset(subdivisions, draw=false)
        # señales
        self.connect("expose_event", self.expose)
        self.connect("button_press_event", self.select)
        # Los eventos del raton no estan activados para el DrawingArea
        self.add_events(gtk.gdk.BUTTON_PRESS_MASK)


    @property
    def subdivisions(self):
        return len(self.selected_list)


    @property
    def current_fraction(self):
        return (len(selected for selected in self.selected_list if selected), self.subdivisions)


    def reset(self, subdivisions, draw=True):
        # variables de estado de la torta
        self.selected_list = subdivisions * [False]
        if draw:
            context = self.window.cairo_create()
            self._draw(context)



    def expose(self, widget, event):
        """Manejador del evento expose_event"""
        context = widget.window.cairo_create()
        # Elegimos solo la region expuesta al evento
        context.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
        context.clip()
        self._draw(context)


    def select(self, widget, event):
        """Manejador del evento button_press_event"""
        print event.get_coords()
        x, y = event.get_coords()
        if self._select(x, y):
            context = widget.window.cairo_create()
            self._draw(context)


    def _select(self, ux, uy):
        """Selecciona un trozo de la torta. Devuelve True si un objeto fue
        seleccionado, False en caso contrario."""
        # Transformamos las coordenadas del usuario a coordenadas reales (0-1)
        rect = self.get_allocation()
        wx = float(ux) / float(rect.width)
        wy = float(uy) / float(rect.height)
        # Centramos
        wx -= 0.5
        wy -= 0.5
        if math.pow(wx, 2) + math.pow(wy, 2) > math.pow(WRADIUS, 2):
            return False
        angle = math.atan2(wy, wx)
        if angle < 0:
            angle += 2 * math.pi
        sector = angle * self.subdivisions / (2 * math.pi)
        index = int(math.floor(sector))
        self.selected_list[index] = not self.selected_list[index]
        return True
        

    def _draw(self, context):
        """Dibuja el contenido del widget"""

        def draw_grid():
            """Dibuja la rejilla de la torta y sus subdivisiones"""
            context.set_source_rgb(0, 0, 0)
            context.arc(WIDTH/2, HEIGHT/2, RADIUS, 0, 2 * math.pi)
            context.stroke()
            for i in range(self.subdivisions):
                angle = 2 * math.pi * i / self.subdivisions
                context.move_to(WIDTH/2, HEIGHT/2)
                context.line_to(
                    WIDTH/2 + RADIUS*math.cos(angle),
                    HEIGHT/2 + RADIUS*math.sin(angle)
                    )
                context.stroke()


        def mask_image(image):
            """Enmascara la imagen de la torta y dibuja solo los trozos que no
            fueron seleccionados
            """
            # al crear un cairo.Context los cambios se graban en el Surface que se le pase al constructor
            # por lo tanto necesitamos usar dummy_image para no alterar image que es propio a la clase
            dummy_image = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
            image_ctx = cairo.Context(dummy_image)
            # ponemos la imagen como source_surface de modo que cairo no nos escriba arriba
            image_ctx.set_source_surface(image)
            image_ctx.paint()
            # el metodo de enmascaramiento es dibujar en modo "borrar" ya que mask no quiso andar
            image_ctx.set_operator(cairo.OPERATOR_CLEAR)
            for index, selected in enumerate(self.selected_list):
                if selected:
                    angle_start = 2 * math.pi * index / self.subdivisions
                    angle_end = 2 * math.pi * (index + 1) / self.subdivisions
                    image_ctx.move_to(WIDTH/2, HEIGHT/2)
                    image_ctx.line_to(
                        WIDTH/2 + RADIUS*math.cos(angle_start),
                        HEIGHT/2 + RADIUS*math.sin(angle_start)
                        )
                    image_ctx.arc(WIDTH/2, HEIGHT/2, RADIUS, angle_start,
                        angle_end)
                    image_ctx.close_path()
                    image_ctx.fill()
            # cargamos la imagen con las partes borradas sobre el context general
            context.set_source_surface(dummy_image)
            context.paint()


        # Escala la imagen al tamaño de la superficie
        # WIDTH/HEIGHT corresponden al tamaño de los graficos
        rect = self.get_allocation()
        context.scale(
            float(rect.width) / WIDTH,
            float(rect.height) / HEIGHT
            )

        # Dibuja el fondo
        context.set_source_surface(self.image_bg)
        context.paint()

        # Dibuja el frente 
        mask_image(self.image_fg)

        # Dibuja la rejilla
        draw_grid()



if __name__ == "__main__":
    # Probamos el nuevo widget Cake
    window = gtk.Window()
    try:
        cake = Cake(int(sys.argv[1]))
    except IndexError:
        cake = Cake(6)
    window.add(cake)
    window.connect("destroy", gtk.main_quit)
    window.show_all()
    gtk.main()
