#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.event import Event

class Speechrecognitioncommanddetected(Event):
    """
    speechrecognition.command.detected event
    """

    EVENT_NAME = u'speechrecognition.command.detected'
    EVENT_SYSTEM = False
    EVENT_PARAMS = [u'hotword', u'command']

    def __init__(self, bus, formatters_broker, events_broker):
        """
        Constructor

        Args:
            bus (MessageBus): message bus instance
            formatters_broker (FormattersBroker): formatters broker instance
            events_broker (EventsBroker): events broker instance
        """
        Event.__init__(self, bus, formatters_broker, events_broker)

