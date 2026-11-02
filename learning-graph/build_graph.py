#!/usr/bin/env python3
"""Builds learning-graph.csv (+ metadata/taxonomy-names/color-config) for
ECON 1101 directly from the existing 16 chapters' structure, rather than
inventing a disconnected concept list. Concepts and their presentation order
are derived from each chapter's headings and Key Terms table."""
import csv
import json

CH = []

def add(label, deps, tax):
    CH.append((label, deps, tax))

# ---- Chapter 1: Foundations (FOUND) ----
add("Scarcity", [], "FOUND")
add("Choice", ["Scarcity"], "FOUND")
add("Opportunity Cost", ["Scarcity", "Choice"], "FOUND")
add("Sunk Cost", ["Opportunity Cost"], "FOUND")
add("Marginal Analysis", ["Opportunity Cost"], "FOUND")
add("Marginal Benefit", ["Marginal Analysis"], "FOUND")
add("Marginal Cost", ["Marginal Analysis"], "FOUND")
add("Production Frontier", ["Scarcity", "Choice"], "FOUND")
add("Productive Efficiency", ["Production Frontier"], "FOUND")
add("Increasing Opportunity Cost", ["Production Frontier"], "FOUND")
add("Comparative Advantage", ["Opportunity Cost"], "FOUND")
add("Absolute Advantage", ["Comparative Advantage"], "FOUND")
add("Specialization", ["Comparative Advantage"], "FOUND")
add("Ceteris Paribus", ["Scarcity"], "FOUND")
add("Positive Economics", ["Ceteris Paribus"], "FOUND")
add("Normative Economics", ["Positive Economics"], "FOUND")
add("Economic Model", ["Ceteris Paribus"], "FOUND")

# ---- Chapter 2: Supply and Demand (SUPDEM) ----
add("Market", ["Scarcity"], "SUPDEM")
add("Demand", ["Market"], "SUPDEM")
add("Law of Demand", ["Demand"], "SUPDEM")
add("Demand Curve", ["Law of Demand"], "SUPDEM")
add("Quantity Demanded", ["Demand Curve"], "SUPDEM")
add("Determinants of Demand", ["Demand Curve"], "SUPDEM")
add("Change in Demand", ["Determinants of Demand"], "SUPDEM")
add("Supply", ["Market"], "SUPDEM")
add("Law of Supply", ["Supply"], "SUPDEM")
add("Supply Curve", ["Law of Supply"], "SUPDEM")
add("Determinants of Supply", ["Supply Curve"], "SUPDEM")
add("Change in Supply", ["Determinants of Supply"], "SUPDEM")
add("Market Equilibrium", ["Demand Curve", "Supply Curve"], "SUPDEM")
add("Equilibrium Price", ["Market Equilibrium"], "SUPDEM")
add("Equilibrium Quantity", ["Market Equilibrium"], "SUPDEM")
add("Market Surplus", ["Market Equilibrium"], "SUPDEM")
add("Market Shortage", ["Market Equilibrium"], "SUPDEM")
add("Consumer Surplus", ["Demand Curve", "Marginal Benefit"], "SUPDEM")
add("Producer Surplus", ["Supply Curve", "Marginal Cost"], "SUPDEM")
add("Total Surplus", ["Consumer Surplus", "Producer Surplus"], "SUPDEM")
add("Normal Good", ["Determinants of Demand"], "SUPDEM")
add("Inferior Good", ["Determinants of Demand"], "SUPDEM")
add("Substitute Goods", ["Determinants of Demand"], "SUPDEM")
add("Complement Goods", ["Determinants of Demand"], "SUPDEM")

