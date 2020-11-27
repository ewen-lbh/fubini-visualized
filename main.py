from manim import *


class TestScene(Scene):
    def construct(self):
        title = Tex("Fubini, visualized.")
        title.scale(2.5)
        self.play(Write(title))
        self.play(FadeOut(title))
        fubini_séparé = MathTex(r"\sum_{i=0}^n", r"\sum_{j=0}^n", r"f(i, j)")
        fubini_séparé.scale(2)
        self.play(ShowCreation(fubini_séparé))
        self.wait(3)
        self.play(ApplyMethod(fubini_séparé.scale, 0.5))
        self.play(ApplyMethod(fubini_séparé.shift, 3 * UP))
        self.play(Write(MathTex(r"\mathcal{L}\{f^{(n)}\} = p^n F(p) - \sum_{k=0}^{|n|-1} p^{n-k} f^{(k)}(0)")))
