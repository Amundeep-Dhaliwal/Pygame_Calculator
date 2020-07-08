import pygame, math
pygame.init()
pygame.font.init()

width, height = 400, 800
icon = pygame.image.load(r'C:\Users\Amundeep\Pictures\Camera Roll\calculator.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Amun\'s Calculator')
screen = pygame.display.set_mode((width, height))
background = (105,105,105)
white = (255,255,255)
black = (0,0,0)
class Display:
    def __init__(self, color, x, y, width, height, screen):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.calc = ''
        self.ans = None
        self.store_calc = None
        self.store_ans = None
    
    def draw(self, key=''):
        pygame.draw.rect(self.screen, self.color, (int(self.x), int(self.y), int(self.width), int(self.height)), 0)
        font = pygame.font.SysFont('comicsans', 20)
        
        if key == 'AC':
            self.store_calc = self.calc
            self.store_ans = self.ans
            self.ans = None
            self.calc = ''
            return
        elif key == 'DEL':
            self.calc = self.calc[:-1]
            return
        elif key == '=' and self.calc == '':
            return
        elif key == '=':
            for i in (self.calc):
                if i == '×':
                    self.calc =self.calc.replace('×', '*')
                elif i == '÷':
                    self.calc = self.calc.replace('÷', '/')  
            self.ans = eval(self.calc)
            return
            
        self.calc += key
        if self.calc:
            calc = font.render((self.calc), 1, black)
            self.screen.blit(calc, (int(self.x +10), int(self.y +10)))
        if self.ans:
            ans = font.render(str(self.ans), 1,black)
            self.screen.blit(ans, (int((self.x+self.width) -20), int((self.y +self.height) -20)))
           
        #print(self.calc)
        pygame.display.update()


class Button():
    def __init__(self, color,text_color,pressed, x, y, width, height, screen,display, symbol,size = 50):
        self.color = color
        self.text_color = text_color
        self.pressed = pressed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.display = display
        self.symbol = symbol
        self.size = size
        
    
    def draw(self, clicked = False):
        if clicked: 
            #print(self.symbol)
            self.display.draw(self.symbol)
            pygame.draw.rect(self.screen, black, (int(self.x - 2), int(self.y - 2), int(self.width + 4), int(self.height +4)))
            pygame.draw.rect(self.screen, self.pressed, (int(self.x), int(self.y), int(self.width), int(self.height)))
        else:
            pygame.draw.rect(self.screen, background, (int(self.x - 2), int(self.y - 2), int(self.width + 4), int(self.height +4)))
            pygame.draw.rect(self.screen, self.color, (int(self.x), int(self.y), int(self.width), int(self.height)))
        
        font = pygame.font.SysFont('comicsans', self.size)
        text = font.render(self.symbol, 1, self.text_color)
        self.screen.blit(text, (int(self.x + (self.width - text.get_width())/2), int(self.y + ((self.height - text.get_height())/2))))
        
        pygame.display.update()
        #pygame.time.delay(1)

    def hover(self, pos):
        # for the rollover effects
        if self.x <= pos[0] <= self.x +self.width and self.y <= pos[1] <= self.y +self.height:
            return True
    
    def clicked(self,x,y):
        if self.x < x < self.width + self.x and self.y < y < self.height + self.y:
            return True
    