# ---- Chapter 3: Elasticity (ELAS) ----
add("Elasticity", ["Market Equilibrium"], "ELAS")
add("Price Elasticity of Demand", ["Elasticity", "Demand Curve"], "ELAS")
add("Midpoint Elasticity Formula", ["Price Elasticity of Demand"], "ELAS")
add("Elastic Demand", ["Price Elasticity of Demand"], "ELAS")
add("Inelastic Demand", ["Price Elasticity of Demand"], "ELAS")
add("Unit-Elastic Demand", ["Price Elasticity of Demand"], "ELAS")
add("Perfectly Inelastic Demand", ["Inelastic Demand"], "ELAS")
add("Perfectly Elastic Demand", ["Elastic Demand"], "ELAS")
add("Determinants of Price Elasticity", ["Price Elasticity of Demand"], "ELAS")
add("Total Revenue Test", ["Elastic Demand", "Inelastic Demand"], "ELAS")
add("Price Elasticity of Supply", ["Elasticity", "Supply Curve"], "ELAS")
add("Income Elasticity of Demand", ["Elasticity", "Normal Good"], "ELAS")
add("Cross-Price Elasticity of Demand", ["Elasticity", "Substitute Goods"], "ELAS")
add("Tax Incidence", ["Price Elasticity of Demand", "Price Elasticity of Supply"], "ELAS")

# ---- Chapter 4: Consumer Theory (CONS) ----
add("Utility", ["Marginal Analysis"], "CONS")
add("Total Utility", ["Utility"], "CONS")
add("Marginal Utility", ["Total Utility"], "CONS")
add("Diminishing Marginal Utility", ["Marginal Utility"], "CONS")
add("Equal Marginal Principle", ["Marginal Utility", "Marginal Analysis"], "CONS")
add("Budget Constraint", ["Market"], "CONS")
add("Indifference Curve", ["Utility"], "CONS")
add("Marginal Rate of Substitution", ["Indifference Curve"], "CONS")
add("Consumer Optimum", ["Budget Constraint", "Indifference Curve"], "CONS")
add("Tangency Condition", ["Consumer Optimum", "Marginal Rate of Substitution"], "CONS")
add("Income Effect", ["Consumer Optimum"], "CONS")
add("Substitution Effect", ["Consumer Optimum"], "CONS")
add("Giffen Good", ["Income Effect"], "CONS")
add("Demand Curve Derivation", ["Tangency Condition", "Demand Curve"], "CONS")

# ---- Chapter 5: Production and Costs (PROD) ----
add("Production Function", ["Marginal Analysis"], "PROD")
add("Total Product", ["Production Function"], "PROD")
add("Marginal Product", ["Total Product"], "PROD")
add("Average Product", ["Total Product"], "PROD")
add("Diminishing Marginal Returns", ["Marginal Product"], "PROD")
add("Short Run", ["Production Function"], "PROD")
add("Long Run", ["Production Function"], "PROD")
add("Fixed Cost", ["Short Run"], "PROD")
add("Variable Cost", ["Short Run"], "PROD")
add("Total Cost", ["Fixed Cost", "Variable Cost"], "PROD")
add("Average Fixed Cost", ["Fixed Cost"], "PROD")
add("Average Variable Cost", ["Variable Cost"], "PROD")
add("Average Total Cost", ["Total Cost"], "PROD")
add("Short-Run Marginal Cost", ["Total Cost", "Marginal Cost"], "PROD")
add("Long-Run Average Cost", ["Average Total Cost", "Long Run"], "PROD")
add("Economies of Scale", ["Long-Run Average Cost"], "PROD")
add("Diseconomies of Scale", ["Economies of Scale"], "PROD")
add("Minimum Efficient Scale", ["Economies of Scale"], "PROD")

# ---- Chapter 6: Perfect Competition (PCOMP) ----
add("Perfect Competition", ["Market Equilibrium"], "PCOMP")
add("Price Taker", ["Perfect Competition"], "PCOMP")
add("Marginal Revenue", ["Price Taker"], "PCOMP")
add("MR Equals MC Rule", ["Marginal Revenue", "Short-Run Marginal Cost"], "PCOMP")
add("Shutdown Rule", ["MR Equals MC Rule", "Average Variable Cost"], "PCOMP")
add("Short-Run Firm Supply Curve", ["Shutdown Rule"], "PCOMP")
add("Short-Run Industry Supply Curve", ["Short-Run Firm Supply Curve"], "PCOMP")
add("Economic Profit", ["Total Cost"], "PCOMP")
add("Accounting Profit", ["Economic Profit"], "PCOMP")
add("Long-Run Competitive Equilibrium", ["Economic Profit", "Long-Run Average Cost"], "PCOMP")
add("Allocative Efficiency", ["Long-Run Competitive Equilibrium", "Total Surplus"], "PCOMP")

