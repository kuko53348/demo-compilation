import flet as ft

from data.client_data import LobbyModel

class LobbyPage(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors('black12')
        self.ink_color = ft.Colors('yellow')

        self.content = ft.Column(
            alignment = ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            run_alignment = ft.CrossAxisAlignment.CENTER,
            spacing = 8,
            run_spacing = 8,
            controls = [

                ft.Container(
                    expand=True,
                    image=ft.DecorationImage(
                        src="wallpaper.jpg",
                        fit=ft.ImageFit.COVER,
                        opacity=0.4
                    ),
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                blur=(8, 8),
                                border_radius=ft.border_radius.only(
                                    top_left=0, top_right=0, bottom_left=0, bottom_right=120
                                ),
                                border=ft.border.all(width=2, color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors.YELLOW_ACCENT_100)),
                                alignment=ft.alignment.bottom_right,
                                bgcolor=ft.Colors.with_opacity(
                                    opacity=0.21, color=ft.Colors("white")
                                ),
                            ),

                            ft.Container(
                                padding=ft.padding.all(32),
                                expand=True,
                                content=ft.Column(
                                                alignment = ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                                expand = True,
                                                spacing = 16,
                                                run_spacing = 16,


                                            controls=[
                                                # Banner Title
                                                ft.Text(
                                                    value=LobbyModel.lobbyModelCard.header,
                                                    size=42,
                                                    weight=ft.FontWeight.W_900,
                                                    color=ft.Colors.with_opacity(opacity=0.7, color=ft.Colors.YELLOW_ACCENT_100),
                                                ),
                                                # Banner Description
                                                ft.Text(
                                                    value=LobbyModel.lobbyModelCard.sub_header,
                                                    size=17,
                                                    color=ft.Colors.GREY_400,
                                                    weight=ft.FontWeight.W_600,
                                                ),
                                                ft.Text(
                                                    value=LobbyModel.lobbyModelCard.body_text,
                                                    size=17,
                                                    color=ft.Colors.GREY_400,
                                                    weight=ft.FontWeight.W_600,
                                                ),
                                                ft.Text(
                                                    value=LobbyModel.lobbyModelCard.help_info,
                                                    size=17,
                                                    color=ft.Colors.GREY_400,
                                                    weight=ft.FontWeight.W_600,
                                                ),
                                            ],

                                        ),
                            ),
                            ft.Container(
                                # left=32,
                                padding=ft.padding.all(16),
                                alignment=ft.alignment.bottom_right,
                                on_click=lambda _: self.page.go('/home'),
                                content=ft.Container(
                                    blur=(12,12),
                                    bgcolor=ft.Colors.with_opacity(opacity=0.05,color=ft.Colors.YELLOW_ACCENT_100),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    border=ft.border.all(
                                        width=2,
                                        color=ft.Colors.with_opacity(
                                            opacity=0.1, color=ft.Colors.YELLOW_ACCENT_100
                                        ),
                                    ),
                                    padding=ft.padding.all(12),
                                    content=ft.Icon(name="keyboard_arrow_right_rounded"),
                                ),
                            ),
                        ]
                    ),
                ),  # <
            ],
        )