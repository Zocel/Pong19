__name__ = "Pong19-Zero"
__author__ = "LE COZ Yann"
__copyright__ = "Copyright 2019"
__version__ = "0.0.1"
__email__ = "yann.lecoz@ynov.com"

# Importation des librairies
from tkinter import *
import math
from time import *

# Déclaration des variables globales
# Fenêtres
endgameview = None
settingview = None
playview = None
menuview = None
pauseview = None
# Widgets
sz_arena = None
cr_arena = None
cr_rackets = None
cr_ball = None
spd_ball = None
# Déplacement de la balle et des raquettes
ball = None
h_speed_ball, v_speed_ball = 0, 0
speed_racket = 30
# Score
winpoints = None
left_score, right_score = 0, 0
display_right_score = None
display_left_score = None
# Couleur
color_background = None
color_foreground = None
color_rackets = None
color_ball = None
# Temps
start_time = 0
stop_time = 0
# Bonus
bonus = None
color_bonus = None


def open_endgame():
    global endgameview
    global left_score, right_score
    global start_time, stop_time

    # Définition des dimensions de la fenêtre "endgameview"
    endgame_width = 100
    half_endgame_width = endgame_width / 2
    endgame_height = 100
    half_endgame_height = endgame_height / 2

    # Construction de la fenêtre principale "endgameview"
    endgameview = Tk()
    endgameview.title("Fin de Partie")
    endgameicon = PhotoImage(file=".icones/endgameicon.png")
    endgameview.call("wm", "iconphoto", endgameview._w, endgameicon)
    # Empêchement de la redimensionner
    endgameview.resizable(width=False, height=False)
    # Création du canvas "fen_endgame"
    fen_endgame = Canvas(
        endgameview, width=endgame_width, height=endgame_height, bd=-1
    )

    # Création du label "Scores"
    Label(endgameview, text="Scores", font=("Staatliches", "40")).grid(
        row=1, column=2
    )
    # Création du label "Gagnant"
    Label(endgameview, text="Gagnant", font=("Staatliches", "20")).grid(
        row=2, column=1
    )
    # Création du label "Perdant"
    Label(endgameview, text="Perdant", font=("Staatliches", "20")).grid(
        row=2, column=3
    )
    # Affichage du joueur gagnant et du joueur perdant
    if left_score > right_score:
        Label(
            endgameview, text="Joueur Gauche", font=("Staatliches", "30")
        ).grid(row=3, column=1)
        Label(endgameview, text=left_score, font=("Staatliches", "30")).grid(
            row=4, column=1
        )
        Label(
            endgameview, text="Joueur Droit", font=("Staatliches", "30")
        ).grid(row=3, column=3)
        Label(endgameview, text=right_score, font=("Staatliches", "30")).grid(
            row=4, column=3
        )
        left_score = 0
        right_score = 0
    else:
        Label(
            endgameview, text="Joueur Droit", font=("Staatliches", "30")
        ).grid(row=3, column=1)
        Label(endgameview, text=right_score, font=("Staatliches", "30")).grid(
            row=4, column=1
        )
        Label(
            endgameview, text="Joueur Gauche", font=("Staatliches", "30")
        ).grid(row=3, column=3)
        Label(endgameview, text=left_score, font=("Staatliches", "30")).grid(
            row=4, column=3
        )
        left_score = 0
        right_score = 0

    # Création du label "Durée de la Partie"
    Label(
        endgameview, text="Durée de la Partie", font=("Staatliches", "20")
    ).grid(row=5, column=2)
    # Affichage du temps de la partie
    Label(
        endgameview,
        text=strftime("%H : %M : %S", gmtime(stop_time - start_time - 2)),
        font=("Staatliches", "30"),
    ).grid(row=6, column=2)

    def first_exit_endgame():
        """
        Fonction permettant la redirection vers l'écran de jeu
        à partir de la fenêtre de "Fin de Partie"
        """
        global endgameview

        # Fermeture de l'écran de Fin de partie
        endgameview.destroy()
        open_play()

    def second_exit_endgame():
        """
        Fonction permettant la redirection vers le menu principal
        à partir de la fenêtre de "Fin de Partie"
        """
        global endgameview

        # Fermeture de l'écran de Fin de partie
        endgameview.destroy()
        open_menu()

    # Création du bouton "Refaire une partie"
    Button(
        endgameview,
        text="Refaire une partie",
        activebackground="#22427C",
        activeforeground="#99CCFF",
        font=("Roboto", "11"),
        borderwidth=2,
        command=first_exit_endgame,
    ).grid(row=7, column=0)
    # Création du bouton "Aller au menu principal"
    Button(
        endgameview,
        text="Aller au menu principal",
        activebackground="#464856",
        activeforeground="white",
        font=("Roboto", "11"),
        borderwidth=2,
        command=second_exit_endgame,
    ).grid(row=7, column=4)

    # Lancement de la "boucle principale"
    endgameview.mainloop()


