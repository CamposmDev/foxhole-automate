from pynput.keyboard import Key, KeyCode

KEYCODE_W: KeyCode = KeyCode.from_char('w')
KEYCODE_A: KeyCode = KeyCode.from_char('a')
KEYCODE_S: KeyCode = KeyCode.from_char('s')
KEYCODE_D: KeyCode = KeyCode.from_char('d')

def is_wasd(key: (Key | KeyCode | None)) -> bool:
    return key in [KeyCode.from_char(char) for char in 'wasd']