#!/usr/bin/python

from enum import Enum

# each number represents the pitch for the note

class Notes(Enum):
    __order__ = 'A B C D E F G'
    A = 0;
    B = 2;
    C = 3;
    D = 5;
    E = 7;
    F = 8;
    G = 10;

orderedNotes = list(Notes)

notes = {
    "A*" : 11,
    "A"  : 0,
    "A#" : 1,

    "B*" : 1,
    "B"  : 2,
    "B#" : 3,

    "C*" : 2,
    "C"  : 3,
    "C#" : 4,

    "D*" : 4,
    "D"  : 5,
    "D#" : 6,

    "E*" : 6,
    "E"  : 7,
    "E#" : 8,

    "F*" : 7,
    "F"  : 8,
    "F#" : 9,

    "G*" : 9,
    "G"  : 10,
    "G#" : 11
}

# going up full steps and half steps on semitones

def fullstep(pitch):
    return (pitch + 2)%12

def halfstep(pitch):
    return (pitch + 1)%12

#interval patterns shown as arrays

Major = ['f','f','h','f','f','f','h']

#Given a note and interval pattern, gives you all the semitones

def NotesInKey(note,KeyType):
    result = notes.get(note)
    results = [result]
    print(result)
    for x in KeyType:
        if x == 'f':
            result = fullstep(result)
        elif x == 'h':
            result = halfstep(result)
        results.append(result)
    return results


def getToneFromNote():
    #notesList = list(Notes)
    for i in range(0,3):
        print(notes[i])

var = NotesInKey("A", Major)

print(var)
