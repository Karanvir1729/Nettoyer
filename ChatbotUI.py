import flet as ft
from PromptGenerator.chatbot import generate_response


class Bot:
    def __init__(self):
        self.question = "What are your interests?"

    def get_question(self, input):
        # pass in AI
        self.question = generate_response(input)


def main(page: ft.Page):
    bot = Bot()

    def add_bot(bot, input):
        # Calls bot question
        bot.get_question(input)
        page.add(ft.Text(bot.question, size=15))

    def add_clicked(e):
        page.add(ft.Text(new_task.value, size=15))
        print(new_task.value)
        add_bot(bot, new_task.value)
        new_task.value = ""
        page.update()
        print(page._get_children())
    new_task = ft.TextField(hint_text="Type your reply?")
    page.add(ft.Text(bot.question, size=15))
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))
    page.scroll = 'auto'
    page.update()


ft.app(target=main)
