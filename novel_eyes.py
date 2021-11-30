import random

# A sketch for something more interesting, 
# which will not have this sort of pun for its name.

# random.seed(69105);

# For each iris color, 1% of the population is represented by 20 strings
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
color_comment += [", though made up, as those familiar with matters ocular explain, of brown pigment"] * 2

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

def color():
    return random.choice(color_phrase)

def iris_sentence():
    text = random.choice(["the iris, with its radial stroma, is ", "the iris is ", "the iris is ", "it’s ", "it’s ", "it’s ", "it is ", "that outer ring is ", "there around the pupil, ", "", "like an amazingly regular flower, "]) + color() + "."
    return text.capitalize();

size = (["tiny"] * 5) + (["there, a dot"] * 4) + (["unremarkable"] * 5) + (["large"] * 4) + ["surrounded by this color and texture", "highly constricted", "barely a dot", "a negative space", "dead center", "an absence, but looks like a black discus", "dark purple", "immense", "prodigious", "enlarged"]

def pupil_sentence():
    text = "the pupil is " + random.choice(size) + "."    
    return text.capitalize();

def sclera_sentence():
    return random.choice([""] * 5 + ["Sclera like an egg.", "In a pure white surround.", "The sclera shot with some red.", "White around it veined with red.", "The white bloodshot.", "All of it set in a sea of red."])

subject = (["it "] * 6) + ["this ", "the whole assemblage ", "all of it ", "this orb "]

moves = ["moves ", "foveates ", "turns ", "pivots ", "swivels ", "angles "]

fast_adj = ([""] * 8) + ["at once ", "rapidly ", "with a jitter "]

slow_adj = ([""] * 8) + ["and lingers ", "meditatively ", "bit by bit "]

direction = ["left to right, then top to bottom", "left to right, then top to bottom", "right to left, then top to bottom", "top to bottom, then left to right", "top to bottom, then left to right", "top to bottom, then left to right"]

def all_over():
    text1 = ""
    text1 += random.choice(["", "at first "])
    text1 += random.choice(direction + ["right in the middle, then outwards from there", "erratically", "in various directions"]) + ". "
    text2 = " "
    text2 += random.choice(["Then, the motion is ", "The movement continues "])
    text2 += random.choice(["toward each margin", "more slowly but still irregularly", "almost in a spiral"])
    return text1 + text2

def typical_prose():
    text = (random.choice(subject) + random.choice(moves) + random.choice(fast_adj) + random.choice(direction) + ". ").capitalize()
    if (random.random() < .3):
        text += " " + "Then a pause, a backtracking. "
    if (random.random() < .1):
        text += " " + "Now and then, a long hesitation, varied movement. "
    return text

def typical_poetry():
    text = (random.choice(subject) + random.choice(moves) + random.choice(slow_adj) + random.choice(direction) + ". ").capitalize() 
    if (random.random() < .3):
        text += " " + "A skip upwards, then back. "
    if (random.random() < .1):
        text += " " + "The progression is in a regular shape. "
    return text

def visual_poetry():
    return (random.choice(subject) + random.choice((["skips"] * 3) + moves) + random.choice(slow_adj + fast_adj) + all_over()) + ". ".capitalize() 

sentences = "";

for i in range(1800):
    text_style = random.choice([typical_prose] * 50 + [typical_poetry] * 4 + [visual_poetry]);
    sentences += iris_sentence() + " " + pupil_sentence() + " " + sclera_sentence() + " " + text_style() + " \n\n\n"

sentences += iris_sentence() + " " + pupil_sentence() + " " + sclera_sentence() + " "

for i in range(120):
   text = (random.choice(subject) + random.choice((["skips"] * 3) + moves) + random.choice(slow_adj + fast_adj) + all_over()) + ". ".capitalize()
   if (random.random() < .1):
       text += " The lids " + random.choice(["narrow. ", "squeeze together for a moment. "])
   sentences += text

sentences += "A tear. The lids close."

print(sentences)

print(len(sentences.split()))
