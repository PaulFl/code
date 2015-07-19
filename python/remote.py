import XboxController
import socket

TCP_IP = '192.168.0.14'
TCP_PORT = 3000

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendSocket.connect((TCP_IP, TCP_PORT))

def callback(controlId, value):
	print("Id: ")
	print(controlId)
	print("	")
	print("value: ")
	print(value)

def XAxisCallback(value):
	print("XValue: ", value)
	sendSocket.send(str(value))


def YAxisCallback(value):
	print("YValue: ", value)
	sendSocket.send(str(value))


xboxCont = XboxController.XboxController(
		controllerCallBack = None,
		joystickNo = 0,
		deadzone = 0.1,
		scale = 1,
		invertYAxis = True)

xboxCont.setupControlCallback(
		xboxCont.XboxControls.LTHUMBX,
		XAxisCallback)

xboxCont.setupControlCallback(
		xboxCont.XboxControls.LTHUMBY,
		YAxisCallback)



xboxCont.start()
