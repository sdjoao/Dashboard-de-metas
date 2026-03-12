def calcular_percentual(dataFrame):
    realizado = dataFrame["realizado"]
    meta = dataFrame["meta"]
    dataFrame["percentual"] = realizado / meta * 100
    return dataFrame

def calcular_metricas(dataFrame):
    totalMeta = dataFrame["meta"].sum()
    totalRealizado = dataFrame["realizado"].sum()
    totalPercentual = totalRealizado / totalMeta * 100
    data = {
        "meta_total": totalMeta,
        "realizado_total": totalRealizado,
        "percentual_final": totalPercentual
    }
    return data