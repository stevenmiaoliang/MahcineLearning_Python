from math import  sqrt

#don't do normalized
def distanceEuler(features1,features2):
    if len(features1) != len(features2):
        return -1
    sum_of_squares = sum([pow(features1[i]-features2[i],2) for i in range(len(features1))])
    return  sum_of_squares

# do normalied
def distancePerson(features1,features2):
    if len(features1) != len(features2):
        return -1
    sum1 = sum(features1);
    sum2 = sum(features2)

    sum1sq = sum([pow(v,2) for v in features1])
    sum2sq = sum([pow(v,2) for v in features2])

    pSum = sum([features1[i]*features2[i] for i in range(len(features1))])
    num = pSum - (sum1*sum2/len(features1))
    den = sqrt((sum1sq-pow(sum1,2)/len(features1))*(sum2sq-pow(sum2,2)/len(features2)))
    if den == 0:return  0
    return 1.0-num/den


if __name__ == '__main__':
    features1 = [2,2,3,4,5,6,7,8,9];
    features2 = [1, 2, 3, 4, 5, 6, 7,9, 9];

    print  distanceEuler(features1,features2)


