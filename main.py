from pynput import mouse
from pprint import pprint
from pynput import keyboard
from jinja2 import Environment, FileSystemLoader

KeyMap = {"ctrl": "KEY_LEFT_CTRL", "shift": "KEY_LEFT_SHIFT", "alt": "KEY_LEFT_ALT", "cmd": "KEY_LEFT_GUI",
          "ctrl_r": "KEY_RIGHT_CTRL", "shift_r": "KEY_RIGHT_SHIFT", "alt_r": "KEY_RIGHT_ALT", "cmd_r": "KEY_RIGHT_GUI",
          "up": "KEY_UP_ARROW", "down": "KEY_DOWN_ARROW", "left": "KEY_LEFT_ARROW", "right": "KEY_RIGHT_ARROW",
          "backspace": "KEY_BACKSPACE", "tab": "KEY_TAB", "enter": "KEY_RETURN", "esc": "KEY_ESC",
          "delete": "KEY_DELETE", "caps_lock": "KEY_CAPS_LOCK", "f1": "KEY_F1", "f2": "KEY_F2", "f3": "KEY_F3",
          "f4": "KEY_F4", "f5": "KEY_F5", "f6": "KEY_F6", "f7": "KEY_F7", "f8": "KEY_F8", "f9": "KEY_F9",
          "f10": "KEY_F10", "f11": "KEY_F11", "f12": "KEY_F12", "f13": "KEY_F13", "f14": "KEY_F14", "f15": "KEY_F15",
          "f16": "KEY_F16", "f17": "KEY_F17", "f18": "KEY_F18", "f19": "KEY_F19", "f20": "KEY_F20", "f21": "KEY_F21",
          "f22": "KEY_F22", "f23": "KEY_F23", "f24": "KEY_F24", "space": " "}

KeyStep = list()


def generate_code_snip() -> dict:
    code_snip = {"code": ""}
    alph = list()
    for Step in KeyStep:
        temp = ""
        if Step["status"]:
            temp = "  Keyboard.press("
        else:
            temp = "  Keyboard.release("
        if Step["key"] in KeyMap:
            if Step["key"] == "space":
                temp = temp + "'" + " " + "');\n"

            else:
                temp = temp + KeyMap[Step["key"]] + ");\n"
        else:
            if KeyStep.index(Step) + 1 != len(KeyStep) and KeyStep[KeyStep.index(Step) + 1]["key"] not in KeyMap:
                if Step["status"] == 1:
                    alph.append(Step["key"])
                continue
            else:
                if len(alph) == 0:
                    if Step["status"]:
                        temp = "  Keyboard.press('{}');\n".format(Step["key"])
                    else:
                        temp = "  Keyboard.release('{}');\n  delay(1000);\n".format(Step["key"])
                    code_snip["code"] = code_snip["code"] + temp
                    continue
                temp = "  Keyboard.println(\"{}\");\n  delay(1000);\n".format("".join(alph))
                code_snip["code"] = code_snip["code"] + temp
                alph.clear()
                continue
        if not Step["status"]:
            temp = temp + "  delay(1000);\n"
        code_snip["code"] = code_snip["code"] + temp
    return code_snip


def output_ino(code_snip: dict) -> None:
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('temp_sketch.ino')
    with open("final_sketch.ino", 'w+', encoding='utf-8') as fo:
        out = template.render(code=code_snip["code"])
        fo.write(out)


def on_press(key):
    temp = dict()
    try:
        print('{} pressed'.format(
            key.char))
        temp["key"] = key.char
        temp["status"] = 1
    except AttributeError:
        print('{} pressed'.format(
            key))
        if key == keyboard.Key.esc:
            return False
        temp["key"] = str(key).split(".")[1]
        temp["status"] = 1
    KeyStep.append(temp)


def on_release(key):
    temp = dict()
    print('{0} released'.format(
        key))
    try:
        temp["key"] = key.char
        temp["status"] = 0
    except AttributeError:
        temp["key"] = str(key).split(".")[1]
        temp["status"] = 0
    KeyStep.append(temp)


def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


def main():
    # with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener, mouse.Listener(
    #         on_move=on_move,
    #         on_scroll=on_scroll,
    #         on_click=on_click) as mouse_listener:
    #     keyboard_listener.join()
    #     mouse_listener.join()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
        keyboard_listener.join()
    code_snip = generate_code_snip()
    output_ino(code_snip)


if __name__ == '__main__':
    main()