def open_setting():
    """
    Fonction gérant l'écran de configuration
    """
    global settingview, menuview
    global sz_arena, cr_arena, cr_rackets, cr_ball
    global spd_ball
    global winpoints

    # Fermeture du Menu principal
    menuview.destroy()

    # Définition des dimensions de la fenêtre "settingview"
    setting_width = 400
    setting_height = 600

    # Construction de la fenêtre principale "settingview"
    settingview = Tk()
    settingview.title("Configuration de la Partie")
    settingicon = PhotoImage(file=".icones/settingicon.png")
    settingview.call("wm", "iconphoto", settingview._w, settingicon)
    # Empêchement de la redimensionner
    settingview.resizable(width=False, height=False)
    # Création du canvas "fen_setting"
    fen_setting = Canvas(
        settingview, width=setting_width, height=setting_height, bd=-1
    )

    # Création de la rubrique "Arène"
    # Création du label "Arène"
    lbl_arena = Label(settingview, text="Arène", font=("Roboto", "11"))
    # Création du bonton de menu "Taille de l'Arène"
    mnb_sz_arena = Menubutton(
        settingview,
        activebackground="#464856",
        activeforeground="white",
        text="Taille de l'Arène",
        font=("Roboto", "10"),
        relief="raised",
    )
    # Création de la liste déroulante avec les trois configurations possibles
    mnb_sz_arena.mnu_arena = Menu(
        mnb_sz_arena,
        activebackground="#464856",
        activeforeground="white",
        font=("Roboto", "9"),
        tearoff=0,
    )
    mnb_sz_arena["menu"] = mnb_sz_arena.mnu_arena
    sz_arena = IntVar()
    mnb_sz_arena.mnu_arena.add_radiobutton(
        label="Entraînement", variable=sz_arena, value=1
    )
    mnb_sz_arena.mnu_arena.add_radiobutton(
        label="Basique", variable=sz_arena, value=0
    )
    mnb_sz_arena.mnu_arena.add_radiobutton(
        label="Tournoi", variable=sz_arena, value=2
    )
    # Création du bonton de menu "Couleur de l'Arène"
    mnb_cr_arena = Menubutton(
        settingview,
        activebackground="#464856",
        activeforeground="white",
        text="Couleur de l'Arène",
        font=("Roboto", "10"),
        relief="raised",
    )
    # Création de la liste déroulante avec les deux configurations possibles
    mnb_cr_arena.mnu_arena = Menu(
        mnb_cr_arena,
        activebackground="#464856",
        activeforeground="white",
        font=("Roboto", "9"),
        tearoff=0,
    )
    mnb_cr_arena["menu"] = mnb_cr_arena.mnu_arena
    cr_arena = IntVar()
    mnb_cr_arena.mnu_arena.add_radiobutton(
        label="Défaut", variable=cr_arena, value=0
    )
    mnb_cr_arena.mnu_arena.add_radiobutton(
        label="Négatif", variable=cr_arena, value=1
    )

    # Création du label "Nombre de points gagnants"
    lbl_winpoints = Label(
        settingview, text="Nombre de points gagnants", font=("Roboto", "10")
    )
    # Création du champ de texte pour le Nombre de points gagnants
    winpoints = IntVar()
    Entry(
        settingview,
        highlightbackground="#D5D5D6",
        highlightcolor="#464856",
        highlightthickness=3,
        insertontime=0,
        textvariable=winpoints,
        font=("Staatliches", "12"),
        justify="center",
        width=5,
    ).grid(row=4, column=1)

    # Création du label "Raquettes"
    lbl_rackets = Label(settingview, text="Raquettes", font=("Roboto", "11"))
    # Création du bonton de menu "Couleur des Raquettes"
    mnb_cr_rackets = Menubutton(
        settingview,
        activebackground="#464856",
        activeforeground="white",
        text="Couleur des Raquettes",
        font=("Roboto", "10"),
        direction="right",
        relief="raised",
    )
    # Création de la liste déroulante avec les quatres configurations possibles
    mnb_cr_rackets.mnu_rackets = Menu(
        mnb_cr_rackets,
        activebackground="#464856",
        activeforeground="white",
        font=("Roboto", "9"),
        tearoff=0,
    )
    mnb_cr_rackets["menu"] = mnb_cr_rackets.mnu_rackets
    cr_rackets = IntVar()
    mnb_cr_rackets.mnu_rackets.add_radiobutton(
        label="Défaut", variable=cr_rackets, value=0
    )
    mnb_cr_rackets.mnu_rackets.add_radiobutton(
        label="Saphir", variable=cr_rackets, value=1
    )
    mnb_cr_rackets.mnu_rackets.add_radiobutton(
        label="Émeraude", variable=cr_rackets, value=2
    )
    mnb_cr_rackets.mnu_rackets.add_radiobutton(
        label="Rubis", variable=cr_rackets, value=3
    )

    # Création de la rubrique "Balle"
    # Création du label "Balle"
    lbl_ball = Label(settingview, text="Balle", font=("Roboto", "11"))
    # Création du bonton de menu "Vitesse de la Balle"
    mnb_spd_ball = Menubutton(
        settingview,
        activebackground="#464856",
        activeforeground="white",
        text="Vitesse de la Balle",
        font=("Roboto", "10"),
        relief="raised",
    )
    # Création de la liste déroulante avec les trois configurations possibles
    mnb_spd_ball.mnu_ball = Menu(
        mnb_spd_ball,
        activebackground="#464856",
        activeforeground="white",
        font=("Roboto", "9"),
        tearoff=0,
    )
    mnb_spd_ball["menu"] = mnb_spd_ball.mnu_ball
    spd_ball = IntVar()
    mnb_spd_ball.mnu_ball.add_radiobutton(
        label="Lente", variable=spd_ball, value=1
    )
    mnb_spd_ball.mnu_ball.add_radiobutton(
        label="Nomale", variable=spd_ball, value=0
    )
    mnb_spd_ball.mnu_ball.add_radiobutton(
        label="Rapide", variable=spd_ball, value=2
    )

    # Création du bonton de menu "Couleur de la Balle"
    mnb_cr_ball = Menubutton(
        settingview,
        activebackground="#464856",
        activeforeground="white",
        text="Couleur de la Balle",
        font=("Roboto", "10"),
        relief="raised",
    )
    # Création de la liste déroulante avec les quatres configurations possibles
    mnb_cr_ball.mnu_ball = Menu(
        mnb_cr_ball,
        activebackground="#464856",
        activeforeground="white",
        font=("Roboto", "9"),
        tearoff=0,
    )
    mnb_cr_ball["menu"] = mnb_cr_ball.mnu_ball
    cr_ball = IntVar()
    mnb_cr_ball.mnu_ball.add_radiobutton(
        label="Défaut", variable=cr_ball, value=0
    )
    mnb_cr_ball.mnu_ball.add_radiobutton(
        label="Saphir", variable=cr_ball, value=1
    )
    mnb_cr_ball.mnu_ball.add_radiobutton(
        label="Émeraude", variable=cr_ball, value=2
    )
    mnb_cr_ball.mnu_ball.add_radiobutton(
        label="Rubis", variable=cr_ball, value=3
    )

    def exit_setting():
        """
        Fonction permettant d'aller à l'écran de jeu à partir de la fenêtre
        "Configuration de la partie"
        """
        global settingview

        # Fermeture de l'écran de Configuration de la partie
        settingview.destroy()
        open_play()

    # Création du bouton "Configurer la partie"
    Button(
        settingview,
        text="Configurer la partie",
        activebackground="#11692A",
        activeforeground="#CCFFCC",
        font=("Roboto", "11"),
        borderwidth=2,
        command=exit_setting,
    ).grid(row=9, column=1)

    # Placement des widgets
    lbl_arena.grid(row=1, column=1)
    mnb_sz_arena.grid(row=2, column=0)
    mnb_cr_arena.grid(row=2, column=2)
    lbl_winpoints.grid(row=3, column=1)
    lbl_rackets.grid(row=5, column=1)
    mnb_cr_rackets.grid(row=6, column=1)
    lbl_ball.grid(row=7, column=1)
    mnb_spd_ball.grid(row=8, column=0)
    mnb_cr_ball.grid(row=8, column=2)

    # Lancement de la "boucle principale"
    settingview.mainloop()


