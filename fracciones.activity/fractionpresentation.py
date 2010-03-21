# -*- coding: utf-8 -*-
"""
Contain the presentation of the game, a widget descendant from container.

"""
import logging
import gtk
import pango

import gtkcake
from fractionlogic import FractionLogic


log = logging.getLogger()


class FractionPresentation(gtk.VBox):
    def __init__(self):
        super(FractionPresentation, self).__init__()
        # Change font size
        settings = gtk.settings_get_default()
        settings.set_string_property("gtk-font-name", "Sans 40", "FractionPresentation")

        # instantiate logic
        self.logic = FractionLogic()
        self.logic.generate()
        # create main widget:
        # menu/label/cake/button
        # 1. Add the menu bar
        mb = gtk.MenuBar()
        self.pack_start(mb, False, False, 0)
        
        # game menu
        gamemenu = gtk.Menu()
        gamem = gtk.MenuItem("Game")
        gamem.set_submenu(gamemenu)

        new = gtk.MenuItem("New")
        new.connect("activate", self.menu_game_new)
        gamemenu.append(new)

        exit = gtk.MenuItem("Exit")
        exit.connect("activate", self.menu_game_exit)
        gamemenu.append(exit)

        mb.append(gamem)
        # help menu
        helpmenu = gtk.Menu()
        helpm = gtk.MenuItem("Help")
        helpm.set_submenu(helpmenu)

        about = gtk.MenuItem("About")
        about.connect("activate", self.menu_help_about)
        helpmenu.append(about)

        mb.append(helpm)
        # 2. label
        label = gtk.Label("""Select %i/%i"""%self.logic.get_current())
        self.pack_start(label, False, True)
        self.label = label
        # 3. cake
        aspect = gtk.AspectFrame()
        cake = gtkcake.Cake(self.logic.get_current()[1])
        aspect.add(cake)
        self.pack_start(aspect)
        self.cake = cake
        # 4. button
        button = gtk.Button("Check")
        button.connect("clicked", self.on_clicked_check)
        self.pack_start(button, False, True)
        # Connect signals
        # show all widgets
        self.show_all()


        # try reparent cake
        self.menu_game_new()


    def menu_game_new(self):
        print "menu_game_new"
        self.logic.generate()
        self.label.set_text("""Select %i/%i"""%self.logic.get_current())
        self.cake.reset(self.logic.get_current()[1])


    def menu_game_exit(self):
        print "menu_game_exit"
        gtk.main_quit()

    
    def menu_help_about(self):
        print "menu_help_about"
        about = gtk.AboutDialog()
        about.set_program_name("Fracciones")
        about.run()
        about.destroy()


    def on_clicked_check(self, widget):
        """Clicked button check"""
        print "on_clicked_check"
        if self.logic.is_equal(self.cake.get_current_fraction()):
            print "ok"
            self.menu_game_new()
        else:
            print "wrong"


if __name__ == "__main__":
    class Main(gtk.Window):
        def __init__(self):
            super(Main, self).__init__() 
            self.add(FractionPresentation())
            self.connect("destroy", gtk.main_quit)
            self.show()
    Main()
    gtk.main()
