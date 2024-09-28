from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

Analyzer = SentimentIntensityAnalyzer()


def analyze(text):
    try:
        sentiment = Analyzer.polarity_scores(text)

        if sentiment["compound"] >= 0.05:
            print("Positive")
        elif sentiment["compound"] <= -0.05:
            print("Negative")
        else:
            print("Neutral")
    except Exception as e:
        print(e)


Text = input("Please enter a text: ")
analyze(Text)
