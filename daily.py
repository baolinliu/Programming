from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)
import random 
def forecast():
	return 'same as %s' % random.choice(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

if __name__ == '__main__':
        forecast()