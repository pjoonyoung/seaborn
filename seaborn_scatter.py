import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset('iris')

# sns.regplot(x='petal_length',y='petal_width',data=iris)
# sns.scatterplot(x='petal_length',y='petal_width',data=iris,
#                 hue='species',style = 'species',s=100
#                 )

sns.pairplot(iris, diag_kind='kde',hue='species') # 모든 변수에 대한 산점도 그리기
plt.show()