import pandas as pd
from Deductions import Deductions
from GradingInformation import GradingInformation
from DeductionsAndComments import DeductionsAndComments
import os.path
from os import path


# method that will obtain the excel file in the current directoy that is to be read from
def get_file():
    while True:
        file = input("Please input the xls file for grading. "
                     "Note that it must have extension .xls and be in the current directory:")
        if path.exists(file):
            break
        print("Error! The file must be ing the current directory and have extension .xls")

    file_string = './' + file

    return file_string


# method that will load the excel file and convert its contents into a list of dictionaries
def load_excel(file_string):
    df = pd.read_excel(file_string)
    df_list_dict = df.to_dict('records')

    return df_list_dict


# method that will create a deductions object that will permit constant time lookup based
# on the deductions id
def obtain_deductions(df_list_dict):
    deds = Deductions()
    deds.obtain_deductions(df_list_dict)

    return deds


# method that will parse the deductions and comments that have been entered
# and write canvas grading information for each student in the excel file
def grade_and_write_excel(df_list_dict, deds, file):
    for_canvas = GradingInformation(df_list_dict, deds, file)
    for_canvas.create_graded_list_dict()
    for_canvas.populate_grades_in_excel()


# definition for main
def main():
    file = get_file()
    df_list_dict = load_excel(file)
    deds = obtain_deductions(df_list_dict)
    grade_and_write_excel(df_list_dict, deds, file)


# main
if __name__ == '__main__':
    main()
