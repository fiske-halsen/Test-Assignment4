# Assigenment 4

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

* In the ```//Assert``` section u will see that we give the ```Verify()``` methods a parameter of ```Times.Never()```. 
With this we verify that the mock is never to be verified.

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

* In the ```//Assert``` section u will see that we give the ```Verify()``` methods a parameter of ```Times.Exactly(2)```. WIth this parameter we verify that the mock is to be called exactly 2 times.
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

**4. How do you verify that a mock was called with specific parameters ?**

* In the ```//Assert``` section u will see that we give the ```Verify()``` an arrow function. We expect that the methods is being called with argument ```p = 1``` with the ```It.is``` method

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
            _bookingStorageMock.Verify(mock => mock.GetBookingsForCustomerId(It.Is<int>(p => p == 1)));
        }
```

**5. How do you use a predicate to verify the properties of the arguments given to a call to the nock ?**

* Predicates are expressions that can be evaluted to a boolean value i.e. true or false. As seen on the example below, we have created a predicate that says the argument p should be creater than 0 ```It.Is<int>(p => p > 0))```. Note that the predicate is only evaluated when the method is actually invoked and in the below case p represents the invoking parameter for GetBookingsForCustomerId.

```csharp
   [Test]
        public async Task GetBookingsForCustomer_Should_Return_Bookinglist()
        {
            //Arrange
            _bookingStorageMock.Setup(mock => mock.GetBookingsForCustomerId(It.Is<int>(p => p > 0))).ReturnsAsync(GetFakeBookings());

            //Act
            var actualMocked = await _bookingService.GetBookingsForCustomerId(1);
            var expected = GetFakeBookings();

            //Assert
            Assert.That(actualMocked.Count, Is.EqualTo(expected.Count));
            _bookingStorageMock.Verify(mock => mock.GetBookingsForCustomerId(It.Is<int>(p => p == 1)));
        }
```
