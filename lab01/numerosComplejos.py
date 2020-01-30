from sys import stdin
import math


def suma(r,t):
    k = (r[0] + t[0], r[1] + t[1])
    return k

def resta(r,t):
    k = (r[0] - t[0], r[1] - t[1])
    return k

def multiplicacion(r,t):
    k = (r[0]*t[0] - r[1]*t[1],r[0]*t[1] + r[1]*t[0])
    return k

def division(r,t):
    k = ((r[0]*t[0] + r[1]*t[1])/(t[0]**2+t[1]**2),(r[1]*t[0] - r[0]*t[1])/(t[0]**2+t[1]**2))
    return k

def modulo(r):
    k = (r[0]**2 + r[1]**2)**(1/2)
    return k

def conjugado(r):
    k = (r[0], -1*r[1])
    return k

def cartesianasAPolares(r):
    l = (r[0]**2+r[1]**2)**(1/2)
    s = math.atan2(r[1],r[0])
    return (l,s)

def polaresACartesianas(e):
    h = e[0]
    c = e[1]*(math.pi/180)
    return (h*math.cos(c),h*math.sin(c))

def fase(c):
    return math.atan2(c[1],c[0])

