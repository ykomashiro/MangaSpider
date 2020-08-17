import abc


class BasicDownload:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def parse(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass
