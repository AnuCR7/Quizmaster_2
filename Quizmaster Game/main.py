import pgzrun
WIDTH=870
HEIGHT=670
TITLE='Quizmaster Game'

qfile='questions.txt'
questions=[]
question_count=0
question_index=0
time_left=10
score=0
is_game_over=False

mbox=Rect(0,0,880,80)
mbox.move_ip(0,0)

qbox=Rect(0,0,650,150)
qbox.move_ip(20,100)

tbox=Rect(0,0,150,150)
tbox.move_ip(700,100)

tibox=Rect(0,0,150,350)
tibox.move_ip(700,300)

abox1=Rect(0,0,300,150)
abox1.move_ip(20,300)

abox2=Rect(0,0,300,150)
abox2.move_ip(20,500)

abox3=Rect(0,0,300,150)
abox3.move_ip(370,300)

abox4=Rect(0,0,300,150)
abox4.move_ip(370,500)

answerbox=[abox1,abox2,abox3,abox4]

def draw ():
    global time_left
    screen.clear()
    screen.fill('blue')
    screen.draw.filled_rect(mbox,'blue')
    screen.draw.filled_rect(qbox,'orange')
    screen.draw.filled_rect(tibox,'dark green')
    screen.draw.filled_rect(tbox,'green')
    for i in answerbox:
        screen.draw.filled_rect(i,'yellow')
    m_message='Welcome to Quizmaster!'
    screen.draw.textbox(m_message,mbox,color='white')
    screen.draw.textbox('Skip',tibox,color='white',angle=-90)
    screen.draw.textbox(str(time_left),tbox,color='white',shadow=(0.5,0.5),scolor='black')
    screen.draw.textbox(qreturn[0],qbox,color='white')
    index=1
    for i in answerbox:
        screen.draw.textbox(qreturn[index],i,color='white')
        index=index+1
    
def move_message():
    mbox.x=mbox.x-2
    if mbox.right < 0:
        mbox.left=WIDTH

def read_questions():
    global question_count, question_index ,questions
    q=open(qfile,'r')
    for qu in q:
        questions.append(qu)
        question_count=question_count+1
    q.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(',')

def on_mouse_down (pos):
    global answerbox
    index=1
    for i in answerbox:
        if i.collidepoint(pos):
            if index is int(qreturn[5]):
                correct_answer()
            else:
                Game_Over()
        index=index+1
    if tibox.collidepoint(pos):
        skip_question()

            

def correct_answer():
    global score, qreturn, questions, time_left
    score=score+1
    if questions:
        qreturn=read_next_question()
        time_left=10
    else:
        Game_Over()
    

    
def Game_Over():
    global score, time_left, questions, is_game_over
    message=f'Game Over! \n You scored{score}'
    time_left=0
    questions=[message,'-','-','-','-',5]
    is_game_over=True

def skip_question():
    global time_left,questions,qreturn
    if questions and not is_game_over:
        qreturn=read_next_question()
        time_left=10
    else:
        Game_Over()

def update_timer():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        Game_Over()

def update():
    move_message()
read_questions()
qreturn=read_next_question()
clock.schedule_interval(update_timer,1)
pgzrun.go()