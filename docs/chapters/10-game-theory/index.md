# Chapter 10: Game Theory

## Learning Objectives

After completing this chapter, you will be able to:

1. Define a game in terms of players, strategies, and payoffs, and represent it as a payoff matrix
2. Identify dominant and dominated strategies
3. Find the Nash equilibrium (or equilibria) of a simultaneous game
4. Explain the prisoner's dilemma and why mutually beneficial cooperation can fail
5. Distinguish coordination games from games of pure conflict
6. Explain how repeated interaction can sustain cooperation
7. Solve sequential games using backward induction
8. Apply game theory to oligopoly, auctions, and bargaining

---

!!! mascot-welcome "Finally — The Tools to Read Your Rivals' Minds"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every choice has a trade-off, and this chapter is about trade-offs that get tangled up with someone else's choices too. We spent all of Chapter 9 reasoning informally about rivals anticipating each other — now you get the actual toolkit: payoff matrices, dominant strategies, Nash equilibrium, and backward induction. By the end, you'll be able to predict how strategic situations resolve, from boardrooms to auction houses to a police interrogation room.

## 10.1 What Is a Game?

A **game** is any strategic situation in which the outcome for each participant depends not only on that participant's own choice but on the choices of others. Formally, a game has three elements:

- **Players** — the decision-makers (e.g., two firms, two bidders, two countries)
- **Strategies** — the complete set of actions available to each player
- **Payoffs** — the outcome (typically profit, utility, or some numerical score) each player receives for every possible combination of strategies chosen

We summarize a simple two-player, two-strategy game in a **payoff matrix**: a table whose rows are one player's strategies, whose columns are the other player's strategies, and whose cells list the payoff to each player (Row player's payoff, Column player's payoff) under that combination.

!!! example "Reading a payoff matrix"
    | | **Firm B: Low Price** | **Firm B: High Price** |
    |---|---|---|
    | **Firm A: Low Price** | (10, 10) | (50, 5) |
    | **Firm A: High Price** | (5, 50) | (30, 30) |

    If Firm A charges a Low Price and Firm B charges a High Price, Firm A earns 50 and Firm B earns 5 — the first number in each cell always belongs to the row player (Firm A), the second to the column player (Firm B).

Game theory formalizes the strategic reasoning this textbook has used informally since oligopoly (Chapter 9): every oligopoly pricing decision, cartel agreement, and antitrust case is, at its core, a game.

!!! mascot-thinking "The Shift: Solving for a Combination, Not a Single Choice"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Here's the mental shift for this whole chapter: instead of solving for one person's optimal choice, you're solving for a *combination* of choices — one per player — that are each other's best responses at the same time. Every tool coming up, dominant strategies, Nash equilibrium, backward induction, is just a different technique for finding that self-consistent combination.

---

## 10.2 Dominant Strategies

A **dominant strategy** is a strategy that gives a player a higher payoff than any other strategy available, *no matter what the other player does*. A strategy that is always worse than some alternative, regardless of the opponent's choice, is called a **dominated strategy** — a rational player never plays one.

!!! example "Finding a dominant strategy"
    | | **B: Confess** | **B: Stay Silent** |
    |---|---|---|
    | **A: Confess** | (−5, −5) | (0, −10) |
    | **A: Stay Silent** | (−10, 0) | (−1, −1) |

    Check Player A's options: if B Confesses, A's best response is Confess (−5 beats −10). If B Stays Silent, A's best response is still Confess (0 beats −1). Since Confess is A's best response *regardless* of what B does, **Confess is A's dominant strategy**. By the matrix's symmetry, Confess is also B's dominant strategy.

Not every game has a dominant strategy for every player — many games require a more general equilibrium concept, introduced next.

---

## 10.3 Nash Equilibrium

A **Nash equilibrium** (John Nash, 1950) is a combination of strategies, one for each player, such that **no player can improve their own payoff by unilaterally changing their own strategy**, given the strategies chosen by everyone else. It is a *mutual best response*: each player's strategy is optimal given what the others are doing.

**Finding a Nash equilibrium by inspection:** underline or circle each player's best response to each of the other player's strategies; any cell where *both* players' payoffs are marked as best responses is a Nash equilibrium.

