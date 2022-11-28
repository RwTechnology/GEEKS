from Views.Vue import Vue
from Services.TextColors import TextColors
from Services.TextAnimation import TextAnimation

vue = Vue()
color = TextColors()
animation = TextAnimation()

name_app = "MAX LONDON PETROVIC"

animation.animation_text(f"{color.BLUE}{color.BOLD} {name_app} {color.END}\n")

vue.main()
