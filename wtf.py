#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WTF(Gtk.Window):
    def __init__(self, file_list=None, width=1024, height=768):
        super(WTF, self).__init__()

    def run(self):
        self.show_all()
        Gtk.main()

    def set_key_handler(self, fcn):
        pass

    def quit(self):
        Gtk.main_quit()

if __name__ == "__main__":
    win = WTF()
    win.run()