!!! mascot-tip "Stay Organized on a Bigger Matrix"
    ![Professor Owl with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Here's a shortcut for keeping track on a matrix bigger than 2x2: go column by column and underline Player A's best payoff in each column, then go row by row and circle Player B's best payoff in each row. Any cell with both an underline and a circle is a Nash equilibrium — no mental juggling required.

!!! example "Finding the Nash equilibrium"
    | | **B: Left** | **B: Right** |
    |---|---|---|
    | **A: Up** | (8, 3) | (2, 2) |
    | **A: Down** | (5, 5) | (4, 8) |

    Check A's best response to each of B's choices: if B plays Left, A's best response is Up (8 > 5). If B plays Right, A's best response is Down (4 > 2).

    Check B's best response to each of A's choices: if A plays Up, B's best response is Left (3 > 2). If A plays Down, B's best response is Right (8 > 5).

    (Up, Left) is a Nash equilibrium: A's best response to Left is Up, *and* B's best response to Up is Left — both conditions hold simultaneously. Checking (Down, Right): A's best response to Right is Down, *and* B's best response to Down is Right — both conditions hold here too. **This game has two Nash equilibria: (Up, Left) and (Down, Right).**

Every dominant-strategy equilibrium is a Nash equilibrium (if Confess is dominant for both players in Section 10.2's example, (Confess, Confess) is trivially a mutual best response), but not every Nash equilibrium involves dominant strategies — many games (like the one above) have Nash equilibria without any dominant strategy at all.

---

## 10.4 The Prisoner's Dilemma

The **prisoner's dilemma** is the most famous game in economics: a game in which each player has a dominant strategy, but the resulting equilibrium leaves *both* players worse off than if they had cooperated.

!!! example "The classic prisoner's dilemma"
    Two suspects are held separately. Each can **Confess** (implicating the other) or **Stay Silent**. Payoffs are years of prison avoided (higher is better):

    | | **B: Confess** | **B: Stay Silent** |
    |---|---|---|
    | **A: Confess** | (−5, −5) | (0, −10) |
    | **A: Stay Silent** | (−10, 0) | (−1, −1) |

    As shown in Section 10.2, Confess is the dominant strategy for both players, so the Nash equilibrium is **(Confess, Confess)**, giving each player −5. Yet **(Silent, Silent)** would have given each player −1 — strictly better for both. Rational, self-interested behavior by each individual player produces a *worse* outcome for both than mutual cooperation would have.

!!! mascot-thinking "The Single Most Important Insight in This Chapter"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Sit with that result for a second. Each player reasoned perfectly in their own self-interest, and the two of them together still landed somewhere worse than if they'd both just cooperated. Individually rational behavior and a collectively good outcome are not the same thing — and a huge share of economics lives in exactly that gap.

The prisoner's dilemma structure explains the cartel instability from Chapter 9: each cartel member's dominant strategy is to "cheat" (produce more than its quota) regardless of what the other does, yet mutual cheating leaves both firms worse off than if both had honored the cartel agreement.

| Oligopoly Cartel | Prisoner's Dilemma Equivalent |
|---|---|
| Honor the quota | Stay Silent |
| Cheat on the quota | Confess |
| Mutual cheating (Nash equilibrium) | Mutual confession |
| Mutual cartel compliance (better for both, but not an equilibrium) | Mutual silence |

---

## 10.5 Coordination Games

Not every game is a prisoner's dilemma. In a **coordination game**, players benefit from matching each other's choice, and there is no built-in conflict of interest pulling them toward a worse joint outcome.

!!! example "Pure coordination: choosing a technology standard"
    | | **B: Format X** | **B: Format Y** |
    |---|---|---|
    | **A: Format X** | (10, 10) | (0, 0) |
    | **A: Format Y** | (0, 0) | (10, 10) |

    Both (Format X, Format X) and (Format Y, Format Y) are Nash equilibria — each player is happy as long as they match the other. The challenge is not conflicting interests but *agreeing on which equilibrium to coordinate on*.

A variant, the **battle of the sexes**, adds a mild conflict of interest on top of the coordination problem: both players prefer to be together over being apart, but each has a different preferred activity.

!!! example "Battle of the sexes"
    | | **B: Opera** | **B: Game** |
    |---|---|---|
    | **A: Opera** | (3, 2) | (0, 0) |
    | **A: Game** | (0, 0) | (2, 3)|

    (Opera, Opera) and (Game, Game) are both Nash equilibria. A prefers the first, B prefers the second — unlike the prisoner's dilemma, both equilibria are individually rational outcomes; the difficulty is purely about *which* equilibrium the two players land on, not whether to cooperate at all.

---

## 10.6 Repeated Games and Cooperation

The one-shot prisoner's dilemma predicts that players never cooperate. But in a **repeated game** — the same players interacting over and over — cooperation can emerge as an equilibrium, because players can reward cooperation and punish defection in future rounds.

The best-known cooperative strategy in a repeated prisoner's dilemma is **tit-for-tat**: cooperate on the first round, then on every subsequent round do whatever the opponent did in the previous round.

!!! note "Why repetition changes the outcome"
    In a one-shot game, cheating has no future cost. In a repeated game (with no fixed, known end date, or an indefinite/infinite horizon), cheating today can trigger retaliation tomorrow, reducing *all future* payoffs. If players value the future enough (a high enough discount factor), the threat of future punishment can make "honor the cartel quota" (or "stay silent") a Nash equilibrium of the *repeated* game — even though "cheat" remains the dominant strategy in any single round viewed in isolation.

This is precisely how real-world cartels (Chapter 9) sometimes sustain cooperation for years: firms interact repeatedly, can observe (with a lag) whether rivals are cheating on output quotas, and can credibly threaten a price war in response — converting a one-shot incentive to cheat into a repeated-game equilibrium of sustained cooperation.

!!! warning "Finite, known-end games unravel"
    If both players know the game will be played a *fixed, known* number of rounds, the logic of repeated cooperation can fail: in the last round there is no future to protect, so both players defect (as in the one-shot game); knowing this, both defect in the second-to-last round too (since the last round's cooperation incentive is already gone); this reasoning unravels all the way back to the first round. Sustained cooperation is most robust when the game's end is uncertain or indefinitely distant.

---

## 10.7 Sequential Games and Backward Induction

In a **sequential game**, players move one after another (rather than simultaneously), and later movers can observe earlier moves before choosing their own. Sequential games are typically represented with a **game tree**, and solved using **backward induction**: start at the final decision nodes and work backward, at each step assuming every player will choose the best available action given what will happen afterward.

!!! mascot-encourage "Working Backward Feels Backward — That's Normal"
    ![Professor Owl encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If "start at the end and work backward" feels disorienting at first, you're not alone — most people need to trace through one full example before it clicks. Just hold onto the rule: solve the *last* decision first, treat that solved decision as a known fact, then solve the decision one step earlier, and repeat until you're back at move one.

!!! example "A simple market-entry game, solved by backward induction"
    An entrant firm decides whether to **Enter** a market or **Stay Out**. If it Enters, the incumbent firm decides whether to **Fight** (start a price war) or **Accommodate** (share the market peacefully).

    Payoffs (Entrant, Incumbent):

    - Stay Out: (0, 50)
    - Enter, then Incumbent Fights: (−10, 10)
    - Enter, then Incumbent Accommodates: (20, 20)

    **Backward induction, step 1 (last mover first):** if the entrant has already entered, what does the incumbent do? Fight gives the incumbent 10; Accommodate gives the incumbent 20. The incumbent's best response to entry is **Accommodate**.

    **Backward induction, step 2 (work back to the first mover):** knowing the incumbent will Accommodate (not Fight) if it enters, the entrant compares Enter-then-Accommodate (20) to Stay Out (0). The entrant's best choice is **Enter**.

    **Solution: Entrant enters; Incumbent accommodates.** Note that a threat to "Fight" announced *before* the entrant decides would not be credible — once entry has actually occurred, fighting (10) is worse for the incumbent than accommodating (20), so a rational entrant should ignore the threat. This is the concept of a **non-credible threat**.

Backward induction is the sequential-game counterpart to Nash equilibrium: it rules out strategies (like "I'll fight if you enter") that are not actually optimal when the moment to carry them out arrives.

---

## 10.8 Applications: Oligopoly, Auctions, and Bargaining

Game theory's tools recur across economics:

- **Oligopoly (Chapter 9):** The Cournot and Bertrand models are simultaneous games solved for Nash equilibrium; cartel instability is a repeated prisoner's dilemma; entry deterrence and predatory pricing are sequential games solved by backward induction.
- **Auctions:** In a **sealed-bid, second-price auction** (the winner pays the *second*-highest bid, not their own), a bidder's dominant strategy is to bid exactly their true value for the item — bidding higher risks overpaying if you win, and bidding lower only risks losing an auction you'd have profited from, with no offsetting benefit, since the price you pay is set by the other bidder either way.
- **Bargaining:** Sequential bargaining (e.g., alternating-offer negotiations over a fixed sum of money) is solved by backward induction from an assumed final deadline, showing that the party with more patience (or a credible threat to walk away) secures a larger share — a formal foundation for real-world negotiation strategy.

!!! mascot-warning "Don't Import First-Price Instincts Into a Second-Price Auction"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A common mix-up: carrying over the instinct to "shade your bid below your value," which is smart advice for a first-price auction, into a second-price auction, where it's exactly wrong. Because the *winner* pays the *second*-highest bid, not their own, shading down only risks losing a profitable auction for no benefit. Bid your true value, every time.

!!! tip "The common thread"
    Every application above shares the same discipline: write down who moves, what they can do, and what they get — then find the strategy combination from which no one wants to unilaterally deviate (Nash equilibrium for simultaneous games; backward induction for sequential ones). This same discipline, applied to firms rather than individuals, is exactly what powered the oligopoly models of Chapter 9.

---

## Key Terms

| Term | Definition |
|---|---|
| **Game** | A strategic situation defined by players, strategies, and payoffs |
| **Payoff matrix** | A table showing each player's payoff for every combination of strategies |
| **Dominant strategy** | A strategy that is a player's best choice regardless of what others do |
| **Dominated strategy** | A strategy that is always worse than some alternative, regardless of others' choices |
| **Nash equilibrium** | A strategy combination in which no player can gain by unilaterally changing strategy |
| **Prisoner's dilemma** | A game where dominant strategies lead to an outcome worse for both players than mutual cooperation |
| **Coordination game** | A game where players benefit from matching each other's choice |
| **Battle of the sexes** | A coordination game with a mild conflict over which equilibrium is reached |
| **Repeated game** | A game played multiple times by the same players, enabling reward/punishment strategies |
| **Tit-for-tat** | A repeated-game strategy: cooperate first, then mirror the opponent's previous move |
| **Sequential game** | A game in which players move in turns, observing earlier moves |
| **Backward induction** | Solving a sequential game by reasoning from the last move backward to the first |
| **Non-credible threat** | An announced future action that would not actually be optimal to carry out |

---

## Practice Problems

### Problem 1 — Dominant Strategy

| | **B: Advertise** | **B: Don't Advertise** |
|---|---|---|
| **A: Advertise** | (4, 4) | (8, 2) |
| **A: Don't Advertise** | (2, 8) | (6, 6) |

**a)** Does Firm A have a dominant strategy? Find it.  
**b)** Does Firm B have a dominant strategy?  
**c)** What is the Nash equilibrium? Is it the best joint outcome for both firms?

??? success "Solution"
    **a)** If B Advertises, A's best response is Advertise (4 > 2). If B Doesn't Advertise, A's best response is Advertise (8 > 6). **Advertise is A's dominant strategy.**

    **b)** By the matrix's symmetry, **Advertise is also B's dominant strategy.**

    **c)** The Nash equilibrium is **(Advertise, Advertise)**, giving each firm a payoff of 4. This is *not* the best joint outcome — (Don't Advertise, Don't Advertise) gives each firm 6. This is a prisoner's dilemma: both firms would be better off if neither advertised, but each firm's dominant strategy leads them to advertise anyway.

