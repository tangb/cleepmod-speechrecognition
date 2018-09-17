#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.formatters.formatter import Formatter

__all__ = [u'SpeechRecognitionHotwordDetectedFormatter']

class SpeechRecognitionHotwordDetectedFormatter(Formatter):
    """
    SpeechRecognition hotword detected to SpeechRecognitionHotwordProfile
    """
    def __init__(self, events_factory):
        """
        Constuctor

        Args:
            events_factory (EventsFactory): events factory instance
        """
        Formatter.__init__(self, events_factory, u'speechrecognition.hotword.detected', SpeechRecognitionHotwordProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.detected = True

        return profile