# ---- Chapter 7: Monopoly (MONOP) ----
add("Monopoly", ["Perfect Competition"], "MONOP")
add("Barrier to Entry", ["Monopoly"], "MONOP")
add("Natural Monopoly", ["Barrier to Entry", "Economies of Scale"], "MONOP")
add("Price Maker", ["Monopoly"], "MONOP")
add("Monopolist Marginal Revenue", ["Marginal Revenue", "Price Maker"], "MONOP")
add("Monopoly Profit Maximization", ["Monopolist Marginal Revenue", "Short-Run Marginal Cost"], "MONOP")
add("Deadweight Loss", ["Monopoly Profit Maximization", "Total Surplus"], "MONOP")
add("Price Discrimination", ["Monopolist Marginal Revenue"], "MONOP")
add("First-Degree Discrimination", ["Price Discrimination"], "MONOP")
add("Second-Degree Discrimination", ["Price Discrimination"], "MONOP")
add("Third-Degree Discrimination", ["Price Discrimination", "Price Elasticity of Demand"], "MONOP")
add("Arbitrage", ["Price Discrimination"], "MONOP")
add("Marginal-Cost Pricing Regulation", ["Natural Monopoly", "Deadweight Loss"], "MONOP")
add("Average-Cost Pricing Regulation", ["Natural Monopoly", "Accounting Profit"], "MONOP")
add("Antitrust Policy", ["Monopoly"], "MONOP")
add("Sherman Antitrust Act", ["Antitrust Policy"], "MONOP")

# ---- Chapter 8: Monopolistic Competition (MCOMP) ----
add("Monopolistic Competition", ["Perfect Competition", "Monopoly"], "MCOMP")
add("Product Differentiation", ["Monopolistic Competition"], "MCOMP")
add("Brand Loyalty", ["Product Differentiation"], "MCOMP")
add("Monopolistic Short-Run Profit", ["Monopolistic Competition", "Monopolist Marginal Revenue"], "MCOMP")
add("Monopolistic Zero Profit", ["Monopolistic Short-Run Profit", "Long-Run Competitive Equilibrium"], "MCOMP")
add("Markup Over Marginal Cost", ["Monopolistic Zero Profit"], "MCOMP")
add("Excess Capacity", ["Markup Over Marginal Cost", "Minimum Efficient Scale"], "MCOMP")
add("Non-Price Competition", ["Product Differentiation"], "MCOMP")
add("Informative Advertising", ["Non-Price Competition"], "MCOMP")
add("Persuasive Advertising", ["Non-Price Competition"], "MCOMP")
add("Product Variety", ["Excess Capacity"], "MCOMP")

# ---- Chapter 9: Oligopoly (OLIG) ----
add("Oligopoly", ["Perfect Competition", "Monopoly"], "OLIG")
add("Strategic Interdependence", ["Oligopoly"], "OLIG")
add("Cournot Model", ["Strategic Interdependence"], "OLIG")
add("Cournot Best-Response Function", ["Cournot Model"], "OLIG")
add("Cournot-Nash Equilibrium", ["Cournot Best-Response Function"], "OLIG")
add("Bertrand Model", ["Strategic Interdependence"], "OLIG")
add("Bertrand Paradox", ["Bertrand Model", "Perfect Competition"], "OLIG")
add("Collusion", ["Strategic Interdependence"], "OLIG")
add("Cartel", ["Collusion"], "OLIG")
add("Kinked Demand Curve", ["Strategic Interdependence"], "OLIG")
add("Concentration Ratio", ["Oligopoly"], "OLIG")
add("Herfindahl-Hirschman Index", ["Concentration Ratio"], "OLIG")
add("Oligopoly Antitrust Policy", ["Antitrust Policy", "Herfindahl-Hirschman Index"], "OLIG")

