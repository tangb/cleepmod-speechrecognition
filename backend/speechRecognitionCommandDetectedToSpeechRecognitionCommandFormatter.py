#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.formatter import Formatter
from raspiot.profiles.speechRecognitionCommandProfile import SpeechRecognitionCommandProfile

class SpeechRecognitionCommandDetectedToSpeechRecognitionCommandFormatter(Formatter):
    """
    SpeechRecognition command detected to SpeechRecognitionCommandProfile
    """
    def __init__(self, events_broker):
        """
        Constuctor

        Args:
            events_broker (EventsBroker): events broker instance
        """
        Formatter.__init__(self, events_broker, u'speechrecognition.command.detected', SpeechRecognitionCommandProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.error = False

        return profile

