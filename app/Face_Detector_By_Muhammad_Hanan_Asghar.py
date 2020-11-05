import streamlit as st
import cv2
from PIL import Image
import numpy as np


# Reading Image
def detect(IMG):

	# Reading HaarCascade File
	clf = cv2.CascadeClassifier("frontalface_haarcascade.xml")

	# Detecting Face
	face = clf.detectMultiScale(IMG, 1.3, 5)
	for x, y, w, h in face:
		# Adding Rectangle
		image = cv2.rectangle(IMG, (x, y), (x+w, y+h), (255,0,0), 2)

	return (image, len(face))




def main():
	st.title('Face Detector By Muhammad Hanan Asghar')
	st.set_option('deprecation.showfileUploaderEncoding', False)
	hide_menu_style = """
        	<style>
        	#MainMenu {visibility: hidden;}
 		footer {visibility: hidden;}       
		</style>
        	"""
	st.markdown(hide_menu_style, unsafe_allow_html=True)
	
	# Side bar
	activities = ["Home","About"]
	choice = st.sidebar.selectbox("Pick Something Fun", activities)

	if choice == "Home":
		st.write("Using Computer Vision with Python")
		image_file = st.file_uploader("Upload Image", type=['jpeg', 'png', 'jpg'])
		if image_file is not None:
			if st.button("Process"):
				try:
					imag = np.array(Image.open(image_file).convert("RGB"))
					print(imag)
					result_image, faces = detect(imag)
					st.image(result_image, caption="Image After Processing", use_column_width = True)
					st.success(f"Found {faces} Faces")
				except:
					st.warning("Error in Processing the Image")
	elif choice == "About":
		st.write("Hi, My Name is Muhammad Hanan Asghar.I make this project if you want to get the source files of this project then go to this URL : ")
		github_url = """
			<a href="https://github.com/MuhammadHananAsghar" target='_blank'>Muhammad Hanan Asghar</a>
		"""
		st.markdown(github_url, unsafe_allow_html=True)

if __name__ == "__main__":
	main()
