def returnfunction(text1): 
	def printfunc(text2):	
		print(text1+text2)
	return printfunc
	
func = returnfunction('foo')

func('bar')
