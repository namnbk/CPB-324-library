import google.colab
import pandas as pd
import matplotlib.pyplot as plt

def _upload_file():
    """
    Prompt the user to upload a file from their local computer to Google Colab.

    Returns:
        str: The name of the uploaded file. 

    Raises:
        Error: If file cannot be uploaded.
    """
    uploaded = google.colab.files.upload()  
    filename = list(uploaded.keys())[0]  # get the file name
    print(f"File '{filename}' uploaded successfully!")
    return filename
       

def upload_and_parse_excel():
    """
    Upload an excel file from local computer and
    parse a column of data.

    This function will always parse 
        the **"datasheet"** sheet, and
        the **"data"** column 
    from the excel. Thus, make sure to provide the matching excel file. 

    Returns:
        list[int | float]: a list of all numbers from **"data"** column.

    Raises:
        Error: Provided sheet or column's name doesn not match. 
    """
    filename = _upload_file()
    excel_engine = pd.ExcelFile(filename)
    excel_sheet = excel_engine.parse("datasheet")
    return excel_sheet["data"]

def plot_histogram(raw_data, title, xlabel, ylabel):
    """
    Plots a histogram for the given raw data.

    Args:
        raw_data (list[int | float]): A list of numerical values to generate the histogram.
        title (str): The title of the histogram plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        None: The function displays the histogram but does not return any value.
    """
    plt.hist(raw_data)  # histogram plot
    plt.title(title)  # title
    plt.xlabel(xlabel)  #  x-axis label
    plt.ylabel(ylabel)  # y-axis label
    plt.show()

def frequency_table(raw_data):
    """
    Computes the frequency table for a given dataset.

    Args:
        raw_data (list[int | float]): A pandas Series containing categorical or numerical data.

    Returns:
        pd.Series: A frequency table where index values represent unique elements,
                   and corresponding values represent their frequencies.
    """
    # Compute the frequency table
    frequencies = raw_data.value_counts()
    # Sort the values for display
    sorted_frequencies = frequencies.sort_index()
    sorted_frequencies