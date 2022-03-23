import sys
import time
import random
def aprint(text, delay):
  for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(delay)
  print()

aprint("Talking Ben created by IlyaYevtyhov", 0.07)
aprint("GitHub - https://github.com/IlyaYevtyhov/TalkingBen", 0.04)
while True:
    print()
    answer = input("Задайте вопрос Бену -> ")
    if answer == "":
        print("Вы не задали вопрос Бену")
    else:
        r = random.randint(1, 3)
        if r == 1:
            aprint("Ben: Ahaha", 0.07)
        elif r == 2:
            aprint("Ben: Yes", 0.07)
        elif r == 3:
            aprint("Ben: No", 0.07)