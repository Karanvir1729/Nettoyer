import flet
from flet import (
    AppBar, Banner, Checkbox,
    Column,
    Container, FilledTonalButton, FloatingActionButton,
    Icon, IconButton,
    OutlinedButton,
    Page,
    PopupMenuButton, PopupMenuItem, Row,
    Slider, Tab,
    Tabs,
    Text,
    TextButton, TextField,
    UserControl,
    colors,
    icons, padding, page,
)

class Bot:
    def __init__(self):
        self.question = "question"

    def get_question(self):
        # pass in AI
        self.question = "answer"#call AI asking qustion

class Tag(UserControl):
    def __init__(self, tag_name, tag_delete):
        super().__init__()
        self.tag_name = tag_name
        self.tag_delete = tag_delete

    def build(self):
        self.display_tag = Checkbox(
            value=False, label=self.tag_name)

        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_tag,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete Tag",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        return Column(controls=[self.display_view])

    def save_clicked(self, e):
        self.display_tag.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_tag.value
        self.tag_status_change(self)

    def delete_clicked(self, e):
        self.tag_delete(self)

class chat_box(UserControl):
    def __init__(self, chat_box_name, chat_box_delete):
        super().__init__()
        self.isTag = True
        self.chat_box_name = chat_box_name

    def build(self):

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[Text(self.chat_box_name)])

        return Column(controls=[self.display_view])

class TodoApp(UserControl):
    def __init__(self, p):
        super().__init__()
        self.page = p

    def build(self):
        bot = Bot()
        self.addButton = FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked)

        self.new_tag = TextField(
            hint_text="What needs to be done?",
            expand=True)

        self.tags = Column()
        self.tags_chat = Column()
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="Chat Mode"), Tab(text="Current Tags"), Tab(text="Settings")],
        )
        self.settings = Column(controls=[Slider(min=0, max=100, divisions=10, label="{value}%")], visible=False)

        self.new_tag = TextField(
            hint_text="Add Tags Manually Here",
            expand=True)

        self.items_left = Text("0 Tags")
        self.tags.visible = False
        self.tags_chat.visible = True
        self.items_left.value = f"{0} Tags"
        self.addButton.on_click=self.add_clicked_chat
        appbar = AppBar(
            title=Text("AppBar Example"),
        )
        # application's root control (i.e. "view") containing all other controls

        self.page.banner = Banner(
            bgcolor=colors.BLACK,
            content=Text(""),
            actions=[Row([Text(value="Nettoyer", style="headlineMedium")], alignment="center"),
                Row(controls=[Row(width=500, controls=[self.new_tag], alignment="center"), self.addButton], alignment="center"),
                Row(controls=[self.filter], alignment="center")],
            content_padding = padding.only(left=16.0, top=0, right=16.0, bottom=0)
        )
        self.page.banner.open = True
        return Column(
            width=600,
            controls=[
                self.settings,
                Column(
                    spacing=25,
                    controls=[
                        self.tags,self.tags_chat,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Apply Tags", on_click=self.clear_clicked
                                ),
                            ],
                        )
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        if self.new_tag.value:
            tag = Tag(self.new_tag.value, self.tag_delete)
            self.tags.controls.append(tag)
            self.new_tag.value = ""
            self.new_tag.focus()
            self.update()

    def add_clicked_chat(self, e):
        if self.new_tag.value:
            tag = FilledTonalButton(self.new_tag.value, disabled=True)
            container = Row(controls=[tag], alignment="start")

            self.tags_chat.controls.append(container)
            self.new_tag.value = ""
            self.new_tag.focus()
            self.update()

            tag = FilledTonalButton("beep boop", disabled=True)
            container = Row(controls=[tag], alignment="end")
            self.tags_chat.controls.append(container)
            self.new_tag.value = ""
            self.new_tag.focus()
            self.update()

    def tag_delete(self, tag):
        self.tags.controls.remove(tag)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for tag in self.tags.controls[:]:
            if tag.completed:
                self.tag_delete(tag)

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        if status == "Current Tags":
            self.settings.visible = False
            self.tags.visible = True
            self.tags_chat.visible = False
            self.items_left.value = f"{count} Tags"
            self.addButton.on_click=self.add_clicked

        elif status == "Chat Mode":
            self.settings.visable = False
            self.tags.visible = False
            self.tags_chat.visible = True
            self.items_left.value = f"{count} Tags"
            self.addButton.on_click=self.add_clicked_chat

        else:
            self.settings.visible = True
            self.tags.visible = False
            self.tags_chat.visible = False

        super().update()


def main(page: Page):
    page.title = "Nettoyer"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()

    # create application instance
    app = TodoApp(page)

    # add application's root control to the page
    page.add(app)

flet.app(target=main)
