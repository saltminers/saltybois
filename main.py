# IMPORTS
import sys
import csv
import pygame
import random
import tkinter as tk
from tkinter import ttk

# Made global for easy access
global xQuestion, CE_msg

xQuestion = ("Are you ok?", "Woah there partner", "Easy...", "Is this a good roll?", "Woah...",
           "Crying is the best option", "Are you sure you're ok?",
           "I'm not gonna say anything but...", "...")
CE_msg = ("It's a CE bro...", "You wouldn't like it anyway")

# Pygame Initialization
pygame.init()
clock = pygame.time.Clock()

# Screen dimensions
d_width = 1024
d_height = 576

# Load assets
Summon_main_menu = pygame.image.load('assets/Story_Summon.png')
screen = pygame.display.set_mode((d_width, d_height))
bg_sound = pygame.mixer.Sound('assets/FGObg.mp3')

# Extra step of making the image assets smaller
Summon_main_menu = pygame.transform.scale(Summon_main_menu, (1024, 576))

# Play bg sound
bg_sound.play()

#   Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        (x, y) = pygame.mouse.get_pos()
        #        print(x, y)

# If clicking on Summon 1x
        if 258 < x < 462 and 404 < y < 481 and event.type == pygame.MOUSEBUTTONDOWN:
            servant_select = servant_randomizer()
            y = search_Servant(servant_select)

            if servant_select is None:
                CE = random.choice(CE_msg)
                DisplaySummon(CE)

            else:
                print(y)
                DisplaySummon(y)

# If clicking on Summon 10x
        if 560 < x < 762 and 406 < y < 481 and event.type == pygame.MOUSEBUTTONDOWN:
            pass

# If clicking on Exit
        if 31 < x < 140 and 4 < y < 61 and event.type == pygame.MOUSEBUTTONDOWN:
            print("Exit")
            sys.exit()

        else:
            pass

# Screen update and frame rates
    screen.blit(Summon_main_menu, (0, 0))
    pygame.display.update()
    clock.tick(30)

# Randomizes summon according to weight
    def servant_randomizer() -> str:

        # Weights
        servant_Weight = [1, 3, 40]
        ce_Weight = [4, 12, 40]

        # Values
        summon_Type = ["Servant", "Craft Essence"]
        Rarity = ["SSR", "SR", "R"]  # For Servants and CEs
        ServantList_SSR = (
            'sv1', 'sv2', 'sv3', 'sv4', 'sv5', 'sv6', 'sv7', 'sv8', 'sv9', 'sv10', 'sv11', 'sv12', 'sv13',
            'sv14', 'sv15', 'sv16')

        ServantList_SR = (
            'sv17', 'sv18', 'sv19', 'sv20', 'sv21', 'sv22', 'sv23', 'sv24', 'sv25', 'sv26', 'sv27', 'sv28',
            'sv29', 'sv30', 'sv31', 'sv32', 'sv33', 'sv34', 'sv35', 'sv36', 'sv37', 'sv38', 'sv39', 'sv40',
            'sv41', 'sv42')

        ServantList_R = (
            'sv43', 'sv44', 'sv45', 'sv46', 'sv47', 'sv48', 'sv49', 'sv50', 'sv51', 'sv52', 'sv53', 'sv54',
            'sv55', 'sv56', 'sv57', 'sv58', 'sv59', 'sv60', 'sv61', 'sv62', 'sv63', 'sv64', 'sv65', 'sv66',
            'sv67', 'sv68', 'sv69', 'sv70', 'sv71', 'sv72', 'sv73')

# Assigns whether CE or Servant
        summon_choice = random.choices(summon_Type, (44, 56))

# Assigns Rarity regardless if CE or not
        rarity_Rng = "".join(random.choices(Rarity, ce_Weight))

# Assigns servant depending on rarity and weight
        if "".join(summon_choice) == summon_Type[0]:
            rarity_Rng = "".join(random.choices(Rarity, servant_Weight))

            if rarity_Rng == "SSR":
                Serv_sv = random.choices(ServantList_SSR)
                return "".join(Serv_sv)

            if rarity_Rng == "SR":
                Serv_sv = random.choices(ServantList_SR)
                return "".join(Serv_sv)

            else:
                Serv_sv = random.choices(ServantList_R)
                return "".join(Serv_sv)

        else:
            return None

# Searches for servant in csv file
    def search_Servant(codename):
        with open("assets/Servant_List.csv") as sl:
            reader = csv.reader(sl, delimiter=',')
            for line in reader:
                if line[0] == codename:
                    return line[2], line[1]

                else:
                    None

# Creates a Dialog Box
    def DisplaySummon(value):
        pp = tk.Tk()
        screen_width = pp.winfo_screenwidth()
        screen_height = pp.winfo_screenheight()

        width = 250
        height = 80

#   Centers window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        pp.geometry('%dx%d+%d+%d' % (width, height, x, y))

        pp.wm_title("Summon")

        x_qs = random.choice(xQuestion)

        label = ttk.Label(pp, text=value)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(pp, text=x_qs, command=pp.destroy)
        B1.pack()
        pp.mainloop()
