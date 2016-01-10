import sys

def main():
	n = int(input().strip())
	t = [int(t_temp) for t_temp in input().strip().split(' ')]

	lastTime = t[0]
	for time in t:
	    if time <= lastTime:
	        lastTime += 1
	    else:
	        lastTime = time + 1
	     
	print(lastTime-1)

if __name__ == "__main__":
	sys.exit(main())