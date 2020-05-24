zalupa = 'zalupa'

import time

import win32gui

import win32ui

import win32process

import win32api

import random

import pyautogui

import pynput

import os

from pynput.keyboard import Key, Listener


def on_press(key):
    zalupa
    print("PRESSED", key)
    zalupa
    if str(key) == "Key.print_screen":
        zalupa
        a = random.randint(0, 1)
        zalupa
        print(a)
        zalupa
        loshadi_i_zalupi = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        zalupa
        os.system('taskkill /F /PID ' + str(loshadi_i_zalupi[1]))
        zalupa
        time.sleep(3)
        zalupa


with Listener(on_press=on_press) as listener:
    listener.join()

"""
я ебял.
"""
