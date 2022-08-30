import os
import time
os.remove("data.txt")
fichier = open("data.txt", "a")
fichier.write(
    '#include <Keyboard.h> \nconst int BUTTON_PIN = 3; \nint lastState = HIGH; \nint currentState; \nString fr(String text){\n  int i = 0;\n  String _en = " =qwertyuiopasdfghjkl;zxcvbnQWERTYUIOPASDFGHJKL:ZXCVBNm,./M<>?1234567890!@#$%^&*()",\n         _fr = " =azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN,;:!?./ & \\"\'(- _  1234567890",\n         str = "";\n  while (text[i] != 0){\n    str = str + (String)_en[_fr.indexOf((String)text[i++])];\n  }\n  return str;\n}\nvoid setup() { \n   Serial.begin(9600); \n   Keyboard.begin();\n   delay(1000);\n   pinMode(BUTTON_PIN, INPUT_PULLUP); \n} \nvoid loop() { \n  currentState = digitalRead(BUTTON_PIN); \n  if(lastState == LOW && currentState == HIGH){ \n   Serial.println("1"); \n ')
help = '\n     "open" pour executer un programme \n     "text" pour ecrire du text \n     "download" pour télécharger un fichier depuis un liens http.s \n     "file" pour importer un fichier texte a écrire sur le pc\n '
print(help)
while True:

    command = input("Que voulez vous faire ? : ")
    if command == "open":
        app = input("Que voulez vous executer ? : ")
        if app == "quit":
            pass
        else:
            fichier.write(
                f'   Keyboard.press(KEY_LEFT_GUI); \n   Keyboard.press("r"); \n   delay(10); \n   Keyboard.releaseAll(); \n   delay(200); \n   Keyboard.print(fr("{app}")); \n   Keyboard.press(KEY_RETURN); \n   delay(100); \n   Keyboard.releaseAll();\n ')

    if command == "text":
        print('\n   "enter" pour faire appuyer sur le touche entrer \n')
        while True:
            text = input("Que voulez vous écrire ? : ")
            if text == "quit":
                break
            if text == "enter":
                fichier.write(
                    f'   Keyboard.press(KEY_RETURN); \n   delay(100); \n')
            else:
                fichier.write(
                    f'   Keyboard.print(fr("{text}")); \n   delay(500); \n')

    if command == "download":
        while True:
            fichier.write(
                '   Keyboard.press(KEY_LEFT_GUI); \n   Keyboard.press('r'); \n   delay(10); \n   Keyboard.releaseAll();\n   Keyboard.print(fr("powershell")); \n   Keyboard.press(KEY_RETURN); \n   delay(100); \n   Keyboard.releaseAll();\n ')
            URL = input("Que voulez vous installer ? (URL) : ")
            path = input(f"Où voulez vous installer {URL} ? : ")
            if URL == "quit":
                fichier.write(
                    f'\nexit')
                break
            else:
                fichier.write(
                    f'   Keyboard.print(fr("Invoke-WebRequest -Uri "{URL}" -OutFile "{path}" ")); \n')

    if command == "file":
        fichier.write(
            f'   Keyboard.press(KEY_LEFT_GUI); \n   Keyboard.press('r'); \n   delay(10); \n   Keyboard.releaseAll(); \n   delay(200); \n   Keyboard.print(fr("notepad")); \n   Keyboard.press(KEY_RETURN); \n   delay(100); \n   Keyboard.releaseAll();\n ')

        infile = input(
            "Quel est le nom du fichier a ouvrir ? ( extension doit être inclu, le fichier gardera le nom et l'extension par defaut ): ")
        path = input("Où voulez vous enregistrer le fichier ? : ")
        f = open(infile)
        text = f.read()
        text = text.replace('\n', """   Keyboard.press(KEY_RETURN); """)
        print("Le fichier sera écrit de cette façon : ")
        print(text)
        fichier.write(
            f'   Keyboard.print(fr("{text}")); \n   delay(1000); \n   Keyboard.press(KEY_LEFT_CTRL); \n   Keyboard.press('s'); \n   delay(100); \n   Keyboard.releaseAll();\n   Keyboard.print(fr("{infile}")); \n' "")
        for i in range(7):
            fichier.write(f'   Keyboard.press(KEY_TAB);\n')
        fichier.write(
            f'   Keyboard.press(KEY_RETURN);\n   Keyboard.print(fr("{path}")); \n')

    if command == "help":
        print(help)

    if command == "quit":
        break


fichier.write(
    '   } else { \n    Serial.println("0"); \n   }\nlastState = currentState;\n} \n')
fichier.close()
print("Le fichier a bien été enregistré sous le nom de data.txt")
time.sleep(10)
