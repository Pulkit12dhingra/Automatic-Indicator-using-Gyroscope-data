# required libraries import

from flask import Flask, render_template, request
import algorithm
import time
import threading

# start the flask app engine
app = Flask(__name__)


# load the index page
@app.route("/")
def home():
    filename="both_off"
    strd="static/images/{}.jpg".format(filename)
    return render_template("/index.html", info=strd)


# get input form data and do computation
@app.route("/get_data",methods=['GET'])
def get_data():

    # x y z coordinates of gyroscope reading
    x = request.args['x']
    y = request.args['y']
    z = request.args['z']

    # check if the user has inputed anything
    if x != "" and y!= "" and z!= "":

        # get the direction 
        filename= algo(float(y))

        # display the directon
        strd="static/images/{}.jpg".format(filename)
        return render_template("/index.html", info=strd)
    
    else:
        
        # if data is incomplete
        filename="both_off"
        strd="static/images/{}.jpg".format(filename)
        return render_template("/index.html", pnfo="Enter the details", info=strd)

    


# the algorithm
def algo(Y):
  # take the X coord Y coord and Z coord readings 
  # object
  ather=algorithm.indicator()

  # check if we need to turn on the indicator or not
  if ather.turn_indicator(Y):

    
    # Get the direction of the indicator where we need to turn
    dir=ather.indicator_direction(Y)
    
    # Get the intensity of indicator
    inten=ather.intensity(Y)

    # Turn the indicator on
    on=ather.time_lv(inten,dir)

    # if the lately_on is active
    if on:
      
      # start a thread to monitor the next activity
      # if no idicator is activated for next five seconds 
      # the lately_on will be automatically be reset to False
      t1=threading.Thread(target=ather.lately_on_controller)
    
    # lately_on is not active
    else:
      pass

  # indicator is not active
  else:
    pass
  return dir

if __name__ == "__main__":
    app.debug=False
    app.run()