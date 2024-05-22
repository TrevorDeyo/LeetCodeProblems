from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        missingNums = []

        for num in range(len(arr) + k):
            if num not in arr and num != 0:
                missingNums.append(num)


        if len(missingNums) < k:
            if len(missingNums) <= 1:
                return arr[-1] + k

            add = k - len(missingNums)
            if arr[-1] > missingNums[-1]:
                last = arr[-1]
            else:
                last = missingNums[-1]
            
            return last + add

        return missingNums[k-1]

solution = Solution()

if solution.findKthPositive(arr = [1,2], k = 1) == 3:
    print('passed1')

if solution.findKthPositive(arr = [2,3,4,7,11], k = 5) == 9:
    print('passed2')

if solution.findKthPositive(arr = [1,2,3,4], k = 2) == 6:
    print('passed3')

if solution.findKthPositive(arr = [5,6,7,8,9], k = 9) == 14:
    print('passed4')

if solution.findKthPositive(arr = [1,3,5,9,12,15,16,18,19,20,21,22,23,25,26,27,28,30,32,33,34,35,40,41,42,45,48,49,51,53,54,58,60,61,62,63,65,66,67,68,69,72,73,78,79,80,81,82,84,85,89,90,91,92,93,94,96,97,101,105,106,107,108,111,114,117,118,119,120,123,124,125,127,129,130,131,132,133,134,135,136,137,138,139,141,142,149,153,155,156,158,159,161,162,165,166,167,171,172,173,174,176,177,178,180,181,182,183,184,186,189,192,193,194,196,197,198,199,201,202,206,207,208,210,211,212,213,214,216,217,219,222,224,226,227,228,230,231,232,235,237,238,241,242,243,244,246,247,250,251,252,255,256,258,260,262,263,264,265,266,268,269,270,271,272,276,278,279,281,282,284,285,286,287,289,290,293,294,296,297,298,300,304,306,307,310,311,315,316,319,321,322,324,326,328,329,330,332,337,338,343,344,345,346,347,348,349,351,353,354,355,356,357,359,361,363,364,365,366,367,368,369,370,371,372,373,375,376,377,378,379,380,381,382,383,385,386,388,389,390,392,395,396,399,401,402,403,404,405,406,407,408,409,412,414,416,417,418,419,421,423,424,427,429,430,431,432,433,435,436,438,440,441,443,444,445,446,447,449,451,452,454,456,457,458,460,462,463,464,465,466,467,469,471,472,473,475,476,477,478,479,483,484,485,486,493,494,497,498,500,501,502,504,506,508,511,512,513,515,516,518,519,520,522,524,525,526,527,529,530,532,533,535,538,539,540,541,542,543,544,545,546,548,549,550,553,557,558,560,561,562,564,566,567,568,569,571,572,573,574,575,576,577,578,579,580,583,584,585,586,588,591,594,595,596,597,598,603,607,608,609,612,616,618,622,624,625,629,631,632,633,634,637,638,639,640,641,642,644,645,648,649,650,653,654,655,657,658,660,661,662,663,664,665,667,668,669,670,672,674,675,678,679,681,682,684,687,689,692,693,696,697,698,699,700,701,705,708,710,711,712,713,716,720,723,724,726,727,730,731,732,733,734,735,736,737,738,740,741,742,744,745,747,748,750,751,755,757,760,761,762,764,765,767,768,770,771,772,775,777,780,781,782,788,790,797,798,800,802,805,806,810,811,812,813,814,815,816,817,818,819,820,821,822,823,825,827,828,829,831,832,833,835,836,837,840,841,842,843,844,846,847,848,850,851,853,855,856,857,858,859,860,861,862,863,867,870,872,875,877,882,883,884,885,886,887,888,889,890,891,892,893,896,898,902,904,905,906,908,909,911,913,914,915,918,920,924,925,927,928,929,931,933,934,935,936,938,939,941,942,943,944,947,948,949,950,951,952,953,954,955,957,960,961,962,963,964,965,967,969,972,974,975,976,977,978,979,980,981,984,985,987,988,989,991,992,993,994,996,1000], k = 381) == 1001:
    print('passed5')