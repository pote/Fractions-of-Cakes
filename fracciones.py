#! /usr/bin/env python

import math
import gtk


W = None
H = None

def draw_arc(cr, color_fg, color_bg, center_x, center_y, radius, angle_start, angle_end):
    cr.set_source_rgb(*color_fg)
    cr.move_to(center_x, center_y)
    nx = center_x + radius * math.cos(angle_start)
    ny = center_y + radius * math.sin(angle_start)
    cr.line_to(nx, ny)
    cr.arc(center_x, center_y, radius, angle_start, angle_end)
    cr.close_path()
    cr.stroke_preserve()
    cr.set_source_rgb(*color_bg)
    cr.fill()


class Arco:
    def __init__(self, x, y, r, N):
        assert N > 2
        self.x0 = x
        self.y0 = y
        self.r = r
        self.N = N
        self.selected = [0] * N


    def arco(self, pos):
        xa = pos[0]
        ya = pos[1]
        xb = xa - W 
        yb = (ya - H)

        if math.pow(xb, 2) + math.pow(yb, 2) > math.pow(self.r, 2):
            return None
        angle = math.atan2(yb, xb)
        if angle < 0: angle += 2*math.pi
        sector2 = angle*self.N/(2*math.pi)
        return int(math.floor(sector2))


    def presionar_arco(self, cr, i):
        if self.selected[i]:
            self.selected[i] = 0
        else:
            self.selected[i] = 1
        self.dibujar_torta(cr)


    def dibujar_torta(self, cr):
        for i in xrange(self.N):
            angle_start = 2*math.pi*i/self.N
            angle_end = 2*math.pi*(i+1)/self.N
            #if angle_start < 0:  angle_start += 2*math.pi
            #if angle_end < 0:  angle_end += 2*math.pi
            if self.selected[i]:
                fg = (1.0, 1.0, 0.0)
                bg = (0.0, 1.0, 1.0)
            else:
                fg = (1.0, 0.0, 0.0)
                bg = (0.0, 1.0, 0.0)
            draw_arc(cr, fg, bg, self.x0, self.y0, self.r, angle_start, angle_end)



class fracciones(object):
    def __init__(self):
        global W, H

        builder = gtk.Builder()
        builder.add_from_file("fracciones.xml")
        builder.connect_signals(self)

        self.builder = builder
        self.window = builder.get_object("window")
        self.label = builder.get_object("label")
        self.status = builder.get_object("statusbar")
        self.drawingarea = builder.get_object("drawingarea")
        self.window.show()

        # Crear la torta.
        self.w = self.drawingarea.allocation.width 
        self.h = self.drawingarea.allocation.height
        r = 80
        self.N = N = 5
        W = self.w /2.0
        H = self.h /2.0
        self.arco = Arco(W, H, r, N)
        self.coords = (0, 0)
 

    def on_window_motion_notify_event(self, widget, event):
        self.coords = coords = event.get_coords()
        text = "%i/%i"%(sum(self.arco.selected), self.N)
        self.status.push(1, text)

        
    def on_window_destroy(self, userdata):
        gtk.main_quit()


    def on_drawingarea_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        self.arco.dibujar_torta(cr)


    def on_drawingarea_button_press_event(self, widget, event):
        x, y = event.get_coords()
        result = self.arco.arco(event.get_coords())
        if result is not None:
            cr = widget.window.cairo_create()
        self.arco.presionar_arco(cr, result)


    def on_drawingarea_motion_notify_event(self, widget, event):
        pass


if __name__ == "__main__":
    app = fracciones()
    gtk.main()
