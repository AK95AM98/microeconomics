# Quiz: Behavioral Economics

Test your understanding of bounded rationality, heuristics and biases, prospect theory, present bias, framing, social preferences, and nudges with these review questions.

---

#### 1. What is "bounded rationality"?

<div class="upper-alpha" markdown>
1. The idea that people make decisions with limited information, limited time, and limited cognitive ability, rather than through unlimited, perfectly rational calculation
2. The assumption that all consumers have identical preferences
3. A model in which firms, not individuals, are the only boundedly rational agents
4. The claim that people never make systematic errors in judgment
</div>

??? question "Show Answer"
    The correct answer is **A**. Bounded rationality, coined by Herbert Simon, describes decision-making limited by finite information, cognitive capacity, and time, which leads people to satisfice rather than exhaustively optimize. Option B describes an unrelated preference assumption, option C incorrectly restricts the concept to firms when it applies broadly to individuals, and option D directly contradicts the chapter's central claim that bounded rationality produces systematic errors.

    **Concept Tested:** Bounded Rationality

---

#### 2. What does "loss aversion" mean in prospect theory?

<div class="upper-alpha" markdown>
1. People are indifferent between gains and losses of equal size
2. People feel the pain of a loss more strongly than the pleasure of an equivalent gain
3. People always avoid any gamble that involves the possibility of a loss
4. People discount future losses more heavily than future gains
</div>

??? question "Show Answer"
    The correct answer is **B**. Loss aversion means losses loom larger than equivalent gains, with experimental estimates putting the loss-aversion coefficient at roughly 2, so a loss feels about twice as intense as an equal-sized gain. Option A contradicts the entire concept, option C overstates the claim since people do sometimes accept gambles with potential losses, just not symmetrically with gains, and option D confuses loss aversion with a time-discounting concept from a different section of the chapter.

    **Concept Tested:** Loss Aversion

---

#### 3. What is the relationship between a "heuristic" and a "cognitive bias"?

<div class="upper-alpha" markdown>
1. A cognitive bias is a type of heuristic that always improves decision-making
2. Heuristics and cognitive biases are unrelated concepts that never co-occur
3. A heuristic is a mental shortcut that is often useful, but it can produce a cognitive bias, a systematic and predictable error in judgment
4. A cognitive bias is a random, unpredictable mistake with no identifiable cause
</div>

??? question "Show Answer"
    The correct answer is **C**. A heuristic is a useful mental shortcut for making fast decisions, but applying it in the wrong context can produce a cognitive bias — a systematic, predictable deviation from rational judgment, such as the availability heuristic leading to overestimated shark-attack risk. Option A reverses the logical relationship, option B denies the direct causal connection the chapter establishes, and option D is false since cognitive biases are specifically described as systematic and predictable, not random.

    **Concept Tested:** Heuristic

---

#### 4. How does "present bias" (captured by the beta-delta model) differ from standard exponential discounting?

<div class="upper-alpha" markdown>
1. Present bias means people place more weight on the distant future than on the near future
2. Exponential discounting assumes people never value the present more than the future
3. Present bias and exponential discounting are mathematically identical models
4. Present bias applies an extra, steeper discount only between the present and the very next period, while exponential discounting applies the same discount rate between any two periods of equal gap
</div>

??? question "Show Answer"
    The correct answer is **D**. The quasi-hyperbolic model adds the parameter $\beta$, which applies a steeper discount only when the present is one side of the comparison, while comparisons between two future periods use the ordinary exponential rate $\delta$ — a time-inconsistency exponential discounting does not produce. Option A reverses the actual direction of the extra discounting, option B mischaracterizes exponential discounting's assumption about relative weighting, and option C denies the clear mathematical distinction between the two models.

    **Concept Tested:** Present Bias

---

#### 5. Using the value function $v(x)=x^{0.5}$ for gains and $v(x)=-2(-x)^{0.5}$ for losses, what is the prospect-theory value of a gamble offering a 50% chance of gaining $225 and a 50% chance of losing $25?

<div class="upper-alpha" markdown>
1. 2.5
2. 50
3. 100
4. -5
</div>

??? question "Show Answer"
    The correct answer is **A**. $v(225)=225^{0.5}=15$ and $v(-25)=-2(25)^{0.5}=-10$, so the prospect value is $0.5(15)+0.5(-10)=7.5-5=2.5$. Option C is the gamble's expected monetary value ($0.5(225)+0.5(-25)=100$) rather than its prospect-theory value, and options B and D result from arithmetic slips in combining the two value-function outputs.

    **Concept Tested:** Prospect Theory

---

#### 6. Using the quasi-hyperbolic discounting model with $\beta=0.8$ and $\delta=0.92$, what is the discount factor applied between this year and next year, compared to the discount factor applied between two future years that are one year apart?

<div class="upper-alpha" markdown>
1. 0.92 for both comparisons
2. 0.736 between this year and next year; 0.92 between two future years
3. 0.736 for both comparisons
4. 0.92 between this year and next year; 0.736 between two future years
</div>

??? question "Show Answer"
    The correct answer is **B**. The present-to-next-year comparison applies the full $\beta\delta=0.8\times0.92=0.736$, while a comparison between two future years uses only the standard exponential factor $\delta=0.92$, since $\beta$ applies only when the present is involved. Options A and C both incorrectly apply the same factor to both comparisons, and option D reverses which comparison gets the steeper discount.

    **Concept Tested:** Hyperbolic Discounting

