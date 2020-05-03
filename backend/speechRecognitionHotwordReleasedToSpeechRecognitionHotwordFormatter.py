#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.formatter import Formatter
from raspiot.profiles.speechRecognitionHotwordProfile import SpeechRecognitionHotwordProfile

class SpeechRecognitionHotwordReleasedToSpeechRecognitionHotwordFormatter(Formatter):
    """
    SpeechRecognition hotword released to SpeechRecognitionHotwordProfile
    """
    def __init__(self, events_broker):
        """
        Constuctor

        Args:
            events_broker (EventsBroker): events broker instance
        """
        Formatter.__init__(self, events_broker, u'speechrecognition.hotword.released', SpeechRecognitionHotwordProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.detected = False

        return profile