# ---- Chapter 10: Game Theory (GAME) ----
add("Game", ["Marginal Analysis"], "GAME")
add("Payoff Matrix", ["Game"], "GAME")
add("Dominant Strategy", ["Payoff Matrix"], "GAME")
add("Dominated Strategy", ["Dominant Strategy"], "GAME")
add("Nash Equilibrium", ["Payoff Matrix"], "GAME")
add("Prisoners Dilemma", ["Dominant Strategy", "Nash Equilibrium"], "GAME")
add("Coordination Game", ["Nash Equilibrium"], "GAME")
add("Repeated Game", ["Prisoners Dilemma"], "GAME")
add("Tit-for-Tat Strategy", ["Repeated Game"], "GAME")
add("Sequential Game", ["Nash Equilibrium"], "GAME")
add("Backward Induction", ["Sequential Game"], "GAME")
add("Non-Credible Threat", ["Backward Induction"], "GAME")

# ---- Chapter 11: Factor Markets (FACTOR) ----
add("Derived Demand", ["Production Function"], "FACTOR")
add("Marginal Revenue Product", ["Derived Demand", "Marginal Product"], "FACTOR")
add("Labor Hiring Rule", ["Marginal Revenue Product"], "FACTOR")
add("Labor Demand Curve", ["Labor Hiring Rule"], "FACTOR")
add("Work-Leisure Trade-off", ["Budget Constraint"], "FACTOR")
add("Labor Supply Substitution Effect", ["Work-Leisure Trade-off", "Substitution Effect"], "FACTOR")
add("Labor Supply Income Effect", ["Work-Leisure Trade-off", "Income Effect"], "FACTOR")
add("Backward-Bending Labor Supply", ["Labor Supply Income Effect"], "FACTOR")
add("Labor Market Equilibrium", ["Labor Demand Curve", "Backward-Bending Labor Supply"], "FACTOR")
add("Monopsony", ["Labor Market Equilibrium", "Monopoly"], "FACTOR")
add("Marginal Cost of Labor", ["Monopsony"], "FACTOR")
add("Monopsony Hiring Rule", ["Marginal Cost of Labor", "Marginal Revenue Product"], "FACTOR")
add("Interest Rate", ["Market"], "FACTOR")
add("Present Value", ["Interest Rate"], "FACTOR")
add("Loanable Funds Market", ["Present Value", "Market Equilibrium"], "FACTOR")
add("Economic Rent", ["Market Equilibrium"], "FACTOR")
add("Human Capital", ["Present Value"], "FACTOR")

# ---- Chapter 12: Market Failures (MKTFAIL) ----
add("Market Failure", ["Allocative Efficiency"], "MKTFAIL")
add("Externality", ["Market Failure"], "MKTFAIL")
add("Negative Externality", ["Externality"], "MKTFAIL")
add("Positive Externality", ["Externality"], "MKTFAIL")
add("Excludability", ["Market Failure"], "MKTFAIL")
add("Rivalry", ["Market Failure"], "MKTFAIL")
add("Public Good", ["Excludability", "Rivalry"], "MKTFAIL")
add("Common-Pool Resource", ["Rivalry"], "MKTFAIL")
add("Tragedy of the Commons", ["Common-Pool Resource"], "MKTFAIL")
add("Information Asymmetry", ["Market Failure"], "MKTFAIL")
add("Adverse Selection", ["Information Asymmetry"], "MKTFAIL")
add("Moral Hazard", ["Information Asymmetry"], "MKTFAIL")
add("Market Power as Failure", ["Market Failure", "Deadweight Loss"], "MKTFAIL")
add("Pigouvian Tax", ["Negative Externality"], "MKTFAIL")
add("Rent-Seeking", ["Market Power as Failure"], "MKTFAIL")
add("Government Failure", ["Pigouvian Tax", "Rent-Seeking"], "MKTFAIL")

