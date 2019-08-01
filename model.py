import controller, sys
import model   # Pass a reference to this module to each update call in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = -1 
simultons = set()
selected_type = None
step = False



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global cycle_count, simultons, running, step, selected_type
    running = False
    cycle_count =  0
    step = False
    selected_type = None
    simultons.clear()


#start running the simulation
def start ():
    global running 
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running 
    running = False


#tep just one update in the simulation
def step ():
    global step 
    step = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_type
    selected_type = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global simultons
    if selected_type == 'Remove':
        rmv = set() # make a set of items to remove and then remove them - if remove while iter through simultons
                    # set, will cause an exception because cannot modify while itering.
        for s in simultons:
            if s.contains((x, y)):
                rmv.add(s)
        for s in rmv:
            simultons.remove(s)
    elif selected_type != None:
        add(eval('{}({}, {})'.format(selected_type, x, y)))
    else:
        print('No simulton type selected')


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    simul = set()
    for s in simultons:
        if p(s):
            simul.add(s)
    return simul


#call update for each simulton in the simulation (pass the model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global step, running, simultons, cycle_count
    if step or running: 
        cycle_count += 1 
        temp_simul = set(simultons)
        for s in temp_simul: 
            if s in simultons: 
                s.update(model)
        if step: 
            step = False
            running = False
        


#delete from the canvas every simulton being simulated; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    for s in simultons: 
        s.display(controller.the_canvas)
