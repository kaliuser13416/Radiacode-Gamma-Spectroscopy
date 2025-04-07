import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import lxml
import os

def plot_data():
    plt.bar(pos, DataPoints)
    plt.title('Spectrum')
    plt.xlabel('keV')
    plt.show()

def import_xml(xml_in):
    with open(xml_in, 'r') as raw_data:
        raw = raw_data.read()
    Bs_data = BeautifulSoup(raw, "xml")
    channel = 0
    SUM = 0
    list_coefficients = []
    
    spectrum = str(Bs_data.find('Spectrum'))
    spectrum = spectrum.replace('</Spectrum>', '')
    spectrum = spectrum.replace('<Spectrum>', '')
    spectrum = spectrum.replace('<DataPoint>', '')
    spectrum = spectrum.replace('</DataPoint>', '')
    
    coefficients = str(Bs_data.find('Coefficients'))
    coefficients = coefficients.replace("<Coefficients>","")
    coefficients = coefficients.replace("</Coefficients>","")
    coefficients = coefficients.replace("<Coefficient>","")
    coefficients = coefficients.replace("</Coefficient>","")
    
    time = str(Bs_data.find('MeasurementTime'))
    time = time.replace("<MeasurementTime>","")
    time = time.replace("</MeasurementTime>","")
    time = int(time)
    
    for line in coefficients.split('\n'):
        if line != "":
            list_coefficients.append(float(line))
    a = list_coefficients[0]
    b = list_coefficients[1]
    c = list_coefficients[2]
    
    print("-----------Raw-Data-------------")
    for point in spectrum.split("\n"):
        if point != '':
            temp = int(point)
            DataPoints.append(temp)
            SUM = SUM + temp
            keV = a + b*channel + c*channel*channel
            Rounded = round(keV)
            pos.append(keV)
            print(f'keV: {keV}, count: {temp}')
            channel = channel + 1
    print("-------------------------------")
    
    print(f'coefficients: {list_coefficients}')
    print(f"Data gathered over: {time} seconds")
    print(f'Total count: {SUM}')
    print(f"avg cps: {SUM / time}")
    plot_data()

def main():
    i = 0
    file_list = os.listdir()
    print("-----------------------------")
    for file in os.listdir():
        if file.endswith(".xml"):
            print(f'{i} | {file}')
            xml_list.append(file)
            i = i + 1
    print("-----------------------------")
    selection = int(input("# XML to import : "))
    selected = xml_list[selection]
    import_xml(selected)

if __name__ == '__main__':
    DataPoints = []
    pos = []
    xml_list = []
    main()
