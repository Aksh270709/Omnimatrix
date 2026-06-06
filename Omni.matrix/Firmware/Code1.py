from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.row_pins = (26, 27, 28)
keyboard.col_pins = (29, 6, 7)

keyboard.diode_orientation = 1

keyboard.keymap = [
    [
        KC.LCTRL(KC.Z), KC.LCTRL(KC.LSFT(KC.Z)), KC.LGUI(KC.LALT(KC.PSCR)),
        KC.EQUAL, KC.LCTRL(KC.BSLASH), KC.LCTRL(KC.X),
        KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LALT(KC.TAB)
        ]
]

if __name__ == '__main__':
    keyboard.go()