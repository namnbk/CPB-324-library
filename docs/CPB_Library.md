Module CPB_Library
==================

Functions
---------

`frequency_table(raw_data)`
:   Computes the frequency table for a given dataset.
    
    Args:
        raw_data (list[int | float]): A pandas Series containing categorical or numerical data.
    
    Returns:
        pd.Series: A frequency table where index values represent unique elements,
                   and corresponding values represent their frequencies.

`plot_histogram(raw_data, title, xlabel, ylabel)`
:   Plots a histogram for the given raw data.
    
    Args:
        raw_data (list[int | float]): A list of numerical values to generate the histogram.
        title (str): The title of the histogram plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    
    Returns:
        None: The function displays the histogram but does not return any value.

`upload_and_parse_excel()`
:   Upload an excel file from local computer and
    parse a column of data.
    
    This function will always parse 
        the "DATASHEET sheet, and
        the "DATA" column 
    from the excel. Thus, make sure to provide the matching excel file. 
    
    Returns:
        list[int | float]: a list of all numbers from **"data"** column.
    
    Raises:
        Error: Provided sheet or column's name doesn not match.