# Quiz: Game Theory

Test your understanding of payoff matrices, dominant strategies, Nash equilibrium, the prisoner's dilemma, and backward induction with these review questions.

---

#### 1. What are the three elements that formally define a "game" in game theory?

<div class="upper-alpha" markdown>
1. Players, strategies, and payoffs
2. Prices, quantities, and costs
3. Supply, demand, and equilibrium
4. Dominant strategies, Nash equilibria, and payoff matrices
</div>

??? question "Show Answer"
    The correct answer is **A**. A game is formally defined by its players (the decision-makers), the strategies available to each, and the payoffs each player receives for every combination of strategies chosen. Option B and C describe market concepts unrelated to the formal structure of a game, and option D lists solution concepts and representations used to *analyze* a game, not the elements that define one.

    **Concept Tested:** Game

---

#### 2. What is a "dominant strategy"?

<div class="upper-alpha" markdown>
1. A strategy that gives the highest total payoff summed across all players
2. A strategy that only works if announced before the game begins
3. The strategy that results in the fewest possible outcomes
4. A strategy that is a player's best choice no matter what strategy the other player chooses
</div>

??? question "Show Answer"
    The correct answer is **D**. A dominant strategy gives a player a higher payoff than any alternative, regardless of what the other player does, which is why a rational player will always choose it when one exists. Option A describes joint payoff maximization, which is a different and unrelated concept, option B confuses it with the separate idea of a non-credible threat, and option C describes an irrelevant property about outcome counts.

    **Concept Tested:** Dominant Strategy

---

#### 3. What defines a "Nash equilibrium"?

<div class="upper-alpha" markdown>
1. A strategy combination that maximizes the sum of both players' payoffs
2. A strategy combination in which no player can improve their own payoff by unilaterally changing their own strategy, given the other player's strategy
3. The outcome where both players use a dominant strategy
4. The first strategy combination found when checking a payoff matrix
</div>

??? question "Show Answer"
    The correct answer is **B**. A Nash equilibrium is a mutual best response: each player's chosen strategy is optimal given what the other player is doing, so neither wants to deviate unilaterally. Option A describes joint payoff maximization, which a Nash equilibrium does not guarantee (as the prisoner's dilemma shows), option C describes only one special case since many Nash equilibria involve no dominant strategy at all, and option D describes an arbitrary search procedure rather than a defining condition.

    **Concept Tested:** Nash Equilibrium

---

#### 4. What makes the prisoner's dilemma a notable result in game theory?

<div class="upper-alpha" markdown>
1. It shows that two players each acting in their own rational self-interest can reach an equilibrium that leaves both of them worse off than if they had cooperated
2. It shows that games with dominant strategies never have a Nash equilibrium
3. It shows that cooperation is always the dominant strategy for both players
4. It shows that payoff matrices only apply to oligopoly pricing decisions
</div>

??? question "Show Answer"
    The correct answer is **A**. In the prisoner's dilemma, each player's dominant strategy leads to a Nash equilibrium that is worse for both players than if they had both cooperated, illustrating a gap between individually rational behavior and a collectively good outcome. Option B is false since a dominant-strategy equilibrium is trivially a Nash equilibrium, option C reverses the actual result (defection, not cooperation, is dominant), and option D wrongly limits the game's relevance to a single application.

    **Concept Tested:** Prisoners Dilemma

---

#### 5. How does a coordination game differ fundamentally from a prisoner's dilemma?

<div class="upper-alpha" markdown>
1. A coordination game has only one Nash equilibrium, while a prisoner's dilemma always has multiple equilibria
2. A coordination game never has a dominant strategy for either player, while a prisoner's dilemma always does for both
3. In a coordination game, players benefit from matching each other's choice, with no built-in conflict pulling them toward a worse joint outcome, unlike the prisoner's dilemma
4. A coordination game can only be solved using backward induction, not Nash equilibrium
</div>

??? question "Show Answer"
    The correct answer is **C**. In a coordination game, such as choosing a shared technology standard, both players simply want to match each other's choice, and the challenge is agreeing on which equilibrium to coordinate on rather than resolving a conflict of interest, unlike the prisoner's dilemma where individual incentives pull players away from the mutually best outcome. Option A reverses the typical equilibrium counts (coordination games often have multiple equilibria), option B happens to be true about dominant strategies but is not the fundamental distinction the question asks about, and option D incorrectly denies that coordination games are solved using Nash equilibrium.

    **Concept Tested:** Coordination Game

---

#### 6. In a sequential game solved by backward induction, why is a threatened action considered "non-credible" if the threatening player would not actually want to carry it out once the moment arrives?

<div class="upper-alpha" markdown>
1. Because backward induction ignores all threats regardless of credibility
2. Because non-credible threats are illegal under antitrust law
3. Because sequential games never allow for threats of any kind
4. Because a rational opponent can anticipate that the threat would not actually be followed through, and should therefore ignore it when deciding their own earlier move
</div>

