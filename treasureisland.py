print('''
      _.--._  _.--._
,-=.-":;:;:;\':;:;:;"-._
\\\:;:;:;:;:;\:;:;:;:;:;\\
 \\\:;:;:;:;:;\:;:;:;:;:;\\
  \\\:;:;:;:;:;\:;:;:;:;:;\\
   \\\:;:;:;:;:;\:;::;:;:;:\\
    \\\;:;::;:;:;\:;:;:;::;:\\
     \\\;;:;:_:--:\:_:--:_;:;\\ 
      \\\_.-"      :      "-._\\
       \`_..--""--.;.--""--.._=>
        ''')
print("Welcome to treasure Island!")
print("Your mission is to find the treasure.")
left_right = input("Where do you want to go, left or right? ")
left_right_lower = left_right.lower()
if left_right_lower == "left":
    swim_wait = input("You have arrived at the river, Do you want to swim or wait?\n")
    swim_wait_lower = swim_wait.lower()
    if swim_wait_lower == "wait":
        door = input(''' You have been successfully teleported to the doors of Mooria.\n
        Which door do you wanna open, Red, Blue or Yellow? ''')
        door_lower = door.lower()
        if door_lower == "yellow":
            print("You Win")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
