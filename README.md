#Radiacode-Gamma-Spectroscopy #gamma-spectroscopy

[demo] (https://youtu.be/LSACMZD3J_g)

This is a python program to Gamma Spectroscopy analysis for Radiacode devices. This program only works with .XML exports of the data. The XML export has device calibration data which is needed for converting channel numbers into keV. To run download Main.py, install the requirements with pip3, move the XML files to the same directory, then run Main.py. On start up Main.py looks for XML file in its current working directory and then lists them. After selecting a file Main.py will convert all of the channel numbers into keV, list the raw data, display some basic data, then it launch gui histogram usning matplotlib.pyplot

Requirements:
Pyhton 3.10+
  BeautifulSoup4
  matplotlib
  lxml
