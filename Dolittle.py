import tkinter
import pickle
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, IntVar

datafile = 'Doolittle data.dat'

class KnowledgeBase:
    def __int__(self):
        self.animals = set( )
        self.queries = []

#Load the knoledge base
try:
    with open(datafile, 'rb') as f:
        unpickler = pickle.Unpickler(f)
        knowledgeBase = unpickler.load( )
        print ('Loaded existing knowledge base')
except FileNotFoundError:
    knowledgeBase = KnowledgeBase( )
    print('No knowledge base found -- creating new one')

# To do: everything else

#Save the database
with open(datafile, 'wb') as f:
    pickler = pickle.Pickler(f)
    pickler.dump(knowledgeBase)
    print('Saved knowledge base')