entradaSegundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = entradaSegundos // 86400

segundosHorasResto = entradaSegundos % 86400

horas = segundosHorasResto // 3600

segundosMinutosResto = segundosHorasResto % 3600

minutos = segundosMinutosResto // 60

segundos = segundosMinutosResto % 60

print(dias,"dias,", horas, "horas,",minutos,"minutos e", segundos,"segundos.")
