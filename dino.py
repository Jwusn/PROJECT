import os
import time
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dinosaur(position):
    print(' ' * position + 'o')

def main():
    position = 0
    jump = False

    while True:
        clear_screen()
        print_dinosaur(position)

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                jump = True

        if jump:
            position += 1
        else:
            position -= 1

        if position > 20:
            jump = False
            position = 20

        time.sleep(0.1)

if __name__ == "__main__":
    main()