# ---- Chapter 13: Externalities and Public Goods (EXTPUB) ----
add("Social Marginal Cost", ["Negative Externality", "Marginal Cost"], "EXTPUB")
add("Social Marginal Benefit", ["Positive Externality", "Marginal Benefit"], "EXTPUB")
add("Marginal External Cost", ["Social Marginal Cost"], "EXTPUB")
add("Marginal External Benefit", ["Social Marginal Benefit"], "EXTPUB")
add("Externality Deadweight Loss", ["Social Marginal Cost", "Deadweight Loss"], "EXTPUB")
add("Pigouvian Subsidy", ["Social Marginal Benefit", "Pigouvian Tax"], "EXTPUB")
add("Coase Theorem", ["Negative Externality", "Marginal Cost"], "EXTPUB")
add("Cap-and-Trade", ["Pigouvian Tax"], "EXTPUB")
add("Marginal Abatement Cost", ["Cap-and-Trade"], "EXTPUB")
add("Samuelson Condition", ["Public Good"], "EXTPUB")
add("Free-Rider Problem", ["Public Good", "Dominant Strategy"], "EXTPUB")
add("Median Voter Theorem", ["Free-Rider Problem"], "EXTPUB")
add("Individual Transferable Quota", ["Cap-and-Trade", "Common-Pool Resource"], "EXTPUB")
add("Congestion Pricing", ["Common-Pool Resource", "Pigouvian Tax"], "EXTPUB")

# ---- Chapter 14: Information Economics (INFO) ----
add("Market for Lemons", ["Adverse Selection"], "INFO")
add("Adverse Selection Death Spiral", ["Market for Lemons"], "INFO")
add("Signaling", ["Information Asymmetry"], "INFO")
add("Education Signaling Model", ["Signaling", "Human Capital"], "INFO")
add("Screening", ["Information Asymmetry"], "INFO")
add("Separating Equilibrium", ["Signaling", "Screening"], "INFO")
add("Principal-Agent Problem", ["Moral Hazard"], "INFO")
add("Incentive Compatibility", ["Principal-Agent Problem"], "INFO")
add("Agency Cost", ["Principal-Agent Problem"], "INFO")
add("Credit Rationing", ["Adverse Selection"], "INFO")

# ---- Chapter 15: Behavioral Economics (BEHAV) ----
add("Bounded Rationality", ["Utility"], "BEHAV")
add("Satisficing", ["Bounded Rationality"], "BEHAV")
add("Heuristic", ["Bounded Rationality"], "BEHAV")
add("Cognitive Bias", ["Heuristic"], "BEHAV")
add("Prospect Theory", ["Cognitive Bias", "Total Utility"], "BEHAV")
add("Loss Aversion", ["Prospect Theory"], "BEHAV")
add("Endowment Effect", ["Loss Aversion"], "BEHAV")
add("Present Bias", ["Prospect Theory"], "BEHAV")
add("Hyperbolic Discounting", ["Present Bias", "Present Value"], "BEHAV")
add("Time Inconsistency", ["Hyperbolic Discounting"], "BEHAV")
add("Framing Effect", ["Cognitive Bias"], "BEHAV")
add("Mental Accounting", ["Framing Effect"], "BEHAV")
add("Social Preferences", ["Cognitive Bias"], "BEHAV")
add("Inequity Aversion", ["Social Preferences"], "BEHAV")
add("Nudge", ["Framing Effect", "Present Bias"], "BEHAV")
add("Libertarian Paternalism", ["Nudge"], "BEHAV")

# ---- Chapter 16: International Trade (TRADE) ----
add("Ricardian Trade Model", ["Comparative Advantage"], "TRADE")
add("Gains From Trade", ["Ricardian Trade Model"], "TRADE")
add("Terms of Trade", ["Gains From Trade"], "TRADE")
add("Factor Endowment", ["Production Function"], "TRADE")
add("Heckscher-Ohlin Model", ["Factor Endowment", "Ricardian Trade Model"], "TRADE")
add("Factor-Price Equalization", ["Heckscher-Ohlin Model"], "TRADE")
add("Trade Winners and Losers", ["Gains From Trade"], "TRADE")
add("Trade Adjustment Assistance", ["Trade Winners and Losers"], "TRADE")
add("Tariff", ["Market Equilibrium", "Gains From Trade"], "TRADE")
add("Tariff Welfare Loss", ["Tariff", "Deadweight Loss"], "TRADE")
add("Import Quota", ["Tariff"], "TRADE")
add("Quota Rent", ["Import Quota"], "TRADE")
add("World Trade Organization", ["Tariff"], "TRADE")
add("Infant Industry Argument", ["Tariff"], "TRADE")
add("Protectionism", ["Infant Industry Argument"], "TRADE")
add("Globalization", ["Gains From Trade", "Trade Winners and Losers"], "TRADE")
add("Trade Deficit", ["Gains From Trade"], "TRADE")
add("Balance of Payments", ["Trade Deficit"], "TRADE")
add("Current Account", ["Balance of Payments"], "TRADE")

