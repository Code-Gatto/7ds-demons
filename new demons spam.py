from windowcapture import WindowCapture
from vision import Vision
from time import time, sleep
import cv2 as cv
import admin
import numpy as np
import threading

if not admin.isUserAdmin():
    admin.runAsAdmin()


def click_im(rectangles, im):
    (gx, gy) = wincap.get_game_position()
    (x, y) = im.get_click_point(rectangles)
    (x, y) = ((x + gx), (y + gy))
    wincap.click(x, y)

def sleep_and_click(sec, im, confidence=0.6):
    sleep(sec)
    fscreenshot = wincap.get_screenshot()
    rectangles = im.find(fscreenshot, confidence)
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
    wincap =  WindowCapture('The Seven Deadly Sins: Grand Cross')

def spam(spamming, diff):
    last_clicked = None
    loop_time = time()
    z = 0
    death_count = 0
    thread_time = 0
    while True:
        sleep(0.1)
        screenshot = wincap.get_screenshot()
        output_im = screenshot
        cv.imshow('Matches', output_im)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if loop_time >= thread_time:
            #do we need to search for demon ok
            if last_clicked == None or last_clicked == auto or last_clicked == green_ok:
                rectangles = demon_ok.find(screenshot, 0.6)
                output_im = demon_ok.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), demon_ok, 0.6])
                    t.start()
                    loop_time = time()
                    last_clicked = demon_ok
                    z += 1
                    print(f"done with {z} demons")
            if last_clicked == None or last_clicked == auto or last_clicked == green_ok:
                rectangles = dead.find(screenshot, 0.6)
                output_im = dead.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), dead, 0.6])
                    t.start()
                    loop_time = time()
                    last_clicked = dead
                    death_count += 1
                    print(f"we died {death_count} times")
            # pressing normal ok if people are being little shits
            if last_clicked == None or (time() - loop_time) >= 5 or last_clicked == dead:
                rectangles = green_ok.find(screenshot, 0.68)
                output_im = green_ok.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
            #do we need to search for battle menu
            if last_clicked == None or last_clicked == demon_ok or last_clicked == green_ok or (last_clicked == battle_menu and (time() - loop_time) >= 15) or last_clicked == dead:
                rectangles = battle_menu.find(screenshot, 0.65)
                output_im = battle_menu.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), battle_menu, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = battle_menu
                    print("clicking battle menu")
            #do we need to search for demons tab
            if last_clicked == None or last_clicked == battle_menu:
                rectangles = demons.find(screenshot, 0.65)
                output_im = demons.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), demons, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = demons
                    print("clicking demons menu")
            #do we need to search for the demon, change according to demon you want to spam
            if last_clicked == None or last_clicked == demons or (last_clicked == accept_raid and (time() - loop_time) >= 30) or (last_clicked == diff and (time() - loop_time) >= 120):
                rectangles = spamming.find(screenshot, 0.65)
                output_im = spamming.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), spamming, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = spamming
                    print("picking demon")
            #do we need to pick difficulty
            if last_clicked == None or last_clicked == spamming or last_clicked == green_ok:
                rectangles = diff.find(screenshot, 0.65)
                output_im = diff.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.2), diff, 0.6])
                    t.start()
                    loop_time = time()
                    last_clicked = diff
                    print("picking diff")
            #do we need to search for accept raid
            if last_clicked == diff:
                rectangles = accept_raid.find(screenshot, 0.85)
                output_im = accept_raid.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 8.5), accept_raid, 0.65])
                    t.start()
                    last_clicked = accept_raid
                    loop_time = time()
                    print("accepting raid")
            #do we need to search for prep
            if last_clicked == None or last_clicked == accept_raid or (last_clicked == prep and (time() - loop_time) >= 2):
                rectangles = prep.find(screenshot, 0.55)
                output_im = prep.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.001), prep, 0.5])
                    t.start()
                    loop_time = time()
                    last_clicked = prep
                    print("ready")
            #autoing the demon
            if last_clicked == None or last_clicked == prep:
                rectangles = auto.find(screenshot, 0.85)
                output_im = auto.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 20), auto, 0.75])
                    t.start()
                    loop_time = time()
                    last_clicked = auto
                    print("autoing")
        # print(time()-loop_time)
        if (time() - loop_time) >= 180:
            loop_time = time()
            last_clicked = None
            print("time")
    print("done")
   
#edit the line below
spam(bunny, hell)
