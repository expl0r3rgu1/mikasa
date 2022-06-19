#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *

db = mysql.connector.connect(
    host = HOST,
    user = USER,
    passwd = PASSWORD,
    database = DATABASE,
    auth_plugin = AUTH_PLUGIN
)

db_cursor = db.cursor()

empty_layout = [
    [sg.Text('Mikasa')],
    [sg.Button('Visualizza clienti')]
]

window = sg.Window('Mikasa', empty_layout, margins=(400, 200))