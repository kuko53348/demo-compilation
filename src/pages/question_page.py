import flet as ft

from data.client_data import QuestionModel
from modules.question_page import QuestionCard


class QuestionPage(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors('black12')
        self.ink_color = ft.Colors('yellow')
        self.image = ft.DecorationImage(src='wallpaper_2.jpg',fit=ft.ImageFit.COVER,opacity=0.05)  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN

        self.content = ft.Column(
            scroll = ft.ScrollMode.HIDDEN, # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            expand = True,
            spacing = 0,
            run_spacing = 0,
            controls = [
                QuestionCard(
                    page=self.page,
                    target=_.target,
                    questions_1=_.questions_1,
                    questions_2=_.questions_2,
                    questions_3=_.questions_3,
                    questions_4=_.questions_4,
                    questions_5=_.questions_5,
                    reference=_.reference,
                ) for _ in QuestionModel.questions
            ],
        )