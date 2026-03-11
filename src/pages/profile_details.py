import flet as ft

from data.client_data import ProfileModel
from modules.double_text import DoubleText
from modules.row_double_text import RowDoubleText

# name
# carrer
# location
# contact
# profile
# experience
# education
# skills
# language

class ProfileDetails(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page

        self.ProfileModel = ProfileModel.ProfileModel[self.page.session.get('index_page')]
        self.padding = ft.padding.only(left = 0, right = 0, bottom = 0, top = 0)


        self.content = ft.SafeArea(
            content=ft.Container(
              image = ft.DecorationImage(src='wallpaper_2.jpg',fit=ft.ImageFit.COVER,opacity=0.05),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
              content=ft.Container(
                padding = ft.padding.only(left = 12, right = 12, bottom = 12, top = 12),
                blur=(8,8),
                content=ft.Column(
                    scroll = ft.ScrollMode.HIDDEN, # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                    height=(self.page.window.height if self.page.window.height else self.page.height) - 5,
                    controls=[
                      ft.Container(
                            border_radius = ft.border_radius.only(top_left = 28, top_right = 28, bottom_left = 28, bottom_right = 28),
                            border = ft.border.all(width = 2, color = ft.Colors.with_opacity(opacity=0.1,color=ft.Colors.WHITE)),
                            shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.Colors.GREY_900, offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,),
                            image = ft.DecorationImage(src=self.ProfileModel.avatar_image,fit=ft.ImageFit.COVER,),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                            alignment = ft.alignment.top_left,
                            padding=ft.padding.all(8),
                            height = 320,
                            # ink_color = ft.Colors('yellow'),
                            expand = True,
                            bgcolor = ft.Colors('black12'),
                            content=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK_ROUNDED,
                                bgcolor=ft.Colors.GREY_900,
                                on_click=lambda _:self.page.go('/home')
                                ),
                            ),
                      ft.Container(
                            content=ft.Column(
                                scroll = ft.ScrollMode.HIDDEN, # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                                spacing = 8,
                                run_spacing = 8,
                                controls=[
                                  ft.Column(
                                      controls=[
                                          ft.Text(
                                              size=18,
                                              value=self.ProfileModel.name,
                                              expand=True,
                                          ),
                                          ft.Row(
                                                  alignment = ft.MainAxisAlignment.START,
                                                  vertical_alignment = ft.CrossAxisAlignment.START,
                                                  expand = True,
                                                  spacing = 8,
                                                  run_spacing = 8,
                                              controls=[
                                                  ft.Icon(name=ft.Icons.PLACE_ROUNDED,size=15),
                                                  ft.Text(value=self.ProfileModel.location)
                                              ]
                                          )
                                      ],
                                  ),
                                  RowDoubleText(
                                       page=self.page,
                                       header='Education',
                                       body=self.ProfileModel.education
                                  ),
                                  ft.Tabs(
                                          height=200,
                                          selected_index=0,
                                          animation_duration=300,
                                          tabs=[
                                              ft.Tab(
                                                  text="Profile",
                                                  content=ft.Container(
                                                      content=ft.Column(
                                                            scroll = ft.ScrollMode.HIDDEN, # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                                                            controls=[
                                                              ft.Text(
                                                                value=self.ProfileModel.profile
                                                            ),
                                                          ]
                                                      ),
                                                        alignment=ft.alignment.top_left
                                                  ),
                                              ),
                                              ft.Tab(
                                                  text="Experience",
                                                  content=ft.Container(
                                                      content=ft.Column(
                                                            scroll = ft.ScrollMode.HIDDEN, # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                                                            controls=[
                                                              ft.Text(
                                                                value=self.ProfileModel.experience
                                                            ),
                                                          ]
                                                      ),
                                                        alignment=ft.alignment.top_left
                                                  ),
                                              ),
                                              ft.Tab(
                                                  text="Responsability",
                                                  content=ft.Container(
                                                      content=ft.Column(
                                                            scroll = ft.ScrollMode.HIDDEN, # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                                                            controls=[
                                                              ft.Text(
                                                                value=self.ProfileModel.responsability
                                                            ),
                                                          ]
                                                      ),
                                                        alignment=ft.alignment.top_left
                                                  ),
                                              ),
                                          ],
                                          expand=1,
                                      ),
                                   ft.Divider(thickness=0.1,),
                                   # Rest of profile
                                   DoubleText(
                                       page=self.page,
                                       header='Skills',
                                       body=self.ProfileModel.skills
                                    ),
                                   ft.Divider(thickness=0.1,),
                                   DoubleText(
                                       page=self.page,
                                       header='Research',
                                       body=self.ProfileModel.academic
                                    ),
                                   ft.Container(height=50,),
                                ]
                            )
                            ),
                    ]
                ),
              ),
            ),
        )


