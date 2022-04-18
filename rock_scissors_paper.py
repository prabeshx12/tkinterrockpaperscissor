import random
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x650')
root.title('Game')

r = IntVar()


def get_user_image():
    global value
    value = int(r.get())
    if value == 0:
        user_choice.config(image=image_list[value])
    elif value == 1:
        user_choice.config(image=image_list[value])
    else:
        user_choice.config(image=image_list[value])
    random_choice.config(image=white_image)
    winner_label.config(text="")


def start_game():
    random_value = random.randint(0, 2)
    random_choice.config(image=image_list[random_value])
    if random_value == value:
        winner_label.config(text="The game is tied!!")
    elif value == 0 and (random_value == 1):
        winner_label.config(text="The Computer Won The Game!!")
    elif random_value == 0 and (value == 1):
        winner_label.config(text="You Won The Game!!")
    elif value == 0 and random_value == 2:
        winner_label.config(text="You Won The Game!!")
    elif value == 2 and random_value == 0:
        winner_label.config(text="The Computer Won The Game!!")
    elif value == 1 and random_value == 2:
        winner_label.config(text="The Computer Won The Game!!")
    elif random_value == 1 and value == 2:
        winner_label.config(text="You Won The Game!!")


# window for welcome screen
welcome_screen_label = Label(root, text="Welcome to Rock Scissor Paper Game", bg="dodgerblue", height=2, width=40, font="TimesNewRoman, 16").pack(padx=10, pady=10)


user_choice_label = Label(root, text="Choose your choice", font="TimesNewRoman, 14", height=1, width=20, bg="lightgreen").pack(padx=10, pady=10)


# resizing images according to need
image_one = Image.open('images/rock_cc.png')
resized_one = image_one.resize((100, 100), Image.ANTIALIAS)
rock_image = ImageTk.PhotoImage(resized_one)

image_two = Image.open('images/paper_cc.png')
resized_two = image_two.resize((100, 100), Image.ANTIALIAS)
paper_image = ImageTk.PhotoImage(resized_two)

image_three = Image.open('images/scissor_cc.png')
resized_three = image_three.resize((100, 100), Image.ANTIALIAS)
scissor_image = ImageTk.PhotoImage(resized_three)

image_four = Image.open('images/white.png')
resized_four = image_four.resize((100, 100), Image.ANTIALIAS)
white_image = ImageTk.PhotoImage(resized_four)


# defining the list of images
image_list = [rock_image, paper_image, scissor_image]


# background for the images
background_image_frame = Frame(root, bg="lightpink")
background_image_frame.pack(padx=10, pady=10)


# rock label
frame_one = Label(background_image_frame, height=100, width=100, image=rock_image)
frame_one.pack(padx=10, pady=10, side=LEFT)


# paper label
frame_two = Label(background_image_frame, height=100, width=100, image=paper_image)
frame_two.pack(padx=10, pady=10, side=LEFT)


# scissor label
frame_three = Label(background_image_frame, height=100, width=100, image=scissor_image)
frame_three.pack(padx=10, pady=10, side=RIGHT)


# background for radio buttons
background_radio = Frame(root, bg="lightseagreen")
background_radio.pack()


# radio rock
rock_radio = Radiobutton(background_radio, variable=r, value=0, text="ROCK", font="TimesNewRoman, 10")
rock_radio.pack(padx=25, pady=10, side=LEFT)


# radio paper
paper_radio = Radiobutton(background_radio, variable=r, value=1, text="PAPER", font="TimesNewRoman, 10")
paper_radio.pack(padx=25, pady=10, side=LEFT)


# radio scissor
scissor_radio = Radiobutton(background_radio, variable=r, value=2, text="SCISSOR", font="TimesNewRoman, 10")
scissor_radio.pack(padx=25, pady=10, side=RIGHT)


# defining button
done_button = Button(root, font="TimesNewRoman, 12", text="OK", padx=20, bg="lightgrey", command=get_user_image)
done_button.pack(pady=10)

# defining the choices
background_choice_frame = Frame(root, bg="lightgreen")
background_choice_frame.pack(pady=10)

label_one = Label(background_choice_frame, text="Your Choice", font="TimesNewRoman, 11")
label_one.pack(padx=15, pady=1, side=LEFT)

label_two = Label(background_choice_frame, text="Computer Choice", font="TimesNewRoman, 11")
label_two.pack(padx=15, pady=1, side=RIGHT)


# game show host
background_game = Frame(root, bg="yellowgreen", height=180, width=600)
background_game.pack(padx=5, pady=5)

user_choice = Label(background_game, bg="white")
user_choice.pack(padx=20, pady=10, side=LEFT)

random_choice = Label(background_game, bg="white")
random_choice.pack(padx=20, pady=10, side=RIGHT)


# winner declaration
winner_label = Label(root, text="", width=40, font="TimesNewRoman, 12", bg="lightseagreen")
winner_label.pack(padx=10, pady=2)


# game starting
start_button = Button(root, text="START", font="TimesNewRoman, 12", bg="lightgrey", padx=10, command=start_game)
start_button.pack(pady=10)


if __name__ == '__main__':
    root.mainloop()