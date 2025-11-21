from manim import * 

class MultipleFunctions(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE}
        )
        self.play(Create(axes))
        self.wait(1)

        # Define functions
        def func1(x):
            return x**2

        def func2(x):
            return x**3

        def func3(x):
            return -x

        # Plot first function
        graph1 = axes.plot(func1, color=RED)
        label1 = axes.get_graph_label(graph1, label="x^2")
        self.play(Create(graph1), Write(label1))

        # >>> BOTTOM-RIGHT BOX
        box_text = Text("Function 1", font_size=28, color=WHITE)
        box_rect = SurroundingRectangle(
            box_text, color=WHITE,
            fill_color=BLACK, fill_opacity=1
        )
        func1_box = VGroup(box_rect, box_text).to_corner(DR)
        func1_box.set_z_index(10)
        self.play(FadeIn(func1_box))
        # <<<

        self.wait(1)
        self.play(FadeOut(graph1), FadeOut(label1), FadeOut(func1_box))

        # Plot second function
        graph2 = axes.plot(func2, color=GREEN)
        label2 = axes.get_graph_label(graph2, label="x^3")
        self.play(Create(graph2), Write(label2))

        # >>> BOTTOM-RIGHT BOX
        box_text = Text("", font_size=28, color=WHITE)
        box_rect = SurroundingRectangle(
            box_text, color=WHITE,
            fill_color=BLACK, fill_opacity=1
        )
        func2_box = VGroup(box_rect, box_text).to_corner(DR)
        func1_box.set_z_index(10)
        self.play(FadeIn(func2_box))
        # <<<

        self.wait(1)
        self.play(FadeOut(graph2), FadeOut(label2), FadeOut(func2_box))

        # Plot third function
        graph3 = axes.plot(func3, color=YELLOW)
        label3 = axes.get_graph_label(graph3, label="-x")
        self.play(Create(graph3), Write(label3))

        # >>> BOTTOM-RIGHT BOX
        box_text = Text("Function 3", font_size=28, color=WHITE)
        box_rect = SurroundingRectangle(
            box_text, color=WHITE,
            fill_color=BLACK, fill_opacity=1
        )
        func3_box = VGroup(box_rect, box_text).to_corner(DR)
        func1_box.set_z_index(10)
        self.play(FadeIn(func3_box))
        # <<<

        self.wait(2)
        self.play(FadeOut(graph3), FadeOut(label3), FadeOut(func3_box))
    
# To run in VS code, it can be ran using this in a terminal:  manim -pql Main_manim_display_draft1.py MultipleFunctions
# If its not working, lmk and I'll try to change it up