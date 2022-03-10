from Deductions import Deductions, Deduction
from CanvasRepresentation import CanvasRepresentation
from DeductionsAndComments import DeductionsAndComments
import xlwt
import xlrd
from xlutils.copy import copy


# class that represent the grading information for a project
class GradingInformation:
    def __init__(self, grading_list_dict, deductions, file_name):
        self.grading_list_dict = grading_list_dict
        self.deductions = deductions
        self.file_name = file_name

    # method that will iterate over the grading_list_dic and populate the fields for canvas grades appropriately
    def create_graded_list_dict(self):
        for i in range(len(self.grading_list_dict)):
            deductions_comments = DeductionsAndComments(self.deductions, self.grading_list_dict[i]['Deductions'])
            canvas_represenation = CanvasRepresentation(self.grading_list_dict[0]['Total Points'], deductions_comments)
            self.grading_list_dict[i]["Canvas Comments"] = canvas_represenation.canvas_string
            self.grading_list_dict[i]["Final Grade"] = canvas_represenation.grade

        print(self.grading_list_dict)

    # string representation is the grading_list_dic and the deductions
    def __str__(self):
        return str(self.grading_list_dict) + '\n' + str(self.deductions)

    # method that will write the grading_list_dic to the excel file specified
    def populate_grades_in_excel(self):
        excel = xlrd.open_workbook(self.file_name)
        contents = copy(excel)
        sheet = contents.get_sheet(0)

        # write the information to the appropriate location in the google sheet
        for i in range(len(self.grading_list_dict)):
            sheet.write(i+1, 5, str(self.grading_list_dict[i]["Canvas Comments"]))
            if self.grading_list_dict[i]["Final Grade"] > 0:
                sheet.write(i+1, 6, self.grading_list_dict[i]["Final Grade"])
            else:
                sheet.write(i + 1, 6, 0)
            sheet.write(i+1, 7, self.grading_list_dict[0]['Total Points'])

        # save the file
        contents.save(self.file_name)
