import hailstone.sequence
import hailstone.bitmap

# create the sequence fo hailstone numbers for 17
l = []
n = 17
hailstone.sequence.update(n, l)
print('hailstone sequence of 17:')
print(l)
# create the bitmap fo hailstone numbers for 17
# bitmap allows for numbers up to 10,000
m = hailstone.bitmap.generate(n, 10000)
print('hailstone bitmap of 17:')
hailstone.bitmap.print_map(m)

# accumulate into a bitmap all hailstone numbers of numbers 1-100
for n in range(1, 100):
    hailstone.bitmap.update(n, m)

print('aggreagte hailstone bitmap of [1,99]:')
hailstone.bitmap.print_map(m)

