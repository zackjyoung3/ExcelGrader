from Deductions import Deduction


# class that represents the canvas representation of a students grade
class CanvasRepresentation:
    # constructor
    def __init__(self, total_points, deductions_comments):
        self.canvas_string = ""
        self.grade = total_points
        self.deductions_comments = deductions_comments
        self.get_representation()

    # overloaded += operator that permits distinguishing between a deduction and a comment and
    # allows either it to be added to the existing CanvasRepresentation accordingly
    def __iadd__(self, deduction_or_comment):
        if isinstance(deduction_or_comment, Deduction):
            self.canvas_string += (str(deduction_or_comment) + '\n')
            self.grade -= deduction_or_comment.deduction_amount
        else:
            if deduction_or_comment == "None":
                self.canvas_string += 'Excellent Work!\n'
            else:
                self.canvas_string += 'Comment: ' + deduction_or_comment + '\n'

    # method get the representation of this CanvasRepresentation
    def get_representation(self):
        for deduction_comment in self.deductions_comments:
            self.__iadd__(deduction_comment)

