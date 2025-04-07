import pyautogui

from AutoControl.Move.moveMouse import MoveMouse
p1 = pyautogui.position()
mm = MoveMouse()
print(p1)
mm.mouse_move(p1[0]+24,p1[1]+24)