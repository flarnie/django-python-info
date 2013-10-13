# Comparing Ruby and Python

## Toolsets

| Ruby          | Python        |
| ------------- |---------------|
| [rvm][rvm]    | [virutal env][v-env] |
| [Ruby on Rails][r-o-r] | [Django][django] |
| [Sinatra][sinatra] | [Flask][flask]  |
| [Ruby Gems][gems]: `gem install my_library` |  [PyPI and Packages][pip]: `pip install my_library` |

[rvm]: http://rvm.io/
[v-env]: http://www.virtualenv.org/en/latest/
[r-o-r]: http://rubyonrails.org/
[django]: https://www.djangoproject.com/
[sinatra]: http://www.sinatrarb.com/documentation.html
[flask]: http://flask.pocoo.org/
[gems]: http://rubygems.org/
[pip]: https://pypi.python.org/pypi

## Key Differences

| Ruby          | Python        |
| ------------- |---------------|
| Blocks, Procs, and Lambdas | [Generators][generators-python] |
| `do .. end` and `{ .. }` | [Indentation][indentation-python] |
| closures are blocks that have full r/w access to outer scope var.s | closures are nested functions that have only r access to outer scope var.s |
| Only `false` and `nil` are untruthy | `0` of anything, an empty anything, `False` and `None` [are all untruthy][truth-testing-python] |
| No multiple inheritance | [Multiple Inheritance][mult-inh-python] |
| Modules can be used for namespacing, but it's kind of a pain | [Auto-namespacing][namespacing-python] of any libraries or modules by default |
| Call a method with `instance.method_name` | Call a method with `instance.method_name()`.  Forget the parens at your own peril! | 

### Basic Generator Example

```python
# define a generator function
def generate_factors(num):
  fac = num
  while fac > 1:
    if num % fac == 0
    yield fac
  fac -= 1
  
# use the generator
for f in generate_factors(10):
  print f
  
# prints out the factors
=> 10
=> 5
=> 2
```

[generators-python]: http://www.dreamincode.net/forums/topic/198034-generators/
[indentation-python]: http://www.secnetix.de/olli/Python/block_indentation.hawk
[truth-testing-python]: http://docs.python.org/2/library/stdtypes.html#truth-value-testing
[mult-inh-python]: http://docs.python.org/release/1.5/tut/node66.html
[namespacing-python]: http://docs.python.org/2/tutorial/modules.html
[adv-generators-python]: http://www.dreamincode.net/forums/topic/287295-advanced-python-generators/