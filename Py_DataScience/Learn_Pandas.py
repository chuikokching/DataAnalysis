import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #load CSV file
    test = pd.read_csv('Test_Dataset.csv');

    #load Excel file
    # test_xlsx = pd.read_excel('Test_Dataset.xlsx');

    #load Txt file
    # test_txt=pd.read_csv('Test_Dataset.txt',delimiter='\t');

    print(test);
    print(test.head(5));


    print_hi('PyCharm');