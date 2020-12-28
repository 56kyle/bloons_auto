from tower import Tower


class WizardMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'wizard_monkey'
        kwargs['range'] = 215
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
