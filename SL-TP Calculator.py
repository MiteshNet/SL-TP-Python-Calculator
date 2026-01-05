"""
Option SL-TP Calculator
Usage: run this script and input LTP (premium). It calculates:
 - Stoploss at 20% of premium (i.e., SL = LTP - 20%)
 - Targets at +40% and +50% of premium (1:2 and 1:2.5 approx when SL=20%)
"""

def compute_sl_tp(ltp: float, sl_pct: float = 20.0, target_pcts=(40.0, 50.0)):
    """
    Compute SL and Targets based on percentages of the premium.
    ltp: premium price (float)
    sl_pct: stoploss percentage (e.g., 20 for 20%)
    target_pcts: iterable of target percentages (e.g., (40,50))
    Returns a dict with rounded values.
    """
    if ltp <= 0:
        raise ValueError("LTP must be positive.")
    sl_amount = ltp * (sl_pct / 100.0)
    sl_price = round(ltp - sl_amount, 2)
    results = {
        "entry": round(ltp, 2),
        "sl_pct": sl_pct,
        "sl_price": sl_price,
        "risk_amount": round(sl_amount, 2),
        "targets": []
    }
    for t in target_pcts:
        tgt_amount = ltp * (t / 100.0)
        tgt_price = round(ltp + tgt_amount, 2)
        results["targets"].append({"target_pct": t, "target_price": tgt_price, "reward_amount": round(tgt_amount, 2)})
    return results

def pretty_print(results):
    print(f"Entry (LTP): ₹{results['entry']}")
    print(f"Stoploss: {results['sl_pct']}%  →  ₹{results['sl_price']}  (risk ₹{results['risk_amount']})")
    for i, t in enumerate(results['targets'], start=1):
        rr = round((t['reward_amount'] / results['risk_amount']), 2) if results['risk_amount'] else None
        print(f"Target {i}: +{t['target_pct']}%  →  ₹{t['target_price']}  (reward ₹{t['reward_amount']}, R:R ≈ {rr}:1)")
    '''print("\\nTrail suggestions:")
    print(" - After hitting Target 1, move SL to entry (break-even).")
    print(" - After hitting Target 2, trail SL to capture profits or use a % trailing rule.")'''

if __name__ == '__main__':
    try:
        raw = input('Enter LTP (premium) — e.g. 100: ').strip()
        ltp = float(raw)
        res = compute_sl_tp(ltp, sl_pct=20.0, target_pcts=(40.0, 50.0))
        pretty_print(res)
    except Exception as e:
        print('Error:', e)
