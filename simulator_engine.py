# Projectile motion
import math
import random
import pygame
from sympy import symbols, solve
import time

from functions import *
from button import *


GREY = (71, 95, 119)
BLACK = (18, 18, 18)
WHITE = (217, 217, 217)
RED = (252, 91, 122)
GREEN = (29, 161, 16)
BLUE = (78, 193, 246)
ORANGE = (252, 76, 2)
YELLOW = (254, 221, 0)
PURPLE = (155, 38, 182)
AQUA = (0, 249, 182)
ALPHA = (193, 188, 196, 1)

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE]


g = 9.81


class Projectile(pygame.sprite.Sprite):
    def __init__(self, v0, angle, origin):
        # call pygame.sprite.Sprite class __init__
        super(Projectile, self).__init__()

        self.angle = abs(angle)
        self.angleRad = math.radians(self.angle)

        self.v0 = v0
        self.x, self.y = origin
        self.t0 = time.time()

        self.vx0 = v0 * math.cos(self.angleRad)
        self.vy0 = v0 * math.sin(self.angleRad)

        self.color = random.choice(COLORS)

        self.dy = 0
        self.dx = 0

        self.tf = self.timeOfFlight()

        self.path = []

    def updateY(self, t):
        return round((9.81 * t**2) / 2 + self.vy0 * t, 4)

    def updateX(self, t):
        return round(self.vx0 * t, 4)

    def timeOfFlight(self):
        tf = symbols("x")
        expr = ((-9.81 * tf**2) / 2) + self.vy0 * tf
        sol = solve(expr)
        sol = sol[1]
        return sol

    def getRange(self):
        return round(self.vx0 * self.tf, 4)

    def getMaxHeight(self):
        return round(((self.v0**2) * (math.sin(self.angleRad) ** 2)) / (2 * 9.81))

    #        tf = self.tf/2
    #        return round((9.81*tf**2)/2+ self.vy0*tf, 4)

    def update(self, origin, win, toggle):
        if self.x > self.getRange() + origin[0]:
            lastpos = self.path[0]
            if toggle:
                for pos in self.path[: -1 : int(500 / self.v0)]:
                    pygame.draw.circle(win, WHITE, pos, 1)
                    lastpos = pos
            else:
                for pos in self.path[:-1:1]:
                    if math.sqrt( ((lastpos[0] - pos[0]) ** 2) + ((lastpos[1] - pos[1]) ** 2) ) > 10:  
                        # difference in distance bigger than 10
                        pygame.draw.circle(win, WHITE, pos, 1)
                        lastpos = pos
        else:
            self.x = origin[0] - self.updateX(self.t0 - time.time())
            self.y = origin[1] + self.updateY(self.t0 - time.time())
            self.path.append((self.x, self.y))
            lastpos = self.path[0]
            pygame.draw.circle(win, WHITE, self.path[-1], 5, 1)
            if toggle:
                for pos in self.path[: -1 : int(500 / self.v0)]:
                    pygame.draw.circle(win, WHITE, pos, 1)
                    lastpos = pos
            else:
                for pos in self.path[:-1:1]:
                    if math.sqrt( ((lastpos[0] - pos[0]) ** 2) + ((lastpos[1] - pos[1]) ** 2) ) > 10:  
                        # difference in distance bigger than 10
                        pygame.draw.circle(win, WHITE, pos, 1)
                        lastpos = pos

        pygame.draw.circle(win, self.color, self.path[-1], 5)


def renderGame(
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
):
    pygame.draw.line(win, WHITE, origin, (origin[0] + 1120, origin[1]), 2)
    pygame.draw.line(win, WHITE, origin, (origin[0], origin[1] - 580), 2)
    pygame.draw.line(win,ALPHA, origin, end, 4)
    pygame.draw.circle(win, WHITE, origin, 3)
    pygame.draw.arc(win, ALPHA, arcrect, 0, -arct, 2)

    projectile_group.update(origin, win, toggle=toggle_status)

    # Info *******************************************************************
    vel_text = pygame.font.SysFont("Calibri", 14, bold=True).render(
        "Velocity (m/s): ", True, WHITE
    )
    win.blit(vel_text, (835, 72))
    angle_text = pygame.font.SysFont("Calibri", 14, bold=True).render(
        "Launch Angle (°):", True, WHITE
    )
    win.blit(angle_text, (812, 27))
    toggle_text = pygame.font.SysFont("Calibri", 14, bold=True).render(
        "Time-based streak:", True, WHITE
    )
    win.blit(toggle_text, (590, 27))

    title = font.render("Projectile Motion", True, WHITE)
    thetatext = font.render(f"Angle : {int(abs(angle))}", True, WHITE)
    win.blit(title, (80, 30))


    if currentp:
        veltext = font.render(f"Velocity : {currentp.v0}m/s", True, WHITE)
        timetext = font.render(
            f"Time : {round(currentp.timeOfFlight(),2)}s", True, WHITE
        )
        rangetext = font.render(f"Range : {round(currentp.getRange(),2)}m", True, WHITE)
        heighttext = font.render(
            f"Max Height : {round(currentp.getMaxHeight(),2)}m", True, WHITE
        )
        win.blit(veltext, (WIDTH - 150, 204))
        win.blit(timetext, (WIDTH - 150, 224))
        win.blit(rangetext, (WIDTH - 150, 244))
        win.blit(heighttext, (WIDTH - 150, 264))
        win.blit(thetatext, (WIDTH - 150, 184))


def eventhandler(
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
    s_angle,
    s_vel,
):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            currentMenu = "Menu"

        if event.key == pygame.K_r:
            projectile_group.empty()
            currentp = None

    if event.type == pygame.MOUSEBUTTONDOWN:
        clicked = True

    if event.type == pygame.MOUSEBUTTONUP:
        clicked = False

    if event.type == custom_events[0].type:
        angle = s_angle * -1
        if -90 < angle <= 0:
            if len(projectile_group.sprites()) <= 2:
                projectile = Projectile(s_vel, angle, origin)
                projectile_group.add(projectile)
                currentp = projectile
            else:
                if show_text == False:
                    show_text = True
                    start_time = pygame.time.get_ticks()

    if event.type == custom_events[1].type:
        projectile_group.empty()
        currentp = None

    return currentMenu, clicked, currentp, angle, show_text, start_time