??? question "Show Answer"
    The correct answer is **D**. Backward induction solves the later decision first; if carrying out a threatened action would actually be worse for the threatening player than not carrying it out, a rational opponent anticipates this and safely ignores the threat when making an earlier move. Option A and C both overstate the rule by denying threats any role at all, and option B invents an unrelated legal consequence.

    **Concept Tested:** Non-Credible Threat

---

#### 7. In the payoff matrix below (Row, Column payoffs for Firm A, Firm B), what is Firm A's dominant strategy?

| | B: Low Price | B: High Price |
|---|---|---|
| A: Low Price | (6, 6) | (12, 3) |
| A: High Price | (3, 12) | (9, 9) |

<div class="upper-alpha" markdown>
1. High Price, since it yields the highest joint payoff
2. Low Price, since it gives Firm A a higher payoff than High Price regardless of B's choice
3. There is no dominant strategy for Firm A in this matrix
4. High Price, since it is Firm A's best response to B's Low Price
</div>

??? question "Show Answer"
    The correct answer is **B**. If B plays Low Price, A earns 6 from Low Price versus 3 from High Price; if B plays High Price, A earns 12 from Low Price versus 9 from High Price — Low Price is better for A regardless of B's choice. Option A confuses joint payoff maximization with an individual dominant strategy, option C is wrong since a dominant strategy does exist here, and option D misidentifies A's best response to B's Low Price, which is actually Low Price, not High Price.

    **Concept Tested:** Dominant Strategy

---

#### 8. Using the payoff matrix below, which strategy combination(s) are Nash equilibria?

| | B: Left | B: Right |
|---|---|---|
| A: Up | (7, 7) | (1, 6) |
| A: Down | (6, 1) | (5, 5) |

<div class="upper-alpha" markdown>
1. Only (Up, Left)
2. Only (Down, Right)
3. Both (Up, Left) and (Down, Right)
4. Neither combination is a Nash equilibrium
</div>

??? question "Show Answer"
    The correct answer is **C**. If B plays Left, A's best response is Up (7 > 6), and if A plays Up, B's best response is Left (7 > 6), confirming (Up, Left); if B plays Right, A's best response is Down (5 > 1), and if A plays Down, B's best response is Right (5 > 1), confirming (Down, Right). Options A and B each capture only one of the two valid equilibria, and option D incorrectly denies that either combination satisfies the mutual-best-response condition.

    **Concept Tested:** Nash Equilibrium

---

#### 9. A firm decides whether to Launch a new product or Not Launch. If it Launches, a rival then decides whether to Compete aggressively or Coexist. Payoffs (Firm, Rival) are: Not Launch = (0, 40); Launch-then-Compete = (−8, 15); Launch-then-Coexist = (18, 25). Using backward induction, what is the equilibrium outcome?

<div class="upper-alpha" markdown>
1. The firm launches, and the rival coexists, since coexisting gives the rival a higher payoff than competing once the firm has already launched
2. The firm does not launch, since the rival would retaliate by competing aggressively
3. The firm launches, and the rival competes aggressively, since that is the rival's dominant strategy
4. The firm launches, but the outcome is unpredictable without more information
</div>

??? question "Show Answer"
    The correct answer is **A**. Solving backward, if the firm has already launched, the rival compares Compete (15) to Coexist (25) and chooses Coexist; anticipating this, the firm compares Launch-then-Coexist (18) to Not Launch (0) and chooses to Launch. Option B assumes a threat of retaliation that would not actually be credible once launch has occurred, option C misidentifies the rival's best response as Compete when Coexist is clearly better, and option D ignores that backward induction yields a definite, predictable solution.

    **Concept Tested:** Backward Induction

---

#### 10. In an indefinitely repeated version of a prisoner's-dilemma-style cartel game, two firms use a tit-for-tat strategy, cooperating (honoring quotas) as long as the other does, and retaliating with cheating after any defection. Under what condition is mutual cooperation most likely to be sustained as an equilibrium of the repeated game?

<div class="upper-alpha" markdown>
1. When firms place very little value on future profits relative to immediate gains from cheating
2. When the game has a fixed, publicly known final round
3. When firms value future profits highly enough that the loss from future retaliation outweighs the one-time gain from cheating today
4. When only one firm is aware that the game will be repeated
</div>

??? question "Show Answer"
    The correct answer is **C**. Cooperation is sustained when the discounted loss from triggering permanent future retaliation exceeds the one-time gain a firm could capture by cheating today — this requires firms to value future profits highly (a high discount factor). Option A describes the opposite condition, under which cooperation unravels, option B describes a finite, known-end game, which the chapter notes causes cooperation to break down through backward induction, and option D is irrelevant since both firms' awareness (and incentive structure) matters symmetrically.

    **Concept Tested:** Repeated Game

---
