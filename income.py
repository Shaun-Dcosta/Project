import flet as ft

class IncomePage(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def create_pie_chart(data, colors, icons):
            normal_radius = 100
            hover_radius = 110
            normal_title_style = ft.TextStyle(
                size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
            )
            hover_title_style = ft.TextStyle(
                size=16,
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
                shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
            )
            normal_badge_size = 40
            hover_badge_size = 50

            def badge(icon, size):
                return ft.Container(
                    ft.Icon(icon),
                    width=size,
                    height=size,
                    border=ft.border.all(1, ft.colors.BROWN),
                    border_radius=size / 2,
                    bgcolor=ft.colors.WHITE,
                )

            def on_chart_event(e: ft.PieChartEvent):
                for idx, section in enumerate(chart.sections):
                    if idx == e.section_index:
                        section.radius = hover_radius
                        section.title_style = hover_title_style
                        section.badge.width = hover_badge_size
                        section.badge.height = hover_badge_size
                        section.badge.border_radius = hover_badge_size / 2
                    else:
                        section.radius = normal_radius
                        section.title_style = normal_title_style
                        section.badge.width = normal_badge_size
                        section.badge.height = normal_badge_size
                        section.badge.border_radius = normal_badge_size / 2
                chart.update()

            chart = ft.PieChart(
                sections=[
                    ft.PieChartSection(
                        value,
                        title=f"{value}%",
                        title_style=normal_title_style,
                        color=color,
                        radius=normal_radius,
                        badge=badge(icon, normal_badge_size),
                        badge_position=0.98,
                    )
                    for value, color, icon in zip(data, colors, icons)
                ],
                sections_space=0,
                center_space_radius=0,
                on_chart_event=on_chart_event,
                expand=True,
            )
            return chart

        income_chart = ft.Container(
            content=create_pie_chart(
                [60, 20, 15, 5],
                [ft.colors.BLUE, ft.colors.GREEN, ft.colors.ORANGE, ft.colors.PURPLE],
                [ft.icons.WORK, ft.icons.ATTACH_MONEY, ft.icons.SAVINGS, ft.icons.CARD_GIFTCARD]
            ),
            width=400,
            height=400,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=10,
            alignment=ft.alignment.center,
        )

        def create_data_table(title, data):
            return ft.Container(
                content=ft.Column([
                    ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Source")),
                            ft.DataColumn(ft.Text("Amount")),
                            ft.DataColumn(ft.Text("Frequency")),
                        ],
                        rows=[
                            
                            ft.DataRow(cells=[ft.DataCell(ft.Text(row[0])), ft.DataCell(ft.Text(row[1])), ft.DataCell(ft.Text(row[2]))]) 
                            for row in data
                        ],
                    )
                ]),
                width=400,
                margin=ft.margin.only(top=20),
            )

        income_data = [
            ("Salary", "$4,000", "Monthly"),
            ("Freelance", "$800", "Monthly"),
            ("Investments", "$600", "Monthly"),
            ("Gifts", "$200", "Annually"),
        ]

        income_table = create_data_table("Income Sources", income_data)

        main_content = ft.Column([
            ft.Text("Income Overview", size=32, weight=ft.FontWeight.BOLD),
            ft.Row([income_chart, income_table], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ], scroll=ft.ScrollMode.AUTO)

        return main_content