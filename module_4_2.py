def test_function(a):
    a = 10
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

inner_function()
