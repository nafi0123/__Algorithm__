def create_lps(pat,M,lps):
	len=0
	lps[0]=0
	i=1
	while i<M:
		if pat[i]==pat[len]:
			len+=1
			lps[i]=len
			i+=1
		else:
			if len!=0:
				len=lps[len-1]
			else:
				lps[i]=0
				i+=1

def KMPSearch(pat,txt):
	M=len(pat)
	N=len(txt)
	lps=[0]*M
	create_lps(pat,M,lps)
	j=0
	i=0
	while (i<N):
		if pat[j]==txt[i]:
			i+=1
			j+=1
		else:
			if j!=0:
				j=lps[j-1]
			else:
				i+=1
		if j==M:
			print(i-M)
			j=lps[j-1]
			
if __name__ == '__main__':
	txt = "texttext"
	pat = "text"
	KMPSearch(pat, txt)
