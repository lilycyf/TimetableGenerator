import requests
from bs4 import BeautifulSoup as bs



def getSections(dept, course):
    
    r = requests.get(f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept={dept}&course={course}')

    allinfo = bs(r.content, from_encoding='utf-8', features="html.parser")

    sections = []

    credits = allinfo.findAll('div', attrs={'class': 'alert alert-info'})[0].nextSibling.string
    

    for box in allinfo.findAll('table', attrs={'class': 'table table-striped section-summary'}):
            for a in box.findAll('tr'):
                if a != box.findAll('tr')[0]:
                    section = a.contents[1].text
                    activity = a.contents[2].text
                    term = a.contents[3].text
                    days = a.contents[5].text
                    startTime = a.contents[6].text
                    endTime = a.contents[7].text
                    if activity != 'Waiting List':
                        sections.append({"Section": section, "Activity": activity, "Term": term, "Days": days, "Start Time": startTime, 
                        "End Time": endTime, "Credits": int(credits[credits.index(" ")+1:])})
    return {f"{dept} {course}": sections}
    
def reformate(courseSet):
    for course in list(courseSet.keys()):
        for section in courseSet.get(course):
            term = section.get("Term")
            days = section.get("Days")
            startTime = section.get("Start Time")
            endTime = section.get("End Time")
            ds = []
            if "Mon" in days:
                ds.append(1)
            if "Tue" in days:
                ds.append(2)
            if "Wed" in days:
                ds.append(3)
            if "Thu" in days:
                ds.append(4)
            if "Fri" in days:
                ds.append(5)
            st = int(startTime[:startTime.index(":")]) + int(startTime[startTime.index(":")+1:])/60
            et = int(endTime[:endTime.index(":")]) + int(endTime[endTime.index(":")+1:])/60
            periods = []
            for d in ds:
                group = (int(term), d, st, et)
                periods.append(group)
            # print(periods)
            section["Reformate"] = periods
            # print(section)


courses = {}
courses.update(getSections("CPSC", "420"))
courses.update(getSections("MATH", "221"))

reformate(courses)

# print(courses)


