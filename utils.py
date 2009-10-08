import math


def draw_arc(cr, color_fg, color_bg, center_x, center_y, radius, angle_start, angle_end):
    """
    Dibuja un arco sobre una superficie de cairo.

    """
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
