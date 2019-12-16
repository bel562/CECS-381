import numpy as np
import matplotlib.pyplot as plt

#***1.1***
a=2.0
b=5.0
beta = .33
mu = 2.5
sigma = .75
n = 1000000
x1 = np.random.uniform(a,b,n)
x2 = np.random.exponential(beta,n)
x3 = np.random.normal(mu,sigma,n)


#Calculate The Mean and STD
Theo_Ux = 3.5
Theo_Ox = np.sqrt(.75)

mu_x= np.mean(x1) #1.1: 3.5
sig_x=np.std(x1) #1.1: .86

mu_x2= np.mean(x2) #1.2:.330
sig_x2=np.std(x2) #1.2: .33

mu_x3= np.mean(x3) #1.3: 2.5
sig_x3=np.std(x3) #1.3:.75

def Graph(a,b,x,switch):
    #Create bins and histogram
    nbins=30 #NUmber of bins
    edgecolor='w' #Color separating bars in the bargraph
    
    bins = [float(x) for x in np.linspace(a,b,nbins)]
    h1, bin_edges = np.histogram(x,bins, density = True)
    #Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] #Width of bars in the bargraph
    plt.close('all')
    
    #Plot the Bar Graph
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor= edgecolor)
    
    #Plot the Uniform PDF
    def UnifPDF(a,b,x):
        f=(1/abs(b-a))*np.ones(np.size(x))
        return f
    def ExpoPDF(x):
        f= 1/beta*np.exp(-(1/beta*x))
        
        return f
    def NormalPDF(x):
        f = np.exp(-(x-mu)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
        return f
    if (switch == 1):
        f = UnifPDF(a,b,b1)
        plt.title('Uniform Distribution', fontsize = 14, fontweight = 'bold')
    elif(switch == 2):
        f = ExpoPDF(b1)
        plt.title('Exponential Distribution', fontsize = 14, fontweight = 'bold')

    else:
        f = NormalPDF(b1)
        plt.title('Normal Distribution', fontsize = 14, fontweight = 'bold')
    
    plt.xlabel('X', fontsize = 14)
    plt.ylabel('PDF', fontsize = 14)
    plt.plot(b1,f,'r')

#Use only graph funcition. Last one used is displayed
Graph(a,b,x1, 1)
Graph(a,b,x2, 2)
Graph(a,b,x3, 3)

