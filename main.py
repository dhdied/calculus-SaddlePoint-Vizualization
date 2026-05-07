from manim import *
import numpy as np

config.background_color = "#1a1b26"

class UltimateSaddlePoint(ThreeDScene):
    def construct(self):
        COLOR_SURFACE = "#bb9af7"      
        COLOR_SURFACE_DARK = "#9d7cd8" 
        COLOR_DANGER = "#f7768e"       
        COLOR_STRAIGHT = "#7dcfff"     
        COLOR_TEXT = "#c0caf5"         
        COLOR_WARN = "#6ce068"         

        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        title_theory = Text("Проблема седловых точек", font_size=36, weight=BOLD, color=WHITE).to_edge(UP)
        self.play(Write(title_theory))

        main_statement = Paragraph(
            "Проблема функции в точке (0;0) заключается в том, что",
            "стандартные проверки по прямым сечениям дают ложное",
            "представление о минимуме. На деле — это седловая точка.",
            line_spacing=0.8, font_size=28, alignment="center"
        ).next_to(title_theory, DOWN, buff=0.8)
        
        self.play(Write(main_statement))
        self.wait(2.5)
        self.play(FadeOut(main_statement))

        eq1 = MathTex("z = (y - x^2)(y - 3x^2)", font_size=48)
        eq2 = MathTex("z = y^2 - 4x^2y + 3x^4", font_size=48, color=COLOR_TEXT).next_to(eq1, DOWN, buff=0.6)
        
        eq_group = VGroup(eq1, eq2).move_to(ORIGIN)
        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformFromCopy(eq1, eq2)) 
        self.wait(2)
        self.play(FadeOut(eq_group))

        crit_title = Text("1. Необходимое условие (Градиент = 0)", font_size=32, color=COLOR_TEXT).next_to(title_theory, DOWN, buff=0.5)
        crit_math = MathTex(r"\begin{cases} z'_x = -8xy + 12x^3 \\ z'_y = 2y - 4x^2 \end{cases}", font_size=40)
        crit_check_text = Text("При M(0,0):", font_size=28, color=COLOR_TEXT)
        crit_check_math = MathTex(r"\begin{cases} -8(0)(0) + 12(0)^3 = 0 \\ 2(0) - 4(0)^2 = 0 \end{cases}", font_size=36).next_to(crit_check_text, RIGHT, buff=0.3)
        crit_check = VGroup(crit_check_text, crit_check_math)
        crit_res = Text("M(0, 0) — критическая точка", font_size=30, color=COLOR_STRAIGHT)
        crit_content = VGroup(crit_math, crit_check, crit_res).arrange(DOWN, buff=0.6).next_to(crit_title, DOWN, buff=0.8)

        self.play(Write(crit_title))
        self.play(Write(crit_math))
        self.wait(1)
        self.play(FadeIn(crit_check))
        self.play(Write(crit_res))
        self.wait(2.5)
        self.play(FadeOut(crit_title), FadeOut(crit_content))

        second_der_title = Text("2. Вторые производные в точке M(0,0)", font_size=32, color=COLOR_TEXT).next_to(title_theory, DOWN, buff=0.5)
        second_der_math = MathTex(
            r"z''_{xx} &= -8y + 36x^2 &\xrightarrow{M} \quad &0 \\",
            r"z''_{yy} &= 2 &\xrightarrow{M} \quad &2 \\",
            r"z''_{xy} &= -8x &\xrightarrow{M} \quad &0",
            font_size=44
        ).next_to(second_der_title, DOWN, buff=1)

        self.play(Write(second_der_title))
        self.play(Write(second_der_math))
        self.wait(2.5)
        self.play(FadeOut(second_der_title), FadeOut(second_der_math))

        hess_title = Text("3. Достаточное условие (Матрица Гессе)", font_size=32, color=COLOR_TEXT).next_to(title_theory, DOWN, buff=0.5)
        hess_math = MathTex(r"\Delta = \begin{vmatrix} 0 & 0 \\ 0 & 2 \end{vmatrix} = 0", font_size=44)
        hess_fail = Text("Детерминант = 0. Тест не дает ответа!", font_size=32, color=COLOR_DANGER, weight=BOLD)
        hess_content = VGroup(hess_math, hess_fail).arrange(DOWN, buff=1).next_to(hess_title, DOWN, buff=1)

        self.play(Write(hess_title))
        self.play(Write(hess_math))
        self.wait(1)
        self.play(FadeIn(hess_fail, scale=1.2))
        self.wait(3.5)
        self.play(FadeOut(title_theory), FadeOut(hess_title), FadeOut(hess_content))

        axes = ThreeDAxes(
            x_range=[-1.2, 1.2, 0.5], y_range=[0, 2.2, 0.5], z_range=[-1.5, 3.0, 1],
            x_length=6, y_length=6, z_length=4
        )
        
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        def func(u, v):
            z = (v - u**2) * (v - 3 * u**2)
            return max(min(z, 3), -1.5)

        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-1.1, 1.1], v_range=[0, 2.1], resolution=(40, 40),
            fill_opacity=0.6, checkerboard_colors=[COLOR_SURFACE, COLOR_SURFACE_DARK], stroke_width=0.2
        )

        danger_floor = Surface(
            lambda u, v: axes.c2p(u, u**2 + v * (2 * u**2), 0),
            u_range=[-1, 1], v_range=[0, 1], fill_opacity=0.4, fill_color=COLOR_DANGER, stroke_width=0
        )
        bound1 = axes.plot(lambda x: x**2, color=COLOR_WARN, x_range=[-1.1, 1.1])
        bound2 = axes.plot(lambda x: 3*x**2, color=COLOR_WARN, x_range=[-0.8, 0.8])

        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=1.5)
        title_3d = Text("Графическая интерпретация", font_size=30, weight=BOLD, color=WHITE).to_edge(UP + LEFT)
        self.add_fixed_in_frame_mobjects(title_3d)
        
        self.play(Write(title_3d))
        self.play(Create(axes), Write(axis_labels), run_time=1)
        self.play(Create(surface), run_time=2)
        
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3.5)
        self.stop_ambient_camera_rotation()

        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2)
        
        map_title = Paragraph(
            "«Красная зона»:", 
            "z < 0 (между параболами)", 
            font_size=24, color=COLOR_DANGER, alignment="left"
        ).to_corner(DL).shift(UP * 0.5)
        
        self.add_fixed_in_frame_mobjects(map_title)
        self.play(Write(map_title))
        self.play(Create(bound1), Create(bound2), FadeIn(danger_floor), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(map_title))

        self.move_camera(phi=75 * DEGREES, theta=20 * DEGREES, run_time=2)

        step1 = Paragraph(
            "Любое прямое сечение y = kx",
            "идет вверх (z > 0)",
            line_spacing=0.8, font_size=24, color=COLOR_STRAIGHT, alignment="center"
        ).to_edge(DOWN) 
        
        self.add_fixed_in_frame_mobjects(step1)
        self.play(Write(step1))

        k_tracker = ValueTracker(1.0)
        
        plane_straight = always_redraw(lambda: Polygon(
            axes.c2p(-1, -k_tracker.get_value(), -1.5), axes.c2p(1, k_tracker.get_value(), -1.5),
            axes.c2p(1, k_tracker.get_value(), 3), axes.c2p(-1, -k_tracker.get_value(), 3),
            fill_opacity=0.2, fill_color=COLOR_STRAIGHT, stroke_width=0
        ))
        line_path = always_redraw(lambda: ParametricFunction(
            lambda t: axes.c2p(t, k_tracker.get_value() * t, func(t, k_tracker.get_value() * t)),
            t_range=[-0.8, 0.8], color=COLOR_DANGER, stroke_width=8
        ))
        t_tracker = ValueTracker(0.0) 
        dot_straight = always_redraw(lambda: Dot3D(
            point=axes.c2p(t_tracker.get_value(), k_tracker.get_value()*t_tracker.get_value(), func(t_tracker.get_value(), k_tracker.get_value()*t_tracker.get_value())),
            color=WHITE, radius=0.1
        ))

        self.play(Create(plane_straight), Create(line_path), FadeIn(dot_straight))
        self.begin_ambient_camera_rotation(rate=0.2)

        self.play(k_tracker.animate.set_value(2.5), run_time=2)
        self.play(k_tracker.animate.set_value(-2.5), run_time=4)
        self.play(k_tracker.animate.set_value(1.0), run_time=2)
        
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(plane_straight), FadeOut(line_path), FadeOut(dot_straight), FadeOut(step1))

        self.move_camera(phi=85 * DEGREES, theta=-70 * DEGREES, zoom=1.1, run_time=2)

        step2 = Text("Сечение по параболе y = 2x² (Падает вниз)", font_size=24, color=COLOR_DANGER).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(step2)
        self.play(Write(step2))

        plane_curved = Surface(lambda u, v: axes.c2p(u, 2*u**2, v), u_range=[-0.9, 0.9], v_range=[-1.5, 3], fill_opacity=0.3, fill_color=COLOR_DANGER, stroke_width=0)
        danger_path = ParametricFunction(lambda t: axes.c2p(t, 2*t**2, func(t, 2*t**2)), t_range=[-0.8, 0.8], color=COLOR_DANGER, stroke_width=10)
        dot_danger = Dot3D(point=danger_path.get_start(), color=WHITE, radius=0.08)

        self.begin_ambient_camera_rotation(rate=-0.15)
        self.play(Create(plane_curved), Create(danger_path), run_time=1)
        
        alert_z = MathTex("z = -x^4", color=COLOR_DANGER, font_size=40).move_to(axes.c2p(0, 1.2, -1.2))
        self.play(MoveAlongPath(dot_danger, danger_path), run_time=4)
        self.play(Write(alert_z))
        self.stop_ambient_camera_rotation()
        self.wait(1.5)

        self.play(FadeOut(step2), FadeOut(plane_curved), FadeOut(dot_danger), FadeOut(alert_z))

        m_dot = Dot3D(point=axes.c2p(0, 0, 0), color=COLOR_WARN, radius=0.15)
        m_label = MathTex("M(0, 0)", font_size=44, color=COLOR_WARN).move_to(axes.c2p(0, 0, 0.7))
        
        res_text = Text("Вывод: M(0,0) — седловая точка", font_size=32, color=COLOR_WARN, weight=BOLD).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(res_text)
        
        self.play(Create(m_dot), Write(m_label), Write(res_text))
        
        self.move_camera(phi=60 * DEGREES, zoom=1.0, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)