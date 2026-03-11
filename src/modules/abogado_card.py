import flet as ft

class AbogadoCard(ft.Container):

    def __init__(self,
                 page: object = None,
                 content: object = None,
                 name: str = "",
                 avatar_image: str="",
                 carrer: str = "",
                 education: str = "",
                 index_page: int=0,
                 ) -> None:
        super().__init__()
        self.page = page

        self.name = name
        self.index_page = index_page
        self.carrer = carrer
        self.education = education
        self.avatar_image = avatar_image

        # attributes
        self.padding = ft.padding.only(left = 8, right = 8,)
        self.alignment = ft.alignment.center
        self.ink = True
        self.bgcolor = ft.Colors('black12')
        self.ink_color = ft.Colors('yellow')

        self.content =ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.only( top=8, bottom=8),
            border_radius=ft.border_radius.all(32),
            width=420,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src=self.avatar_image,
                fit=ft.ImageFit.COVER,
                opacity=0.08,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src=self.avatar_image,
                        width=150,
                        height=250,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        # run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            # Banner Title
                            ft.Column(
                                spacing=24,
                                run_spacing=24,
                                controls=[
                                    ft.Column(
                                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                        expand = True,
                                        spacing = 8,
                                        run_spacing = 8,
                                        controls = [
                                            ft.Text(
                                                value=name,
                                                size=16,
                                                weight=ft.FontWeight.W_900,
                                                color=ft.Colors.GREY_200,
                                            ),
                                            ft.Text(
                                                value=carrer,
                                                # expand=True,
                                                size=11,
                                                color=ft.Colors.GREY_500,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                            ft.Text(
                                                value=education,
                                                # expand=True,
                                                size=11,
                                                color=ft.Colors.GREY_500,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                    ),
                                    ft.Container(
                                        expand=True,
                                        padding=ft.padding.only(
                                            left=8, top=8, right=8, bottom=8
                                        ),
                                        border_radius=ft.border_radius.all(18),
                                        ink_color=ft.Colors("yellow"),
                                        alignment=ft.alignment.center,
                                        width=100,
                                        bgcolor=ft.Colors.GREY_600,
                                        content=ft.Text(
                                            value="Details",
                                            size=16,
                                            weight="bold",
                                            color=ft.Colors.GREY_900,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            on_click=lambda _:self.set_current_index_selected_card(index_page=self.index_page),
        )
    def set_current_index_selected_card(self,index_page: int=0):
        self.page.session.set('index_page',self.index_page)
        self.page.go('/profile')
        self.page.update()