---

#### 7. A city's budget plan is described either as "this plan will preserve 300 of the 500 jobs at the factory" (a gain frame) or as "this plan will result in 200 job losses at the factory" (a loss frame), even though both descriptions refer to the exact same outcome. Based on prospect theory, which pattern of responses would most likely emerge?

<div class="upper-alpha" markdown>
1. Support for the plan would be identical under both frames, since the underlying numbers are the same
2. People would support the loss-framed description more, because loss framing always increases approval
3. People would tend to react more negatively to the loss-framed description, even though it conveys the same information as the gain-framed description, because losses are evaluated more harshly than equivalent gains
4. Framing would have no predictable effect, since cognitive biases apply only to financial decisions, not policy decisions
</div>

??? question "Show Answer"
    The correct answer is **C**. As in the Asian disease problem, identical outcomes framed as a loss ("200 job losses") tend to produce more negative reactions than the same outcome framed as a gain ("300 jobs preserved"), because loss aversion makes losses loom larger even when no new information is conveyed. Option A ignores the well-documented framing effect itself, option B overstates the direction (loss framing does not uniformly increase approval; it depends on the specific gain/loss structure of the choice), and option D wrongly restricts framing effects to financial contexts alone.

    **Concept Tested:** Framing Effect

---

#### 8. In an ultimatum game, a proposer offers to split $20 as $17 for themselves and $3 for the responder. Based on experimental evidence on social preferences and inequity aversion, what is the most likely outcome, and why does it depart from the prediction of pure self-interest?

<div class="upper-alpha" markdown>
1. The responder will almost certainly accept, since $3 is still better than $0, exactly as pure self-interest predicts
2. The proposer will always offer an equal split, since fairness concerns eliminate any incentive to propose an unequal division
3. The game has no predictable outcome, since social preferences make all human behavior random
4. The responder has a meaningful chance of rejecting the offer, since experiments show people often reject offers perceived as unfair (roughly below 20-30% of the pie), sacrificing their own payoff to punish inequity
</div>

??? question "Show Answer"
    The correct answer is **D**. A $3 offer out of $20 is 15% of the pie, below the roughly 20-30% threshold at which experimental responders frequently reject offers, even though pure self-interest predicts acceptance of any positive amount. Option A describes the self-interested prediction the evidence actually contradicts, option B overstates how proposers behave (many do offer less than an equal split), and option C mischaracterizes social preferences as producing randomness rather than a different, but still systematic, pattern of behavior.

    **Concept Tested:** Inequity Aversion

---

#### 9. A retirement plan automatically enrolls new employees at a 4% contribution rate unless they actively opt out, while a competing proposal would mandate a 4% contribution rate for all employees with no opt-out allowed. Evaluate which policy better fits the definition of "libertarian paternalism," and justify your answer.

<div class="upper-alpha" markdown>
1. The mandatory 4% policy, because it guarantees higher retirement savings for everyone
2. The automatic-enrollment policy, because it steers employees toward a default its designers judge to be beneficial while fully preserving each employee's freedom to opt out, unlike the mandatory policy which removes that choice entirely
3. Both policies equally qualify as libertarian paternalism, since both are intended to help employees save more
4. Neither policy qualifies as libertarian paternalism, since both involve the firm making retirement decisions for employees
</div>

??? question "Show Answer"
    The correct answer is **B**. Libertarian paternalism requires preserving freedom of choice while steering behavior through the default; the automatic-enrollment design does exactly this, while the mandatory policy is ordinary paternalism because it removes the option to decline entirely. Option A describes a stronger guarantee but at the cost of eliminating choice, which disqualifies it from the "libertarian" half of the definition, option C incorrectly treats intent alone as sufficient without considering whether choice is preserved, and option D ignores that the automatic-enrollment design does satisfy both halves of the definition.

    **Concept Tested:** Libertarian Paternalism

---

#### 10. A city wants to increase the share of residents who sign up for a recycling program when renewing their utility account, without banning or restricting any resident's choice. Which of the following proposed designs best constitutes an effective nudge consistent with the concepts in this chapter, and which bias does it rely on?

<div class="upper-alpha" markdown>
1. Requiring residents to pay an extra fee unless they join the recycling program, which removes the option to decline at no cost
2. Banning non-recycling entirely, since bans are the most effective way to change behavior
3. Changing the recycling sign-up from an opt-in checkbox to an opt-out default ("you will be enrolled in recycling unless you check here to decline"), relying on status quo bias to keep most residents enrolled while preserving their freedom to decline
4. Providing no information at all about recycling, since any information could bias residents' decisions
</div>

??? question "Show Answer"
    The correct answer is **C**. Switching the default from opt-in to opt-out leverages status quo bias — most residents will leave the default unchanged — while leaving the option to decline fully available at no real cost, exactly matching the chapter's definition of a nudge. Option A imposes a financial penalty that changes economic incentives rather than merely resetting a default, which goes beyond a nudge, option B is an outright restriction, not a nudge, and option D fails to leverage any bias at all and does not address the stated goal.

    **Concept Tested:** Nudge

---
