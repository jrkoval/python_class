import math

class Match:
    def __init__(self):
        self.males = {}
        self.females = {}
        fobj = open('system', 'r')
        for line in fobj:
            fields = line.split()
            name = fields[0]
            gender = fields[1]
            age = int(fields[2])
            salary = int(fields[3])
            if gender == 'm':
                self.males[name] = {'age':age,'salary':salary}
            else:
                self.females[name] = {'age':age,'salary':salary}
    def distance(self, male,female):
        #return distance between specified male and female
        age1 = self.males[male]['age']
        sal1 = self.males[male]['norm']
        age2 = self.females[female]['age']
        sal2 = self.females[female]['norm']

        return math.sqrt( ( age1-age2)**2 + (sal1-sal2)**2)
    
    def recommendFemale(self, male):
        # compute the distance between the specified male with all the other females
        # sort it
        # return the female who is the shortest distance to the male
        distances = []
        
        for female in self.females:
            distance = self.distance(male, female)
            distances.append((distance, female))
        distances.sort()
        return distances[0][1]
    def normalize(self):
        salaries = []
        for male in self.males:
            #salaries.append(male.salary)
            salary = self.males[male]['salary']
            salaries.append(salary)
        for female in self.females:
            #salaries.append(female.salary)
            salary = self.females[female]['salary']
            salaries.append(salary)
            
        min_salary = min(salaries)
        max_salary = max(salaries)
        range = max_salary - min_salary
        for male in self.males:
            #normalize_sal = (male.salary - min_salary)/range
            #self.males[male]['norm'] = normalized_sal
            salary = self.males[male]['salary']
            norm = float((salary-min_salary))/range
            self.males[male]['norm'] = norm
        
        for female in self.females:
            #normalize_sal = (female.salary - min_salary)/range
            #self.females[female]['norm'] = normalized_sal
            salary = self.females[female]['salary']
            norm = float(salary-min_salary)/range
            self.females[female]['norm'] = norm           
    def show(self):
        for male in self.males:
            print(male, end=" ")
            print(self.males[male]['age'],end=" ")
            print(self.males[male]['salary'],end=" ")
            print(self.males[male]['norm'],end=" ")
            
            print()
        for female in self.females:
            print(female, end=" ")
            print(self.females[female]['age'],end=" ")
            print(self.females[female]['salary'],end=" ")
            print(self.females[female]['norm'],end=" ")
            print()

m = Match()
m.normalize()
m.show()
#print(m.distance('murali', 'mary'))
print(m.recommendFemale('murali'))

