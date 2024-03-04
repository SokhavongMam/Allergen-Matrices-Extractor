from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def main():
    try:
        while True:
            # Press tab
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.2)

            # Press Shift + right arrow
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
            time.sleep(0.2)

            # Press Shift + right arrow
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
            time.sleep(0.2)

            # Press alt
            keyboard.press(Key.alt)
            keyboard.release(Key.alt)
            time.sleep(2jlm)

    except KeyboardInterrupt:
        print("Key 'u' interrupted the loop. Exiting...")


if __name__ == "__main__":
    time.sleep(3)
    main()
