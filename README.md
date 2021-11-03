# README #
Implementation of Adam Back's hashcash.
By using the sha hash function which is deterministic and produces random results,
we can use it as a proof of work that calculation was done to find a solution with a specific difficulty.
Hashcash was invented as a antispam technology, but was later implemented in the Bitcoin protocol.

## Difficulty ##
Difficulty is defined as producing a hash from a challenge and token that has 'n' trailing zeroes in binary.

## How to use ##
1. Set a challenge and difficulty (higher number, the more difficult)
2. Mint the token
3. Verify the token against the difficulty.

## Mining and Verification ##
The proof of work is expensive, but the solutions are easy to verify.
This idea was put into the Bitcoin protocol as new blocks need to mined through
expensive calculation but new blocks can be easily verified.