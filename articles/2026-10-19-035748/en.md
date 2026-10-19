# Mastering Java Sealed Classes & Exhaustive Matching

Unlock the power of Java’s sealed classes to enforce strict hierarchies and ensure foolproof pattern matching. Learn how this feature enhances type safety, reduces bugs, and simplifies complex logic with exhaustive checks—perfect for modern Java development.

## 🔑 The Core of This Topic
Java’s sealed classes introduce a **controlled hierarchy** where subclasses are explicitly declared within the parent class, enabling **exhaustive pattern matching**—a game-changer for type safety and maintainability. This feature, introduced in Java 17, ensures that all possible cases are covered when switching on sealed types, eliminating `switch` fall-through errors and making code more predictable.

## ⚡ 5-Second Key Points
- **Sealed hierarchies**: Subclasses must be declared as `permits` within the parent, restricting inheritance to known types.
- **Exhaustive matching**: Switch statements on sealed types guarantee all cases are handled, catching missing branches at compile time.
- **Type safety**: Reduces runtime errors by enforcing strict type boundaries and preventing unintended subclassing.

## 📈 Detailed Breakdown
**Sealed Classes: The Foundation**
Sealed classes act as **closed hierarchies**, where the parent explicitly lists allowed subclasses using the `permits` keyword. This design forces developers to account for every possible variant, making the codebase more robust. For example:

```
sealed interface Shape permits Circle, Square, Triangle {}
```
Here, `Shape` restricts itself to only `Circle`, `Square`, and `Triangle`, ensuring no external subclasses can sneak in.

> 💡 **Insight**: Sealed classes are ideal for **domain-driven design** (DDD) where clear boundaries between entities are critical. They also simplify refactoring by making the inheritance structure explicit.

**Exhaustive Pattern Matching: The Power Move**
The real magic happens when you combine sealed classes with `switch` expressions. Java’s compiler enforces that **every possible sealed subclass** is handled, eliminating the dreaded `default` case for most scenarios. This reduces cognitive load and catches missing cases early:

```
String describe(Shape shape) {
    return switch (shape) {
        case Circle c -> "Circle with radius " + c.radius;
        case Square s -> "Square with side " + s.side;
        case Triangle t -> "Triangle with base " + t.base;
    };
}
```
No `default` needed—Java guarantees completeness.

**Element 2: Practical Use Cases**
Sealed classes shine in **state machines**, **visitor patterns**, and **API design**. For instance, a payment processing system could use sealed classes to model payment methods:

```
sealed interface PaymentMethod permits CreditCard, PayPal, CryptoWallet {}
```
This ensures only valid payment types are processed, reducing runtime errors. Additionally, they work seamlessly with **records** and **pattern matching**, making data handling cleaner and safer.

> 💡 **Insight**: Exhaustive matching is particularly useful in **functional-style Java**, where immutability and type safety are paramount. It aligns with languages like Scala, where such guarantees are standard.

## 🎯 Real-World Impact
- **Fewer runtime errors**: By catching missing cases at compile time, sealed classes and exhaustive matching **eliminate `switch` fall-through bugs** that often slip into production.
- **Better refactoring**: Explicit hierarchies make it easier to **modify or extend** sealed types without breaking existing code.
- **Cleaner APIs**: Libraries using sealed classes can **document supported types clearly**, reducing confusion for consumers.

## ✨ Conclusion
Java’s sealed classes and exhaustive pattern matching are a **win for developers** who prioritize type safety and maintainability. By enforcing strict hierarchies and eliminating `switch` fall-through risks, they turn complex logic into **self-documenting, bug-resistant** code. Adopt them today to write Java that’s **cleaner, safer, and more predictable**—just like the best functional languages.
