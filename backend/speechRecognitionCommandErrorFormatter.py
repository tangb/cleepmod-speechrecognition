#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.formatters.formatter import Formatter

__all__ = [u'SpeechRecognitionCommandErrorFormatter']

class SpeechRecognitionCommandErrorFormatter(Formatter):
    """
    SpeechRecognition command error to SpeechRecognitionCommandProfile
    """
    def __init__(self, events_factory):
        """
        Constuctor

        Args:
            events_factory (EventsFactory): events factory instance
        """
        Formatter.__init__(self, events_factory, u'speechrecognition.command.error', SpeechRecognitionCommandProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.error = True

        return profile
