#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.events.formatter import Formatter
from raspiot.events.speechRecognitionCommandProfile import SpeechRecognitionCommandProfile

class SpeechRecognitionCommandErrorToSpeechRecognitionCommandFormatter(Formatter):
    """
    SpeechRecognition command error to SpeechRecognitionCommandProfile
    """
    def __init__(self, events_broker):
        """
        Constuctor

        Args:
            events_broker (EventsBroker): events broker instance
        """
        Formatter.__init__(self, events_broker, u'speechrecognition.command.error', SpeechRecognitionCommandProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.error = True

        return profile
