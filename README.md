Work Done-
The repo contains rough work done during the opencv course and also the code done along with the week two tutorials. 
All the 21 points on the palm were detected and stored in a list along with draing the lines on the live record coming from the webcam using the hands module done in the handtrackingmodule.
Finger is up is identified using the coordinates of the adjacent points on each finger done in the gesture.py. 
Volume control module was also done in the volumehandcontrol.py. 
Gestures were identified using finger up code and pinch ratio was calculated for the 'ok' gesture. This was used in the test_gesture file

Challenges-
Webcam was not starting initially, had an issue but got resolved.
The new and old mediapipe issue took much long to resolve even though the soln was already told(had to use claude for it).
In Volume Control code, camera shut out when distance between 4 and 8 was more than I assumed.
Resolved just by adding an if statement. And did also tons of syntax errors.
Still have issues installing the file to GitHub. Had to uninstall and again install the mediapipe multiple times because it became corrupt during commiting the files to git :)

Milestones-
All the five gestures are identified till now that are needed for the game. Also added some more gestures myself for fun. Sorry for that.
