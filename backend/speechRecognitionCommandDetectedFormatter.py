#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.formatters.formatter import Formatter

__all__ = [u'SpeechRecognitionCommandDetectedFormatter']

class SpeechRecognitionCommandDetectedFormatter(Formatter):
    """
    SpeechRecognition command detected to SpeechRecognitionCommandProfile
    """
    def __init__(self, events_factory):
        """
        Constuctor

        Args:
            events_factory (EventsFactory): events factory instance
        """
        Formatter.__init__(self, events_factory, u'speechrecognition.command.detected', SpeechRecognitionCommandProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.error = False

        return profile
