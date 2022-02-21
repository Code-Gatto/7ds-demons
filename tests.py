from windowcapture import WindowCapture
from vision import Vision
from time import time, sleep
import cv2 as cv
import admin
import numpy as np
import threading
import pyautogui

if not admin.isUserAdmin():
    admin.runAsAdmin()


def click_im(rectangles, im):
    (gx, gy) = wincap.get_game_position()
    (x, y) = im.get_click_point(rectangles)
    (x, y) = ((x + gx), (y + gy))
    wincap.click(x, y)

def sleep_and_click(sec, im, confidence=0.6):
    sleep(sec)
    global screenshot
    rectangles = im.find(screenshot, confidence)
    if rectangles.size != 0:
        click_im(rectangles, im)


if True:
    battle_menu = Vision('beta_client\\battle_menu.jpg')
    accept_raid = Vision('beta_client\\demons\\accept.jpg')
    tavern = Vision('beta_client\\tavern.jpg')
    bunny = Vision('beta_client\\demons\\bunny.jpg')
    fattie = Vision('beta_client\\demons\\fattie.jpg')
    slenderman = Vision('beta_client\\demons\\slendarman.jpg')
    bell = Vision('beta_client\\demons\\bell.jpg')
    auto = Vision('beta_client\\demons\\auto.jpg')
    demons = Vision('beta_client\\demons\\demons.jpg')
    green_ok = Vision('beta_client\green_ok.jpg')
    hell = Vision('beta_client\\demons\\hell.jpg')
    hard = Vision('beta_client\\demons\\hard.jpg')
    demon_ok = Vision('beta_client\\demons\\demon_ok.jpg')
    prep = Vision('beta_client\\demons\\prep.jpg')
    dead = Vision('beta_client\\demons\\dead_ok.jpg')
    dcd = Vision('beta_client\\reconnect.jpg')
    wincap =  WindowCapture('The Seven Deadly Sins: Grand Cross')

def spam(spamming, diff):
    global screenshot
    last_clicked = None
    loop_time = time()
    z = 0
    clicked = False
    death_count = 0
    thread_time = 0
    timer = time()
    while True:
        # if ((time() - timer) >= 25200) and (last_clicked == demon_ok or last_clicked == battle_menu):
        #     pyautogui.keyDown('alt')
        #     pyautogui.press('f4')
        #     pyautogui.keyUp('alt')
        sleep(0.15)
        screenshot = wincap.get_screenshot()
        output_im = screenshot
        cv.imshow('Matches', output_im)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 1):
            if clicked == False:
                rectangles = dcd.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), dcd, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = None
                    print("DC'd")
            #do we need to search for demon ok
            if clicked == False and (last_clicked == None or last_clicked == prep or last_clicked == auto or last_clicked == green_ok or (last_clicked == demon_ok and (time() - loop_time) >= 10)):
                rectangles = demon_ok.find(screenshot, 0.6)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), demon_ok, 0.6])
                    t.start()
                    clicked = True
                    loop_time = time()
                    if last_clicked != demon_ok:
                        z += 1
                    last_clicked = demon_ok
                    print(f"done with {z} demons")
            if clicked == False and (last_clicked == None or last_clicked == auto or last_clicked == green_ok):
                rectangles = dead.find(screenshot, 0.6)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), dead, 0.6])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = dead
                    death_count += 1
                    print(f"we died {death_count} times")
            # pressing normal ok if people are being little shits
            if clicked == False and (last_clicked == None or (time() - loop_time) >= 5 or last_clicked == dead):
                rectangles = green_ok.find(screenshot, 0.68)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
            #do we need to search for battle menu
            if clicked == False and (last_clicked == None or last_clicked == demon_ok or last_clicked == green_ok or (last_clicked == battle_menu and (time() - loop_time) >= 15) or last_clicked == dead):
                rectangles = battle_menu.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), battle_menu, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = battle_menu
                    print("clicking battle menu")
            #do we need to search for demons tab
            if clicked == False and (last_clicked == None or last_clicked == battle_menu):
                rectangles = demons.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), demons, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = demons
                    print("clicking demons menu")
            #do we need to search for the demon, change according to demon you want to spam
            if clicked == False and (last_clicked == None or last_clicked == demons or (last_clicked == accept_raid and (time() - loop_time) >= 30) or (last_clicked == diff and (time() - loop_time) >= 120)):
                rectangles = spamming.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), spamming, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = spamming
                    print("picking demon")
            #do we need to pick difficulty
            if clicked == False and (last_clicked == None or last_clicked == spamming or last_clicked == green_ok):
                rectangles = diff.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.2), diff, 0.6])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = diff
                    print("picking diff")
            #do we need to search for accept raid
            if clicked == False and last_clicked == diff:
                rectangles = accept_raid.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 8.5), accept_raid, 0.65])
                    t.start()
                    clicked = True
                    last_clicked = accept_raid
                    loop_time = time()
                    print("accepting raid")
            #do we need to search for prep
            if clicked == False and (last_clicked == None or last_clicked == green_ok or last_clicked == accept_raid or (last_clicked == prep and (time() - loop_time) >= 2)):
                rectangles = prep.find(screenshot, 0.55)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.001), prep, 0.5])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = prep
                    print("ready")
            #autoing the demon
            if clicked == False and (last_clicked == None or last_clicked == prep):
                rectangles = auto.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 10), auto, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = auto
                    print("autoing")
            if clicked == True:
                clicked = False
        # print(time()-loop_time)
        if (time() - loop_time) >= 180:
            loop_time = time()
            last_clicked = None
            print("time")
    print("done")

spam(fattie, hell)
