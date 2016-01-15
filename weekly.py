from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)

import random

def forecast():
	return ['snow', 'more snow', 'sleet', 'freezing rain', 'rain', 'fog', 'hail']
def mix():
	weather1 = ['snow', 'more snow', 'sleet','frozen ponds','thunderstorms']
	weather2 = ['freezing rain', 'rain', 'fog', 'hail','tornados']

	return "A mix of %s and %s" % (random.choice(weather1),random.choice(weather2))
if __name__ == '__main__':
        forecast()
