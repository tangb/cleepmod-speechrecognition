#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.events.formatter import Formatter
from raspiot.events.speechRecognitionHotwordProfile import SpeechRecognitionHotwordProfile

class SpeechRecognitionHotwordReleasedToSpeechRecognitionHotwordFormatter(Formatter):
    """
    SpeechRecognition hotword released to SpeechRecognitionHotwordProfile
    """
    def __init__(self, events_factory):
        """
        Constuctor

        Args:
            events_factory (EventsFactory): events factory instance
        """
        Formatter.__init__(self, events_factory, u'speechrecognition.hotword.released', SpeechRecognitionHotwordProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.detected = False

        return profile

