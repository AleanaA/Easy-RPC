import time
from appJar import gui
from pypresence import Presence,exceptions

def rpcstart(btn):
    if btn == "Update":
        RPC.update()
        details = app.getEntry("details")
        if details == "":
            details = None
        state = app.getEntry("state")
        if state == "":
            state = None
        large_image = app.getEntry("large_image")
        if large_image == "":
            large_image = None
        large_text = app.getEntry("large_text")
        if large_text == "":
            large_text = None
        small_image = app.getEntry("small_image")
        if small_image == "":
            small_image = None
        small_text = app.getEntry("small_text")
        if small_text == "":
            small_text = None
        RPC.update(state=state, details=details, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text)
    elif btn == "Time":
        RPC.update()
        details = app.getEntry("details")
        if details == "":
            details = None
        state = app.getEntry("state")
        if state == "":
            state = None
        large_image = app.getEntry("large_image")
        if large_image == "":
            large_image = None
        large_text = app.getEntry("large_text")
        if large_text == "":
            large_text = None
        small_image = app.getEntry("small_image")
        if small_image == "":
            small_image = None
        small_text = app.getEntry("small_text")
        if small_text == "":
            small_text = None
        RPC.update(state=state, details=details, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text, start=time.time())
    else:
        RPC.close()
        app.stop()

def EasyRPC():
    # Create the window
    global app
    app = gui("Easy RPC", "250x350")
    app.configure(resizable=False)

    # Create the text boxes
    app.addEntry("details")
    app.addEntry("state")
    app.addEntry("large_image")
    app.addEntry("large_text")
    app.addEntry("small_image")
    app.addEntry("small_text")

    # Add default values 
    app.setEntryDefault("details", "Top Line")
    app.setEntryDefault("state", "Bottom Line")
    app.setEntryDefault("large_image", "Large Asset")
    app.setEntryDefault("large_text", "Large Hover Text")
    app.setEntryDefault("small_image", "Small Asset")
    app.setEntryDefault("small_text", "Small Hover Text")

    app.addButtons(["Update","Time","Exit"], rpcstart)

    app.go()

def Login(btn):
    if btn == "Cancel":
        loginapp.stop()
    else:
        clientid = loginapp.getEntry("Client ID")
        global RPC
        RPC = Presence(clientid)
        try:
            RPC.connect()
        except exceptions.InvalidPipe:
            loginapp.errorBox("Easy RPC", "Unable to connect to Discord. Is it running?", parent=None)
        try:
            RPC.update()
        except exceptions.InvalidID:
            loginapp.errorBox("Easy RPC", "Client ID is invalid, ensure that it is correct.", parent=None)
            return
        loginapp.stop()
        EasyRPC()

def GetClientID():
    global loginapp
    loginapp = gui("Easy RPC", "400x200")
    loginapp.addLabelEntry("Client ID")
    loginapp.addButtons(["Submit", "Cancel"], Login)
    loginapp.setFocus("Client ID")
    loginapp.go()

GetClientID()
try:
    RPC.close()
except:
    pass