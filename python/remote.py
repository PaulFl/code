import XboxController


def callback(controlId, value):
	print("Id: ")
	print(controlId)
	print("	")
	print("value: ")
	print(value)

def XAxisCallback(value):
	print("XValue: ", value)

def YAxisCallbacl(value):
	print("YValue: ", value)

xboxCont = XboxController.XboxController(
		controllerCallBack = None,
		joystickNo = 0,
		deadzone = 0.1,
		scale = 1,
		invertYAxis = False)

xboxCont.setupControlCallback(
		self.xboxCont.XboxControls.LTHUMBX,
		XAxisCallback)

xboxCont.setupControlCallback(
		self.xboxCont.XboxControls.LTHUMBY,
		YAxisCallback)



xboxCont.start()
