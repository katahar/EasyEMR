# Inspiration
A significant problem faced by medical professionals is quickly accessing a patient's medical records for important information that will direct future diagnoses and treatments. The following are examples of situations in which providers may need access to a patient's medical records: when a patient has conditions that are managed by multiple specialists; when a patient moves and seeks medical care from a different medical provider; or during a medical emergency when it is not possible to ask the patient or their family about pertinent medical history. In these situations, the typical course of accessing the patient's medical records in a HIPPA-compliant manner involves asking the patient to sign a release of medical records form, faxing it to the medical office/hospital where the patient's records are located, and waiting to receive the patient's medical records via fax. This entire process is often tedious and time-consuming, often taking weeks or months to receive a patient's medical records, preventing or delaying the patient from receiving time-sensitive and medically essential care. In medical emergencies, quick access to patient medical records can provide essential information that could mean the difference between life and death. Clearly, there is an immense need in the medical field for secure (HIPPA-compliant), instant access to a patient's medical records.

# What it does
Easy EMR solves this problem by utilizing an RFID mechanism for access to a patient's medical records, directly at the patient's fingertips through a stylish, wearable bracelet. With a quick tap of the RFID bracelet on the healthcare provider's special receiver, their entire medical record can be instantly and securely viewed and edited, eliminating the time-consuming process of accessing medical records via fax and helping healthcare professionals provide life-saving care! This system can also be incorporated into a network of "smart" medical devices (such as at-home pill dispensers, blood pressure monitors, glucose monitors, heart rate monitors, and more), creating a daily log of a patient's health profile for personal use and to aid their medical providers. In short, if implemented on a larger scale, our design aims to create a centralized patient information database while allowing the patients to document their medical activities such as taking medications so that their medical providers can track their progress and history more easily and accurately.

# How we built it
The device is composed of Raspberry pi, servo, Arduino, and RFID sensors. The RFID sensor is connected to the Arduino which sends the RFID information over to the Raspberry pi via serial port. The Raspberry pi parses the RFID data to determine the information on the RFID card. Then update the information on the server accordingly, which is built with Flask. For demo purposes, the servo drives a pill dispenser which will turn on when the patient scans the RFID. And this activity will be reflected on the patient's record.

# Challenges we ran into
The first challenge wasthe time constraint. This project has many components and they all had to work synchronously within the time limit. For instance, the pill dispenser would have been better if it were designed in Solidworks and assembled with some custom parts. Considering the time limit, we used the material available to us and made the dispenser prototype from household objects. Second, some components broke in the process of construction, which took us a long time to debug the system. For example, there was a problem with the raspberry SPI port which caused the communication problem with the RFID sensor. Hence we had to make some necessary changes to the system by wiring the RFID sensor to an Arduino, which sends the data via serial. We had some challenges with setting up the Flask server, which would have ideally connected to the pill dispenser over the network. For the sake of time, we hardwired it to the Pi.

# Accomplishments that we're proud of
We are very proud that we were able to achieve the basic functions and demonstrate the concept of our design within the time limit. Even though there could be many improvements on the system, the prototype is functional enough to show the proof of concept. Each team member worked on an aspect completely new to them, making the realization of the project especially challenging. We had the opportunity to merge the field of medicine and engineering and fuse a medical concept into an actual engineering prototype!

# What we learned
Most of the team members do not have prior experience with hackathons, so it was a very valuable learning experience for us. In the process of building the system, we realized that the original goal was ambitious and might be out of reach due to the time constraint so we modified the goal accordingly.

The team has a very diverse background. It was a very thrilling and fun journey for us, engineering and medical students to collaborate on the same project and deliver the prototype that has medical applicability as well as practical engineering elements.

# What's next
The ultimate goal of this project is to implement the system on a larger scale. The patient only needs to wear the bracelet (For instance, this can be integrated into the current smark watch products such as apple watch, Fitbit, etc) and all the data will be stored on a HIPPA-compliant cloud server. The patient only needs to tap other smart medical devices and the history will be automatically documented and uploaded to the cloud so that the medical provider could easily track the progress. Take the pill dispenser that we used for our demo as an example. The patient will tap the smart wrist band and the dispenser will dispense the pills while also recording the activity. Later when the patient visits the medical provider, the provider only needs to scan the patient's smart wrist band to pull the medical record from the cloud server to view what pills/frequency the patient is taking
