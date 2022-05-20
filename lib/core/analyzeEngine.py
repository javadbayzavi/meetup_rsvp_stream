import pandas as pd
class analyzerEngine:
    def __init__(self) -> None:
        pass

    def analyzeTrend(self, data):
        result = []
        res = pd.DataFrame(data).groupby("group_city", sort = False)
        for name,group in res:
            jdata = {
                        "name": name,
                        "lon" : group["group_lon"].iloc[0],
                        "lat" : group["group_lat"].iloc[0],
                        "point" : len(group)
                    }    
            result.append(jdata)   
        return result
    def classifyVenues(self,data):
        pass

    def classifyTopics(self,data,topic):
        pass