### Problem 2 — Finding Nash Equilibria

| | **B: Left** | **B: Right** |
|---|---|---|
| **A: Up** | (6, 6) | (0, 5) |
| **A: Down** | (5, 0) | (4, 4) |

Find all Nash equilibria of this game.

??? success "Solution"
    Check A's best responses: if B plays Left, A's best response is Up (6 > 5). If B plays Right, A's best response is Down (4 > 0).

    Check B's best responses: if A plays Up, B's best response is Left (6 > 5). If A plays Down, B's best response is Right (4 > 0).

    (Up, Left): A's best response to Left is Up ✓, and B's best response to Up is Left ✓ — this is a Nash equilibrium.

    (Down, Right): A's best response to Right is Down ✓, and B's best response to Down is Right ✓ — this is also a Nash equilibrium.

    **There are two Nash equilibria: (Up, Left) with payoffs (6,6), and (Down, Right) with payoffs (4,4).** Unlike the prisoner's dilemma, players here have aligned interests — both prefer (Up, Left) — but must still coordinate on it.

### Problem 3 — Repeated Games

Two firms play the cartel game from Chapter 9 repeatedly, with no fixed end date. Firm A proposes a tit-for-tat strategy: "I will honor the quota as long as you do; if you ever cheat, I will cheat in every round after that."

