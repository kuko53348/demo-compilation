import flet as ft

class LocationPage(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.image = self.image = ft.DecorationImage(src='map.jpg',fit=ft.ImageFit.COVER,opacity=0.8)  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
        self.padding = ft.padding.only(left = 12, right = 12, bottom = 12, top = 12)
        self.alignment = ft.alignment.bottom_center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors('black12')
        self.ink_color = ft.Colors('yellow')

        self.content = ft.Column(
              alignment=ft.MainAxisAlignment.END,
              horizontal_alignment=ft.CrossAxisAlignment.START,
              spacing=8,
              run_spacing=8,
              width = 420,

              controls=[
                ft.Container(
                    border_radius = ft.border_radius.only(top_left = 8, top_right = 8, bottom_left = 8, bottom_right = 8),
                    border = ft.border.all(width = 2, color = ft.Colors.with_opacity(opacity=0.5,color=ft.Colors("white"))),
                    image = ft.DecorationImage(src='house.jpg',fit=ft.ImageFit.COVER,opacity=0.9),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                    alignment = ft.alignment.center,
                    height = 80,
                    width = 130,
                    ink_color = ft.Colors('yellow'),
                    bgcolor = ft.Colors('black12'),
                ),
                ft.Container(
                    padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                    border_radius=ft.border_radius.all(18),
                    border = ft.border.all(width = 2, color = ft.Colors.with_opacity(opacity=0.5,color=ft.Colors("white")),),
                    bgcolor=ft.Colors.with_opacity(opacity=0.8,color=ft.Colors.GREY_900),
                      shadow=ft.BoxShadow(
                          spread_radius=1,
                          blur_radius=15,
                          color=ft.Colors("black12"),
                          offset=ft.Offset(0, 5),
                      ),
                      blur=(12,12),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            # Banner Title
                           ft.Container(
                               padding=ft.padding.all(8),
                               content=ft.Text(
                                text_align=ft.TextAlign.LEFT,
                                value="Consultoria Abogamos",
                                size=18,
                                weight=ft.FontWeight.W_900,
                                color=ft.Colors.GREY_200,
                            ),),
                           ft.Divider(thickness=0.1,),

                            # Banner Description
                           RowContainer(page=self.page, left_text='City',right_text='Chile',icon_name=ft.Icons.PIN_DROP_ROUNDED),
                           ft.Divider(thickness=0.1,),
                           RowContainer(page=self.page, left_text='Province',right_text='La Serena',icon_name=ft.Icons.PIN_DROP_ROUNDED),
                           ft.Divider(thickness=0.1,),
                           RowContainer(page=self.page, left_text='Telephone',right_text='+53 85545585',icon_name=ft.Icons.LOCAL_PHONE_ROUNDED),
                           ft.Divider(thickness=0.1,),
                           RowContainer(page=self.page, left_text='Address',right_text='53 Avenue 12540',icon_name=ft.Icons.HOME_WORK_ROUNDED),
                           ft.Divider(thickness=0.1,),
                        ]
                        ),
                ),

              ],
          )

class RowContainer(ft.Container):

    def __init__(self, page: object = None, content: object = None,left_text: str="",right_text: str="",icon_name: object=None) -> None:
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(left=8,right=8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True


        self.content = ft.Row(
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Row(
                    controls=[
                        ft.Icon(name=icon_name),
                        ft.Text(value=left_text)
                    ]
                ),
                ft.Text(value=right_text),
            ],
        )