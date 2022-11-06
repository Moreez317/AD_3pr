from firstTask import data_by_decade
import matplotlib.pyplot as plt 
import matplotlib as mpl

data = data_by_decade()

def barGraph():
    fig = plt.figure()

    plt.bar(data.index, data.Price, color=mpl.cm.plasma(data.Price / float(max(data.Price))), edgecolor="black", linewidth=1.5)

    plt.title("Диаграмма среднегодовых цен на золото", fontdict={"fontsize": 14})

    plt.xlabel("год", fontdict={"fontsize": 10})
    plt.ylabel("цена", fontdict={"fontsize": 10})
    plt.xticks(size=8, rotation=45)
    plt.yticks(size=8)

    xmin, xmax = plt.xlim()
    
    plt.xlim(xmin + 3, xmax - 3)
    
    fig.tight_layout()
    
    plt.show()
    
def pieGraph():
    fig = plt.figure()
    
    patches, _, labels = plt.pie(data.Price, startangle=90, autopct="%.1f%%", wedgeprops={"edgecolor": "black","linewidth": 1.5}, textprops={"fontsize": 11})
    
    plt.title("Диаграмма средних цен на золото за десятилетия",
        fontdict={"fontsize": 14})

    plt.legend(patches, data.index, loc=1)
    
    labels[0].update({"text": ""})
    labels[1].update({"text": ""})
    
    fig.tight_layout()
    
    plt.show()


def scatterGraph():
    fig = plt.figure()
    
    plt.plot(data.index, data.Price, "-o", color="crimson", markerfacecolor="white", markeredgecolor="black", markeredgewidth=1.5)
    
    plt.title("Диаграмма средних цен на золото за десятилетия", fontdict={"fontsize": 14})
    
    plt.grid(color="ivory")
    
    ax = plt.gca()
    ax.set_axisbelow(True)
    ax.set_facecolor("#e5ecf6")
    
    fig.tight_layout()
    
    plt.show()

print('Выберете диаграмму: 1 - столбчатая, 2 - круговая, 3 - график')

graphType = int(input())

if graphType == 1:
    barGraph()
elif graphType == 2:
    pieGraph()
elif graphType == 3:
    scatterGraph()