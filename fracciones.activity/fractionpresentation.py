# -*- coding: utf-8 -*-
"""
Contain the presentation of the game, a widget descendant from container.

"""
import logging
import gtk
import pango

import gtkcake
from fractionlogic import FractionLogic
from fractionlogic import Fraction

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


class FractionPresentation(gtk.VBox):
    def __init__(self):
        super(FractionPresentation, self).__init__()
        # Change font size
        #settings = gtk.settings_get_default()
        #settings.set_string_property("gtk-font-name", "Sans 40", "FractionPresentation")

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
        label = gtk.Label("""Eat %i/%i"""%self.logic.get_current())
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
        button.connect("clicked", self.check_cake)
        self.pack_start(button, False, True)

        # show all widgets
        self.show_all()


    def menu_game_new(self, menuitem):
        log.debug("menu_game_new")
        self.new_game()


    def menu_game_exit(self, menuitem):
        log.debug("menu_game_exit")
        gtk.main_quit()

    
    def menu_help_about(self, menuitem):
        print menuitem
        log.debug("menu_help_about")
        about = gtk.AboutDialog()
        about.set_program_name("Fracciones")
        about.run()
        about.destroy()


    def check_cake(self, widget):
        """Clicked button check"""
        log.debug("on_clicked_check")
        if self.logic.is_equal(self.cake.current_fraction):
            md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "GOOD!")
            md.run()
            md.destroy()
            self.new_game()
        else:
            md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "BAD!")
            md.run()
            md.destroy()


    def new_game(self):
        self.logic.generate()
        self.label.set_text("""Eat %i/%i"""%self.logic.get_current())
        self.cake.reset(self.logic.get_current()[1])
