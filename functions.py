import math

radius = 160


def getGradient(p1, p2):
    if p1[0] == p2[0]:
        m = math.radians(90)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m


def getAngleFromGradient(gradient):
    return math.atan(gradient)


def getAngle(pos, origin):
    m = getGradient(pos, origin)
    thetaRad = getAngleFromGradient(m)
    theta = round(math.radians(thetaRad), 2)
    return theta


def getPosOnCircumeference(theta, origin):
    theta = math.radians(theta)
    x = origin[0] + radius * math.cos(theta)
    y = origin[1] + radius * math.sin(theta)
    return (x, y)
