import flet as ft

class QuestionCard(ft.Container):

    def __init__(self,
                 page: object = None,
                 content: object = None,
                 target=str(),
                 questions_1=str(),
                 questions_2=str(),
                 questions_3=str(),
                 questions_4=str(),
                 questions_5=str(),
                 reference=str(),
                 ) -> None:
        super().__init__()
        self.page = page
        self.target = target
        self.questions_1 = questions_1
        self.questions_2 = questions_2
        self.questions_3 = questions_3
        self.questions_4 = questions_4
        self.questions_5 = questions_5
        self.reference = reference

        # properties
        self.padding = ft.padding.only(left = 8, right = 8, bottom = 8, top = 8)
        self.alignment = ft.alignment.center
        self.ink = True
        self.bgcolor = ft.Colors('black12')
        self.ink_color = ft.Colors('yellow')

        self.content = ft.Container(
            width=420,
            padding=ft.padding.only(left=24, top=24, right=24, bottom=24),
            border_radius=ft.border_radius.all(12),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            url=reference,
            url_target=reference,

            content=ft.Column(
                alignment = ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment = ft.CrossAxisAlignment.START,
                expand = True,
                spacing = 12,
                run_spacing = 12,
                controls=[
                    # Banner Title
                    ft.Text(
                        # italic = True,
                        text_align = ft.TextAlign.LEFT,
                        weight = ft.FontWeight.BOLD,
                        font_family = 'Consolas',
                        value=target,
                        size=22,
                        color=ft.Colors("white"),
                    ),
                    # Banner Description
                    ft.Text(
                        value=questions_1,
                        # italic = True,
                        size=13,
                        color=ft.Colors.GREY_500,
                    ),
                    ft.Text(
                        value=questions_2,
                        size=13,
                        color=ft.Colors.GREY_500,
                    ),
                    ft.Text(
                        value=questions_3,
                        size=13,
                        color=ft.Colors.GREY_500,
                    ),
                    ft.Text(
                        value=questions_4,
                        size=13,
                        color=ft.Colors.GREY_500,
                    ),
                    ft.Text(
                        value=questions_5,
                        size=13,
                        color=ft.Colors.GREY_500,
                    ),

                ],

            ),
        )