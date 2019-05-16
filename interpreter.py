
def is_syntax(expr):
  return expr[0] in ['lambda', 'let', 'if', 'equal']


def eval_syntax(expr, env):
  if expr[0] == 'lambda':
    return {'arguments':expr[1], 'expression':expr[2], 'env': env}

  if expr[0] == 'let':
    new_env = dict(list(env.items()) + [(expr[1], eval(expr[2], env))])
    return eval(expr[3], new_env)
  
  if expr[0] == 'if':
    condition = eval(expr[1], env)
    if condition == 1:
      return eval(expr[2], env)
    elif condition == 0:
      return eval(expr[3], env)
    else:
      print('error')

  if expr[0] == 'equal':
    if eval(expr[1], env) == eval(expr[2], env):
      return 1
    return 0


def eval(expr, env):
  if type(expr) is int:
    return expr

  if type(expr) is str:
    if expr in env:
      return env[expr]
    else:
      return expr

  if is_syntax(expr):
    return eval_syntax(expr, env)

  operator = eval(expr[0], env)
  args = [eval(x, env) for x in expr[1:]]

  if type(operator) is dict:  # is lambda
    a = operator['arguments']
    e = operator['expression']
    env_ = operator['env']
    new_env = dict(list(env_.items()) + list(zip(a, args)))
    return eval(e, new_env)
  
  if operator == '+':
    return sum(args)
  
  if operator == '*':
    product = 1
    for i in args:
      product *= i
    return product
  
  if operator == '-':
    return args[0] - sum(args[1:])


m = ["lambda", "a", ["b", ["lambda", "x", [["a", "a"], "x"]]]]
y = ["lambda", "b", [m, m]]

def factorial(x):
  fac = ['lambda', 'f', 
          ['lambda', 'n',
            ['if', ['equal', 'n', 0], 
              1, 
              ['*', 'n', ['f', ['-', 'n', 1]]]]]]
  return eval([[y, fac], x], {})



# References: 
# 
# - https://mvanier.livejournal.com/2897.html
# - https://rosettacode.org/wiki/Y_combinator