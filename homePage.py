import flet as ft
from flet import *
from urllib.parse import urlparse


class Bot:
    def __init__(self):
        self.question = "love me??"

    def get_question(self):
        # pass in AI
        self.question = "yes daddy"  # call AI asking qustion





def main(page: ft.Page):
    bot = Bot()
    new_task = TextField(hint_text="Type your reply?")

    def add_bot(bot):
        # Calls bot question
        bot.get_question()
        return Text(bot.question, size=15)


    def add_clicked(e):

        user = Text(new_task.value, size=15)
        bote = add_bot(bot)
        return (user, bote)

    youparams = "watermelon"

    def route_change(route):
        # CLEAR ALL PAGE
        page.views.clear()
        arr = [  # PAGE ROUTE IS PATH YOU URL HERE
                Text(page.route),
                ElevatedButton(
                    "Go to Second Page",
                    on_click=lambda _: page.go(f"/secondpage/{youparams}")
                ), Text(bot.question, size=15), ElevatedButton("ADD", on_click=add_clicked), new_task
            ]

        chat_view = View(
            "/", arr

        )

        page.views.append(chat_view
        )

        page.scroll = 'auto'
        page.update()

        # GET PARAM FROM HOME PAGE
        param = page.route
        # THIS IS GET VALUE AFTER /secondpage/THIS RES HERE
        res = urlparse(param).path.split("/")[-1]
        print(f"test res is : {res}")

        if page.route == f"/secondpage/{res}":
            page.views.append(
                View(
                    f"/secondpage/{res}",
                    [
                        Text(page.route),
                        Text(f"you params is {res}"),
                        ElevatedButton(
                            "BACK TO HOME PAGE",
                            on_click=lambda _: page.go("/")
                        )

                    ]
                )
            )

    page.update()

    def view_pop(view):
        page.views.pop()
        myview = page.views[-1]
        page.go(myview.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    p = TemplateRoute(page.route)
    if p.match("/second/:id"):
        print("you here ", p.id)
    else:
        print("whatever")


flet.app(target=main)
