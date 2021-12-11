import ray
import math
import time
import csv

import particle
import master
ray.init()

fields = ['Number of Particles', 'Ray', 'Single']
particles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000]
p_fields = ['p', 'Ray']

p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def test_particles():
    time_arr = []
    for i in particles:
        time1 = time.time()
        particle.calculate(i)
        ray_time = time.time() - time1
        time2 = time.time()
        master.calculate(i)
        single_time = time.time()- time2
        time_arr.append([i, ray_time, single_time])
    filename = "changeNumofParticles.csv"
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(time_arr)

def test_p():
    time_arr = []
    for i in p:
        time1 = time.time()
        particle.calculate(1000, i)
        ray_time = time.time() - time1
        time_arr.append([i, ray_time])
    filename = "changep.csv"
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(p_fields)
        csvwriter.writerows(time_arr)

if __name__ == "__main__":
    test_p()