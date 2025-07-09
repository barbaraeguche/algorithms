## bit manipulation

### truth tables & bit operations
with bits, we can perform the following operations:

- **and**: when applied to two bits, both of the bits must be `1` to get a `1`. otherwise, we will get a `0`. 
represented using the `&` symbol.
- **or**: when applied to two bits, only one of the bits has to be a `1` to get a `1`. this means if both bits are `1`, 
we will get a `1` and `0` if both bits are `0`. represented using the `|` symbol.
- **xor**: when applied to two bits, we will get a `1` if only one of the bits is a `1`. otherwise, we will get a `0`. 
represented using the `^` symbol.
- **negation** - negation just flips the current bit. negation of `0` is `1`, and negation of `1` is `0`. represented 
using the `~` symbol.
- **shifting bits**: shifting bits refers to shifting our bits, either to the left or to the right. it takes all the 
bits and shifts them by one position either to the left or to the right. `>>` is a right shift and `<<` is a left shift.

~ technically speaking, shifting to the left means multiplying the given integer by 2 and shifting to the right means
dividing the given integer by 2. doubling and halving, respectively.