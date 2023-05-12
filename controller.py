from PyQt5.QtWidgets import *
from view import *


class Controller(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 5
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL

        self.channel0.setHidden(True)
        self.channel1.setHidden(True)
        self.channel2.setHidden(True)
        self.channel3.setHidden(True)

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_volume_down.clicked.connect(lambda: self.volume(0))
        self.button_volume_up.clicked.connect(lambda: self.volume(1))
        self.button_channel_down.clicked.connect(lambda: self.channel(0))
        self.button_channel_up.clicked.connect(lambda: self.channel(1))
        self.bar_volume_status.setRange(Controller.MIN_VOLUME, Controller.MAX_VOLUME)

    def power(self):
        if not self.__status:
            self.__status = True
            self.label_power_status.setText('On')
            self.display_channel(self.__channel)
        elif self.__status:
            self.__status = False
            self.label_power_status.setText('Off')
            self.channel0.setHidden(True)
            self.channel1.setHidden(True)
            self.channel2.setHidden(True)
            self.channel3.setHidden(True)


    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.label_muted_status.setText('Yes')
                self.label_volume_status.setText('0')
            elif self.__muted:
                self.__muted = False
                self.label_muted_status.setText('No')
                self.label_volume_status.setText(str(self.__volume))


    def volume(self, num):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.label_muted_status.setText('No')

            if num == 0 and self.__volume > Controller.MIN_VOLUME:
                self.__volume -= 1
                self.label_volume_status.setText(str(self.__volume))
                self.bar_volume_status.setValue(self.__volume)
            elif num == 1 and self.__volume < Controller.MAX_VOLUME:
                self.__volume += 1
                self.label_volume_status.setText(str(self.__volume))
                self.bar_volume_status.setValue(self.__volume)



    def channel(self, num):
        if self.__status:
            if num == 0:
                self.__channel -= 1
                if self.__channel < Controller.MIN_CHANNEL:
                    self.__channel = Controller.MAX_CHANNEL
                self.label_channel_status.setText(str(self.__channel))
                self.display_channel(self.__channel)
            if num == 1:
                self.__channel += 1
                if self.__channel > Controller.MAX_CHANNEL:
                    self.__channel = Controller.MIN_CHANNEL
                self.label_channel_status.setText(str(self.__channel))
                self.display_channel(self.__channel)

    def display_channel(self, channel):
        if channel == 0:
            self.channel0.setHidden(False)
            self.channel1.setHidden(True)
            self.channel2.setHidden(True)
            self.channel3.setHidden(True)
        elif channel == 1:
            self.channel1.setHidden(False)
            self.channel0.setHidden(True)
            self.channel2.setHidden(True)
            self.channel3.setHidden(True)
        elif channel == 2:
            self.channel2.setHidden(False)
            self.channel0.setHidden(True)
            self.channel1.setHidden(True)
            self.channel3.setHidden(True)
        elif channel == 3:
            self.channel3.setHidden(False)
            self.channel0.setHidden(True)
            self.channel1.setHidden(True)
            self.channel2.setHidden(True)