def main():
    global screen
    run = True

    display = Display((143,220,156), 5, 50, 390, 150, screen)

    button_0 = Button(white,black,(169,169,169), 10, 750, 40,40, screen,display, '0')
    button_1 = Button(white,black,(169,169,169), 10, 700, 40,40, screen,display, '1')
    button_2 = Button(white,black,(169,169,169), 60, 700, 40,40, screen,display, '2')
    button_3 = Button(white,black,(169,169,169), 110, 700, 40,40, screen,display, '3')
    button_4 = Button(white,black,(169,169,169), 10, 650, 40,40, screen,display, '4')
    button_5 = Button(white,black,(169,169,169), 60, 650, 40,40, screen,display, '5')
    button_6 = Button(white,black,(169,169,169), 110, 650, 40,40, screen,display, '6')
    button_7 = Button(white,black,(169,169,169), 10, 600, 40,40, screen,display, '7')
    button_8 = Button(white,black,(169,169,169), 60, 600, 40,40, screen,display, '8')
    button_9 = Button(white,black,(169,169,169), 110, 600, 40,40, screen,display, '9')
    button_dot = Button(white,black,(169,169,169), 60, 750, 40,40, screen,display, '.')
    
    button_mul = Button(white,black,(169,169,169), 300, 650, 40,40, screen,display, '×')
    button_add = Button(white,black,(169,169,169), 300, 700, 40,40, screen,display, '+')
    button_div = Button(white,black,(169,169,169), 350, 650, 40,40, screen,display, '÷')
    button_sub = Button(white,black,(169,169,169), 350, 700, 40,40, screen,display, '-')

    button_ac = Button((0,0,255),black,(169,169,169), 350, 600, 40,40, screen,display, 'AC', 20)
    button_del = Button((0,0,255),black,(169,169,169), 300, 600, 40,40, screen,display, 'DEL', 20)
    button_eq = Button(white,black,(169,169,169), 350, 750, 40,40, screen,display, '=')

    button_op = Button(black,white,(169,169,169), 60, 550, 40,40, screen,display, '(')
    button_cl = Button(black,white,(169,169,169), 110, 550, 40,40, screen,display, ')')

    screen.fill(background)
    while run:
        #key = None
        display.draw()
        button_dot.draw()
        button_0.draw()
        button_1.draw()
        button_2.draw()
        button_3.draw()
        button_4.draw()
        button_5.draw()
        button_6.draw()
        button_7.draw()
        button_8.draw()
        button_9.draw()

        button_mul.draw()
        button_add.draw()
        button_div.draw()
        button_sub.draw()

        button_ac.draw()
        button_del.draw()
        button_eq.draw()

        button_cl.draw()
        button_op.draw()
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            # quit calculator
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PERIOD or event.key == pygame.K_PERIOD:
                    button_dot.draw(True)

                if event.key == pygame.K_KP0:
                    button_0.draw(True)

                if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    button_1.draw(True)
                    
                if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    button_2.draw(True)
                    
                if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    button_3.draw(True)
                    
                if event.key == pygame.K_KP4 or event.key == pygame.K_4:
                    button_4.draw(True)
                    
                if event.key == pygame.K_KP5 or event.key == pygame.K_5:
                    button_5.draw(True)

                if event.key == pygame.K_KP6 or event.key == pygame.K_6:
                    button_6.draw(True)
                
                if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                    button_7.draw(True)

                if event.key == pygame.K_KP8 or event.key == pygame.K_8:
                    button_8.draw(True)

                if event.key == pygame.K_KP9:
                    button_9.draw(True)
                
                if event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK:
                    button_mul.draw(True)
                
                if event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
                    button_add.draw(True)
                
                if event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
                    button_div.draw(True)
                
                if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                    button_sub.draw(True)


                if event.key == pygame.K_DELETE:
                    button_ac.draw(True)

                if event.key == pygame.K_BACKSPACE:
                    button_del.draw(True)

                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_EQUALS:
                    button_eq.draw(True)
                
                if event.key == pygame.K_9:
                    button_op.draw(True)
                
                if event.key == pygame.K_0:
                    button_cl.draw(True)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_dot.clicked(pos[0], pos[1]):
                    button_dot.draw(True)
                
                if button_0.clicked(pos[0], pos[1]):
                    button_0.draw(True)
                
                if button_1.clicked(pos[0], pos[1]):
                    button_1.draw(True)
                    
                if button_2.clicked(pos[0], pos[1]):
                    button_2.draw(True)
                    
                if button_3.clicked(pos[0], pos[1]):
                    button_3.draw(True)
                    
                if button_4.clicked(pos[0], pos[1]):
                    button_4.draw(True)
                    
                if button_5.clicked(pos[0], pos[1]):
                    button_5.draw(True)
                
                if button_6.clicked(pos[0], pos[1]):
                    button_6.draw(True)
                    
                if button_7.clicked(pos[0], pos[1]):
                    button_7.draw(True)

                if button_8.clicked(pos[0], pos[1]):
                    button_8.draw(True)

                if button_9.clicked(pos[0], pos[1]):
                    button_9.draw(True)
                
                if button_mul.clicked(pos[0], pos[1]):
                    button_mul.draw(True)

                if button_add.clicked(pos[0], pos[1]):
                    button_add.draw(True)

                if button_div.clicked(pos[0], pos[1]):
                    button_div.draw(True)

                if button_sub.clicked(pos[0], pos[1]):
                    button_sub.draw(True)
                
                if button_ac.clicked(pos[0], pos[1]):
                    button_ac.draw(True)
                
                if button_del.clicked(pos[0], pos[1]):
                    button_del.draw(True)
                
                if button_eq.clicked(pos[0], pos[1]):
                    button_eq.draw(True)

                if button_op.clicked(pos[0], pos[1]):
                    button_op.draw(True)
                
                if button_cl.clicked(pos[0], pos[1]):
                    button_cl.draw(True)
        
        # if key != None:
        #     display.draw(key)
            
        

        pygame.display.update()

main()