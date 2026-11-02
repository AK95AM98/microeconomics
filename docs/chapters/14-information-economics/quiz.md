# Quiz: Information Economics

Test your understanding of adverse selection, moral hazard, signaling, screening, and principal-agent problems with these review questions.

---

#### 1. What does Akerlof's "market for lemons" model describe?

<div class="upper-alpha" markdown>
1. A market where sellers always disclose the true quality of their goods
2. A model explaining why moral hazard increases insurance premiums over time
3. A government policy for regulating used car dealerships
4. A model showing how adverse selection can drive high-quality goods out of a market when buyers cannot distinguish quality before purchase
</div>

??? question "Show Answer"
    The correct answer is **D**. Akerlof's model shows that when buyers cannot tell good cars from bad ones, they offer only an average price, which can drive owners of genuinely good cars out of the market and leave a disproportionate share of lemons for sale. Option A describes the opposite of the model's premise, option B describes moral hazard, a timing-distinct problem, and option C describes a policy response rather than the model itself.

    **Concept Tested:** Market for Lemons

---

#### 2. What is "signaling" in information economics?

<div class="upper-alpha" markdown>
1. An informed party taking a costly, differentially-costly action to credibly reveal private information to an uninformed party
2. An uninformed party designing a menu of contracts to sort informed parties by type
3. A government mandate requiring full disclosure of product quality
4. A method for calculating the optimal Pigouvian tax
</div>

??? question "Show Answer"
    The correct answer is **A**. Signaling occurs when the informed party, such as a high-ability worker acquiring education, takes a costly action that is credible precisely because it would not be worth copying for someone without the underlying trait. Option B describes screening, the mirror-image concept initiated by the uninformed party, option C invents a regulatory mandate not part of the signaling concept, and option D is unrelated to information economics.

    **Concept Tested:** Signaling

---

#### 3. What defines a "principal-agent problem"?

<div class="upper-alpha" markdown>
1. A situation where a principal and agent have perfectly aligned interests and no monitoring is needed
2. A pricing strategy used by monopolists to capture consumer surplus
3. A conflict that arises when a principal delegates authority to an agent whose interests are not perfectly aligned with the principal's, and whose actions the principal cannot perfectly monitor
4. A government regulation requiring firms to disclose executive compensation
</div>

??? question "Show Answer"
    The correct answer is **C**. A principal-agent problem combines misaligned incentives with imperfect monitoring, as when shareholders (principals) cannot perfectly observe whether a CEO (agent) is acting in their best interest. Option A describes the opposite situation, with no conflict at all, option B describes an unrelated pricing concept from monopoly theory, and option D describes a specific regulatory tool rather than the underlying economic problem.

    **Concept Tested:** Principal-Agent Problem

---

#### 4. How does screening differ from signaling in terms of who acts first?

<div class="upper-alpha" markdown>
1. In screening, the informed party acts first by choosing a costly signal; in signaling, the uninformed party designs a menu
2. Screening and signaling are identical concepts with different names
3. In both screening and signaling, only the uninformed party ever takes action
4. In screening, the uninformed party designs a menu of options that induces informed parties to reveal their type through self-selection; in signaling, the informed party takes the first costly action
</div>

??? question "Show Answer"
    The correct answer is **D**. In screening, an uninformed party like an insurer designs a menu (such as different premium-deductible combinations) that induces self-selection by type, while in signaling, the informed party moves first by taking a costly action to reveal their own type. Option A reverses the two roles, option B denies a meaningful and well-established distinction, and option C is false since the informed party is the one who acts first under signaling.

    **Concept Tested:** Screening

---

#### 5. What mechanism drives an "adverse selection death spiral" in an insurance market?

<div class="upper-alpha" markdown>
1. Rising premiums driven by a riskier applicant pool push the healthiest remaining buyers to drop coverage, which raises the average risk further and pushes premiums even higher
2. Insurers lower premiums every year to attract more healthy applicants
3. Moral hazard causes all policyholders to file identical numbers of claims
4. Government subsidies always prevent any death spiral from occurring
</div>

??? question "Show Answer"
    The correct answer is **A**. A death spiral unravels precisely because rising premiums disproportionately drive out the lowest-risk participants first, raising the average risk (and thus the price) further in a self-reinforcing cycle. Option B describes the opposite price direction, option C mischaracterizes moral hazard as producing uniform claims rather than variable behavior, and option D makes an unsupported blanket claim about subsidies always preventing the spiral.

    **Concept Tested:** Adverse Selection Death Spiral

---

#### 6. For a signaling equilibrium to successfully separate high-ability from low-ability workers, which condition must hold?

<div class="upper-alpha" markdown>
1. The cost of the signal must be identical for both high- and low-ability workers
2. Low-ability workers must always earn more than high-ability workers
3. The wage premium from the signal must exceed the signal's cost for high-ability workers, while falling short of its cost for low-ability workers
4. The signal must be free for both types to ensure fairness
</div>

