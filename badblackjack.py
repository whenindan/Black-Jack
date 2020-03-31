import sys
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton
import random
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

# The cards
heart=[str(i)+'H' for i in range(2,11)]
heart_sym=['AH','JH','QH','KH']
heart=heart+heart_sym
diamond=[str(i)+'D' for i in range(2,11)]
diamond_sym=['AD','JD','QD','KD']
diamond=diamond+diamond_sym
club=[str(i)+'C' for i in range(2,11)]
club_sym=['AC','JC','QC','KC']
club=club+club_sym
spade=[str(i)+'S' for i in range(2,11)]
spade_sym=['AS','JS','QS','KS']
spade=spade+spade_sym
fulldeck=heart+diamond+club+spade

        # Card Value
cardvalue={'AH':11,'AD':11,'AC':11,'AS':11,'2H':2,'2D':2,'2C':2,'2S':2,
            '3H':3,'3D':3,'3C':3,'3S':3,'4H':4,'4D':4,'4C':4,'4S':4,
            '5H':5,'5D':5,'5C':5,'5S':5,'6H':6,'6D':6,'6C':6,'6S':6,
            '7H':7,'7D':7,'7C':7,'7S':7,'8H':7,'8D':8,'8C':8,'8S':8,
            '9H':9,'9D':9,'9C':9,'9S':9,'10H':10,'10D':10,'10C':10,'10S':10,
            'JH':10,'JD':10,'JC':10,'JS':10,'QH':10,'QD':10,'QC':10,'QS':10,'KH':10,'KD':10,'KC':10,'KS':10
           }
e=0
cpu_draw=[]



