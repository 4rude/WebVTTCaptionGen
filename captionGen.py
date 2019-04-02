# Example input variables:
# Ex. endSecond = 6000
# Ex. filePath = "images/thumbs/thumb"
def webvttCaptionGenerator(endSecond, filePath):

	# This application could have been written to be a lot shorter (more dynamic), however it still works. 
	# This webvtt caption generator generates captions for videos roughly 1 hour and 39 minutes in length.
	# The output of this application is printed to the console. You then will want to copy the console text and 
	# paste it into a file named: thumbs.vtt 
	# This algorithm would optimally output the data into a .vtt file. (TODO)

	# Default start second. This usually wouldn't change. 
	startSecond = 1 
	# The endSecond variable is determined by the user

	# First initialization of num1 - 8 & counterA & B. These are all mainly counters.
	num1 = 0
	num2 = 1
	num3 = 0
	num4 = 0
	num5 = 0
	num6 = 0
	num7 = 0
	num8 = 0
	counterA = 1
	counterB = 1

	# Number of first thumbnail (created with )
	thumbNum = 1

	# Used to start the webvtt file, which is used to display thumbnails created by the ffmpeg (command line/terminal) tool. This is easy to use tool on the MacOS, Window, and Linux platforms.
	# If you need help creating thumbnails for your video this link is a good start: https://stackoverflow.com/questions/8679390/ffmpeg-extracting-20-images-from-a-video-of-variable-length
	print("WEBVTT\n")

	# For loop to run through each thumbnail (var i is each thumbnail)
	for i in range(startSecond, endSecond):

		# 
		if num1 == 60:
			num1 = 0
		elif num2 == 60:
			num2 = 0


		if i == 61:
			num3 += 1
			num1 = 0

		if i == 60:
			num4 += 1
			num2 = 0

		#experiment
		if i > 121:
			counterA += 1

		if i > 122:
			counterB += 1

		if ((counterA % 60) == 0):
			num4 += 1
			num2 = 0

		if ((counterB % 60) == 0):
			num3 += 1
			num1 = 0

		if i == 1:
			print("00:0" + str(num1) + ".000 --> 00:0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i > 1 and i < 10:
			print("0" + str(num3) + ":0" + str(num1) + ".100 --> 0" + str(num4) + ":0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i == 10:
			print("0" + str(num3) + ":0" + str(num1) + ".100 --> 0" + str(num4) + ":" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i > 10 and i < 60:
			print("0" + str(num3) + ":" + str(num1) + ".100 --> 0" + str(num4) + ":" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i == 60:
			print("0" + str(num3) + ":" + str(num1) + ".100 --> 0" + str(num4) + ":0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i == 61:
			print("0" + str(num3) + ":0" + str(num1) + ".100 --> 0" + str(num4) + ":0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i > 61 and i < 70:
		#if num1 > 9 and num2 > 9:
			print("0" + str(num3) + ":0" + str(num1) + ".100 --> 0" + str(num4) + ":0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i == 70:
			print("0" + str(num3) + ":0" + str(num1) + ".100 --> 0" + str(num4) + ":" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i == 71:
			print("0" + str(num3) + ":" + str(num1) + ".100 --> 0" + str(num4) + ":" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")
		if i > 71 and i < 120:
			print("0" + str(num3) + ":" + str(num1) + ".100 --> 0" + str(num4) + ":" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		#edit
		if i == 120:
			print("Hello")
			counterA = 1
			num4 += 1
			num2 = 0
			print("0" + str(num3) + ":" + str(num1) + ".100 --> 0" + str(num4) + ":0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i == 121:
			counterB = 1
			num3 += 1
			num1 = 0
			print("0" + str(num3) + ":0" + str(num1) + ".100 --> 0" + str(num4) + ":0" + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i > 121 and i < 600:
			if num2 == 10:
				num6 = ""
			if num1 == 10:
				num5 = ""
			if num2 == 0:
				num6 = 0
			if num1 == 0:
				num5 = 0
			print("0" + str(num3) + ":" + str(num5) + str(num1) + ".100 --> 0" + str(num4) + ":" + str(num6) + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

		if i >= 600:
			if num2 == 10:
				num6 = ""
			if num1 == 10:
				num5 = ""
			if num2 == 0:
				num6 = 0
			if num1 == 0:
				num5 = 0

			num8 = ""

			print(str(num7) + str(num3) + ":" + str(num5) + str(num1) + ".100 --> " + str(num8) + str(num4) + ":" + str(num6) + str(num2) + ".100" + "\n" + filePath + "" + str(thumbNum) + ".jpg\n")

			num7 = ""

		# This should happen every iteration 
		num1 += 1
		num2 += 1
		thumbNum += 1
