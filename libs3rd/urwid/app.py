import urwid


class BasicView(urwid.WidgetWrap):

    def __int__(self):
        self.body = urwid.AttrWrap(urwid.Text('Empty body'), 'body')
        self.view = urwid.Frame(self.body, header=self.header, footer=self.footer)
        urwid.WidgetWrap.__init__(self, self.view)



class PackageChoice(urwid.WidgetWrap):
    def __init__(self):
        self.options = []
        content = [
            urwid.RadioButton(self.options, u"Unsure"),
            urwid.RadioButton(self.options, u"Yes"),
            urwid.RadioButton(self.options, u"No"),
        ]
        list_box = urwid.ListBox(urwid.SimpleListWalker(content))

        urwid.WidgetWrap.__init__(self, list_box)

    def get_state(self):
        for o in self.options:
            if o.get_state() is True:
                return o.get_label()


class StartView(urwid.WidgetWrap):
    text_intro = [
        ('important', 'Valar Morghulis'),
        ' is a Braavosi greeting said in the High Valyrian language,',
        ' which literally translates to ',
        ('important', "All men must die"),
        ' in the Common Tongue. ',
        ('important', 'Valar Dohaeris'),
        ' is its accompanying greeting, which literally translates to ',
        ('important', "All men must serve"),
        "."
    ]

    def __init__(self):
        text = urwid.Text(self.text_intro)

        listbox_content = [
            urwid.Divider(top=6),
            urwid.Padding(text, align='center', width=('relative', 80)),
            urwid.Divider(),
        ]
        body_content = urwid.ListBox(urwid.SimpleListWalker(listbox_content))

        body = urwid.AttrWrap(body_content, 'body')
        super().__init__(body)



class SetupWizard:
    palette = [
        ('header', 'white', 'dark green', 'bold'),
        ('body', 'default', 'default'),
        ('footer', 'default', 'dark blue'),
        ('reverse', 'light gray', 'black'),
        ('important', 'dark blue', 'light gray', ('standout', 'underline')),
        ('key', 'yellow', 'dark green'),
        ('editfc', 'white', 'dark green', 'bold'),
        ('editbx', 'light gray', 'dark blue'),
        ('editcp', 'black', 'light gray', 'standout'),
        ('bright', 'dark gray', 'light gray', ('bold', 'standout')),
        ('buttnf', 'white', 'dark blue', 'bold'),
    ]

    header_text = ('header', [
        "XXXXX Offline Setup Wizard",
    ])

    footer_text = ('footer', [
        " Continue", ('key', " F2 "),
        "    Quit", ('key', " F4 "),
    ])

    def __init__(self):
        self.last_body = None
        self.header = urwid.AttrWrap(urwid.Text(self.header_text), 'header')
        self.footer = urwid.AttrWrap(urwid.Text(self.footer_text), 'footer')
        self.current_body = StartView()
        view = urwid.Frame(self.current_body, header=self.header, footer=self.footer)

        self.loop = urwid.MainLoop(view, self.palette, unhandled_input=self.unhandled_keypress)

    def change_view(self, w):
        self.last_body = self.current_body
        self.current_body = w
        view = urwid.Frame(self.current_body, header=self.header, footer=self.footer)
        self.loop.widget = view


    def unhandled_keypress(self, k):
        """Last resort for keypresses."""

        if k == "f2":
            # self.loop.widget = self.package_choice
            package_choice = PackageChoice()
            self.change_view(package_choice)
        elif k == "f3":
            if self.last_body:
                self.change_view(self.last_body)
        elif k == "f4":
            raise urwid.ExitMainLoop()
        else:
            return
        return True

    def main(self):
        self.loop.run()


if __name__ == '__main__':
    SetupWizard().main()
