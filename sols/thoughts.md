# ATM System - Interviewer Notes

## Interview Session
**Problem:** ATM System Design
**Difficulty:** Medium

---

## Expected Solution Architecture

### Core Components:
1. **Card** - card number, PIN
2. **Account** - account number, balance, linked cards, thread-safe operations
3. **BankService** - manages accounts, authenticates, processes transactions
4. **ATM** - main interface, singleton pattern
5. **CashDispenser** - handles cash dispensing with thread safety
6. **Transaction handling** - withdrawal, deposit, balance inquiry

### Design Patterns Expected:
- Singleton (ATM)
- State Pattern (Idle → HasCard → Authenticated states)
- Chain of Responsibility (cash dispensing with different denominations)
- Thread safety with locks

### Key Features to Implement:
- Card insertion and authentication
- PIN validation
- Balance inquiry
- Cash withdrawal with denomination handling
- Cash deposit
- Concurrent access handling
- Transaction rollback on failure

---

## Interview Progress

### Stage: Design Phase Complete → Moving to Implementation
**Status:** Candidate has completed design and is ready to implement
**Next:** Guide them through implementing the vertical slice (card insertion, authentication, balance check)

---

## Observations

### Clarifying Questions Phase:
- Asked about negative balances / debt handling ✓
- Clarified authentication mechanism ✓
- Asked about transaction logging (good to consider)
- Made assumptions about PIN format
- Initially assumed wrong denominations (100, 20, 10, 5) but corrected after clarification
- Asked excellent edge case question about non-dispensable amounts ✓

### Design Phase:
- Identified 4 main classes: BankingSystem, ATM, CashDispenser, Account, Card
- Properly separated concerns between ATM (user interface) and BankingSystem (data management)
- Added CashDispenser as separate component after prompting
- Recognized need for thread safety in Account (added locks)
- Implemented Singleton pattern for BankingSystem
- Used card_to_acc mapping in BankingSystem (good!)
- Card is simple dataclass - appropriate level of abstraction

## Hints Given
1. Questioned why every operation needs card_number + PIN parameters (led to curr_account design)
2. Asked where banking data lives (led to BankingSystem)
3. Challenged them to separate cash dispensing logic into its own class
4. Suggested Card shouldn't hold Account reference, BankingSystem should manage mapping
5. Clarified deposit doesn't refill ATM cash inventory

## Strengths Noted
- Good intuition for separation of concerns
- Responsive to feedback and adjusted design quickly
- Asked clarifying questions about edge cases
- Recognized need for thread safety
- Clean class structure with appropriate responsibilities

## Areas for Improvement / Watch During Implementation
- BankingSystem.view_balance has wrong signature (has amount: int parameter - typo?)
- CashDispenser thread safety not mentioned (only Account has locks)
- CashDispenser.withdraw_cash returns bool - needs more thought on what it should do/return
- Account has __cards list - unclear if this is needed
- No ATM states mentioned yet (Idle, HasCard, Authenticated) - candidate may discover need during implementation
- Error handling strategy not discussed
- No mention of ATM being singleton (though not strictly required if multiple ATM instances are valid)
- Cash dispensing algorithm not detailed yet (greedy approach, but how to check if amount is dispensable?)

## Expected Implementation Path
1. Start with Card and Account classes (simple)
2. Implement BankingSystem with sample data
3. Implement basic ATM flow: insert_card → authenticate
4. Implement view_balance (vertical slice complete)
5. Then add: withdraw with CashDispenser logic
6. Then add: deposit
7. Discuss: State pattern, error handling, edge cases
8. Discuss: Chain of Responsibility for note dispensing (if they don't discover it naturally)

