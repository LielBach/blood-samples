from blood_samples_reader import read_samples
from sklearn.cluster import MeanShift
from plotly.express import scatter

blood_samples = read_samples('blood-samples.csv')
bloods_samples_predictions = MeanShift().fit_predict(X=blood_samples)

scatter(blood_samples, x=bloods_samples_predictions).show()

