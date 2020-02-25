import urwid

class Question(urwid.WidgetWrap):
    def __init__(self):
        self.options = []
        unsure = urwid.RadioButton(self.options, u"Unsure")
        yes = urwid.RadioButton(self.options, u"Yes")
        no = urwid.RadioButton(self.options, u"No")
        display_widget = urwid.GridFlow([unsure, yes, no], 15, 3, 1, 'left')
        fill = urwid.Filler(display_widget)
        urwid.WidgetWrap.__init__(self, fill)

    def get_state(self):
        for o in self.options:
            if o.get_state() is True:
                return o.get_label()
class Index:
    pass

class SetupWizard:
    palette = [
        ('body', 'default', 'default'),
        ('head', 'white', 'dark blue', 'bold'),
        ('foot', 'dark cyan', 'dark blue', 'bold'),
        ('key', 'light cyan', 'dark blue', 'underline'),
    ]

    header_text = ('head', [
        "XXXXX Offline Setup Wizard",
    ])

    footer_text = ('foot', [
        ('key', "  F2"), " Continue   ",
        ('key', "F4"), " Quit",
    ])

    def __init__(self):
        self.header = urwid.AttrWrap(urwid.Text(self.header_text), 'head')
        self.footer = urwid.AttrWrap(urwid.Text(self.footer_text), "foot")
        self.view = urwid.Frame(urwid.AttrWrap(Question(), 'body'),
                                header=self.header,
                                footer=self.footer)

    def unhandled_keypress(self, k):
        """Last resort for keypresses."""

        if k == "f2":
            pass
        elif k == "f4":
            raise urwid.ExitMainLoop()
        else:
            return
        return True

    def main(self):
        self.loop = urwid.MainLoop(self.view, self.palette, unhandled_input=self.unhandled_keypress)
        self.loop.run()

if __name__ == '__main__':
    SetupWizard().main()


