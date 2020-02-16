


def timetableGenerator(dict, after, before):
    
    timetables = []

    size = 0

    for course in list(dict.keys()):
        #get the time periods for this course
        times = dict[course]

        #expend timetables with possible time periods for this course
        if course == list(dict.keys())[0]:
            for time in times:
                if filter(time, after, before):
                    course_time = (course, time)
                    timetables.append([course_time])

        elif(size != 0):
            for i in range(0, size):
                temp = timetables[0]
                del(timetables[0])
                for time in times:
                    if filter(time, after, before):
                        course_time = (course, time)
                        if(checkNewAddedItem(temp + [course_time])):
                            timetables.append(temp + [course_time])

        size = len(timetables)

    return timetables

def filter(c, after, before):
    for t in c:
        if (t[1] < after or t[2] > before):
            return False
    return True


#Check if last added item have conflict in any one of the previous items in the list
def checkNewAddedItem(x):
    for i in range(0, len(x)-1):
        if(not checkTwoClasses(x[i], x[-1])):
            return False
    return True

#Check if two classes have time conflict, if conflist return false, else return true
def checkTwoClasses(c1, c2):
    for time1 in c1[1]:
        for time2 in c2[1]:
            if (time1[0] == time2[0] and time1[1]<time2[2] and time1[1]>=time2[1]) or \
            (time1[0] == time2[0] and time1[2]<=time2[2] and time1[2]>time2[1]):
                return False
    return True

courseList = {}
courseList = {"CPSC420": [[(1,13,14),(3,13,14),(5,13,14)],[(2,14.5,15),(4,14.5,15)]]}
courseList["CPSC322"] = [[(1,13,14),(3,13,14),(5,13,14)],[(1,14,15),(3,14,15),(5,14,15)]]
courseList["COGS300"] = [[(1,15,16),(3,15,16)]]

timetable = timetableGenerator(courseList, 14, 16)

print(timetable)





        

