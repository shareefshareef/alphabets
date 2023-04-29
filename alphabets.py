class Alphas():
	
	def __init__(self,trow=5,sym="*"):
		self.trows = trow
		self.sym = sym
		
	def a(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or col == 1 or col == z or row == z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def b(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or row == z or col == z or col == z//2 or row == z//2+1 and col>=z//2:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def c(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or row == z or col == 1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def d(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or col == z//2 or col == z or row == z:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def e(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or row == z or row == z//2+1 and col>=z//2 or col == z//2:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def f(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or col == z//2 or row == z//2+1 and col>=z//2:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def g(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or col == 1 or row == z or row == z//2+1 and col>z//2 or col == z and row>=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def h(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col== 1 or col == z or row == z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def i(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or row == z or col == z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def j(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or col == z//2+1 or row==z and col<=z//2+1 or col == 1 and row>=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def k(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 or row+col == z or row-col == 1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def l(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 or row == z:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def m(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 or col ==z or row-col==0 and row<=z//2+1 or row+col == z+1 and row<=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def n(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 or col ==z or row == col:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def o(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 or col ==z or row == 1 or row  == z:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def p(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col ==  1 or row == 1 or row == z//2+1 or col == z and row<=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def q(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 and row<=z//2+1 or row == 1 or row == z//2+1 or col == z:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def r(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col ==  1 or row == 1 or row == z//2+1 or col == z and row<=z//2+1 or row==col and row>=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def s(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1  or row == z or row == z//2+1 or col == 1 and row<=z//2+1 or col == z and row>= z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def t(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or col == z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
			
	def u(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col ==  1 or row == z or col == z:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def v(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row-col == 2 or row+col == z+z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def x(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == col or row+col ==z+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def y(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == col and row<=z//2+1 or row+col == z+1 and row<= z//2+1 or col == z//2+1 and row>=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def z(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == 1 or row == z or row+col == z+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	def w(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if col == 1 or col == z or row == col and row >=z//2+1 or row+col == z+1 and row>=z//2+1:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()

	def one(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == z or col == z//2+1 or row+col == z-1 and row<=z//2:
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()
	
	def two(self):
		z = self.trows
		for row in range(1,z+1):
			
			for col in range(1,z+1):
				
				if row == z or row+col == z-1 and row<=z//2 or row +col == z+1 and row>=z//2 :
					print(self.sym,end=' ')
				else:
					print(' ',end=' ')
			print()