class BlackJack(QWidget):   
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        global myscore
        global cpuscore
        global my_draw
        # Setup layout management
        grid= QGridLayout()
        self.setLayout(grid)

        # Initial Score

        self.myscorelabel=QLabel('My Score:')
        self.cpuscorelabel=QLabel('CPU Score:')
        
        grid.addWidget(self.myscorelabel,3,0)
        grid.addWidget(self.cpuscorelabel,2,0)

        # Initial 2 Cards
        def first():
            global cpuscore
            global myscore
            global cpuc1
            global cpuc2
            global myc1
            global myc2
            cpuc1=random.choice(fulldeck)
            fulldeck.remove(cpuc1)
            cpuc2=random.choice(fulldeck)
            fulldeck.remove(cpuc2)
            cpuscore=cardvalue[cpuc1]+cardvalue[cpuc2]

            myc1=random.choice(fulldeck)
            fulldeck.remove(myc1)
            myc2=random.choice(fulldeck)
            fulldeck.remove(myc2)
            myscore=cardvalue[myc1]+cardvalue[myc2]
          
        # Card I'm going to get
        global myc3,myc4,myc5
        myc3=random.choice(fulldeck)
        fulldeck.remove(myc3)
        myc4=random.choice(fulldeck)
        fulldeck.remove(myc4)
        myc5=random.choice(fulldeck)
        fulldeck.remove(myc5)
                    
        # Initial Score check, repeat if over 21    
        while True:
            first()
            if cpuscore>21:
                continue
            elif myscore>21:
                continue
            else:

                self.myscorelabel.setText('My score: {0}'.format(myscore))
                self.cpuscorelabel.setText('CPU score: {0}'.format(cardvalue[cpuc1]))
                break

        my_draw=[myc1, myc2, myc3, myc4, myc5]
        # Result Label
        self.resultlabel=QLabel('')
        grid.addWidget(self.resultlabel,2,1)
                
        # Game screen
        
        self.cpu_c1=QLabel(self)
        self.cpu_c1pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpuc1))
        self.cpu_c1pix=self.cpu_c1pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c1.setPixmap(self.cpu_c1pix)
        grid.addWidget(self.cpu_c1,1,0)

        self.cpu_c2=QLabel(self)
        self.cpu_c2pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\red_back')
        self.cpu_c2pix=self.cpu_c2pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c2.setPixmap(self.cpu_c2pix)
        grid.addWidget(self.cpu_c2,1,1)

        self.cpu_c3=QLabel(self)
        self.cpu_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.cpu_c3pix=self.cpu_c3pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c3.setPixmap(self.cpu_c3pix)
        grid.addWidget(self.cpu_c3,1,2)

        self.cpu_c4=QLabel(self)
        self.cpu_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.cpu_c4pix=self.cpu_c4pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c4.setPixmap(self.cpu_c4pix)
        grid.addWidget(self.cpu_c4,1,3)

        self.cpu_c5=QLabel(self)
        self.cpu_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.cpu_c5pix=self.cpu_c5pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c5.setPixmap(self.cpu_c5pix)
        grid.addWidget(self.cpu_c5,1,4)

        self.my_c1=QLabel(self)
        self.my_c1pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc1))
        self.my_c1pix=self.my_c1pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c1.setPixmap(self.my_c1pix)
        grid.addWidget(self.my_c1,4,0)

        self.my_c2=QLabel(self)
        self.my_c2pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc2))
        self.my_c2pix=self.my_c2pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c2.setPixmap(self.my_c2pix)
        grid.addWidget(self.my_c2,4,1)

        self.my_c3=QLabel(self)
        self.my_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.my_c3pix=self.my_c3pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c3.setPixmap(self.my_c3pix)
        grid.addWidget(self.my_c3,4,2)

        self.my_c4=QLabel(self)
        self.my_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.my_c4pix=self.my_c4pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c4.setPixmap(self.my_c4pix)
        grid.addWidget(self.my_c4,4,3)

        self.my_c5=QLabel(self)
        self.my_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.my_c5pix=self.my_c5pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c5.setPixmap(self.my_c5pix)
        grid.addWidget(self.my_c5,4,4)
        
        self.bhit=QPushButton('Hit')
        self.bhit.clicked.connect(self.hit)
        grid.addWidget(self.bhit,5,0)

        self.bstand=QPushButton('Stand')
        self.bstand.clicked.connect(self.stand)
        grid.addWidget(self.bstand,5,1)

        self.re=QPushButton('Restart')
        self.re.clicked.connect(self.restart)
        grid.addWidget(self.re,5,2)

        # Window's essentials
        self.setGeometry(500,200,1000,500)
        self.setWindowTitle('Black Jack')
        self.setWindowIcon(QIcon('E:\\Nguyen Trong Dat\\blackjackicon'))
        self.show()

        
    def hit(self):
        global fulldeck
        global cpuscore
        global e
        global myscore
        global myc3, myc4, myc5
        global cpuc3
        global cpuc4
        global cpuc5
        global cardvalue
        e=e+1
        def algorithm():
            global mind
            global cpuscore
            mind=False
            if cpuscore >19:
                mind=False
            elif cpuscore == 18 or cpuscore==19:
                if random.random()<=0.05:
                    mind = True
            elif cpuscore == 17 or cpuscore ==16:
                if random.random()<=0.1:
                    mind =True
            elif cpuscore<16 and cpuscore>=14:
                if random.random()<=0.2:
                    mind=True
            elif cpuscore <14 and cpuscore>=12:
                if random.random()<=0.4:
                    mind=True
            elif cpuscore<12 and cpuscore >10:
                if random.random()<=0.7:
                    mind=True
            else:
                mind=True
            print(mind)
        if e==1:
            self.my_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc3))
            self.my_c3pix=self.my_c3pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.my_c3.setPixmap(self.my_c3pix)
            if myc3 == 'AH' or myc3 == 'AD' or myc3 == 'AC' or myc3 == 'AS':
                if myscore>10:
                    cardvalue[myc3]=1
                else:
                    cardvalue[myc3]=11
            else:
                cardvalue[myc3]=cardvalue[myc3]
              
            myscore=myscore+cardvalue[myc3]
            self.myscorelabel.setText('My score: {0}'.format(myscore))
            

            algorithm()
            if mind:
                self.cpu_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\red_back')
                self.cpu_c3pix=self.cpu_c3pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.cpu_c3.setPixmap(self.cpu_c3pix)
                cpuc3=random.choice(fulldeck)
                fulldeck.remove(cpuc3)
                if cpuc3 == 'AH' or cpuc3 == 'AD' or cpuc3 == 'AC' or cpuc3 == 'AS':
                    if cpuscore>10:
                        cardvalue[myc3]=1
                        cpuscore=cpuscore+cardvalue[cpuc3]
                    else:
                        cardvalue[myc3]=11
                        cpuscore=cpuscore+cardvalue[cpuc3]
                else:
                    cpuscore=cpuscore+cardvalue[cpuc3]
                cpu_draw.append(cpuc3)


            print(cpuscore)

        elif e==2:
            self.my_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc4))
            self.my_c4pix=self.my_c4pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.my_c4.setPixmap(self.my_c4pix)
            if myc4 == 'AH' or myc4 == 'AD' or myc4 == 'AC' or myc4 == 'AS':
                if myscore>10:
                    myscore=myscore+1
                    
                else:
                    myscore=myscore+11
            else:
                
                cardvalue[myc4]=cardvalue[myc4]                    
        
            myscore=myscore+cardvalue[myc4]
            self.myscorelabel.setText('My score: {0}'.format(myscore))

            algorithm()
            if mind:
                self.cpu_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\red_back')
                self.cpu_c4pix=self.cpu_c4pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.cpu_c4.setPixmap(self.cpu_c4pix)
                cpuc4=random.choice(fulldeck)
                fulldeck.remove(cpuc4)
                if cpuc4 == 'AH' or cpuc4 == 'AD' or cpuc4 == 'AC' or cpuc4 == 'AS':
                    if cpuscore>10:
                        cardvalue[myc4]=1
                        cpuscore=cpuscore+cardvalue[cpuc4]
                    else:
                        cardvalue[myc4]=11
                        cpuscore=cpuscore+cardvalue[cpuc4]
                cpu_draw.append(cpuc4)


            print(cpuscore)


        elif e==3:
            self.my_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc5))
            self.my_c5pix=self.my_c5pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.my_c5.setPixmap(self.my_c5pix)    
            if myc5 == 'AH' or myc5 == 'AD' or myc5 == 'AC' or myc5 == 'AS':
                if myscore>10:
                    myscore=myscore+1
                    
                else:
                    myscore=myscore+11
            else:
                cardvalue[myc5]=cardvalue[myc5]
        
            myscore=myscore+cardvalue[myc5]
            self.myscorelabel.setText('My score: {0}'.format(myscore))
        

            
            algorithm()
            if mind:
                self.cpu_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\red_back')
                self.cpu_c5pix=self.cpu_c5pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.cpu_c5.setPixmap(self.cpu_c5pix)
                cpuc5=random.choice(fulldeck)
                fulldeck.remove(cpuc5)
                if cpuc5 == 'AH' or cpuc5 == 'AD' or cpuc5 == 'AC' or cpuc5 == 'AS':
                    if cpuscore>10:
                        cardvalue[myc5]=1
                        cpuscore=cpuscore+cardvalue[cpuc5]
                    else:
                        cardvalue[myc5]=11
                        cpuscore=cpuscore+cardvalue[cpuc5]
                else:
                    cpuscore=cpuscore+cardvalue[cpuc5]
                cpu_draw.append(cpuc5)


            print(cpuscore)
            

                
    def stand(self):
        global cpuscore
        global myscore
        def algorithm():
            global mind

            mind=False
            if cpuscore >19:
                mind=False
            elif cpuscore == 18 or cpuscore==19:
                if random.random()<=0.05:
                    mind = True
            elif cpuscore == 17 or cpuscore ==16:
                if random.random()<=0.1:
                    mind =True
            elif cpuscore<16 and cpuscore>=14:
                if random.random()<=0.15:
                    mind=True
            elif cpuscore <14 and cpuscore>=12:
                if random.random()<=0.4:
                    mind=True
            elif cpuscore<12 and cpuscore >10:
                if random.random()<=0.7:
                    mind=True
            else:
                mind=True
            print(mind)
        for i in range(3-len(cpu_draw)):
            algorithm()
            if mind:
                standcard=random.choice(fulldeck)
                fulldeck.remove(standcard)
                cpu_draw.append(standcard)
                if standcard=='AH' or standcard=='AD' or standcard=='AC' or standcard=='AS':
                    if cpuscore>10:
                        cpuscore=cpuscore+1
                    else:
                        cpuscore=cpuscore+11
                else:
                    cpuscore=cpuscore+cardvalue[standcard]
        if len(cpu_draw)==1:
            self.cpu_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpu_draw[0]))
            self.cpu_c3pix=self.cpu_c3pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c3.setPixmap(self.cpu_c3pix)

            self.cpu_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
            self.cpu_c4pix=self.cpu_c4pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c4.setPixmap(self.cpu_c4pix)

            self.cpu_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
            self.cpu_c5pix=self.cpu_c5pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c5.setPixmap(self.cpu_c5pix)
        elif len(cpu_draw)==2:
            self.cpu_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpu_draw[0]))
            self.cpu_c3pix=self.cpu_c3pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c3.setPixmap(self.cpu_c3pix)

            self.cpu_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpu_draw[1]))
            self.cpu_c4pix=self.cpu_c4pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c4.setPixmap(self.cpu_c4pix)

            self.cpu_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
            self.cpu_c5pix=self.cpu_c5pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c5.setPixmap(self.cpu_c5pix)
        elif len(cpu_draw)==3:
            self.cpu_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpu_draw[0]))
            self.cpu_c3pix=self.cpu_c3pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c3.setPixmap(self.cpu_c3pix)

            self.cpu_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpu_draw[1]))
            self.cpu_c4pix=self.cpu_c4pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c4.setPixmap(self.cpu_c4pix)

            self.cpu_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpu_draw[2]))
            self.cpu_c5pix=self.cpu_c5pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
            self.cpu_c5.setPixmap(self.cpu_c5pix)

        self.cpu_c2pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpuc2))
        self.cpu_c2pix=self.cpu_c2pix.scaled(200,200,Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c2.setPixmap(self.cpu_c2pix)

        self.cpuscorelabel.setText('CPU score: {0}'.format(cpuscore))
        
        res= None
        if cpuscore>21 and myscore>21:
            res='tie'
            print('tie')
        elif cpuscore>21 and myscore<22:
            res='win'
            print('win')
        elif cpuscore<22 and myscore>21:
            res='lose'
            print('lose')
        elif cpuscore>myscore and cpuscore<22 and myscore<22:
            res='lose'
            print('lose')
        elif myscore>cpuscore and cpuscore<22 and myscore<22:
            res='win'
            print('win')
        elif myscore==cpuscore:
            res='tie'
            print('tie')
        if res=='win':
            self.resultlabel.setText('You win')
            self.resultlabel.setFont(QtGui.QFont('Arial', 30))
            self.resultlabel.adjustSize()
            
        elif res=='lose':
            self.resultlabel.setText('You lose')
            self.resultlabel.setFont(QtGui.QFont('Arial', 30))
            self.resultlabel.adjustSize()
        else:
            self.resultlabel.setText('It\'s a draw')
            self.resultlabel.setFont(QtGui.QFont('Arial', 30))
            self.resultlabel.adjustSize()

    def restart(self):
        global cpuscore, myscore
        global e
        global cpu_draw, my_draw
        global cpuc1, cpuc2
        global myc1, myc2, myc3, myc4, myc5
        cpuscore=0
        myscore=0
        self.cpuscorelabel.setText('CPU Score')
        fulldeck.extend(cpu_draw)
        fulldeck.append(cpuc1)
        fulldeck.append(cpuc2)
        fulldeck.extend(my_draw)
        e=0
        my_draw=[]
        cpu_draw=[]
        def first():
            global cpuscore
            global myscore
            global cpuc1
            global cpuc2
            global myc1
            global myc2
            global fulldeck
            cpuc1=random.choice(fulldeck)
            fulldeck.remove(cpuc1)
            cpuc2=random.choice(fulldeck)
            fulldeck.remove(cpuc2)
            cpuscore=cardvalue[cpuc1]+cardvalue[cpuc2]

            myc1=random.choice(fulldeck)
            fulldeck.remove(myc1)
            myc2=random.choice(fulldeck)
            fulldeck.remove(myc2)
            myscore=cardvalue[myc1]+cardvalue[myc2]
            
        myc3=random.choice(fulldeck)
        fulldeck.remove(myc3)
        myc4=random.choice(fulldeck)
        fulldeck.remove(myc4)
        myc5=random.choice(fulldeck)
        fulldeck.remove(myc5)
        while True:
            first()
            if cpuscore>21:

                continue
            elif myscore>21:

                continue
            else:

                self.myscorelabel.setText('My score: {0}'.format(myscore))
                self.cpuscorelabel.setText('CPU score: {0}'.format(cardvalue[cpuc1]))
                break

        self.cpu_c1pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(cpuc1))
        self.cpu_c1pix=self.cpu_c1pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c1.setPixmap(self.cpu_c1pix)

        self.cpu_c2pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\red_back')
        self.cpu_c2pix=self.cpu_c2pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c2.setPixmap(self.cpu_c2pix)


        self.cpu_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.cpu_c3pix=self.cpu_c3pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c3.setPixmap(self.cpu_c3pix)



        self.cpu_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.cpu_c4pix=self.cpu_c4pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c4.setPixmap(self.cpu_c4pix)
 


        self.cpu_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.cpu_c5pix=self.cpu_c5pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cpu_c5.setPixmap(self.cpu_c5pix)

    
        self.my_c1pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc1))
        self.my_c1pix=self.my_c1pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c1.setPixmap(self.my_c1pix)
      

 
        self.my_c2pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\{0}'.format(myc2))
        self.my_c2pix=self.my_c2pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c2.setPixmap(self.my_c2pix)
   


        self.my_c3pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.my_c3pix=self.my_c3pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c3.setPixmap(self.my_c3pix)
 

 
        self.my_c4pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.my_c4pix=self.my_c4pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c4.setPixmap(self.my_c4pix)
   

       
        self.my_c5pix=QPixmap('E:\\Nguyen Trong Dat\\Cards for Python project\\blankslot')
        self.my_c5pix=self.my_c5pix.scaled(200,200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.my_c5.setPixmap(self.my_c5pix)

        self.resultlabel.setText('')
    




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
     
    BlackJack = BlackJack()
     
    sys.exit(app.exec_())
     

 