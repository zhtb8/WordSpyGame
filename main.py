import tkinter as tk
from tkinter import messagebox
import random

class ImpostorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Impostor Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.players = []
        self.impostor = None
        self.word = None
        self.player_index = 0
        self.scores = {}
        
        self.num_players = 0
        
        self.num_players_screen()

    def num_players_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter Number of Players", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        
        self.num_players_entry = tk.Entry(self.root, font=("Arial", 14))
        self.num_players_entry.pack(pady=10)
        
        tk.Button(self.root, text="Next", command=self.get_num_players, font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)

    def get_num_players(self):
        try:
            self.num_players = int(self.num_players_entry.get())
            if self.num_players < 3:
                messagebox.showerror("Error", "At least 3 players required")
            else:
                self.player_names_screen()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def player_names_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter Player Names", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        
        self.entry_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.entry_frame.pack()
        
        self.entries = []
        for i in range(self.num_players):
            entry = tk.Entry(self.entry_frame, font=("Arial", 14))
            entry.pack(pady=5)
            self.entries.append(entry)
        
        tk.Button(self.root, text="Start Game", command=self.start_game, font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=20)

    def start_game(self):
        self.players = [entry.get() for entry in self.entries if entry.get()]
        if len(self.players) < self.num_players:
            messagebox.showerror("Error", "Please enter all player names")
            return
        
        self.impostor = random.choice(self.players)
        self.word = random.choice(["apple", "banana", "grape", "orange"])
        for player in self.players:
            if player not in self.scores:
                self.scores[player] = 0
        
        self.player_index = 0
        self.show_role()

    def show_role(self):
        self.clear_screen()
        
        player = self.players[self.player_index]
        if player == self.impostor:
            role_text = "You are the Impostor!"
        else:
            role_text = f"The word is: {self.word}"
        
        tk.Label(self.root, text=f"{player}'s turn", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        tk.Button(self.root, text="Show Role", command=lambda: self.show_role_message(role_text), font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=20)

    def show_role_message(self, message):
        messagebox.showinfo("Your Role", message)
        self.player_index += 1
        
        if self.player_index < len(self.players):
            self.show_role()
        else:
            self.playing_screen()

    def playing_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Playing...", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        
        tk.Button(self.root, text="Impostor Won", command=lambda: self.end_turn(impostor_won=True), font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Impostor Lost", command=lambda: self.end_turn(impostor_won=False), font=("Arial", 14), bg="#f44336", fg="white").pack(pady=10)

    def end_turn(self, impostor_won):
        self.clear_screen()
        
        if impostor_won:
            self.scores[self.impostor] += 1
            result_text = "Impostor Won!"
        else:
            for player in self.players:
                if player != self.impostor:
                    self.scores[player] += 1
            result_text = "Impostor Lost!"
        
        tk.Label(self.root, text=f"Round Over! {result_text}", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        
        score_text = "\n".join(f"{player}: {score} wins" for player, score in self.scores.items())
        tk.Label(self.root, text=score_text, font=("Arial", 14), bg="#f0f0f0").pack(pady=20)
        
        tk.Button(self.root, text="New Round", command=self.num_players_screen, font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit, font=("Arial", 14), bg="#f44336", fg="white").pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
game = ImpostorGame(root)
root.mainloop()
