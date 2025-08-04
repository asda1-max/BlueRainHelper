class createMenu:

    def __init__(self, menuTitle = "menu"):
        """create new menu"""
        self.title = menuTitle
        self.optionMenu = []
        self.longestText = len(self.title)
        self.isCentered = False

    def addOption(self, newOption = "option"):
        """add new option"""
        curLength = 0
        self.optionMenu.append(newOption)
        curLength = len(newOption) + len(str(len(self.optionMenu))) + 1
        if curLength > self.longestText:
            if len(newOption) % 2 != 0:
                self.longestText = curLength + 1 
            else:
                self.longestText = curLength
        return self
    
    def viewMenu(self, padding = 4):
        """view menu"""
        lineBorder = self.longestText + padding * 2
        spaceAvail = lineBorder - len(self.title)
        spaceRight = int(spaceAvail / 2 )
        spaceLeft = int(spaceAvail - spaceRight)
        print("+" + "-" * lineBorder + "+")
        print("|" + " " * spaceRight + self.title + " " * spaceLeft + "|")
        print("+" + "-" * lineBorder + "+")
        for index, option in enumerate(self.optionMenu, start = 1):
            if self.isCentered == True:
                spaceAvail = self.longestText + 2* padding - len(str(index) + "." + option)
                spaceRight = int(spaceAvail / 2 )
                spaceLeft = int(spaceAvail - spaceRight)
                print("|"+" " * spaceLeft + str(index) + "." + option + " " * spaceRight + "|")
            else:
                spaceAvail = self.longestText + padding - len(str(index) + "." + option)
                print("|"+" " * padding + str(index) + "." + option + " " * spaceAvail + "|")
        print("+" + "-" * lineBorder + "+")
        return self
    
    def setTextCenter(self):
        """set text option to center"""
        self.isCentered = True
        return self
    
    def setTextNormal(self):
        """set text option to center"""
        self.isCentered = False
        return self

    def clears(self):
        """clear menu option"""
        self.optionMenu.clear()
        self.longestText = 10
        return self

