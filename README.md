# Radiacode-Gamma-Spectroscopy

This is a python program to do Gamma Spectroscopy analysis, specifically for Radiacode devices. This program only works with XML exports of the data. The XML export has device calibration data which is needed for converting channel numbers into keV. On start-up Main.py looks for XML files in its current working directory and then lists them. After selecting a file Main.py will convert all of the channel numbers into keV, list the raw data, display some basic data, then it launches a GUI histogram usning the matplotlib.pyplot Python library.

## Demo
https://github.com/user-attachments/assets/f8b5f8c6-3405-4ba5-aef5-11b650c0ac0e

## Requirements
Pyhton 3.10+
- BeautifulSoup4
- matplotlib

## Install
Download Main.py, install the requirements with pip3, move the XML files to the same directory, then run Main.py. 
