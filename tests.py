from windowcapture import WindowCapture
from vision import Vision
from time import time, sleep
import cv2 as cv
import admin
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
    screenshot = wincap.get_screenshot()
    rectangles = im.find(screenshot, confidence)
    if rectangles.size != 0:
        click_im(rectangles, im)

def pick_a_demon(sec, im, confidence):
    screenshot = wincap.get_screenshot()
    rectangles = im.find(screenshot, 0.65)
    output_im = im.draw_rectangles(screenshot, rectangles)
    cv.imshow('Matches', output_im)
    if rectangles.size != 0:
        t = threading.Thread(target=sleep_and_click, args=[(thread_time := sec), im, confidence])
        t.start()

if True:
    battle_menu = Vision('Screenshots/battle_menu.jpg')
    demons = Vision('Screenshots/demons.jpg')
    tavern = Vision('Screenshots/Tavern.jpg')
    green_ok = Vision('Screenshots/green_ok.jpg')
    accept_raid = Vision('Screenshots/accept.jpg')
    bunny = Vision('Screenshots/bunny.jpg')
    fattie = Vision('Screenshots/fattie.jpg')
    slenderman = Vision('Screenshots/slanderman.jpg')
    hell = Vision('Screenshots/hell.jpg')
    hard = Vision('Screenshots/hard.jpg')
    demon_ok = Vision('Screenshots/demon_ok.jpg')
    prep = Vision('Screenshots/prep.jpg')
    auto = Vision('Screenshots/auto.jpg')
    demon = Vision('Screenshots/sync.jpg')
    bell = Vision('Screenshots/bell.jpg')
    wincap =  WindowCapture('The Seven Deadly Sins: Grand Cross')


def spam(spam_demon, difficulty):
    last_clicked = None
    loop_time = time()
    z = 0
    thread_time = 0
    while True:
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if loop_time >= thread_time:
            #do we need to search for battle menu
            if last_clicked == None or last_clicked == demon_ok or last_clicked == green_ok or (last_clicked == battle_menu and (time() - loop_time) >= 30):
                screenshot = wincap.get_screenshot()
                rectangles = battle_menu.find(screenshot, 0.65)
                output_im = battle_menu.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), battle_menu, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = battle_menu
                    print("clicking battle menu")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #do we need to search for demons tab
            if last_clicked == None or last_clicked == battle_menu:
                screenshot = wincap.get_screenshot()
                rectangles = demons.find(screenshot, 0.65)
                output_im = demons.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), demons, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = demons
                    print("clicking demons menu")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #do we need to search for the demon, change according to demon you want to spam
            if last_clicked == None or last_clicked == demons or (last_clicked == difficulty and (time() - loop_time) >= 120):
                screenshot = wincap.get_screenshot()
                rectangles = spam_demon.find(screenshot, 0.65)
                output_im = spam_demon.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), spam_demon, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = spam_demon
                    print("picked demon")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #do we need to pick difficulty
            if last_clicked == None or last_clicked == spam_demon or last_clicked == green_ok or last_clicked == bell:
                screenshot = wincap.get_screenshot()
                rectangles = difficulty.find(screenshot, 0.7)
                output_im = difficulty.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.2), difficulty, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = difficulty
                    print("picked diff")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #do we need to search for accept raid
            if last_clicked == difficulty:
                screenshot = wincap.get_screenshot()
                rectangles = accept_raid.find(screenshot, 0.85)
                output_im = accept_raid.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 8.5), accept_raid, 0.65])
                    t.start()
                    last_clicked = accept_raid
                    loop_time = time()
                    print("accepted raid")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #do we need to search for prep
            if last_clicked == None or last_clicked == accept_raid:
                screenshot = wincap.get_screenshot()
                rectangles = prep.find(screenshot, 0.55)
                output_im = prep.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), prep, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = prep
                    print("ready")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #autoing the demon
            if last_clicked == None or last_clicked == prep:
                screenshot = wincap.get_screenshot()
                rectangles = auto.find(screenshot, 0.75)
                output_im = auto.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 20), auto, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = auto
                    print("autoing")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            if last_clicked == None or last_clicked == auto:
                screenshot = wincap.get_screenshot()
                rectangles = demon_ok.find(screenshot, 0.6)
                output_im = demon_ok.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), demon_ok, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = demon_ok
                    z += 1
                    print(f"done with {z} demons")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            # pressing normal ok if people are being little shits
            if last_clicked == None or (time() - loop_time) >= 60:
                screenshot = wincap.get_screenshot()
                rectangles = green_ok.find(screenshot, 0.75)
                output_im = green_ok.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), green_ok, 0.65])
                    t.start()
                    loop_time = time()
                    last_clicked = green_ok
                    print("someone was a little shit")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
        # print(time()-loop_time)
        if (time() - loop_time) >= 300:
            loop_time = time()
            last_clicked = None
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
    print("done")

spam(fattie, hell)