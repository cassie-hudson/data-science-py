#Visualizing Data

#matplotlib--works well for simple bar charts, line charts and scatterplots--not good for web
#matplotlib.pyplot allows building a visualization step-by-step that can be saved or displayed

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()

#Bar Charts

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Ghandi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#bars are default width 0.8, so adding 0.1 to the left coordinates so each bar is centered

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
#label x axis with bars at center
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()

#Histograms

from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8) #shift each bar to the left by 4, give each bar its correct height, give each bar a wdith of 8

plt.axis([-5, 105, 0, 5]) #first two digits x axis, second two digits y axis

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)

plt.xticks(years)

plt.ylabel("# of times I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False) #if you don't do this, the x-axis will be labeled with 0, 1

plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.show()

#Line charts

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#making multiple calls to plt.plot
#show multiple series on the same chart

plt.plot(xs, variance, 'g-', label = 'variance') #green solid line
plt.plot(xs, bias_squared, 'r-.', label = 'bias^2') #red dot-dashed line
plt.plot(xs, total_error, 'b:', label = 'total error') #blue dotted line

#including a legend; loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Trade-Off")
plt.show()

#SCATTERPLOTS

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#label each plot point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy =(friend_count, minute_count), #put the label with its points
                 xytext =(5, -5), #slighly offset the label
                 textcoords='offset points')
plt.title('Daily Minutes vs. Number of Friends')
plt.xlabel('# of friends')
plt.ylabel('daily minutes spent on the site')
plt.show()

#misleading scattplot

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1")
plt.ylabel("test 2")
plt.show()

#shows equal scale

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.axis("equal")
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1")
plt.ylabel("test 2")
plt.show()