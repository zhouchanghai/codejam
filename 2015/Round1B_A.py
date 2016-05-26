def solve(N):
	if N <= 20: return N

	size = len(str(N))
	step = 11
	d = 2
	#at the beginning of each loop, the number is 100...01 of d digits
	while d < size:
		step += 10**(d//2)-2 + 10**(d-d//2) - 2 + 1 #99...9
		step += 2 # 10...01
		d += 1
	assert d == size
	#N is 100..01
	if 10**(d-1)+1 == N: return step
	#N is 100..00
	if 10**(d-1) == N: return step-1
	#N is 1xx..0
	if N%10 == 0: return solve(N-1)+1
	
	head = str(N)[:size//2]
	tail = str(N)[size//2:]
	#head is 10...0, no reverse needed
	if int(head) == 10**(len(head)-1):
		return step + int(tail) - 1
	#reverse the head
	head = head[::-1]
	step += int(head)-1 + 1 + int(tail)-1
	return step
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N = int(f.readline().strip())
	print N
	res = solve(N)
	print "Case #%d: %s"%(tc, str(res))
	print "="*20
	print >>out, "Case #%d: %s"%(tc, str(res))

out.close()