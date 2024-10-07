import tkinter as tk
from tkinter import Label
import qrcode
import random
import re

def load_words_from_file(filename):
    
    try:
        with open(filename, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []

def generate_random_word(words):
    
    random_word = random.choice(words)
    cleaned_word = re.sub(r'\s*\(.*?\)', '', random_word).strip()
    
    return cleaned_word

def generate_random_sentence(words, num_words=5):
    
    selected_words = [generate_random_word(words) for _ in range(num_words)]
    sentence = ' '.join(selected_words) + '.'
    return sentence.capitalize()

def create_google_search_url(sentence):
    
    return f"https://www.google.com/search?q={sentence.replace(' ', '+')}"

def create_qr_code(url):
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

def show_qr_code_window(url):
    
    root = tk.Tk()
    root.title("QR Code Generator")
    label = Label(root, text="Scan it!")
    label.pack(pady=10)
    qr_image = tk.PhotoImage(file="qr_code.png")
    qr_label = Label(root, image=qr_image)
    qr_label.pack(pady=10)
    qr_label.image = qr_image
    root.mainloop()

def main():
    words = load_words_from_file('dictionary.txt')
    random_sentence = generate_random_sentence(words, num_words=5)
    print(f"Generated Sentence: {random_sentence}")
    search_url = create_google_search_url(random_sentence)
    create_qr_code(search_url)
    show_qr_code_window(search_url)

if __name__ == "__main__":
    main()
