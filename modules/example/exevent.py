#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Busana Apparel Group. All rights reserved.
#
# This product and it's source code is protected by patents, copyright laws and
# international copyright treaties, as well as other intellectual property
# laws and treaties. The product is licensed, not sold.
#
# The source code and sample programs in this package or parts hereof
# as well as the documentation shall not be copied, modified or redistributed
# without permission, explicit or implied, of the author.
#
# This module is part of Centric PLM Integration Bridge and is released under
# the Apache-2.0 License: https://www.apache.org/licenses/LICENSE-2.0

import logging
from core.prochandler import CommandProcessor
from core.msgobject import mq_event


class ExampleEvent(CommandProcessor):

    def __init__(self):
        super(ExampleEvent, self).__init__()

    def do_configure(self):
        # this would be automatically called upon execution
        pass

    @mq_event
    def example_event(self, cono=None, dvno=None):
        logging.info("Hello World EVENT sent with params cono={0}, dvno={1}".format(cono, dvno))

