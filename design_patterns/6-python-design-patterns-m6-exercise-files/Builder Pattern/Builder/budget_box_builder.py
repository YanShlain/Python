from abs_builder import AbsBuilder

class BudgetBoxBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'IN WIN BP655'
     
    def build_mainboard(self):
        self._computer.mainboard = 'ASRock AM1H-ITX'
        self._computer.cpu = 'AMD Athlon 5150'
        self._computer.memory = 'Kingston ValueRAM 4GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'WD Blue 1TB'

    def install_video_card(self):
        self._computer.video_card = 'On board'




