import opensmile


smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.IS10,
    feature_level=opensmile.FeatureLevel.Functionals,
    logfile="1.txt",
    loglevel=6
)
y = smile.process_file('test.wav')
print(y)
y.to_csv("ok.csv")
