# Test-Assignment4


Foobar is a Python library for dealing with word pluralization.

## Mockito Powerups

**1. How do you verify that a mock was called ?**
* In following code snippet you see the Verify() method being called. If the code in the ```//Arrange``` section is not being called, we can not verify the mock.
 
```csharp 
[Test]
        public async Task GetBookingsForCustomer_Should_Return_Bookinglist()
        {
            //Arrange
            _bookingStorageMock.Setup(mock => mock.GetBookingsForCustomerId(1)).ReturnsAsync(GetFakeBookings());

            //Act
            var actualMocked = await _bookingService.GetBookingsForCustomerId(1);
            var expected = GetFakeBookings();


            //Assert
            //Assert.That(actualMocked.Count, Is.EqualTo(expected.Count));
            _bookingStorageMock.Verify(mock => mock.GetBookingsForCustomerId(1));
        }
```
**2. How do you verify that a mock was NOT called ?**

* In the ```//Assert``` section u will see that we give the ```Verify()``` methods a parameter of ```Times.Never()```. With this we verify that the mock is never to be verified.
```csharp 
[Test]
        public async Task GetBookingsForCustomer_Should_Return_Bookinglist()
        {
            //Arrange
            _bookingStorageMock.Setup(mock => mock.GetBookingsForCustomerId(1)).ReturnsAsync(GetFakeBookings());

            //Act
            var actualMocked = await _bookingService.GetBookingsForCustomerId(1);
            var expected = GetFakeBookings();


            //Assert
            //Assert.That(actualMocked.Count, Is.EqualTo(expected.Count));
            _bookingStorageMock.Verify(mock => mock.GetBookingsForCustomerId(1), Times.Never());
        }
```

**3. How do you specify how many times a mock should have been called ?**

* In the ```//Assert``` section u will see that we give the ```Verify()``` methods a parameter of ```Times.Never()```.
```csharp
[Test]
        public async Task GetBookingsForCustomer_Should_Return_Bookinglist()
        {
            //Arrange
            _bookingStorageMock.Setup(mock => mock.GetBookingsForCustomerId(1)).ReturnsAsync(GetFakeBookings());

            //Act
            var actualMocked = await _bookingService.GetBookingsForCustomerId(1);
            var expected = GetFakeBookings();


            //Assert
            //Assert.That(actualMocked.Count, Is.EqualTo(expected.Count));
            _bookingStorageMock.Verify(mock => mock.GetBookingsForCustomerId(1), Times.Exactly(2));
        }
```



## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
