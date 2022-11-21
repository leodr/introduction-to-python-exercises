STORY = """Es waren einmal die {erste_zahl} und die {zweite_zahl}, und
diese multiplizierten sich und ergaben die {multi}.
"""

num1 = int(input("Gib eine Zahl ein      : "))
num2 = int(input("Gib noch eine Zahl ein : "))

print(STORY.format(
    erste_zahl=num1,
    zweite_zahl=num2,
    multi=num1*num2
))
