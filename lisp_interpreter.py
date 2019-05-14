#problems = [
#  ['let', 'x', ['+', 1, 2], 'x'], 
#  [['lambda', ['a', 'b'], ['+', 'a', 'b']], 4, 6]
#]


def eval(expr, env):
  if type(expr) is int:
    return expr

  if type(expr) is str:
    if expr in env:
      return env[expr]
    else:
      return expr

  if expr[0] == 'lambda':
    return {'arguments':expr[1], 'expression':expr[2]}

  operator = eval(expr[0], env)
  args = [eval(x, env) for x in expr[1:]]

  if type(operator) is dict:  # is lambda
    a = operator['arguments']
    e = operator['expression']
    new_env = dict(list(env.items()) + list(zip(a, args)))
    return eval(e, new_env)
  
  if operator == 'let':
    new_env = dict(list(env.items()) + [(expr[1], eval(expr[2], env))])
    return eval(expr[3], new_env)
  
  if operator == '+':
    return sum(args)
  
  if operator == '*':
    product = 1
    for i in args:
      product *= i
    return product

#for p in problems:
#  print(eval(p, {}))
