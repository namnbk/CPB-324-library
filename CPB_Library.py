import google.colab
import pandas as pd
import matplotlib.pyplot as plt

def upload_file():
    # Prompts the user to upload a file 
    # from their local computer to Google Colab
    uploaded = google.colab.files.upload()  
    # Opens a file selection dialog
    filename = list(uploaded.keys())[0]  
    # Get the uploaded file name
    print(f"File '{filename}' uploaded successfully!")
    return filename
       

def parse_excel_data():
    filename = upload_file()
    excel_engine = pd.ExcelFile(filename)
    excel_sheet = excel_engine.parse("datasheet")
    return excel_sheet["data"]

def plot_histogram(raw_data, title, xlabel, ylabel):
    # Plot the histogram of the age distribution data
    plt.hist(raw_data)
    # Specify the title of our plot
    plt.title(title)
    # Labels for x-axis
    plt.xlabel(xlabel)
    # Label for y-axis
    plt.ylabel(ylabel)
    # Show the plot
    plt.show()

def frequency_table(raw_data):
    # Compute the frequency table
    frequencies = raw_data.value_counts()
    sorted_frequencies = frequencies.sort_index()
    sorted_frequencies