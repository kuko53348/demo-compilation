import flet as ft

class RowDoubleText(ft.Container):

    def __init__(self, page: object = None,header: str="", body: str="") -> None:
        super().__init__()
        self.page = page

        self.content = ft.Row(
            # height=100,
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.START,
            spacing = 8,
            run_spacing = 8,
            controls = [
                ft.Text(value=header),
                ft.Text(value=body),
            ],
        )