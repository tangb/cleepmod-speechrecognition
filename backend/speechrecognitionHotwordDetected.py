#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.event import Event

class Speechrecognitionhotworddetected(Event):
    """
    speechrecognition.hotword.detected event
    """

    EVENT_NAME = u'speechrecognition.hotword.detected'
    EVENT_SYSTEM = False
    EVENT_PARAMS = []

    def __init__(self, bus, formatters_broker, events_broker):
        """
        Constructor

        Args:
            bus (MessageBus): message bus instance
            formatters_broker (FormattersBroker): formatters broker instance
            events_broker (EventsBroker): events broker instance
        """
        Event.__init__(self, bus, formatters_broker, events_broker)

