# Design Pattern
- attempts to record those aspects of a recurring design in object-oriented systems
- in order to solve a problem or a class of problems
## Creational Pattern
- Early stage of object lifecycle
- Patterns that solve the problems associated with object creation and initialization
    - Singleton pattern:
        - makes sure any instances of a class share the same initial state
        - or only one instance of a class is created
    - Prototype pattern:
        - smart approach to instantiate hundreds of similar objects
    - Factory pattern:
        - creating class instances in repeatable and predictable fashion
    - Builder pattern:
        - separates out the construction of an object
        - same construction or assembling process can be used
        - to build different representative instances
## Structural Pattern
- Patterns that concern themselves with the composition and assembling of objects into meaningful and useful structures
- Patterns that provide the architect and developer with reusable behaviors
    - Proxy pattern:
        - wraps another object to do operations while accessing to it
    - Adapter pattern:
        - a special object that converts the interface of one object to another object that the client expects or can understand it
        - an adapter wraps one of the objects to hide the complexity of conversion

## Behavioral Pattern
- Later stage of object lifecycle
- Patterns that solve the problems originating with runtime interactions of objects
    - Observer pattern: object want to be notified when the state of a resource changes
    - Iterator pattern: 