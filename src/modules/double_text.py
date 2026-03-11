import flet as ft

class DoubleText(ft.Container):

    def __init__(self, page: object = None,header: str="", body: str="") -> None:
        super().__init__()
        self.page = page

        self.content = ft.Column(
            height=100,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            spacing = 8,
            run_spacing = 8,
            controls = [
                ft.Text(value=header),
                ft.Text(value=body),
            ],
        )