import infoGetter

MAX_CREDITS_PER_TERM = 15

def timetableGenerator(dict, after, before, ignore):
    
    timetables = []
    first = 1

    size = 0

    for course in list(dict.keys()):
        #get the time periods for this course
        sections = dict[course]

        while(len(sections) > 0):
            acticity = sections[0].get("Activity")

            
            tempSections = []
                
            for section in sections:
                if section.get("Activity") == acticity:
                    tempSections.append(section)
                    # sections.remove(section)
            for t in tempSections:
                sections.remove(t)

            if acticity not in ignore:
        #expend timetables with possible time periods for this course
                if first:
                    for section in tempSections:
                        if filter(section.get("Reformate"), after, before):
                            course_time = (course, section)
                            timetables.append([course_time])
                    first = 0

                elif(size != 0):
                    for i in range(0, size):
                        temp = timetables[0]
                        del(timetables[0])
                        for section in tempSections:
                            if filter(section.get("Reformate"), after, before):
                                course_time = (course, section)
                                if(checkNewAddedItem(temp + [course_time])):
                                    timetables.append(temp + [course_time])

                size = len(timetables) 

    return timetables

def filter(c, after, before):
    for t in c:
        if (t[2] < after or t[3] > before):
            return False
    return True


#Check if last added item have conflict in any one of the previous items in the list
def checkNewAddedItem(x):
    term = x[-1][1].get("Term")
    credits = x[-1][1].get("Credits")
    for i in range(0, len(x)-1):
        if(x[i][1].get("Term") == term):
            credits = credits + x[i][1].get("Credits")
    if credits > MAX_CREDITS_PER_TERM: return False
    for i in range(0, len(x)-1):
        if(not checkTwoClasses(x[i], x[-1])):
            return False
    
    return True

#Check if two classes have time conflict, if conflist return false, else return true
def checkTwoClasses(c1, c2):
    for time1 in c1[1].get("Reformate"):
        for time2 in c2[1].get("Reformate"):
            if (time1[0] == time2[0] and time1[1] == time2[1] and time1[2]<time2[3] and time1[2]>=time2[2]) or \
            (time1[0] == time2[0] and time1[1] == time2[1] and time1[3]<=time2[3] and time1[3]>time2[2]):
                return False
    return True

courses = {}
courses.update(infoGetter.getSections("CPSC", "420"))
courses.update(infoGetter.getSections("COGS", "300"))
courses.update(infoGetter.getSections("COGS", "303"))
courses.update(infoGetter.getSections("MATH", "221"))
courses.update(infoGetter.getSections("PHIL", "451"))
courses.update(infoGetter.getSections("CPSC", "312"))
courses.update(infoGetter.getSections("STAT", "344"))
courses.update(infoGetter.getSections("CPSC", "322"))
courses.update(infoGetter.getSections("CPSC", "304"))


infoGetter.reformate(courses)
ignore = []
ignore.extend(["Tutorial", "Laboratory"])

timetable = timetableGenerator(courses, 11, 24, ignore)

for tt in timetable:
    for t in tt:
        # if "Reformate" in t[1]:
        #     del t[1]["Reformate"]
        print(t)
    print("---------------------------------------------")





        

