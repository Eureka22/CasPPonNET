import numpy as np
import scipy
from sklearn import *
import matplotlib.pyplot as plt
import csv
from dateutil.parser import parse
import requests
from bs4 import BeautifulSoup
from mpl_toolkits.basemap import Basemap,shiftgrid
import pickle


m = Basemap(width=2400000,height=1800000,projection='lcc',
            resolution='h',lat_1=15.,lat_2=-7,lat_0=9,lon_0=-10.)
# draw coastlines.
m.drawcoastlines()
# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(fill_color='aqua')
m.drawcounties()
# fill continents, set lake color same as ocean color.
m.fillcontinents(color='coral',lake_color='aqua')
parallels = np.arange(-20.,20,3.)
# labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(-20.,20.,3.)
m.drawmeridians(meridians,labels=[True,False,False,True])

f = open('city.pkl','r')
c = pickle.load(f)
posx = [info[3] for info in c]
posy = [info[4] for info in c]

for i in range(len(posx)):
    xpt,ypt = m(posy[i], posx[i])
    m.plot(xpt,ypt,'ro') 
    plt.text(xpt+100000,ypt+100000,'%s' % (c[i][1]))
    


plt.savefig('map.png', dpi=300)
plt.savefig('map.pdf')
plt.show()
