How to install opencv:


Under CV folder: 
git clone git clone https://github.com/opencv/opencv.git
cd opencv
git checkout remotes/origin/3.4

Under CV folder: 
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout remotes/origin/3.4

Under CV folder:
cd opencv
mkdir build
cmake ../
cmake WITH_GTK=ON PYTHON_EXECUTABLE=/user/bin/python3.6 ../


Add opencv-python library into python3.7:
pip3 install opencv-python

Run .py:
(venv) [hwa150@cs18229kq ~/Downloads/CV/lab01]$ python3.6 load_video_file.py 
