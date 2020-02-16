import requests
from bs4 import BeautifulSoup as bs



def getSections(dept, course):
    
    r = requests.get(f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept={dept}&course={course}')

    print(r.status_code)

    allinfo = bs(r.content, from_encoding='utf-8', features="html.parser")

    sections = []

    for box in allinfo.findAll('table', attrs={'class': 'table table-striped section-summary'}):
            for a in box.findAll('tr'):
                if a != box.findAll('tr')[0]:
                    section = a.contents[1].text
                    activity = a.contents[2].text
                    term = a.contents[3].text
                    days = a.contents[5].text
                    startTime = a.contents[6].text
                    endTime = a.contents[7].text
                    sections.append({"Section": section, "Axticity": activity, "Term": term, "Days": days, "Start Time": startTime, 
                    "End Time": endTime})
    return {f"{dept} {course}": sections}
    

courses = []
courses.append(getSections("cpsc", "420"))
courses.append(getSections("MATH", "221"))

print(courses)


