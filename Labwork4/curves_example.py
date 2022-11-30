import matplotlib.pyplot as plt
import numpy as np

def curve1():
    plt.figure()
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x))
    plt.show()
    #plt.savefig('curve1.png')

def curve2():
    plt.figure()
    x = np.linspace(0, 10, 1000)
    # Color specified by name, solid line
    plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='blue')
    # Short name for the color, line with dashes
    plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='green')
    # Gray value between 0 and 1, lines and points
    plt.plot(x, np.sin(x - 2), color='0.75', linestyle='dashdot', label='gray')
    # Color specified in RGB, with dots
    plt.plot(x, np.sin(x - 3), color='#FF0000', linestyle='dotted', label='red')
    plt.show()
    #plt.savefig('curve2.png')

def curve1_AxesLegend():
    plt.figure()
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x))
    plt.xlabel("X")
    plt.ylabel("sin(X)")
    plt.legend(loc="upper left")
    plt.title("Y=sin(X)")
    plt.show()
    #plt.savefig('curve1_Axes_Legend.png')

def curve2_AxesLegend():
    plt.figure()
    x = np.linspace(0, 10, 1000)
    # Color specified by name, solid line
    plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='sin(x-0)')
    # Short name for the color, line with dashes
    plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='sin(x-1)')
    # Gray value between 0 and 1, lines and points
    plt.plot(x, np.sin(x - 2), color='0.75', linestyle='dashdot', label='sin(x-2)')
    # Color specified in RGB, with dots
    plt.plot(x, np.sin(x - 3), color='#FF0000', linestyle='dotted', label='sin(x-3)')
    plt.xlabel("X")
    plt.ylabel("sin(X)")
    plt.legend(loc="upper left")
    plt.title("Example of a multi-curve graph with legend")
    #plt.savefig('curve2_Axes_Legend.png')
    plt.show()

def graphScatter(n):
    x = np.linspace(0, 1, n)
    y = np.random.random(n)
    plt.figure()
    plt.scatter(x,y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper left")
    plt.title("Example of a point cloud graph")
    #plt.savefig('point_cloud.png')
    plt.show()
    return [x,y]

def graphScatter2(x,y):
    plt.figure()
    plt.scatter(x,y,s=3,c="green")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper left")
    plt.title("Example of a scatter plot")
    plt.show()
    #plt.savefig('point_cloud2.png')

def graphHisto():
    plt.figure()
    x = np.random.random(200)
    plt.hist(x)
    plt.xlabel('X')
    plt.ylabel("Number of occurrences")
    plt.legend(loc="upper left")
    plt.title("Example of a histogram")
    plt.show()
    #plt.savefig('histo.png')
    return x

def graphHisto2(x):
    plt.figure()
    y = np.random.random(200)
    plt.hist([x,y], label=['x','y'])
    plt.ylabel("Number of occurrences")
    plt.legend(loc="upper left")
    plt.title("Example with two histograms on the same figure")
    plt.show()
    #plt.savefig('histo2.png')
    return y

def graphHisto3(x,y):
    plt.figure()
    plt.hist([x,y], bins=5, label=['x','y'])
    plt.ylabel("Number of occurrences")
    plt.legend(loc="upper left")
    plt.title("Example with two histograms on the same figure")
    plt.show()
    #plt.savefig('histo3.png')

def multifigure():
    plt.figure()
    
    plt.subplot(121)
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x));
    plt.xlabel("X")
    plt.ylabel("sin(X)")
    plt.legend(loc="upper left")
    
    plt.subplot(122)
    x = np.linspace(0, 1, 100)
    y = np.random.random(100)
    plt.scatter(x,y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper left")
    
    plt.show()
    #plt.savefig("multi.png")

def multifigure2():
    plt.figure()
    
    plt.subplot(221)
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x));
    plt.ylabel("sin(X)")
    plt.legend(loc="upper left")
    
    plt.subplot(222)
    x = np.linspace(0, 1, 100)
    y = np.random.random(100)
    plt.scatter(x,y)
    plt.ylabel("Y")
    plt.legend(loc="upper left")

    plt.subplot(223)
    x = np.random.random(200)
    plt.hist(x)
    plt.ylabel("Number of occurrences")
    plt.legend(loc="upper left")
    
    plt.subplot(224)
    y = np.random.random(200)
    plt.hist([x,y], bins=5, label=['x','y'])
    plt.legend(loc="upper left")
    
    plt.show()
    #plt.savefig("multi2.png")
    
def multifigure3():
    plt.figure()
    
    plt.subplot(212)
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x));
    plt.ylabel("sin(X)")
    plt.legend(loc="upper left")

    plt.subplot(221)
    x = np.random.random(200)
    plt.hist(x)
    plt.ylabel("Number of occurrences")
    plt.legend(loc="upper left")
    
    plt.subplot(222)
    y = np.random.random(200)
    plt.hist([x,y], bins=5, label=['x','y'])
    plt.legend(loc="upper left")
    
    plt.show()
    #plt.savefig("multi3.png")

curve1()
curve2()
curve1_AxesLegend()
curve2_AxesLegend()
[x,y] = graphScatter(300)
graphScatter2(x,y)
x = graphHisto()
y = graphHisto2(x)
graphHisto3(x,y)
multifigure()
multifigure2()
multifigure3()