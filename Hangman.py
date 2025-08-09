from tkinter import *
from tkinter import messagebox
import random

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/|\\", "   "),
    4: (" o ", "/|\\", "/ \\"),
    5: (" |\n"
        " |\n"
        " |_\no ", "/|\\", "/ "),
    6: (" |\n"
        " |\n"
        " |_\no ", "/|\\", "/\\ "),
}

words = (
    "aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat",
    "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat",
    "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra",
    "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog",
    "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin",
    "eagle", "echidna", "eel", "eland", "elephant", "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo",
    "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish",
    "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk",
    "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex",
    "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey",
    "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird",
    "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey",
    "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx",
    "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican",
    "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea",
    "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer",
    "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse",
    "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid",
    "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite",
    "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel",
    "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra"
)

window = Tk()
window.title("Hangman")
window.config(background="pink")

answer = ""
hint = []
wrong_guesses = 0
guessed_letters = set()

def new_game():
    global answer, hint, wrong_guesses, guessed_letters
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters.clear()
    update_display()
    enable_buttons(True)

def update_display():
    hangman_image.set("\n".join(hangman_art[wrong_guesses]))
    word_display.set(" ".join(hint))

def guess_letter(letter):
    global wrong_guesses
    if letter in guessed_letters:
        messagebox.showinfo("Hangman", f"You've already guessed '{letter}'!")
        return
    guessed_letters.add(letter)
    if letter in answer:
        for i, char in enumerate(answer):
            if char == letter:
                hint[i] = letter
    else:
        wrong_guesses += 1
    update_display()
    check_game_status()

def check_game_status():
    if "_" not in hint:
        messagebox.showinfo("Hangman", "Congratulations! You've guessed the word!")
        enable_buttons(False)
    elif wrong_guesses >= len(hangman_art) - 1:
        messagebox.showwarning("Hangman", f"You've been hanged! The word was '{answer}'.")
        enable_buttons(False)

def enable_buttons(enable):
    for button in letter_buttons:
        button.config(state=NORMAL if enable else DISABLED)

hangman_image = StringVar()
Label(window, textvariable=hangman_image, font=("Courier", 18), justify=LEFT).grid(row=0, column=0, columnspan=10, padx=10, pady=10)

word_display = StringVar()
Label(window, textvariable=word_display, font=("Courier", 24)).grid(row=1, column=0, columnspan=10, padx=10)

letter_buttons = []
for idx, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
    btn = Button(window, text=char.upper(), font=("Helvetica", 16), width=4,
                 command=lambda c=char: guess_letter(c))
    btn.grid(row=2 + idx // 9, column=idx % 9, padx=5, pady=5)
    letter_buttons.append(btn)

Button(window, text="New Game", command=new_game, font=("Helvetica", 16)).grid(row=5, column=4, columnspan=2, pady=20)

new_game()
window.mainloop()
