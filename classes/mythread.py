# -*- coding: UTF-8 -*-

import re
import blocks
import myservo

def get_center_stick():
	center = {'x': 0, 'y': 0}
	center['x'] = blocks.block.x + (blocks.block.width / 2)
	center['y'] = blocks.block.y + (blocks.block.height / 2)

	return center

def run_color_code_thread(serialServo):
	while 1:
		center = get_center_stick()

		if center['x'] > 200 and center['x'] < 285: 
			#print "rotate left"
			myservo.servoPos['rotationPos'] -= 1
		elif center['x'] > 0 and center['x'] < 200: 
			#print "base left"
			myservo.servoPos['basePos'] -= 1
		elif center['x'] > 355 and center['x'] < 440:
			#print "rotate right"
			myservo.servoPos['rotationPos'] += 1
		elif center['x'] > 440 and center['x'] < 640:
			#print "base right"
			myservo.servoPos['basePos'] += 1
		else:
			#print "deadzone x"
			pass

		if center['y'] > 0 and center['y'] < 175:
			#print "head up"
			myservo.servoPos['headPos'] -= 1
		elif center['y'] > 225 and center['y'] < 400:
			#print "head down"
			myservo.servoPos['headPos'] += 1
		else:
			#print "deadzone y"
			pass

		serialServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))

def run_voice_thread(brain, fSM, serialServo, serialLed):
	while 1:

		brain.ledRingColor['red'] = 5
		brain.ledRingColor['green'] = 30
		brain.ledRingColor['blue'] = 5
		
		serialServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
		serialLed.write("%s, %s, %s" % (brain.ledRingColor['red'], brain.ledRingColor['green'], brain.ledRingColor['blue']))
		

		input = brain.mic.active_listen()
		print input
		if re.search(r'\b(power down|powerdown)\b', input, re.IGNORECASE):
			fSM.to_transition("toShutdown")
			break
		elif re.search(r'\b(dankje|tot ziens)\b', input, re.IGNORECASE):
			brain.speaker.say("graag gedaan. Bye Bye")
			fSM.to_transition("toScanning")
			break
		else:
			brain.ledRingColor['red'] = 30
			brain.ledRingColor['green'] = 5
			brain.ledRingColor['blue'] = 5
			
			serialServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
			serialLed.write("%s, %s, %s" % (brain.ledRingColor['red'], brain.ledRingColor['green'], brain.ledRingColor['blue']))
			
			
			brain.query(input)