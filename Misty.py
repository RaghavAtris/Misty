import datetime
import pyautogui
import pywhatkit
import webbrowser
import sys
from Body.Listen import MicExecution
from Body.Speak import Speak
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from MistyUiUi import Ui_MainWindow
from pynput.keyboard import Key,Controller
keyboard = Controller()
print(">> Starting The Misty : Wait for few Seconds")

def YouTube(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    Speak("This is what I found for your query")
    pywhatkit.playonyt(term)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        MainExecution(self)

def MainExecution(self): 

    Speak("Hello There, I'm Misty. Your Own Virtual Consciousness. How can I be of Your Service?")

    while True:
        self.Data = MicExecution(self)
        self.Data = str(self.Data)
        if len(self.Data)<3:
            pass
        
        elif "time" in self.Data:
            time = datetime.datetime.now().strftime('%I:%M %p')
            Speak(f"It's {time}.")

        elif "date" in self.Data:
            date = datetime.datetime.now().strftime("%b %d %Y")
            Speak(f"It's {date}.")

        elif "show table" in self.Data or "open table" in self.Data:
            from PIL import Image
            image_path = "Assets\Table.png"
            with Image.open(image_path) as image:
                image.show()
                pass

        elif "hi" in self.Data or "hello" in self.Data or "hey" in self.Data:
            Speak("Hello There, How can i be of your service?")

        elif "element" in self.Data or "elements":
             Speak("Please enter the atomic number of the element :")
             pyautogui.keyDown("alt")
             pyautogui.press("tab")
             pyautogui.keyUp("alt")
             while True:
                print("")
                user_input = input("Please enter the atomic number of the element : ")
                if user_input == "1":
                    Speak("Atomic Number: 1.Symbol: H. Hydrogen is the lightest and most abundant element in the universe.It is a colorless, odorless, and highly flammable gas. Hydrogen is essential for many industrial processes, such as petroleum refining and ammonia production.")
                    break
                elif user_input == "2":
                    Speak("Helium (He). Atomic Number: 2. Symbol: He .Helium is the second lightest element and the second most abundant in the universe after hydrogen. It is a colorless, odorless, and inert gas. Helium is widely used in cryogenics, as it has the lowest boiling point of any element and can be used to achieve extremely low temperatures.")
                    break
                elif user_input == "3":
                    Speak("Lithium (Li). Atomic Number: 3 .Symbol: Li. Lithium is a soft, silvery-white metal. It is the lightest metal and the least dense solid element. Lithium is used in batteries, particularly in rechargeable lithium-ion batteries used in portable electronics and electric vehicles.")
                    break
                elif user_input == "4":
                    Speak("Beryllium (Be). Atomic Number: 4. Symbol: Be .Beryllium is a hard, grayish metal. It is relatively rare and toxic. Beryllium is used in various industries, including aerospace, electronics, and nuclear applications, due to its exceptional strength and heat resistance.")
                    break
                elif user_input == "5":
                    Speak("Boron (B). Atomic Number: 5 Symbol: B. Boron is a black, semi-metallic element. It is primarily found in compounds rather than in its pure elemental form. Boron is used in a variety of applications, such as in the production of borosilicate glass, agricultural fertilizers, and certain types of ceramics.")
                    break
                elif user_input == "6":
                    Speak("Carbon (C). Atomic Number: 6.Symbol: C Carbon is a non-metallic element that exists in various forms, including diamond, graphite, and amorphous carbon.It is the key building block of organic compounds and is essential for life as we know it. Carbon has numerous applications, including in steel production, energy storage (as in batteries), and as a component of various materials, such as carbon fiber.")
                    break
                elif user_input == "7":
                    Speak("Nitrogen (N). Atomic Number: 7. Symbol: N. Nitrogen is a colorless, odorless, and mostly inert gas. It makes up about 78% of Earth's atmosphere. Nitrogen is widely used in industrial processes, such as in the production of ammonia, fertilizers, and as a coolant or protective gas in various applications.")
                    break
                elif user_input == "8":
                    Speak("Oxygen (O). Atomic Number: 8. Symbol: O. Oxygen is a colorless, odorless, and highly reactive gas. It is essential for supporting combustion and is necessary for most forms of life. Oxygen is used in various industries, including steel production, water treatment, and medical applications.")
                    break
                elif user_input == "9":
                    Speak("Fluorine (F). Atomic Number: 9. Symbol: F. Fluorine is a highly reactive and corrosive pale yellow gas. It is the most electronegative element and can form compounds with almost all other elements. Fluorine is used in the production of numerous industrial and consumer products, including refrigerants, pharmaceuticals, and high-performance plastics.")
                    break
                elif user_input == "10":
                    Speak("Neon (Ne). Atomic Number: 10. Symbol: Ne. Neon is a colorless, odorless, and inert gas. It is commonly used in lighting, such as in neon signs and fluorescent lamps. Neon is also used in cryogenic applications and as a protective gas in certain types of lasers.")
                    break
                elif user_input == "11":
                    Speak("Sodium (Na). Atomic Number: 11. Symbol: Na. Sodium is a soft, silvery-white metal. It is highly reactive and can easily react with water. Sodium is commonly used in the production of chemicals, as a heat transfer fluid, and in the manufacturing of glass and ceramics.")
                    break
                elif user_input == "12":
                    Speak("Magnesium (Mg). Atomic Number: 12. Symbol: Mg. Magnesium is a shiny, grayish metal. It is the eighth most abundant element in the Earth's crust. Magnesium is used in various applications, including as an alloying agent in aluminum, in the production of lightweight metals, and as a component in fireworks and flares.")
                    break
                elif user_input == "13":
                    Speak("Aluminum (Al). Atomic Number: 13. Symbol: Al. Aluminum is a silvery-white, lightweight metal. It is the most abundant metal in the Earth's crust. Aluminum is widely used in numerous industries, including aerospace, construction, packaging, and electrical transmission lines.")
                    break
                elif user_input == "14":
                    Speak("Silicon (Si). Atomic Number: 14. Symbol: Si. Silicon is a hard, brittle crystalline solid. It is the second most abundant element in the Earth's crust after oxygen. Silicon is a key component in the production of semiconductors, solar cells, and various electronic devices.")
                    break
                elif user_input == "15":
                    Speak("Phosphorus (P). Atomic Number: 15. Symbol: P. Phosphorus exists in several forms, including white, red, and black phosphorus. It is highly reactive and can spontaneously ignite in air. Phosphorus is used in fertilizers, detergents, and various chemical processes.")
                    break
                elif user_input == "16":
                    Speak("Sulfur (S). Atomic Number: 16. Symbol: S. Sulfur is a yellow, brittle non-metal. It is found in various minerals and as a component of proteins. Sulfur is used in the production of sulfuric acid, fertilizers, and rubber products.")
                    break
                elif user_input == "17":
                    Speak("Chlorine (Cl). Atomic Number: 17. Symbol: Cl. Chlorine is a greenish-yellow, highly reactive gas. It is widely used as a disinfectant and in the production of PVC, solvents, and various chemicals. Chlorine is an essential element for maintaining clean drinking water.")
                    break
                elif user_input == "18":
                    Speak("Argon (Ar). Atomic Number: 18. Symbol: Ar. Argon is a colorless, odorless, and inert gas. It is the third most abundant gas in the Earth's atmosphere. Argon is used in various applications, including as a shielding gas in welding, as a protective atmosphere for certain metals, and in lighting.")
                    break
                elif user_input == "19":
                    Speak("Potassium (K). Atomic Number: 19. Symbol: K. Potassium is a soft, silvery-white metal. It is highly reactive and can react vigorously with water. Potassium is an essential nutrient for plants and animals, and it is used in fertilizers and in some industrial processes.")
                    break
                elif user_input == "20":
                    Speak("Calcium (Ca). Atomic Number: 20. Symbol: Ca. Calcium is a soft, grayish-white alkaline earth metal. It is the fifth most abundant element in the Earth's crust. Calcium is crucial for the formation and maintenance of bones and teeth, and it is also used in the production of cement, steel, and various alloys.")
                    break
                else:
                    break

        elif "what" in self.Data or "how" in self.Data or "where" in self.Data or "when" in self.Data or "which" in self.Data or "who" in self.Data or "tell me about" in self.Data:
             import wikipedia as googleScrap
             self.Data = self.Data.replace("tell me about","")
             self.Data = self.Data.replace("misty","")
             Speak("This what I found on the Web")

             try:
                 pywhatkit.search(self.Data)
                 result = googleScrap.summary(self.Data,2)
                 Speak(result)

             except:
                 Speak("No speakable data available for your Query")

        elif "goodbye" in self.Data or "bye" in self.Data or "good bye" in self.Data or "offline" in self.Data or "break" in self.Data or "sleep" in self.Data:
                Speak("nice talking to you!")
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 18:
                    Speak("Have a Nice day!")
                    sys.exit()
                elif hour >= 18 and hour < 24:
                    Speak("Goodnight, Sweet dreams!")
                    sys.exit()  
                                          
startExecution = MainThread()  

class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Assets\Misty.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
Ui_MainWindow = Main()
Ui_MainWindow.show()
exit(app.exec_())