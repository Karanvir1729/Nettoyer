import flet as ft


class Bot:
    def __init__(self):
        self.question = "love me??"

    def get_question(self):
        # pass in AI
        self.question = "yes daddy"  # call AI asking qustion


def main(page: ft.Page):
    bot = Bot()

    def add_bot(bot):
        # Calls bot question
        bot.get_question()
        page.add(ft.Text(bot.question, size=15))

    def add_clicked(e):
        page.add(ft.Text(new_task.value, size=15))

        add_bot(bot)
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Type your reply?")
    page.add(ft.Text(bot.question, size=15))
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))
    page.add(ft.ElevatedButton(
        "BACK TO HOME PAGE",
        on_click=lambda _: page.go("/")
    ))
    page.scroll = 'auto'
    page.update()


ft.app(target=main)
