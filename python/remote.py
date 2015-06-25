import XboxController


def callback(controlId, value):
	print("Id: ")
	print(controlId)
	print("	")
	print("value: ")
	print(value)

xboxCont = XboxController.XboxController(
		controllerCallBack = callback,
		joystickNo = 0,
		deadzone = 0.1,
		scale = 1,
		invertYAxis = False)


xboxCont.start()
