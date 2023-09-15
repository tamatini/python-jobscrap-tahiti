class Job:
    def __init__(self, title, description, requirement, start_date, end_date):
        self.title = title
        self.description = description
        self.requirement = requirement
        self.start_date = start_date
        self.end_state = end_date

    def __str__(self):
        return f"Job[title='{self.title}', description='{self.description}', requirement='{self.requirement}', " \
               f"startDate='{self.start_date}', endDate='{self.end_state}']"
