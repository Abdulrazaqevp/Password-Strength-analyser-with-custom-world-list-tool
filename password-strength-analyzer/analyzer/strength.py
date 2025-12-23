from zxcvbn import zxcvbn

def analyze_password(password):
    r = zxcvbn(password)
    return {
        "score": r["score"],
        "crack_time": r["crack_times_display"]["offline_fast_hashing_1e10_per_second"],
        "suggestions": r["feedback"]["suggestions"]
    }
def strength_label(score):
    return ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"][score]
