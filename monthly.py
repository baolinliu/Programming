from __future__ import absolute_import, division, print_function, unicode_literals

import random 

def forecast():
	return 'For the month of %s' % random.choice(['January','February','March','April','May','June','July','August','September', 'October','November','December'])

	if __name__ == '__main__':
		forecast()