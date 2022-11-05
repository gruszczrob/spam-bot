import pyautogui, time
print("Podaj text do spamowania \n >", end="")
imie = input()
print("Podaj ile razy spamować? \n >", end="")
razy = int(input())
print("Podaj ile chcesz czekać zanim zaczniemy spamować? (zalecane przynajmnie 5 sekund \n >", end="")
czas = int(input())
time.sleep(czas)
while(razy>0):
    pyautogui.typewrite(imie)
    pyautogui.press("enter")
    razy-=1
