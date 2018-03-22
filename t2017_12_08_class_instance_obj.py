# coding: utf-8


class URI(object):

    @classmethod
    def adapter_service(cls, service_cls):
        cls.SERVICE_CLS = service_cls
        print 'xxixi'
        return service_cls

@URI.adapter_service
class Service(object):

    clients = {}


def get_service():
    print 'nothing'