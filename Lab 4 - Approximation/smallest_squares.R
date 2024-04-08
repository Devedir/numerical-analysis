Q <- function(m, x, a_vec) {
  acc <- a_vec[1]
  for (i in 1:m) {
    acc <- acc + a_vec[i+1] * x^i
  }
  return(acc)
}

S <- function(k, n, x_vec) {
  acc <- 1.0
  for (i in 2:n) {
    acc <- acc + x_vec[i]^k
  }
  return(acc)
}

T <- function(k, n, x_vec, y_vec) {
  acc <- 0
  for (i in 1:n) {
    acc <- acc + x_vec[i]^k * y_vec[i]
  }
  return(acc)
}

approximating <- function(x, x_vec, y_vec, m) {
  n <- length(x_vec)
  
  S_mat <- matrix(numeric((m+1)^2), m+1, m+1)
  for (row in 0:m) {
    for (col in 0:m) {
      S_mat[row+1, col+1] <- S(row + col, n, x_vec)
    }
  }
  
  T_vec <- numeric(m+1)
  for (i in 0:m) {
    T_vec[i+1] <- T(i, n, x_vec, y_vec)
  }
  
  a_vec <- solve(S_mat, T_vec)
  return(Q(m, x, a_vec))
}

# przykładowe dane
x_values <- c(1, 2, 5, 7)
y_values <- c(3.2, 2, 2.5, 3.8)

# funkcja jednej zmiennej do rysowania
example <- function(x) {
  return(approximating(x, x_values, y_values, 2))
}
curve(Vectorize(example, 'x')(x), min(x_values) - 1, max(x_values) + 1, lwd=2, ylab='y')
points(x_values, y_values, pch=16, col='red')
