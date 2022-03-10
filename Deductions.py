from math import isnan


# class that encapsulates the information of a single deduction for grading
class Deduction:
    def __init__(self, deduction_string, deduction_amount):
        self.deduction_string = deduction_string
        self.deduction_amount = deduction_amount

    def __str__(self):
        return self.deduction_string + '(-' + str(self.deduction_amount) + ')'


# Deductions is a dictionary of deductions that will permit constant time lookup for the descriptions and
# points associated with a deduction
class Deductions(dict):
    def __init__(self, *args, **kw):
        super(Deductions, self).__init__(*args, **kw)
        self.item_list = list(super(Deductions, self).keys())

    def __setitem__(self, key, value):
        if key in self.keys():
            raise Exception("Duplicate deduction ID Error")
        self.item_list.append(key)
        super(Deductions, self).__setitem__(key, value)

    def __iter__(self):
        return iter(self.item_list)

    def keys(self):
        return self.item_list

    def values(self):
        return [self[key] for key in self]

    def itervalues(self):
        return (self[key] for key in self)

    # method that will obtain a single deduction
    def obtain_deduction(self, deduction_dict):
        key = deduction_dict['Deduction ID']
        value = Deduction(deduction_dict['Deduction Description'], deduction_dict['Points Deducted'])
        self.__setitem__(key, value)

    # method that will populate all of the deductions
    def obtain_deductions(self, grading_list_dicts):
        i = 0
        while not isnan(grading_list_dicts[i]['Points Deducted']):
            self.obtain_deduction(grading_list_dicts[i])
            i += 1



