from tkinter import *
#TODO: import your_random_home_work_library

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        #self.secret_number = random.randint(1, 10) #no random library yet
        self.guess = None
        self.num_guesses = 0
        
        self.message = "Guess a number from 1 to 10"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        self.entry = Entry(master)

        self.guess_button = Button(master, text="Guess", command=self.guess_number)
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    def guess_number(self):
        pass

    def reset(self):
        pass

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()