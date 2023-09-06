import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle

from sys import exit
from functions import *
from simulator_engine import *
from solver_engine import *

from button import *

pygame.init()
SCREEN = WIDTH, HEIGHT = 1200, 660

# pygame variables
info = pygame.display.Info()
width = info.current_w
height = info.current_h

win = pygame.display.set_mode(SCREEN)

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont("verdana", 12)


# general variables
currentMenu = "Menu"  # Menu, Solver, Simulator

# define fonts
menuFont = pygame.font.SysFont("arialblack", 40)
smallFont = pygame.font.SysFont("arialblack", 18)

# define colours
TEXT_COL = (200, 200, 200)

# events
custom_events = []
SimFire_Click = pygame.event.Event(pygame.USEREVENT + 1)
Remove_Click = pygame.event.Event(pygame.USEREVENT + 2)
custom_events.extend([SimFire_Click, Remove_Click])


# toggle
streak_toggle = Toggle(win, 740, 25, 50, 20)

# buttons
buttonSolver = Button("Solver", 600, 120, (300, 220), 5, menuFont)
buttonSimulator = Button("Simulator", 600, 120, (300, 400), 5, menuFont)
buttonSimBack = Button("X", 40, 40, (10, 15), 5, smallFont, color="#ff0000")
buttonSimFire = Button(
    "Fire", 185, 30, (975, 110), 5, smallFont, color="#ff0000", event=SimFire_Click
)
buttonRemove = Button(
    "Remove", 185, 30, (975, 150), 5, smallFont, color="#eb7d34", event=Remove_Click
)
buttonSolve = Button("SOLVE", 210, 80, (710, 530), 5, menuFont, color="#DC143C")
buttonClear = Button("CLEAR", 210, 80, (960, 530), 5, menuFont, color=GREY)

# sliders
speed_slider = Slider(win, 980, 75, 175, 15, min=45, max=150, step=1)
speed_output = TextBox(
    win,
    932,
    73,
    30,
    22,
    fontSize=21,
    borderThickness=0,
    textColour=WHITE,
    radius=4,
    colour=(52, 78, 91),
)

angle_slider = Slider(win, 980, 30, 175, 15, min=1, max=89, step=1)
angle_output = TextBox(
    win,
    932,
    28,
    30,
    22,
    fontSize=21,
    borderThickness=0,
    textColour=WHITE,
    radius=4,
    colour=(
        52,
        78,
        91,
    ),
)

# Solver UI


title_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Enter the values you know:", True, WHITE
)
insufficent_text = pygame.font.SysFont("Calibri", 30, bold=True).render(
    "Insufficient information provided", True, (220, 20, 60)
)
impossible_text = pygame.font.SysFont("Calibri", 30, bold=True).render(
    "Impossible trajectory: check values", True, (220, 20, 60)
)
# rang1
vitesse_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Velocity (m/s): ", True, WHITE
)

textbox_speed = TextBox(
    win,
    340,
    100,
    200,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE,
    radius=10,
    borderThickness=5,
)

angle_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Angle (°): ", True, WHITE
)

textbox_angle = TextBox(
    win,
    820,
    100,
    200,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE, 
    radius=10,
    borderThickness=5,
)
vitesse_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Velocity (m/s): ", True, WHITE
)

# rang2
vitesse_verticale_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Vertical Velocity (m/s): ", True, WHITE
)

textbox_vertical_speed = TextBox(
    win,
    490,
    240,
    200,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE, 
    radius=10,
    borderThickness=5,
)

tf_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Air time (s): ", True, WHITE
)

textbox_tf = TextBox(
    win,
    980,
    230,
    200,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE, 
    radius=10,
    borderThickness=5,
)

# rang3
vitesse_horizontal_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Horizontal Velocity (m/s): ", True, WHITE
)

textbox_horizontal_speed = TextBox(
    win,
    540,
    380,
    200,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE, 
    radius=10,
    borderThickness=5,
)

range_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Range (m): ", True, WHITE
)

textbox_range = TextBox(
    win,
    990,
    380,
    190,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE, 
    radius=10,
    borderThickness=5,
)

# rang4
max_height_text = pygame.font.SysFont("Calibri", 40, bold=True).render(
    "Maximum Height (m): ", True, WHITE
)

textbox_max_height = TextBox(
    win,
    470,
    520,
    200,
    90,
    fontSize=65,
    colour=GREY,
    borderColour=(220, 20, 60),
    textColour=WHITE, 
    radius=10,
    borderThickness=5,
)


def renderTexts():
    win.blit(title_text, (336, 30))
    win.blit(vitesse_text, (50, 120))
    win.blit(angle_text, (610, 120))
    win.blit(vitesse_verticale_text, (50, 260))
    win.blit(tf_text, (730, 260))
    win.blit(vitesse_horizontal_text, (50, 400))
    win.blit(range_text, (770, 400))
    win.blit(max_height_text, (50, 540))

# Simulator variables
origin = (60, 600)
radius = 250
v0 = 100
clicked = False
currentp = None
projectile_group = pygame.sprite.Group()

angle = -30
end = getPosOnCircumeference(angle, origin)
arct = math.radians(angle)
arcrect = pygame.Rect(origin[0] - 30, origin[1] - 30, 60, 60)