FLAGGED_EDGE = ("Cournot-Nash Equilibrium", "Nash Equilibrium")

assert all(len(l) <= 32 for l, _, _ in CH), "label over 32 chars: " + str([l for l,_,_ in CH if len(l) > 32])

labels_seen = {}
rows = []
for i, (label, deps, tax) in enumerate(CH, start=1):
    if label in labels_seen:
        raise SystemExit(f"duplicate label: {label}")
    labels_seen[label] = i
    for d in deps:
        if d not in labels_seen:
            raise SystemExit(f"concept '{label}' depends on '{d}' which is not yet defined")
    rows.append([i, label, list(deps), tax])

src, dst = FLAGGED_EDGE
src_id = labels_seen[src]
dst_id = labels_seen[dst]
rows[src_id - 1][2] = rows[src_id - 1][2] + [dst]

with open("learning-graph.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ConceptID", "ConceptLabel", "Dependencies", "TaxonomyID"])
    for cid, label, deps, tax in rows:
        dep_ids = "|".join(str(labels_seen[d]) for d in deps)
        w.writerow([cid, label, dep_ids, tax])

print(f"Wrote {len(rows)} concepts to learning-graph.csv")
print(f"Flagged edge: #{src_id} {src!r} -> #{dst_id} {dst!r} (Ch9 depends on Ch10 concept -- backward chapter reference)")

TAXONOMY_NAMES = {
    "FOUND": "Foundations",
    "SUPDEM": "Supply and Demand",
    "ELAS": "Elasticity",
    "CONS": "Consumer Theory",
    "PROD": "Production and Costs",
    "PCOMP": "Perfect Competition",
    "MONOP": "Monopoly",
    "MCOMP": "Monopolistic Competition",
    "OLIG": "Oligopoly",
    "GAME": "Game Theory",
    "FACTOR": "Factor Markets",
    "MKTFAIL": "Market Failures",
    "EXTPUB": "Externalities and Public Goods",
    "INFO": "Information Economics",
    "BEHAV": "Behavioral Economics",
    "TRADE": "International Trade",
}
with open("taxonomy-names.json", "w") as f:
    json.dump(TAXONOMY_NAMES, f, indent=2)

COLOR_CONFIG = {
    "FOUND": "SteelBlue",
    "SUPDEM": "DarkSlateBlue",
    "ELAS": "DarkGreen",
    "CONS": "LimeGreen",
    "PROD": "Gold",
    "PCOMP": "DarkGoldenrod",
    "MONOP": "Khaki",
    "MCOMP": "Teal",
    "OLIG": "DodgerBlue",
    "GAME": "LightSkyBlue",
    "FACTOR": "Crimson",
    "MKTFAIL": "DarkRed",
    "EXTPUB": "MediumPurple",
    "INFO": "Indigo",
    "BEHAV": "DarkOrchid",
    "TRADE": "HotPink",
}
with open("color-config.json", "w") as f:
    json.dump(COLOR_CONFIG, f, indent=2)

METADATA = {
    "title": "ECON 1101: Principles of Microeconomics",
    "description": "A learning graph for an undergraduate principles of microeconomics course covering scarcity and opportunity cost, supply and demand, elasticity, consumer and producer theory, market structures, game theory, factor markets, market failures, information economics, behavioral economics, and international trade.",
    "creator": "Prof. Sharat Batra, University of Minnesota",
    "date": "2026-11-01",
    "version": "1.0",
    "format": "Learning Graph JSON v1.0",
    "schema": "https://raw.githubusercontent.com/dmccreary/learning-graphs/refs/heads/main/src/schema/learning-graph-schema.json",
    "license": "CC BY-NC-SA 4.0 DEED",
}
with open("metadata.json", "w") as f:
    json.dump(METADATA, f, indent=2)

print("Wrote taxonomy-names.json, color-config.json, metadata.json")