def open_play():
    """
    Fonction gérant l'écran de jeu
    """
    global settingview, playview, sz_arena
    global cr_arena, cr_rackets, cr_ball
    global color_background, color_foreground, color_rackets, color_ball
    global ball, h_speed_ball, v_speed_ball
    global display_left_score, display_right_score, left_score, right_score
    global start_time

    # Définition des dimensions de la fenêtre "playview"
    if sz_arena.get() == 0:
        play_width = 654
        play_height = 400
    elif sz_arena.get() == 1:
        play_width = 458
        play_height = 280
    elif sz_arena.get() == 2:
        play_width = 851
        play_height = 520
    half_play_width = play_width / 2
    half_play_height = play_height / 2
    # Définition des dimensions des Buts
    left_width_goal = 25 * play_width / 327
    right_width_goal = play_width - left_width_goal
    middle_play_width = (half_play_width - left_width_goal) / 2
    # Définition des variables de positionnement de la balle
    primary_hposition_ball = half_play_width - 6
    primary_vposition_ball = half_play_height - 6
    secondary_hposition_ball = half_play_width + 6
    secondary_vposition_ball = half_play_height + 6
    # Définition des variables des raquettes
    min_racket_height = half_play_height - 40
    max_racket_height = half_play_height + 40

    # Définition des couleurs de l'arrière-plan et du premier-plan
    if cr_arena.get() == 0:
        color_background = "black"
        color_foreground = "white"
    elif cr_arena.get() == 1:
        color_background = "white"
        color_foreground = "black"

    # Définition de la couleur des raquettes
    if cr_rackets.get() == 0:
        color_rackets = color_foreground
    elif cr_rackets.get() == 1:
        color_rackets = "#22427C"
    elif cr_rackets.get() == 2:
        color_rackets = "#11692A"
    elif cr_rackets.get() == 3:
        color_rackets = "#800000"

    # Définition de la vitesse de la balle
    if spd_ball.get() == 0:
        h_speed_ball = 1.3
        v_speed_ball = 1.3
    elif spd_ball.get() == 1:
        h_speed_ball = 0.7
        v_speed_ball = 0.7
    elif spd_ball.get() == 2:
        h_speed_ball = 1.9
        v_speed_ball = 1.9

    # Définition de la couleur de la balle
    if cr_ball.get() == 0:
        color_ball = color_foreground
    elif cr_ball.get() == 1:
        color_ball = "#22427C"
    elif cr_ball.get() == 2:
        color_ball = "#11692A"
    elif cr_ball.get() == 3:
        color_ball = "#800000"

    start_time = time()  # On récupère le temps de départ

    # Mise en mouvement de la balle

    def move_ball():
        """
        Fonction permettant à la balle de se déplacer
        """
        global ball, h_speed_ball, v_speed_ball
        global display_left_score, display_right_score, left_score, right_score, winpoints
        global stop_time

        # Si la valeur en primary_vposition est inférieur à 6
        # OU la valeur en secondary_vposition est supérieur à la play_height - 6
        if (
            fen_play.coords(ball)[1] < 6
            or fen_play.coords(ball)[3] > play_height - 6
        ):
            v_speed_ball *= -1

        # Collision de la balle avec les raquettes
        if (
            fen_play.coords(ball)[0] < fen_play.coords(left_racket)[2]
            and fen_play.coords(ball)[3] > fen_play.coords(left_racket)[1]
            and fen_play.coords(ball)[1] < fen_play.coords(left_racket)[3]
        ) or (
            fen_play.coords(ball)[2] > fen_play.coords(right_racket)[0]
            and fen_play.coords(ball)[3] > fen_play.coords(right_racket)[1]
            and fen_play.coords(ball)[1] < fen_play.coords(right_racket)[3]
        ):
            h_speed_ball *= -1

        fen_play.move(ball, h_speed_ball, v_speed_ball)

        # Traitement des scores
        if winpoints.get() != math.fabs(left_score - right_score):
            if fen_play.coords(ball)[0] < left_width_goal - 1:
                fen_play.delete(display_right_score)
                right_score += 1
                display_right_score = fen_play.create_text(
                    half_play_width + middle_play_width,
                    half_play_height,
                    text=right_score,
                    font=("Staatliches", "43"),
                    fill=color_foreground,
                )
                fen_play.delete(ball)
                ball = fen_play.create_oval(
                    primary_hposition_ball,
                    primary_vposition_ball,
                    secondary_hposition_ball,
                    secondary_vposition_ball,
                    fill=color_ball,
                )
                fen_play.after(550)  # Temporisation de 550ms
            elif fen_play.coords(ball)[2] > right_width_goal + 1:
                fen_play.delete(display_left_score)
                left_score += 1
                display_left_score = fen_play.create_text(
                    half_play_width - middle_play_width,
                    half_play_height,
                    text=left_score,
                    font=("Staatliches", "43"),
                    fill=color_foreground,
                )
                fen_play.delete(ball)
                ball = fen_play.create_oval(
                    primary_hposition_ball,
                    primary_vposition_ball,
                    secondary_hposition_ball,
                    secondary_vposition_ball,
                    fill=color_ball,
                )
                fen_play.after(550)  # Temporisation de 550ms
        else:
            # Fermeture de l'écran Partie de jeu
            playview.destroy()
            stop_time = time()  # On récupère le temps de fin
            # Overture de la fenêtre des Scores
            open_endgame()

        fen_play.after(10, move_ball)

    # Mise en mouvement des raquettes

    def move_racket(event):
        """
        Fonction permettant de bouger les raquettes
        """
        global speed_racket

        # Déclaration de la variable "key"
        key = event.keysym

        # Déplacement de la raquette de gauche
        if fen_play.coords(left_racket)[1] <= 10:
            if key == "f" or key == "F":
                fen_play.move(left_racket, 0, speed_racket)
        elif fen_play.coords(left_racket)[3] >= play_height - 10:
            if key == "r" or key == "R":
                fen_play.move(left_racket, 0, -speed_racket)
        else:
            if key == "r" or key == "R":
                fen_play.move(left_racket, 0, -speed_racket)
            if key == "f" or key == "F":
                fen_play.move(left_racket, 0, speed_racket)
        # Déplacement de la raquette de droite
        if fen_play.coords(right_racket)[1] <= 10:
            if key == "Down":
                fen_play.move(right_racket, 0, speed_racket)
        elif fen_play.coords(right_racket)[3] >= play_height - 10:
            if key == "Up":
                fen_play.move(right_racket, 0, -speed_racket)
        else:
            if key == "Up":
                fen_play.move(right_racket, 0, -speed_racket)
            if key == "Down":
                fen_play.move(right_racket, 0, speed_racket)

    # Construction de la fenêtre principale "playview"
    playview = Tk()
    playview.title("Partie de jeu")
    playicon = PhotoImage(file=".icones/playicon.png")
    playview.call("wm", "iconphoto", playview._w, playicon)
    # Empêchement de la redimensionner
    playview.resizable(width=False, height=False)

    # Création du Canvas "fen_play"
    fen_play = Canvas(
        playview,
        width=play_width,
        height=play_height,
        borderwidth=0,
        background=color_background,
    )
    fen_play.pack()

    # Création de la ligne du haut
    fen_play.create_line(
        0, 0, play_width + 1, 0, fill=color_foreground, width=10
    )
    # Création de la ligne du bas
    fen_play.create_line(
        0,
        play_height,
        play_width + 1,
        play_height,
        fill=color_foreground,
        width=10,
    )

    # Séparation de la fenêtre en deux
    fen_play.create_line(
        half_play_width,
        10,
        half_play_width,
        play_height - 10,
        fill=color_foreground,
        dash=(20, 10),
        width=4,
    )
    # Démarcation des Zones de Buts
    fen_play.create_line(
        left_width_goal,
        10,
        left_width_goal,
        play_height - 10,
        fill=color_foreground,
        dash=(6, 6),
        width=2,
    )
    fen_play.create_line(
        right_width_goal,
        10,
        right_width_goal,
        play_height - 10,
        fill=color_foreground,
        dash=(6, 6),
        width=2,
    )
    # Création des raquettes
    left_racket = fen_play.create_line(
        left_width_goal,
        min_racket_height,
        left_width_goal,
        max_racket_height,
        fill=color_rackets,
        width=6,
    )
    right_racket = fen_play.create_line(
        right_width_goal,
        min_racket_height,
        right_width_goal,
        max_racket_height,
        fill=color_rackets,
        width=6,
    )
    # Création de la balle
    ball = fen_play.create_oval(
        primary_hposition_ball,
        primary_vposition_ball,
        secondary_hposition_ball,
        secondary_vposition_ball,
        fill=color_ball,
    )

    # Affichage des scores en début de partie
    display_left_score = fen_play.create_text(
        half_play_width - middle_play_width,
        half_play_height,
        text=left_score,
        font=("Staatliches", "43"),
        fill=color_foreground,
    )
    display_right_score = fen_play.create_text(
        half_play_width + middle_play_width,
        half_play_height,
        text=right_score,
        font=("Staatliches", "43"),
        fill=color_foreground,
    )

    def pause_play(event):
        """
        Fonction permettant de mettre en pause une partie de jeu
        et d'ouvrir l'écran "Partie en pause"
        """
        global pauseview
        global h_speed_ball, v_speed_ball
        global speed_racket

        # Définition des dimensions de la fenêtre "endgameview"
        pause_width = 100
        pause_height = 100

        # Mise en pause de la balle et des raquettes
        h_speed_ball, v_speed_ball = 0, 0
        speed_racket = 0
        move_racket(event)

        # Affichage de l'écran de pause
        pauseview = Toplevel()
        pauseview.title("Partie actuellement en pause")
        pauseview.transient(playview)
        # Empêchement de la redimensionner
        pauseview.resizable(width=False, height=False)
        # Création du canvas "fen_pause"
        fen_pause = Canvas(
            pauseview, width=pause_width, height=pause_height, bd=-1
        )

        def first_exit_pause():
            """
            Fonction permettant la redirection vers l'écran de jeu
            et la remise en mouvement de la balle
            """
            global pauseview
            global h_speed_ball, v_speed_ball
            global speed_racket

            # Fermeture de l'écran de Fin de partie
            pauseview.destroy()

            # Définition de la vitesse de la balle
            if spd_ball.get() == 0:
                h_speed_ball = 1.3
                v_speed_ball = 1.3
            elif spd_ball.get() == 1:
                h_speed_ball = 0.7
                v_speed_ball = 0.7
            elif spd_ball.get() == 2:
                h_speed_ball = 1.9
                v_speed_ball = 1.9
            playview.update()
            speed_racket = 30
            move_racket(event)

        def second_exit_pause():
            """
            Fonction permettant de mettre fin à l'application
            """
            global playview, pauseview

            # Fermeture de l'écran de Fin de partie et de la Partie de jeu
            pauseview.destroy()
            playview.destroy()

        # Création du label "Voulez-vous reprendre cette partie ?"
        Label(
            pauseview,
            text="Voulez-vous reprendre cette partie ?",
            font=("Roboto", "12"),
        ).grid(row=0, column=2)
        # Création des boutons "Oui" et "Non"
        Button(
            pauseview,
            text="Oui",
            activebackground="#22427C",
            activeforeground="#99CCFF",
            borderwidth=2,
            command=first_exit_pause,
            font=("Roboto", "11"),
        ).grid(row=1, column=1)
        Button(
            pauseview,
            text="Non",
            activebackground="#800000",
            activeforeground="#FFCCCC",
            borderwidth=2,
            command=second_exit_pause,
            font=("Roboto", "11"),
        ).grid(row=1, column=3)

    playview.bind("<Control-p>", pause_play)
    playview.bind("<Key>", move_racket)

    move_ball()

    # Lancement de la "boucle principale"
    playview.mainloop()


