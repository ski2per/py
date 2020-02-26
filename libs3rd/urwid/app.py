import urwid


class PackageChoice(urwid.WidgetWrap):
    signals = ['checkbox_change']

    def __init__(self):
        self.options = []
        self.debug = urwid.Text('hehe')

        # To use 'user_data', set 'on_state_change'
        checkbox_list = [
            urwid.CheckBox("Basic Environment(Docker, Python)", on_state_change=self._emit_change, user_data='basic'),
            urwid.CheckBox("xLedger Platform", on_state_change=self._emit_change, user_data='xledger'),
            urwid.CheckBox("Luna Platform", on_state_change=self._emit_change, user_data="luna"),
        ]

        choice = urwid.Pile(checkbox_list)
        content = [
            urwid.Divider(top=6),
            urwid.Text(('title', 'Choose Component to Install:')),
            urwid.Divider(top=1),
            # urwid.AttrWrap(choice, 'header'),
            choice,
            urwid.Divider(),
            self.debug
        ]

        list_box = urwid.Padding(urwid.ListBox(urwid.SimpleListWalker(content)), width=('relative', 80), align="center")
        urwid.WidgetWrap.__init__(self, list_box)

    def _emit_change(self, *args):
        self._emit('checkbox_change', args)

    def get_package_list(self):
        packages = []
        for cb in self.content:
            packages.append(cb.get_state())
            # if cb.get_state():
            #     packages.append(cb.label)

        return packages

    # def get_state(self):
    #     for o in self.options:
    #         if o.get_state() is True:
    #             return o.get_label()


class PopupDialog(urwid.WidgetPlaceholder):
    def __init__(self, original_widget):
        super().__init__(original_widget)
        PopupDialog.super
        super(PopupDialog, self).__init__()
        content = [
            urwid.Text("Quit Setup Wizard ?"),
            urwid.Columns([
                urwid.Button('Yes'),
                urwid.Button('No'),
            ])
        ]
        urwid.WidgetWrap.__init__(self, urwid.ListBox(urwid.SimpleListWalker(content)))




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
        ('title', 'light red', 'black'),
        ('important', 'dark blue', 'light gray', ('standout', 'underline')),
        ('key', 'yellow', 'dark green'),
        ('background', 'default', 'light gray'),
        ('editfc', 'white', 'dark green', 'bold'),
        ('editbx', 'light gray', 'dark blue'),
        ('editcp', 'black', 'light gray', 'standout'),
        ('bright', 'dark gray', 'light gray', ('bold', 'standout')),
        ('debug', 'white', 'dark blue', 'bold'),
    ]

    header_text = ('header', [
        "XXXXX Offline Setup Wizard",
    ])

    footer_text = ('footer', [
        " Continue", ('key', " F2 "),
        "    Quit", ('key', " F4 "),
    ])

    components = []

    def __init__(self):
        self.debug = urwid.AttrWrap(urwid.Text('DEBUG'), 'debug')

        self.last_content = None

        self.header = self._build_header()
        self.footer = self._build_footer()

        self.current_content = StartView()


        view = urwid.Frame(self.current_content, header=self.header, footer=self.footer)
        self.loop = urwid.MainLoop(view, self.palette, unhandled_input=self._unhandled_control)

    def _build_header(self):
        widget_list = [
            urwid.AttrWrap(urwid.Text(self.header_text), 'header'),
            self.debug,
        ]
        return urwid.Columns(widget_list)

    def _build_footer(self):
        return urwid.AttrWrap(urwid.Text(self.footer_text), 'footer')

    def _handle_checkbox_change(self, *args):
        _, state, label = args[1]
        if state:
            if label not in self.components:
                self.components.append(label)
        else:
            try:
                self.components.remove(label)
            except ValueError:
                pass

        self.debug.set_text(','.join(self.components))
        # self.debug.set_text(f'{user_data}')

    def _unhandled_control(self, k):
        """Last resort for keypresses."""

        if k == "f2":
            self.debug.set_text("you press F2")
            package_choice = PackageChoice()
            urwid.connect_signal(package_choice, 'checkbox_change', self._handle_checkbox_change)
            self.set_view(package_choice)

        elif k == "f3":
            self.debug.set_text("you press F3")
            popup = PopupDialog()
            self.set_view(popup)

        elif k == "f4":
            self.debug.set_text("you press F4")
            self.popup_quit()
            # raise urwid.ExitMainLoop()
        else:
            return
        return True

    def set_view(self, widget):
        self.last_content = self.current_content
        self.current_content = widget
        view = urwid.Frame(self.current_content, header=self.header, footer=self.footer)
        self.loop.widget = view

    def popup_quit(self):
        top_w = PopupDialog()
        self.original_widget = overlay = urwid.Overlay(top_w, self.original_widget, align="center", width=50, valign="middle", height=50)
        self.set_view(overlay)


    def main(self):
        self.loop.run()


if __name__ == '__main__':
    SetupWizard().main()
