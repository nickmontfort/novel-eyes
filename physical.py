import random

# random.seed(69105);

# For each eye (iris) color, 1% of the population is represented by 20 strings
color = []
color += ["brown"] * 140
color += ["medium brown"] * 10
color += ["black"] * 8
color += ["blue"] * 20
color += ["hazel"] * 10
color += ["gray"] * 6
color += ["green"] * 4
color += ["amber"] * 2

# These correspond to the colors
color_comment = []

# Brown
color_comment += [""] * 66
color_comment += [", as is so often the case"] * 30
color_comment += [", that most typical color"] * 18
color_comment += [", that most typical hue"] * 2
color_comment += [" like loam"] * 10
color_comment += [" as the earth"] * 8
color_comment += [" as the nourishing earth"]
color_comment += [" as the unforgiving earth"]
color_comment += [" against the sun"] * 4

# Medium brown
color_comment += [""] * 8
color_comment += [", or, one might say, chestnut"] * 2

# Black
color_comment += [""] * 6
color_comment += [", or as pedants will tell you, actually a very deep brown"] * 2

# Blue
color_comment += [""] * 12
color_comment += [" as the sky"] * 3
color_comment += [" as clear sky"]
color_comment += [" as the far sky"]
color_comment += [" as a lucid pond"]
color_comment += [", though made up, oddly enough, of brown pigment"] * 2

# Hazel
color_comment += [""] * 6
color_comment += [", containing green, blue, gold, and brown"] * 2
color_comment += [", with those characteristic hints of green, blue, gold, and brown"] * 2

# Gray
color_comment += [""] * 4
color_comment += [", hard as it is to distinguish this color from blue"] * 2

# Green
color_comment += [""] * 3
color_comment += [", as if reflecting nature"]

# Amber
color_comment += [""]
color_comment += [", that rarest of colors"]

color_phrase = []

for i in range(200):
    color_phrase += [color[i] + color_comment[i]]

color_phrase = []

for i in range(200):
    color_phrase += [color[i] + color_comment[i]]

print(random.choice(color_phrase))
