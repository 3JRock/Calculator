import tkinter
import tkinter.messagebox
class GUITest:
    def __init__(self):
        self.mainwindow = tkinter.Tk() 
        self.firstNum = '' # records the first number entered
        self.mem = [] # records the button presses
       
        self.display = tkinter.Canvas(self.mainwindow,bg='#c0c0c0',height=40,width=150)
        self.display.pack()

        # self.display = tkinter.Canvas(self.mainwindow,bg='#000000',height=43,width=153)
        # self.display.pack()

        self.topframe = tkinter.Frame(self.mainwindow)
        self.b1 = tkinter.Button(self.topframe,font=100, text = '1', 
command = self.numMem1)
        self.b2 = tkinter.Button(self.topframe,font=100, text = '2', 
command = self.numMem2)
        self.b3 = tkinter.Button(self.topframe,font=100, text = '3', 
command = self.numMem3)

        self.b1.pack(side='left')
        self.b2.pack(side='left')
        self.b3.pack(side='left')
        self.topframe.pack()

        self.midframe = tkinter.Frame(self.mainwindow)
        self.b4 = tkinter.Button(self.midframe,font=100, text = '4', 
command = self.numMem4)
        self.b5 = tkinter.Button(self.midframe,font=100, text = '5', 
command = self.numMem5)
        self.b6 = tkinter.Button(self.midframe,font=100, text = '6', 
command = self.numMem6)

        self.b4.pack(side='left')
        self.b5.pack(side='left')
        self.b6.pack(side='left')
        self.midframe.pack()


        self.botframe = tkinter.Frame(self.mainwindow)
        self.b7 = tkinter.Button(self.botframe,font=100, text = '7', 
command = self.numMem7)
        self.b8 = tkinter.Button(self.botframe,font=100, text = '8', 
command = self.numMem8)
        self.b9 = tkinter.Button(self.botframe,font=100, text = '9', 
command = self.numMem9)
        
        self.b7.pack(side='left')
        self.b8.pack(side='left')
        self.b9.pack(side='left')
        
        self.botframe.pack(side='top')

        self.b0 = tkinter.Button(self.mainwindow,font=100, text = '0', 
command = self.numMem0)
        self.b0.pack()


        self.rightframe = tkinter.Frame(self.mainwindow)
        self.add = tkinter.Button(self.rightframe,font=100, text = '+', 
command = self.add)
        self.add.pack()

        self.equal = tkinter.Button(self.rightframe,font=100, text = '=', 
command = self.equal)
        self.equal.pack()
        self.rightframe.pack(side='right')




        
        self.quit = tkinter.Button(self.mainwindow,font=100, text = 'Quit', command = 
self.mainwindow.destroy)
        self.quit.pack(side='left')
        
        tkinter.mainloop()


    def numMem1(self):
        self.mem.append('1')
        print(self.mem)

    def numMem2(self):
        self.mem.append('2')
        print(self.mem)

    def numMem3(self):
        self.mem.append('3')
        print(self.mem)

    def numMem4(self):
        self.mem.append('4')
        print(self.mem)        
    
    def numMem5(self):
        self.mem.append('5')
        print(self.mem)

    def numMem6(self):
        self.mem.append('6')
        print(self.mem)


    def numMem7(self):
        self.mem.append('7')
        print(self.mem)


    def numMem8(self):
        self.mem.append('8')
        print(self.mem)


    def numMem9(self):
        self.mem.append('9')
        print(self.mem)


    def numMem0(self):
        self.mem.append('0')
        print(self.mem)



    def add(self): 
        self.firstNum = '+'.join(self.mem)
        print(self.firstNum)
        self.mem.clear()
        
        

    def equal(self):
        if '+' in self.firstNum:
            firstNum = int(self.firstNum)
            secondNum = ''.join(self.mem)
            secondNum = int(secondNum)
            print(firstNum+secondNum)
            







def main():
    mygui = GUITest()
main()