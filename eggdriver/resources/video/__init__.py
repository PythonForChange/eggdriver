import cv2
from eggdriver.resources.math.constants import itself
from eggdriver.resources.video.effects import *
from eggdriver.resources.video.backgrounds import *

counterIterator = 0

def forever():
    return True

def stop():
    return input()

def count(value = 100, step = 1):
    global counterIterator
    counterIterator += step
    print(value - counterIterator)
    result = counterIterator < value
    return result

defaultEffect = [(itself, [])]
defaultCondition = (count, [100])
defaultUser = 'WEBCAM'

def changeBackground(image, bg_image, background_effects = defaultEffect):
    th, th_inv = removeBG(image)
    bg = maskImage(bg_image, th_inv)
    for ef in background_effects:
        args = [bg] + ef[1]
        bg = ef[0](*args)
    fg = maskImage(image, th)
    final = cv2.bitwise_or(bg, fg)
    return final

def capture():
    print("Turning on the WebCam...")
    return cv2.VideoCapture(0)

def applyEffects(image, effects, background_effects):
    for ef in effects:
        args = [image] + ef[1]
        image = ef[0](*args)
    return changeBackground(image, image, background_effects)

def webCam(user = defaultUser, effects = defaultEffect, background_effects = defaultEffect, number_of_windows = 1, apply_effects_to = "all", condition = defaultCondition):
    global counterIterator
    counterIterator = 0
    cap = capture()
    while (cap.isOpened()):
        ret, image = cap.read()
        if ret == True and condition[0](*condition[1]):
            for i in range(number_of_windows):
                if apply_effects_to == "all":
                    image = applyEffects(image, effects, background_effects)
                else:
                    image = applyEffects(image, [effects[i]], [background_effects[i]])
                cv2.imshow(user, image)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else: break
    cap.release()
    cv2.destroyAllWindows()

def changeBackgroundWebCam(user = defaultUser, new_background = solidBackground(), effects = defaultEffect, condition = defaultCondition):
    webCam(user, [(changeBackground, [new_background])] + effects, condition)

class WEBCAM():
    """Manage the default WEBCAM

Eg:
w = ed.WEBCAM("My name")
w.default(background_effects= [(ed.blur, [])], effects = [(ed.changeBackground, [ed.solidBackground()])])
# it turns on your WEBCAM and displays it with blur and green-screen effects added"""
    def __init__(self, user, condition = count, *args):
        self.user = user
        self.condition = (condition, args)
    def default(self, effects = defaultEffect, background_effects = defaultEffect, number_of_windows = 1, apply_effects_to = "all",):
        webCam(user = self.user,
            effects = effects,
            background_effects = background_effects,
            number_of_windows = number_of_windows,
            apply_effects_to = apply_effects_to,
            condition = self.condition)
    def changeBackground(self, new_background, effects = defaultEffect, background_effects = defaultEffect, number_of_windows = 1, apply_effects_to = "all"):
        changeBackgroundWebCam(user = self.user,
            new_background = new_background,
            effects = effects,
            background_effects = background_effects,
            number_of_windows = number_of_windows,
            apply_effects_to = apply_effects_to,
            condition = self.condition)

class User():
    def __init__(self, username = "video"):
        self.user = username
        self.background = 0
        self.ef = defaultEffect
    def setBackground(self, background):
        self.background = background
    def addEffect(self, *effects):
        self.ef = effects
    def meeting(self, condition = forever, *args):
        if type(self.background) == int:
            webCam(self.user, condition, *args)
        else:
            changeBackgroundWebCam(self.user, self.background, condition, *args)