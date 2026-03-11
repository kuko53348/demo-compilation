class QuestionTemplate:
    def __init__(self,
                 target: str="",
                 questions_1: str="",
                 questions_2: str="",
                 questions_3: str="",
                 questions_4: str="",
                 questions_5: str="",
                 reference: str=""
                ):
        self.target = target
        self.questions_1 = questions_1
        self.questions_2 = questions_2
        self.questions_3 = questions_3
        self.questions_4 = questions_4
        self.questions_5 = questions_5
        self.reference = reference

class ClientProfileTemplate:
    def __init__(self,
                 name: str="",
                 carrer: str="",
                 location: str="",
                 contact: str="",
                 profile: str="",
                 avatar_image: str="",
                 experience: str="",
                 education: str="",
                 skills: str="",
                 language: str="",
                 graduation: str="",
                 academic: str="",
                 responsability: str="",

                ):
        self.name = name
        self.carrer = carrer
        self.location = location
        self.contact = contact
        self.profile = profile
        self.avatar_image = avatar_image
        self.experience = experience
        self.education = education
        self.skills = skills
        self.language = language
        self.graduation = graduation
        self.academic = academic
        self.responsability = responsability

class LobbyModelCard:
    def __init__(self,
                 header: str="",
                 sub_header: str="",
                 body_text: str="",
                 help_info: str=""
                ):

        self.header = header
        self.sub_header = sub_header
        self.body_text = body_text
        self.help_info = help_info