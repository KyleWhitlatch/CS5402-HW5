from sklearn.cluster import k_means
import numpy as np

X = np.array([[3,5],
              [3,4],
              [2,8],
              [2,3],
              [6,2],
              [6,4],
              [7,3],
              [7,4],
              [8,5],
              [7,6]])

q1 = np.array([[4,6],[5,4]])
q3 = np.array([[3,3],[8,3]])

def main():
    kmeans = k_means(X,n_clusters=2,init=q3)
    print(kmeans)


if __name__ == '__main__':
    main()