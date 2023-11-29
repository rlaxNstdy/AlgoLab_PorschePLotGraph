import matplotlib.pyplot as plt
x = (2010, 2011, 2012, 2013, 2014, 2015, 2016 , 2017 , 2018 ,2019)
y = (25320,29023,35043,42323,47007,51756,54280,55420,57202,61568)

plt.plot(x,y)

plt.xlabel('Year')
plt.ylabel('Units ')
plt.title('Porsche Sales in North America')

plt.grid(True)

plt.savefig('line_plot_porsche.png')

plt.show()