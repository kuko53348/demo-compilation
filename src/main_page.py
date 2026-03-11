import flet as ft
from pages.lobby_page import LobbyPage
from pages.location_page import LocationPage
from pages.contact_page import ContactPage
from pages.question_page import QuestionPage
from pages.app_bar import nav_app_bar ,nav_drawer_widget
from pages.profile_details import ProfileDetails

class page_app_view(ft.View):

    ''''
    ## Create frame view
    ```python
    >>> current_view = page_app_view(
    >>>                page = self.page,
    >>>                route = self.route,
    >>>                content = ft.ElevatedButton(
    >>>                    text = 'Home',
    >>>                    on_click = lambda _: self.page.go('/'),
    >>> ))
    ```
    '''

    def __init__(self, page: object = None, route: str = str(), content: object = None, show_navigation: bool = False,index_page = None,) -> None:
        super().__init__()
        self.page = page # type: ignore
        self.route = route
        self.padding = 0
        self.content = content
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.controls: list = [self.content]
        self.index_pages_dict: dict = {
            0: ContactPage(page=self.page),
            1: QuestionPage(page=self.page),
            2: LocationPage(page=self.page),
            3: LocationPage(page=self.page),
        }
        self.controls: list = [
            (
                self.index_pages_dict.get(index_page)
                if not index_page == None
                else content
            ),
        ]
        if show_navigation:
            self.appbar = ft.AppBar(
                title=ft.Text("Consultoria Cerena"),
                center_title=True,
                bgcolor=ft.Colors("grey900"),
                automatically_imply_leading=False,
            )

            # self.floating_action_button_location = (
            #     ft.FloatingActionButtonLocation.MINI_END_TOP
            # )
            self.drawer = nav_drawer_widget(
                page=self.page,icon_image='icon.jpg',
                developer_image='my_avatar.png',
                logo_image='splash_android.png',
                drawer_widget=self
            )
            # self.floating_action_button = ft.FloatingActionButton(
            #     icon=ft.Icons.MENU_BOOK_ROUNDED,
            #     bgcolor=ft.Colors("grey900"),
            #     mini=True,
            #     foreground_color=ft.Colors.AMBER_100,
            #     disabled_elevation=True,
            #     focus_elevation=0,
            #     on_click=lambda _: self.open_drawer(),
            # )

            self.navigation_bar = ft.NavigationBar(
                selected_index=0,
                bgcolor=ft.Colors("grey900"),
                # offset=(0, -0.05),
                height=60,
                on_change=lambda _: self.change_screens(index_page=_.control),
                elevation=32,
                destinations=[

                    ft.NavigationBarDestination(
                        label="Contacto",
                        icon=ft.Icons.SUPERVISED_USER_CIRCLE_OUTLINED,
                        selected_icon=ft.Icons.SUPERVISED_USER_CIRCLE,
                    ),

                    # ft.NavigationBarDestination(
                    #     label="Document",
                    #     icon=ft.Icons.WATER_OUTLINED,
                    #     selected_icon=ft.Icons.WATER_ROUNDED,
                    # ),
                    ft.NavigationBarDestination(
                        label="Preguntas",
                        icon=ft.Icons.LOCAL_LIBRARY_OUTLINED,
                        selected_icon=ft.Icons.LOCAL_LIBRARY,
                    ),
                    ft.NavigationBarDestination(
                        label="Ubicacion",
                        icon=ft.Icons.PIN_DROP_OUTLINED,
                        selected_icon=ft.Icons.PIN_DROP,
                    ),
                ],
            )
            self.appbar = nav_app_bar(
                page=self.page,
                title="Consultoria",
                visible=True,
                menu_drawer=self.drawer,
                bgcolor=ft.Colors("grey900"),
                icon_left=ft.Icons.ASSURED_WORKLOAD,
                icon_right=ft.Icons.NOW_WIDGETS_ROUNDED,
            )

    def change_screens(self, index_page = object):
        dynamic_index =  index_page.selected_index
        self.page.session.set("current_idex", dynamic_index)

        self.controls = [
            self.index_pages_dict.get(dynamic_index),
        ]
        self.update()

class flet_box_app:

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.left = 3
        self.page.window.top = 3
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window.height = 720
        self.page.window.width = 320

        self.page.on_route_change = lambda _: self.on_route_change(
            page = self.page,
            route = '/',
            )

        # self.page.go('/home')
        # self.page.go('/profile')
        self.page.go('/')

    def on_route_change(self, page: object = None, route: str = str()) -> None:
        self.page = page
        self.route = route
        self.page.views.clear()

        if self.page.route == '/':
            self.page.views.append(
                page_app_view(
                    page = self.page,
                    route = self.route,
                    content = LobbyPage(page=self.page),
                    show_navigation=False,
                        )
                    )
        if self.page.route == '/home':
            self.page.views.append(
                page_app_view(
                    page = self.page,
                    route = self.route,
                    content = ContactPage(page=self.page),
                    show_navigation=True,
                        )
                    )
        if self.page.route == '/profile':
            self.page.views.append(
                ProfileDetails(page=self.page)
                    )

        self.page.update()

def main():
    ft.app(
        target = flet_box_app,
        assets_dir = 'assets',
    )

if __name__ == '__main__':
    main()
