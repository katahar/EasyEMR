'''
    Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
import variable
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')  # still relative to module
   
@app.route("/")
def index():
    # Read Sensors Status
    patientArray = [["Tim", "3.29.02", "Male", "132 North Ave",
                    "50 lbs", " 60 in ", "Penecillin",
                    "Diabetes on Father's side", "Lisinopril", "10.25.12, 10.26.12"],
                    ["Jenny", "3.19.02", "Female", "132 South Ave",
                    "50 lbs", " 55 in ", "Allergic to Shellfish",
                    "Hypertension", "Metformin", "1.21.12, 1.21.12"]]
    
    
    index = 0
    redInd= ""
    if True:
        with open("/home/pi/Desktop/PitttChallengeVersion 2/patientID.data","r") as patID:
            inputS = patID.read()
            
            parsed = inputS.split(" ",1)
            redInd =parsed[0]
            parsed = parsed[1]
            #print(parsed)
            print(redInd)
            
            time = parsed[1:]
            #print(time)
            patID.close()   
    if(redInd =="21521120095"):
         index = 0
    else:
         index = 1
    templateData = {
              'name' : patientArray[index][0],
              'patientID': redInd,
              'DOB'  : patientArray[index][1],
              'Gender'  : patientArray[index][2],
              'Address'  : patientArray[index][3],
              'Weight'  : patientArray[index][4],
              'Height'  : patientArray[index][5],
              'Allergies'  : patientArray[index][6],
              'Hist'  : patientArray[index][7],
              'Meds' : patientArray[index][8],
              'PUpdate' : patientArray[index][9]
            
}
    return render_template('index.html', **templateData)
  
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

