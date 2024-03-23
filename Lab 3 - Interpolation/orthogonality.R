p <- function(i, x) {
  if (i == 0) return(1)
  if (i == 1) return(x)
  return(((2*i+1)/(i+1))*x*p(i-1,x) - (i/(i+1))*p(i-2, x))
}

pp <- function(i, j, x) {
  return(p(i, x) * p(j, x))
}

for (i in 0:6) {
  for (j in 0:6) {
    if (i == j) next
    ppv <- Vectorize(function(x) pp(i, j, x))
    print(integrate(ppv, -1, 1))
  }
}