**a)** Explain intuitively why this threat can sustain cooperation when a one-shot game cannot.  
**b)** What condition on how much firms value future profits (relative to today's profits) is needed for this to work?

??? success "Solution"
    **a)** In a one-shot game, cheating has no consequence — there is no "tomorrow" in which to be punished. In a repeated game, cheating today triggers retaliation (mutual cheating) in all future rounds, reducing every future period's profit. If the loss from future retaliation outweighs the one-time gain from cheating today, honoring the quota becomes individually rational.

    **b)** Firms must value future profits highly enough (a sufficiently high discount factor/low impatience) that the discounted sum of lower profits from permanent future retaliation exceeds the one-time gain from cheating now. If firms are very impatient (heavily discount the future), the one-time gain from cheating dominates, and cooperation unravels even in a repeated game.

### Problem 4 — Backward Induction

A government decides whether to **Subsidize** a new industry or **Not Subsidize**. If subsidized, a firm then decides whether to **Invest** or **Not Invest**. Payoffs (Government, Firm):

- Not Subsidize: (0, 0)
- Subsidize, then firm Invests: (10, 15)
- Subsidize, then firm Does Not Invest: (−5, 5)

**a)** Using backward induction, what does the firm do if subsidized?  
**b)** What does the government do, anticipating the firm's response?  
**c)** Is there any risk of a non-credible element in this game, and if so, where?

