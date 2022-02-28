# The code is written by Pulkit Dhingra 

# importing required libraries
import time
import threading

# Solution algorithm
class indicator():
  
  # constructor
  def __init__(self):

    # The lately_on variable will indicate wether the indicator was on earlier or not
    self.lately_on=False

  # Function to check if the indicator is required or not
  def turn_indicator(self, y):
    
    # if 0 or close to 0
    if y == 0 or y <= 0.005 and y >= -0.005:
      return False

    # else return 0, not close to zero turn detected
    else:
      return True

  # function determining the indicator direction
  def indicator_direction(self, y):
    if y < 0:
      return "Right"
    else:
      return "Left"

  # indicator intensity
  def intensity(self, y):

    # if the indicator was on currently
    if self.lately_on:

      # turn off the lately on
      self.lately_on = False

      # return the lv 2 indicator setting
      return 2
    
    # not lately on
    else:

      # check for lv1 setting
      if y > 0.005 and y <= 1 or y < -0.005 and y > -1 :
        
        # Turn on the lately on key
        self.lately_on = True

        # return the lv1
        return 1
      
      # lv 2 setting
      else:

        # if lately_on was currently active        
        if self.lately_on:
          
          # Turn off the lately on
          self.lately_on = False

        # if lately_on was not active
        # the indicator was not active earlier
        else:

          # Turn on the lately on
          self.lately_on = True

        # return lv2 setting
        return 2
  
  # function for display and maintaing time duration
  def time_lv(self,level,direction):

    # start timing
    start=time.time()
    
    # for lv1 intensity indicators
    if level==1:

      # stop timing is 10 sec + start
      stop=start+10

      # loop over for 10 sec
      while start!=stop:

        print(direction)
        
        # incrimenting start timing
        start+=1
        
        # sleep for a second
        #time.sleep(1)
    
    else:

      # stop timing is 150 sec + start
      stop=start+150
      
      # loop over for 150 sec
      while start!=stop:

        print(direction)
        
        # incriment start
        start+=1
        
        # sleep for a sec
        #time.sleep(1)

    return self.lately_on

  # controlling the lately_on activation time
  def lately_on_controller(self):

    # start timer
    start=time.time()
    
    # timer for five seconds
    stop = start+5

    # loop over to take 5 second
    while start != stop:
      time.sleep(1)
    
    # Set lately_on to false if no activity
    self.lately_on=False 



