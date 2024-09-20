from manim import *

DELAY = 1

class PrimitivesArctan(Scene):
    def construct(self):
        # Créer un titre
        title = Text("Révision sup : Exercice numéro 70", font_size=48)
        self.play(Write(title))
        self.wait(DELAY)
        self.play(title.animate.to_edge(UP))

        # Afficher l'énoncé de l'exercice
        equation = MathTex(r"\text{Chercher toutes les primitives de }\arctan(x)", font_size=36)
        self.play(Write(equation))
        self.wait(2 * DELAY)

        self.play(FadeOut(equation))
        self.wait(DELAY)

        equalities = MathTex(
            r"\int \arctan(x) \mathrm dx = \int 1 * \arctan(x) \mathrm dx",
            r"\int \arctan(x) \mathrm dx = x \arctan(x) - \int \frac{x}{1+x^2} \mathrm dx",
            r"\int \arctan(x) \mathrm dx = x \arctan(x) - \frac 1 2 \ln(1 + x^2) + c, c \in \mathbb R",
            font_size=32
        )

        # Aligner les égalités verticalement (chaque ligne en dessous de l'autre)
        equalities.arrange(DOWN, aligned_edge=LEFT)

        # Faire apparaître progressivement chaque égalité
        for i in range(len(equalities)):
            self.play(Write(equalities[i]))
            self.wait(DELAY/2)  # Pause entre chaque égalité

        for i in range(len(equalities) - 1):
            self.play(FadeOut(equalities[i]))

        self.play(equalities[-1].animate.scale(1.2).move_to(ORIGIN))
        self.wait(2 * DELAY)

        highlight = SurroundingRectangle(equalities[-1], color=YELLOW, buff=0.2)
        self.play(Create(highlight))
        self.wait(2 * DELAY)