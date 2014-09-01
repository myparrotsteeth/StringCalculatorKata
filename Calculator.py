import re

class Calculator:

    class InvalidInputException(Exception) : pass
    class DigitDelimiterException(Exception) : pass
    class NegativesNotAllowedException(Exception) : pass

    __ACCEPTED_DELIMITERS = [',','\n']
    __CUSTOM_DELIMITER_PATTERN = "//([^\n]*?)\n(.*)$"

    def __init__(self):
        self.__DelimiterRegex = ''
        self.__BuildDelimiterRegex()

    def __BuildDelimiterRegex(self):
        self.__DelimiterRegex = '|'.join(list(map(re.escape,self.__ACCEPTED_DELIMITERS)))

    def Add(self, numbers=None):
        if numbers == "1,-2":
            x = 4
        output = "0"
        if numbers:
            customDelimiters = self.__GetAnyNewDelimitersFromString(numbers)
            if customDelimiters:
                if self.__ListContainsDigitElements(customDelimiters):
                    raise self.DigitDelimiterException
                else:
                    self.__ACCEPTED_DELIMITERS.extend(customDelimiters)
                    self.__BuildDelimiterRegex()
                    numbers = self.__GetStringWithoutCustomDelimiters(numbers)

            if numbers is not None and len(numbers) > 0:
                numbers_list = self.__ConvertStringIntoListOfInts(numbers)
                if self.__ListContainsNegativeNumber(numbers_list):
                    raise self.NegativesNotAllowedException
                else:
                    output = str(sum(numbers_list))

        return output

    def __ListContainsNegativeNumber(self, in_list):
        return True in list(map(lambda n: n < 0,in_list))

    def __ListContainsDigitElements(self,in_list):
        return True in list(map(lambda x: x.isdigit(),in_list))

    def __GetAnyNewDelimitersFromString(self,in_string):
        m = re.match(self.__CUSTOM_DELIMITER_PATTERN,in_string, re.S)
        if m:
            return list(m.group(1))
        else:
            return []

    def __GetStringWithoutCustomDelimiters(self,in_string):
        x = self.__CUSTOM_DELIMITER_PATTERN
        m = re.match(self.__CUSTOM_DELIMITER_PATTERN,in_string, re.S)
        if m:
            return m.group(2)
        else:
            return []

    def __SplitStringIntoList(self,in_string):
        out_list =  [ x.strip() for x in re.split(self.__DelimiterRegex, in_string) ]
        if self.__ListContainsEmptyString(out_list):
            raise self.InvalidInputException
        else:
            return out_list

    def __ConvertStringIntoListOfInts(self,in_string):
        return list(map(int,self.__SplitStringIntoList(in_string)))

    def __ListContainsEmptyString(self,in_list):
        return len( [x for x in in_list if x] ) < len(in_list)