def open_menu():
    """
    Fonction gérant l'écran de menu
    """
    global menuview

    # Définition des dimensions de la fenêtre "menuview"
    menu_width = 250
    half_menu_width = menu_width / 2
    menu_height = 100

    # Construction de la fenêtre principale "menuview"
    menuview = Tk()
    menuview.title("Menu principal")
    menuicon = PhotoImage(file=".icones/menuicon.png")
    menuview.call("wm", "iconphoto", menuview._w, menuicon)
    # Empêchement de la redimensionner
    menuview.resizable(width=False, height=False)
    # Création du canvas "fen_menu"
    fen_menu = Canvas(menuview, width=menu_width, height=menu_height, bd=-1)

    # Création du bouton "Faire une partie"
    btn_play = Button(
        menuview,
        text="Faire une partie",
        activebackground="#22427C",
        activeforeground="#99CCFF",
        font=("Roboto", "11"),
        borderwidth=2,
        command=open_setting,
    )
    # Création du bouton "Quitter"
    btn_exit = Button(
        menuview,
        text="Quitter",
        activebackground="#800000",
        activeforeground="#FFCCCC",
        font=("Roboto", "11"),
        borderwidth=2,
        command=menuview.destroy,
    )
    # Création du label "Y. LE COZ  2019"
    fen_menu.create_text(
        half_menu_width,
        menu_height - 5,
        text=strftime("Y. LE COZ  %Y", gmtime()),
        font=("DINOT", "9"),
        fill="#464856",
    )

    # Placement des widgets
    fen_menu.grid(row=0, column=2, columnspan=2, padx=10, pady=5)
    btn_play.grid(row=0, column=2)
    btn_exit.grid(row=0, column=3)

    # Lancement de la "boucle principale"
    menuview.mainloop()


# Appel de la fonction "open_menu" pour ouvrir le Menu Principal
open_menu()
