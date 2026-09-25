from app.core.sentiment_analyzer import SentimentAnalyzer

def test_sentiment_analysis():
    analyzer = SentimentAnalyzer()

    pos_res = analyzer.analyze("Bu sistem gerçekten harika ve çok başarılı!")
    assert pos_res["tone"] == "positive"

    neg_res = analyzer.analyze("Kodda hata var ve sistem çalışmıyor.")
    assert neg_res["tone"] == "negative"

    urg_res = analyzer.analyze("Acil durum: Sunucuda kritik hata!")
    assert urg_res["tone"] == "urgent"
