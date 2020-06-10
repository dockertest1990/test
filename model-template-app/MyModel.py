
class MyModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """
    
    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing")
        
    def predict_raw(self,request):
        ret = {"test":"here", "names":[1,2,3]}
        return ret
    
    def predict(self, X, feature_names=None):
        return X


