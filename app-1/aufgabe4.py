from time import sleep

print("Vermehrung von Bakterien")

population = 100
hour = 0

while True:
    print(f"Stunde {hour} {population} Bakterien")
    hour += 1
    population *= 4
    sleep(0.25)
