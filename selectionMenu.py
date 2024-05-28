import inputOptions as iopt

class SelectionMenu():
    def __init__(self):
        self.titleText = ""
        self.desc = ""
        self.options = ""
        self.l = []
        self.useList = False
        self.isSingleOption = True
    
    def check_val(self, val):
        if val == None:
            return False
        else:
            return True

    def Title_Text(self):
        print("##############################")
        print(self.titleText)
        print("##############################")
        print()
    
    def Title_With_Description_Text(self):
        print("##############################")
        print(self.titleText)
        print()
        print(self.desc)
        print("##############################")
        print()

    def List_Values(self):
        print("List:")
        print()
        for i in range(len(self.l)):
            print(str(i) + "# " + self.l[i])
        print()

    def SingleOption(self):
        if self.check_val(self.options) and self.isSingleOption:
            print(self.options)
            return iopt.option_choice("")
    
    def MultiOption(self):
        if self.check_val(self.options) and not self.isSingleOption:
            print(self.options)
            return iopt.multiple_par_choice("")

    def mainLoop(self):
        answer = ""
        if self.check_val(self.desc) and self.check_val(self.titleText):
            self.Title_With_Description_Text()
        elif self.check_val(self.titleText):
            self.Title_Text()
        if self.useList:
            self.List_Values()
        answer = self.SingleOption()
        answer = self.MultiOption()
        return answer