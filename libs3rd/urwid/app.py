import urwid

class PackageChoice(urwid.WidgetWrap):
    def __init__(self):
        self.options = []
        list_content = [
            urwid.RadioButton(self.options, u"Unsure"),
            urwid.RadioButton(self.options, u"Yes"),
            urwid.RadioButton(self.options, u"No"),
        ]
        list_box = urwid.LineBox(urwid.SimpleListWalker(list_content))

        urwid.WidgetWrap.__init__(self, list_box)

    def get_state(self):
        for o in self.options:
            if o.get_state() is True:
                return o.get_label()

class Index(urwid.WidgetWrap):
    text_intro = [('important', u"Text"),
                  u" widgets are the most common in "
                  u"any urwid program.  This Text widget was created "
                  u"without setting the wrap or align mode, so it "
                  u"defaults to left alignment with wrapping on space "
                  u"characters.  ",
                  ('important', u"Change the window width"),
                  u" to see how the widgets on this page react.  "
                  u"This Text widget is wrapped with a ",
                  ('important', u"Padding"),
                  u" widget to keep it indented on the left and right."]

    def __init__(self):
        text = urwid.Text(self.text_intro)
        listbox_content = [
            urwid.Padding(text, left=2, right=2, min_width=20),
        ]
        listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
        urwid.WidgetWrap.__init__(self, listbox)




class SetupWizard:
    palette = [
        ('body','black','light gray', 'standout'),
        ('reverse','light gray','black'),
        ('head','white','dark red', 'bold'),
        ('important','dark blue','light gray',('standout','underline')),
        ('editfc','white', 'dark blue', 'bold'),
        ('editbx','light gray', 'dark blue'),
        ('editcp','black','light gray', 'standout'),
        ('bright','dark gray','light gray', ('bold','standout')),
        ('foot','black','dark cyan'),
        ('buttnf','white','dark blue','bold'),
    ]

    header_text = ('head', [
        "XXXXX Offline Setup Wizard",
    ])

    footer_text = ('foot', [
        ('key', "  F2"), " Continue   ",
        ('key', "F4"), " Quit",
    ])

    def __init__(self):
        self.package_choice = PackageChoice()
        self.header = urwid.AttrWrap(urwid.Text(self.header_text), 'head')
        self.footer = urwid.AttrWrap(urwid.Text(self.footer_text), "foot")
        self.view = urwid.Frame(urwid.AttrWrap(Index(), 'body'),
                                header=self.header,
                                footer=self.footer)

    def unhandled_keypress(self, k):
        """Last resort for keypresses."""

        if k == "f2":
            self.loop.widget = self.package_choice
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


