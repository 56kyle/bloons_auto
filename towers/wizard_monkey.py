from tower import Tower


class WizardMonkey(Tower):
    name = 'wizard_monkey'
    range = 215
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
