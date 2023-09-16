class Job:
    def __init__(self, title, description, definition, education, specialisation,
                 skills, experiences, start_date, end_date):
        self.title = title
        self.description = description
        self.definition = definition
        self.education = education
        self.specialisation = specialisation
        self.skills = skills
        self.experience = experiences
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Job[title='{self.title}', description='{self.description}', definition='{self.definition}', " \
               f"education='{self.education}', specialisation='{self.specialisation}' , skills='{self.skills}'" \
               f"experience='{self.experience}', startDate='{self.start_date}', endDate='{self.end_date}']"
