import tkinter as tk

def text_to_emoji(input_text):
    emoji_mapping = {
        "Pizza": "🍕",
        "Annoyed": "🙄",
        "Laughing": "😂",
        "Bored": "😑",
        "Shocked": "😱",
        "Crying": "😭",
        "Cool": "😎",
         "Ghost":"👻",
         "Ninja":"🐱‍👤",
         "Cat":"🐱",
         "Dog":"🐶",
         "Wolf":"🐺",
         "Motorcycle":"🏍",
         "Helicopter":"🚁",
         "Fire":"🔥",
         "Umbrella":"☔",
         "Star":"⭐",
         "Panda":"🐼",
         "Fox": "🦊",
         "Eye":"👀",
         "Bone":"🦴",
         "Chicken":"🐣",
    }

    output_text = input_text
    for emoji_text, emoji_code in emoji_mapping.items():
        output_text = output_text.replace(emoji_text, emoji_code)

    return output_text

def convert_to_emojis():
    input_text = input_entry.get()
    if not input_text:
        output_label.config(text="Please enter some text!")
        return

    try:
        output_text = text_to_emoji(input_text)
        output_label.config(text=output_text)
    except KeyError:
        output_label.config(text="No corresponding emoji found for the given text!")

root = tk.Tk()
root.title("Text to Emoji Converter")

input_entry = tk.Entry(root, width=40, font=("Helvetica", 16))
input_entry.pack(pady=20)

convert_button = tk.Button(root, text="Convert to Emojis", command=convert_to_emojis, font= ("Helvetica",14))
convert_button.pack()

output_label = tk.Label(root, text="", wraplength=300, justify="center", font=("Helvetica",18))
output_label.pack(pady=10)

root.mainloop()
