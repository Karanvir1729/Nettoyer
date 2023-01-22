import flet as ft
from urllib.parse import urlparse


class Bot:
    def __init__(self):
        self.question = "love me??"

    def get_question(self):
        # pass in AI
        self.question = "yes daddy"  # call AI asking qustion


def main(page: ft.Page):
    bot = Bot()
    new_task = ft.TextField(hint_text="Type your reply?")

    def add_bot(bot):
        # Calls bot question
        bot.get_question()
        page.add(ft.Text(bot.question, size=15))

    def add_clicked(e):
        print("sdf ")
        print(new_task.value)
        page.add(ft.Text(new_task.value, size=15))
        add_bot(bot)

        new_task.value = ""
        page.update()
    youparams = "watermelon"

    def route_change(route):
        # CLEAR ALL PAGE
        page.clean()
        #page.views.clear()
        arr = [  # PAGE ROUTE IS PATH YOU URL HERE
            ft.Text(page.route),
            ft.ElevatedButton(
                "Go to Second Page",
                on_click=lambda _: page.go(f"/secondpage/{youparams}")
            ), ft.Text(bot.question, size=15), ft.ElevatedButton("ADD", on_click=add_clicked), new_task
        ]

        chat_view = ft.View(
            "/", arr

        )
        for i in arr:
            page.add(i)
        #page.views.append(chat_view
        #                  )

        page.scroll = 'auto'
        page.update()

        # GET PARAM FROM HOME PAGE
        param = page.route
        # THIS IS GET VALUE AFTER /secondpage/THIS RES HERE
        res = urlparse(param).path.split("/")[-1]
        print(f"test res is : {res}")

        if page.route == f"/secondpage/{res}":
            page.clean()
            page.route = ""
            elem = [
                        ft.Text(f"you params is {res}"),
                        ft.ElevatedButton(
                            "BACK TO HOME PAGE",
                            on_click=lambda _: page.go("/")
                        )

                    ]
            for i in elem:
                page.add(i)

    page.update()

    def view_pop(view):
        page.views.pop()
        myview = page.views[-1]
        page.go(myview.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    p = ft.TemplateRoute(page.route)
    if p.match("/second/:id"):
        print("you here ", p.id)
    else:
        print("whatever")


ft.flet.app(target=main)
