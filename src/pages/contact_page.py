import flet as ft

from data.client_data import ClientProfileTemplate, ProfileModel
from modules.abogado_card import AbogadoCard

few_medium_text = (
    "Flet is a framework that allows building web, desktop and mobile applications Flet is a framework that allows building web, desktop and mobile applications"
)

class ContactPage(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(bottom = 0, top = 0)

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
                AbogadoCard(
                    page=self.page,
                    name=_.name,
                    index_page=index_page,
                    avatar_image=_.avatar_image,
                    carrer=_.carrer,
                    education=_.education,
                    ) for index_page,  _ in enumerate(ProfileModel.ProfileModel)
            ],
        )