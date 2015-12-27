'''
Created on 23.12.2015

@author: marcelkisilowski
'''

if __name__ == '__main__':
    from yahoo_api import yahoo_api
    import matplotlib.pyplot as plt
    import numpy as np
    yapi = yahoo_api()
    ibm = yapi.cache['IBM']
    

plt.plot(range(10),range(10))