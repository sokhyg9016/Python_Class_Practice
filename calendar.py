class Calendar():

    __daysMonth = {
            "January": 31,
            "February": 28,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July":31,
            "August":31,
            "September":30,
            "October": 31,
            "November": 30,
            "December": 31
    }
    
    __daysWeek = [
            "Sun",
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat"
    ]

    def __init__(self, year, start):
        self.__year = year
        self.__start = start
            
    def show(self):

        if (not self.__year% 4 and self.__start % 100 != 0) or not self.__year % 400:
            self.__daysMonth["February"] = 29

        for month in self.__daysMonth.keys():
            print("{:>27} {:d}".format(month, self.__year))
            print("-"*49, end = '')
            print()
            
            for day in self.__daysWeek:
                print("{:>7s}".format(day), end = '')
            print()

            for i in range(self.__start):
                print("{:>7s}".format(" "), end = '')
            
            for i in range(self.__daysMonth[month]):
                print("{:7d}".format(i+1), end = '')
                self.__start += 1

                if self.__start == 7:
                    print()
                    self.__start = 0
            print('\n')

    def getNumDaysWeek(self, day):
        for i in range(len(self.__daysWeek)):
            if day == self.__daysWeek[i]:
                if day == "Sun":
                    return 7
                return self.__daysWeek.index(day)
                
    def calWhatDaysWeek(self, curr, days):
        return self.__daysWeek[(self.getNumDaysWeek(curr)+days)%7]
            

    
def main():
    year = int(input("Enter the year: "))
    start = int(input("Enter the start day of year: "))

    Cal = Calendar(year, start)

    #Cal.show()

    # What is day if curr is Tuesday, and after 10 days?
    curr = "Tue"
    after = 10
    print("Result: ", Cal.calWhatDaysWeek(curr, after))


main()
