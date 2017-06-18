# template for "Stopwatch: The Game"
import simplegui
import time


# define global variables
interval=100
now=0
running = False
total=0
win=0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(i):
    
    D=i%10
    BC=(i//10)%60
    C=BC%10
    B=BC//10
    A=(i//10)//60
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
  
    running= True
  
    
def stop():
    global running
    global total
    global now
    global win
    if running:
         
        running=False
        total+=1
        if now%10==0:
            win+=1
        
   

def reset():
    stop()
    global now
    global total
    global win
    now=0
    total=0
    win=0





# define event handler for timer with 0.1 sec interval
def update_time():
    global now
    if running :
   
        now=now+1
    





# define draw handler
def draw_handler(canvas):
   
    canvas.draw_text(format(now), (250,250), 50, 'Green')
    canvas.draw_text((str(win)+"/"+str(total)),(400,40),30,'Red')
    
    
# create frame
frame = simplegui.create_frame('Stopwatch ', 500, 500)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, update_time)
button1 = frame.add_button('Start', start,50)
button2 = frame.add_button('Stop', stop, 50)
button2 = frame.add_button('Reset',reset, 50)



# register event handlers


# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric

