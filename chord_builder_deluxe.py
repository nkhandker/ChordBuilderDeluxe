#!/usr/bin/python

from enum import Enum

# each number represents the pitch for the note

class Notes(Enum):
    __order__ = 'A B C D E F G'
    A = 1;
    B = 3;
    C = 4;
    D = 6;
    E = 8;
    F = 9;
    G = 11;

notes = list(Notes)

class Flats(Enum):
    __order__ = 'A B C D E F G'
    A = 12;
    B = 2;
    C = 3;
    D = 5;
    E = 7;
    F = 8;
    G = 10;

flats = list(flats)

class Sharps(Enum):
    __order__ = 'A B C D E F G'
    A = 2;
    B = 4;
    C = 5;
    D = 7;
    E = 9;
    F = 10;
    G = 12;

sharps = list(Sharps)

def getToneFromNote():
    #notesList = list(Notes)
    for i in range(0,3):
        print(notes[i])

getToneFromNote()