SimulatorWidgets = [
    speed_slider,
    speed_output,
    angle_slider,
    angle_output,
    streak_toggle,
]
SolverWidgets = [
    textbox_speed,
    textbox_angle,
    textbox_tf,
    textbox_vertical_speed,
    textbox_horizontal_speed,
    textbox_max_height,
    textbox_range,
]


for widget in SolverWidgets:
    widget.setText("?")

start_time = 0
duration = 3000
show_text = False  # Initially, text is hidden
elapsed_time = 0

insufficent_information = False
impossible_trajectory = False

running = True
while running:
    win.fill((52, 78, 91))

    if currentMenu == "Menu":
        for widget in SimulatorWidgets:
            widget.hide()
        for widget in SolverWidgets:
            widget.hide()

        pygame.display.set_caption("Projectile Helper")

        win.blit(pygame.font.SysFont("arialblack", 60).render("Projectile Helper", True, TEXT_COL), (325, 50))

        if buttonSolver.draw(win):
            currentMenu = "Solver"

        if buttonSimulator.draw(win):
            currentMenu = "Simulator"

    elif currentMenu == "Simulator":
        for widget in SimulatorWidgets:
            widget.show()
        for widget in SolverWidgets:
            widget.hide()

        pygame.display.set_caption("Simulator")
        angle_output.setText(angle_slider.getValue())
        speed_output.setText(speed_slider.getValue())
        end = getPosOnCircumeference(-angle_slider.getValue(), origin)
        arct = math.radians(-angle_slider.getValue())
        streak_status = streak_toggle.getValue()
        toggle_status = streak_toggle.getValue()
        renderGame(
            win,
            origin,
            end,
            arcrect,
            arct,
            projectile_group,
            font,
            clock,
            angle,
            currentp,
            WIDTH,
            HEIGHT,
            toggle_status,
        )

        buttonSimFire.draw(win)
        buttonRemove.draw(win)

        if pygame.time.get_ticks() - start_time >= duration:
            show_text = False  # Hide the text

        if show_text == True and len(projectile_group.sprites()) == 3:
            win.blit(
                pygame.font.SysFont("verdana", 40, bold=True).render(
                    "Maximum amount of projectiles reached", True, (220, 20, 60)
                ),
                (WIDTH - 1050, 200),
            )

        if buttonSimBack.draw(win):
            currentMenu = "Menu"

    else:  # Solver
        for widget in SimulatorWidgets:
            widget.hide()
        for widget in SolverWidgets:
            widget.show()

        pygame.display.set_caption("Solver")

        if impossible_trajectory:
            win.blit(impossible_text, (336,614))
        elif insufficent_information:
            win.blit(insufficent_text, (356,614))

        renderTexts()

        if buttonSolve.draw(win):
            impossible_trajectory = False
            v = [
                textbox_speed.getText(),
                textbox_angle.getText(),
                textbox_vertical_speed.getText(),
                textbox_tf.getText(),
                textbox_max_height.getText(),
                textbox_range.getText(),
                textbox_horizontal_speed.getText(),
            ]
            for x in v:
                if x != "?":
                    try:
                        v[v.index(x)] = float(x)
                    except:
                        v[v.index(x)] = None
                else:
                    v[v.index(x)] = None
            try:
                initial_speed, launch_angle, initial_horizontal_speed, initial_vertical_speed, time_of_flight, max_height, range_distance = calculate_parameters(*v)
                if initial_speed == None: #si la fonction n'a pas résolue l'équation
                    insufficent_information = True
                else:
                    insufficent_information = False
                    textbox_speed.setText(round(initial_speed,2))
                    textbox_angle.setText(round(launch_angle,2))
                    textbox_horizontal_speed.setText(round(initial_horizontal_speed,2))
                    textbox_vertical_speed.setText(round(initial_vertical_speed,2))
                    textbox_tf.setText(round(time_of_flight,2))
                    textbox_max_height.setText(round(max_height,2))
                    textbox_range.setText(round(range_distance,2))
            except:
                impossible_trajectory = True

        if buttonClear.draw(win):
            textbox_speed.setText("?")
            textbox_angle.setText("?")
            textbox_horizontal_speed.setText("?")
            textbox_vertical_speed.setText("?")
            textbox_tf.setText("?")
            textbox_max_height.setText("?")
            textbox_range.setText("?")
            insufficent_information = False
            impossible_trajectory = False


        if buttonSimBack.draw(win):
            currentMenu = "Menu"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        if currentMenu == "Simulator":
            liste = eventhandler(
                event,
                origin,
                projectile_group,
                clicked,
                currentMenu,
                currentp,
                angle,
                custom_events,
                show_text,
                start_time,
                angle_slider.getValue(),
                speed_slider.getValue(),
            )
            currentMenu = liste[0]
            clicked = liste[1]
            currentp = liste[2]
            angle = liste[3]
            show_text = liste[4]
            start_time = liste[5]

    clock.tick(FPS)
    if currentMenu != "Menu":
        pygame_widgets.update(pygame.event.get())
    pygame.display.update()


pygame.quit()
