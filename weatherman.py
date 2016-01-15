
# coding: utf-8

# In[ ]:

from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)

import report
def weatherman():
        description = report.get_description()
        print("today's weather:", description)

if __name__ == '__main__':
        weatherman()

