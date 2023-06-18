import tkinter as tk
from tkinter import messagebox
import random
from random_word import RandomWords

# Function to jumble the letters of a word
def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

# Function to check if the guessed word is correct
def check_guess(event=None):
    global score, timer_running, level, high_score
    guess = entry.get().lower()
    if guess == word.lower():
        score += 1
        messagebox.showinfo("Correct", "Congratulations! You guessed it correctly.")
        timer_running = False
        start_timer()
        if score % 5 == 0:
            level += 1
            messagebox.showinfo("Level Up", f"Great job! You have reached level {level}.")
        if score > high_score:
            high_score = score
            save_high_score()
        play_round()
    else:
        messagebox.showerror("Incorrect", "Oops! That's not correct. The word was " + word)

# Function to provide a hint for the current word
def give_hint():
    global word
    hint = word[:2] + "-" * (len(word) - 2)
    messagebox.showinfo("Hint", f"The word starts with '{hint}'.")

# Function to start the timer
def start_timer():
    global time_limit, timer_label, timer_running
    time_limit = 20
    timer_label.config(text="Time: " + str(time_limit))
    timer_running = True
    update_timer()

# Function to update the timer
def update_timer():
    global time_limit, timer_label, timer_running
    time_limit -= 1
    timer_label.config(text="Time: " + str(time_limit))
    if time_limit == 0:
        messagebox.showinfo("Time's Up", "Time's up! You ran out of time.")
        play_round()
    elif timer_running:
        window.after(1000, update_timer)

# Function to play another round
def play_round():
    global word, jumbled_word, level
    if level == 1:
        word = random.choice(easy_words).lower()
    elif level == 2:
        word = random.choice(medium_words).lower()
    else:
        word = random.choice(hard_words).lower()
    jumbled_word = jumble_word(word)
    jumbled_label.config(text=jumbled_word)
    entry.delete(0, tk.END)
    score_label.config(text="Score: " + str(score))
    level_label.config(text="Level: " + str(level))

# Function to quit the game
def quit_game():
    window.destroy()

# Function to save the high score to a file
def save_high_score():
    with open("highscore.txt", "w") as file:
        file.write(str(high_score))

# Function to load the high score from a file
def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Initialize variables
word = ""
jumbled_word = ""
score = 0
level = 1
time_limit = 20
timer_running = False
r = RandomWords()
high_score = load_high_score()

# Word lists based on difficulty levels
easy_words = ["apple", "banana", "cat", "dog", "elephant","car", "book", "tree", "ball", "moon", "bird", "cake", "fish", "rain", "ship"]
medium_words = ["guitar", "jungle", "library", "mountain", "ocean","computer", "guitar", "garden", "puzzle", "mountain", "painting", "camera", "ocean", "butterfly", "castle"]
hard_words = ["xenophobia", "quantum", "syndicate", "zephyr", "xylophone","onomatopoeia", "chrysanthemum", "xylophone", "quizzical", "rhythm", "pharaoh", "czar", "juxtaposition", "pneumonia", "mnemonic"]

# Create the main window
window = tk.Tk()
window.title("Word Jumble Game")
window.geometry("400x300")

# Set background color
window.configure(bg="#FDFEFE")

# Create the label and entry widgets
label = tk.Label(window, text="Unscramble the letters to make a word:", font=("Arial", 12), bg="#FDFEFE")
label.pack()

jumbled_label = tk.Label(window, text="", font=("Arial", 20, "bold"), bg="#FDFEFE")
jumbled_label.pack()

entry = tk.Entry(window, font=("Arial", 14))
entry.pack()

# Bind the Enter key to the check_guess function
entry.bind("<Return>", check_guess)

button = tk.Button(window, text="OK", command=check_guess, font=("Arial", 12), bg="#1ABC9C", fg="#FDFEFE")
button.pack()

hint_button = tk.Button(window, text="Hint", command=give_hint, font=("Arial", 12), bg="#3498DB", fg="#FDFEFE")
hint_button.pack()

# Create a score label
score_label = tk.Label(window, text="Score: " + str(score), font=("Arial", 12), bg="#FDFEFE")
score_label.pack()

# Create a level label
level_label = tk.Label(window, text="Level: " + str(level), font=("Arial", 12), bg="#FDFEFE")
level_label.pack()

# Create a high score label
high_score_label = tk.Label(window, text="High Score: " + str(high_score), font=("Arial", 12), bg="#FDFEFE")
high_score_label.pack()

# Create a timer label
timer_label = tk.Label(window, text="Time: " + str(time_limit), font=("Arial", 12), bg="#FDFEFE")
timer_label.pack()

# Create a quit button
quit_button = tk.Button(window, text="Quit", command=quit_game, font=("Arial", 12), bg="#C0392B", fg="#FDFEFE")
quit_button.pack()

# Run the game
play_round()
start_timer()

# Run the main window event loop
window.mainloop()