??? success "Solution"
    **a)** If subsidized, the firm compares Invest (15) to Not Invest (5). The firm's best response is to **Invest**.

    **b)** Anticipating that the firm will Invest if subsidized, the government compares Subsidize-then-Invest (10) to Not Subsidize (0). The government's best choice is to **Subsidize**.

    **c)** The risk runs the other way: if the firm could credibly threaten "I won't invest even if subsidized" *before* the government decides, the government would compare Subsidize-then-No-Invest (−5) to Not Subsidize (0) and choose Not Subsidize. But once the subsidy is actually granted, the firm's best response is to Invest (15 > 5) — so a pre-subsidy threat not to invest would not be credible, and backward induction correctly predicts the firm invests once the subsidy is in place.

### Problem 5 — Second-Price Auctions

In a sealed-bid, second-price auction, explain why bidding exactly your true value for the item is a dominant strategy, using the logic of "what happens if I bid higher" and "what happens if I bid lower."

??? success "Solution"
    If you bid *above* your true value and win, you might end up paying a price (the second-highest bid) that exceeds your own value — a loss you would have avoided by bidding your true value, since in a second-price auction your own bid never sets the price you pay, only whether you win. If you bid *below* your true value, you risk losing the auction to a bid between your lowered bid and your true value — an auction you would have won (and profited from) had you bid your true value. In neither direction does bidding anything other than your true value ever help, and in both directions it can hurt — so bidding your true value is a dominant strategy regardless of what other bidders do.

---

!!! mascot-celebration "You Can Now Formally Out-Think the Room"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    From payoff matrices to Nash equilibrium to backward induction through a full game tree — you just learned to formally predict how strategic situations resolve, not just guess at them. That's the exact toolkit behind cartel breakdowns, technology-standard wars, and why second-price auctions are designed the way they are.

!!! tip "Next Chapter"
    In [Chapter 11: Factor Markets](../11-factor-markets/index.md), we turn from the markets for goods and services to the markets for the *inputs* that produce them — labor, capital, and land — where firms are no longer sellers but buyers, hiring workers and renting capital according to the same marginal principles developed throughout this unit.
