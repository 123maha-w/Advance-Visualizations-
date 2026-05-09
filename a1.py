import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")
Id = pd.read_csv('Test.csv')

print (Id.head())
print (Id.info())

sns.barplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'])
sns.displot(Id['SepalLengthCm'])
plt.show()

sns.displot(Id['SepalLengthCm'],kde=False,rug=True)
plt.show()

sns.jointplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'])
plt.show()

sns.jointplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'],kind="hex")
plt.show()

sns.jointplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'],kind="kde")
plt.show()

sns.pairplot(Id[['SepalLengthCm','PetalLengthCm','Species']])
plt.show()

sns.stripplot(x=Id['Species'],y=Id['PetalLengthCm'],jitter=True)
plt.show()

sns.swarmplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'])
plt.show()

sns.barplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'],hue=Id['Species'])
plt.show()

sns.countplot(x=Id['Species'])
plt.show()

sns.pointplot(x=Id['SepalLengthCm'],y=Id['PetalLengthCm'],hue=Id['Species'])
plt.show()