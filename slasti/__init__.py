#
# Slasti -- the main package
#
# Copyright (C) 2011 Pete Zaitcev
# See file COPYING for licensing information (expect GPL 2).
#

class AppError(Exception):
    pass
class App404Error(Exception):
    pass

import main, tagbase
