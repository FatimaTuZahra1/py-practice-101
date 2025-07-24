def score(x, y):
    # equation of a circle (x - h)² + (y - k)² = r²
    #central coords h = k = 0, (x)² + (y)² = r²
    radius = ((x**2) + (y**2))**0.5

    if 0 <= radius <= 1:
        return 10
    elif 1<= radius <=5:
        return 5
    elif 5<= radius <= 10:
        return 1
    else:
        return 0

print("The Score is: ",score(0.5,-4))