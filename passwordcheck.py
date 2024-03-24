
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import re
def assess_password_strength(password):
    weights = {
        'length': 3,
        'uppercase': 2,
        'lowercase': 2,
        'digit': 2,
        'special_char': 3,
        'not_common_word': 5,
        'consecutive_chars': -2
    }
    total_score = 0
    if len(password) > 12:
        total_score += weights['length']
    if any(char.isupper() for char in password):
        total_score += weights['uppercase']
    if any(char.islower() for char in password):
        total_score += weights['lowercase']
    if any(char.isdigit() for char in password):
        total_score += weights['digit']
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        total_score += weights['special_char']
    if password.lower() not in ["password", "123456", "qwerty", "letmein", "monkey", "password1"]:
        total_score += weights['not_common_word']
    if re.search(r'(.)\1', password):
        total_score += weights['consecutive_chars']
    if total_score >= 20:
        strength = "Highest"
    elif total_score >= 15:
        strength = "High"
    elif total_score >= 10:
        strength = "Medium"
    elif total_score >= 5:
        strength = "Low"
    else:
        strength = "Lowest"
    return strength, total_score
def assess_passwords():
    output_text.delete(1.0, tk.END)  # Clear previous output
    passwords = input_text.get(1.0, tk.END).splitlines()
    for password in passwords:
        strength, total_score = assess_password_strength(password)
        output_text.insert(tk.END, f"Password: {password.strip()}\n")
        output_text.insert(tk.END, f"Strength: {strength}\n")
        output_text.insert(tk.END, f"Total Score: {total_score}\n\n")

def clear_text():
    input_text.delete(1.0, tk.END)
    output_text.delete(1.0, tk.END)
root = tk.Tk()
root.title("Password Strength Assessment")
input_label = ttk.Label(root, text="Enter passwords:")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, width=40, height=10)
input_text.pack()
assess_button = ttk.Button(root, text="Check Passwords", command=assess_passwords)
assess_button.pack()
clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.pack()
output_label = ttk.Label(root, text="Assessment Results:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, width=40, height=10)
output_text.pack()
root.mainloop()