??? question "Show Answer"
    The correct answer is **C**. A separating equilibrium requires the wage premium to be worthwhile for high-ability workers but not worth the higher cost for low-ability workers to mimic, exactly the condition $c_L(y^*) > w_H - w_L > c_H(y^*)$. Option A contradicts the requirement that costs differ across types (otherwise everyone or no one would signal), option B reverses the expected wage outcome, and option D is false since a costless signal conveys no information at all.

    **Concept Tested:** Separating Equilibrium

---

#### 7. In a used laptop market, good laptops are worth $900 to buyers and $700 to sellers, while bad laptops are worth $250 to buyers and $150 to sellers. If half of all laptops offered are good and half are bad, and buyers cannot distinguish quality before purchase, what happens to the market?

<div class="upper-alpha" markdown>
1. The market settles at a price of $575, since that is the expected value of a random laptop
2. Good laptops are driven out of the market because $575 is below what their owners require to sell, and the price unravels down to $250, reflecting only bad laptops
3. Both good and bad laptops continue to be sold at $575, since this price already reflects the fair average
4. The price rises to $900 because buyers eventually learn to identify good laptops
</div>

??? question "Show Answer"
    The correct answer is **B**. Buyers' initial expected value is $0.5(900)+0.5(250)=\$575$, but owners of good laptops (worth $700 to them) won't sell at $575, so only bad laptops come to market; rational buyers then revise their expectation down to $250, the value of a bad laptop, and the market unravels. Options A and C both incorrectly assume the initial average price is sustainable, and option D contradicts the entire premise that buyers cannot distinguish quality.

    **Concept Tested:** Market for Lemons

---

#### 8. A firm wants a worker to exert high effort, which raises the probability of project success from $p_L=0.3$ to $p_H=0.6$. The worker's disutility of high effort is $12,000, and the firm pays $w_L=\$50{,}000$ on failure. What is the minimum $w_H$ the firm must pay on success to satisfy the incentive compatibility condition?

<div class="upper-alpha" markdown>
1. $90,000
2. $62,000
3. $74,000
4. $110,000
</div>

??? question "Show Answer"
    The correct answer is **A**. The incentive compatibility condition is $(p_H-p_L)(w_H-w_L) \geq c$, so $(0.6-0.3)(w_H-50{,}000)\geq12{,}000 \implies w_H-50{,}000\geq40{,}000 \implies w_H\geq\$90{,}000$. The other options result from arithmetic slips in dividing the cost by the change in probability or in adding the required gap to the wrong base wage.

    **Concept Tested:** Incentive Compatibility

---

#### 9. A high-ability worker's cost of $y$ years of education is $c_H(y)=4{,}000y$, and a low-ability worker's cost is $c_L(y)=12{,}000y$. Firms pay $45,000 to workers with no credential and $80,000 to workers with a credential of $y^*$ years believed to signal high ability. Over what approximate range of $y^*$ does a separating equilibrium exist?

<div class="upper-alpha" markdown>
1. Between 0 and 2.92 years
2. Between 2.92 and 8.75 years
3. Between 8.75 and 12 years
4. No separating equilibrium exists for any $y^*$
</div>

??? question "Show Answer"
    The correct answer is **B**. High types signal only if $35{,}000 \geq 4{,}000y^* \implies y^* \leq 8.75$, and low types avoid mimicking only if $12{,}000y^* > 35{,}000 \implies y^* > 2.92$; a separating equilibrium therefore exists for $y^*$ strictly between about 2.92 and 8.75 years. Option A falls below the threshold needed to deter low-ability mimicry, option C exceeds the threshold at which high-ability workers would no longer find signaling worthwhile, and option D incorrectly denies that any valid range exists.

    **Concept Tested:** Education Signaling Model

---

#### 10. A bank facing asymmetric information about borrower risk considers raising its interest rate to cover the average default risk of its applicant pool. Based on the concept of credit rationing, why might the bank instead choose to deny loans to some borrowers rather than simply raising the rate for everyone?

<div class="upper-alpha" markdown>
1. Because raising the interest rate would attract disproportionately safer borrowers, improving the pool
2. Because banks are legally prohibited from ever raising interest rates on loans
3. Because raising the interest rate could drive away the safest borrowers (who are most sensitive to cost), worsening the average riskiness of the remaining applicant pool and potentially reducing the bank's expected profit
4. Because credit rationing always increases the total amount of lending in the economy
</div>

??? question "Show Answer"
    The correct answer is **C**. Raising rates can trigger the same adverse-selection unraveling seen elsewhere in this chapter: safer borrowers are the ones most likely to be discouraged by a higher rate, leaving the bank with a riskier remaining pool, which is why denying some loans outright can be more profitable than raising the rate indefinitely. Option A describes the opposite of the actual selection effect, option B invents a legal restriction that does not exist, and option D is false since rationing by definition reduces the quantity of loans extended, not increases it.

    **Concept Tested:** Credit Rationing

---
