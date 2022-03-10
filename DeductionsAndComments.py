from Deductions import Deductions, Deduction
from math import isnan


# class that represents the deductions and comments on a single students project
class DeductionsAndComments(list):
    def __init__(self, deductions_dict, deductions_string):
        super(DeductionsAndComments, self).__init__()
        self.deductions_dict = deductions_dict
        self.deds_comments = None
        self.parse_deductions_and_comments(deductions_string)

    # method that parses deductions and comments
    # note that the format needed for this to work is
    # deductions or comments separated by ';'
    def parse_deductions_and_comments(self, deductions_string):
        if isinstance(deductions_string, str):
            deds_comments = deductions_string.split(';')
            deds_comments = [ded_or_comment.strip() for ded_or_comment in deds_comments]
            deds_comments = [ded_or_comment for ded_or_comment in deds_comments if ded_or_comment != '']
            self.extend([self.deductions_dict[ded_or_comment] if ded_or_comment in self.deductions_dict
                         else ded_or_comment for ded_or_comment in deds_comments])
            if len(self) != len(set(self)):
                exception_str = 'Duplicate deduction or comment in ' + deductions_string
                raise Exception(exception_str)
        else:
            self.append('None')

    def __str__(self):
        return str([str(element) for element in self])
