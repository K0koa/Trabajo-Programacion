class IndicadorEconomico:
    def __init__(self, tipo_indicador, fecha_valor, valor, fecha_consulta, id_usuario, fuente=None):
        self.tipo_indicador = tipo_indicador
        self.valor = valor
        self.fecha_valor = fecha_valor
        self.fecha_consulta = fecha_consulta
        self.id_usuario = id_usuario
        self.fuente = fuente

    def __str__(self):
        return f"Indicador: {self.tipo_indicador} | Valor: {self.valor:,.2f} | Fecha: {self.fecha_valor} | Fuente: {self.fuente}"
    
    def a_tupla(self):
        return (self.tipo_indicador, self.valor, self.fecha_valor, self.fuente)