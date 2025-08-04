import os

def pause(msg = "Press Enter To Continue..."):
    """Pause the terminal until user press 'Enter'."""
    input("\n" + msg)

def makingSure(msg = "Are You Sure? (y/n) : " ):
    """Let user making sure of their choice."""
    confirmation = input("\n" + msg)
    if confirmation.strip().lower() in ["y", "yes"]:
        return True
    else:
        return False
    
def wipeScreen():
    """Clear terminal Screen."""
    if os.name == "nt":
        cmd = "cls"
    else:
        cmd = "clear"
    os.system(cmd)

pause()

makingSure()

wipeScreen()



