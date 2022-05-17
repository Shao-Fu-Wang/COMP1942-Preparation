import numpy as np
from fractions import Fraction


def npmap(func, array):
    try:
        my_list = list(array)
        if type(my_list[0]) == np.ndarray:
            my_list = list(map(lambda x: npmap(func, x), my_list))
        else:
            my_list = list(map(func, my_list))
        return np.array(my_list)
    except Exception as e:
        print(e)
        return func(array)


def pca(data):
    # calculate mean vector
    mean = []
    for i in range(len(data[0])):
        print("for dimension {},\nmean = (".format(i + 1), end="")
        temp = 0

        for j in range(len(data)):
            print(data[j][i], end=" ")
            if j != len(data) - 1:
                print("+", end=" ")
            else:
                print(")", end="")
            temp += data[j][i]

        mean.append(temp / len(data))
        print(" / {} = {}".format(len(data), mean[i]))

    print("mean vector = {}".format(mean))
    print()

    # calculate difference between mean vector and data points
    y_matrix = np.zeros((len(data[0]), len(data)))

    for i in range(len(data)):
        print()
        print(
            "for data {} {}, difference from mean vector\n=".format(i + 1, data[i]),
            end=" ",
        )
        print("[", end="")
        for j in range(len(data[i])):
            y_matrix[j, i] = data[i][j] - mean[j]
            print("{} - {}".format(data[i][j], mean[j]), end="")
            if j != len(data[i]) - 1:
                print(",", end=" ")
        print("]", end="")
        print(" = [", end="")
        for j in range(len(data[i])):
            print(y_matrix[j, i], end="")
            if j != len(data[i]) - 1:
                print(",", end=" ")
        print("]")

    print()
    print()
    print("Y = ")
    print(y_matrix)
    y_matrix_T = np.transpose(y_matrix)
    print()
    print("Y^T = ")
    print(y_matrix_T)
    cov_matrix = np.dot(y_matrix, y_matrix_T) / len(data)
    print()
    print("covariance matrix = 1/{} * Y * Y^T = ".format(len(data)))
    print(cov_matrix)
    print()

    # find eigenvalues and eigenvectors
    c = cov_matrix[0, 0] * cov_matrix[1, 1] - cov_matrix[0, 1] * cov_matrix[1, 0]
    b = (cov_matrix[0, 0] + cov_matrix[1, 1]) * -1
    print()
    print("λ^2", end=" + ")
    print(b, end=" * ")
    print("λ", end=" + ")
    print(c, end=" = 0\n")

    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    print("λ = {}".format(eigenvalues))
    print()
    # simplify negatives
    # for i in range(len(eigenvectors)):
    #     temp = True
    #     for j in range(len(eigenvectors[i])):
    #         if eigenvectors[i][j] == abs(eigenvectors[i][j]):
    #             temp = False
    #     if temp == True:
    #        eigenvectors[i] = abs(eigenvectors[i])
    #     eigenvectors[i] = np.sort(eigenvectors[i])[::-1]
    # print("eigenvectors = \n{}".format(eigenvectors))
    print()
    print(type(np.sort(eigenvectors[1])[::-1]))
    print()

    # rearrange eigenvectors
    print()
    print(npmap(float, cov_matrix))
    print()
    einvalues, einvectors = np.linalg.eig(npmap(float, cov_matrix))
    einvalues = npmap(lambda x: Fraction(x).limit_denominator(1000), einvalues)
    # einvalues = npmap(einvalues)
    print("einvalues", einvalues)
    print("einvectors", einvectors)

    einvecs = []
    for i, value in enumerate(einvalues):
        vec = einvectors[:, i]
        einvecs.append(vec)
        x2_ratio = Fraction(vec[0] / vec[1]).limit_denominator(10000)
        minus_matrix = npmap(Fraction, cov_matrix - value * np.identity(2))

    einvec_sorted = [x for _, x in sorted(zip(list(einvalues), list(einvecs)))][::-1]
    einvec_sorted = [x.reshape(2, 1) for x in einvec_sorted]
    phi = np.concatenate(einvec_sorted, axis=1)
    print("phi", phi)

    # phi = np.sort(eigenvectors, axis=0)
    # phi = eigenvectors[0]
    # print("lmao")
    print(phi)
    # for i in range(1, len(eigenvectors)):
    #     phi = np.column_stack((phi, eigenvectors[i]))
    # print()
    # transform the vectors with the eigenvector matrix
    phi_T = np.transpose(phi)
    # phi_T = np.array([[0.4438, -0.8961], [0.8961, 0.4438]])

    print()
    print("Φ=\n{}".format(phi))
    print()
    print("Y = Φ^T * X =")
    print(phi_T)
    print("* X")
    print()
    print()

    trans_data = []
    for i in range(len(data)):
        temp = np.round(np.dot(phi_T, data[i]), 2)
        trans_data.append(np.ndarray.tolist(temp))
        print("for data {},".format(data[i]))
        print("Φ * {} = {}".format(data[i], temp))
        print()
    print()

    # calculate new mean vector
    new_mean = []
    for i in range(len(trans_data[0])):
        print("for dimension {},\nmean = (".format(i + 1), end="")
        temp = 0

        for j in range(len(trans_data)):
            print(trans_data[j][i], end=" ")
            if j != len(trans_data) - 1:
                print("+", end=" ")
            else:
                print(")", end="")
            temp += trans_data[j][i]

        new_mean.append(temp / len(trans_data))
        print(" / {} = {}".format(len(trans_data), new_mean[i]))

    print("mean vector of transformed data points = {}".format(new_mean))
    print()

    for i in range(len(trans_data)):
        print()
        print(
            "for data {} {}, final transformed vector\n=".format(i + 1, data[i]),
            end=" ",
        )
        print("[", end="")
        for j in range(len(trans_data[i])):
            print("{} - {}".format(trans_data[i][j], new_mean[j]), end="")
            if j != len(trans_data[i]) - 1:
                print(",", end=" ")
        print("]", end="")
        print(" = [", end="")
        for j in range(len(trans_data[i])):
            print(trans_data[i][j] - new_mean[j], end="")
            if j != len(trans_data[i]) - 1:
                print(",", end=" ")
        print("]")


# points = [[3, 3], [0, 2], [-1, -1], [2, 0]]
points = [[2, 2], [4, 4], [1, 5], [5, 1]]
# points = [[5, 5], [2, 4], [1, 1], [4, 2]]
# points = [[20, 16], [17, 17], [19, 19], [16, 20]]
# points = [[12, 14], [16, 18], [10, 20], [16, 10]]
# points = [[6, 7], [8, 9], [5, 10], [8, 5]]
pca(points)
