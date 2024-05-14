#khai báo các thư viện
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

cate=ctrl.Antecedent(np.arange(0,100,1),'cate')
wei=ctrl.Antecedent(np.arange(0,20,1),'wei')
tem=ctrl.Antecedent(np.arange(0,16,1),'tem')
loc=ctrl.Antecedent(np.arange(0,11,1),'loc')
area=ctrl.Antecedent(np.arange(0,16,1),'area')
met=ctrl.Consequent(np.arange(0,15,1),'met')

cate['TP']=fuzz.trimf(cate.universe,[0,0,5])
cate['TPS']=fuzz.trimf(cate.universe,[5,10,15])
cate['TPK']=fuzz.trimf(cate.universe,[15,20,25])
cate['ELEC']=fuzz.trimf(cate.universe,[25,30,35])
cate['CLO']=fuzz.trimf(cate.universe,[35,40,45])
cate['FUR']=fuzz.trimf(cate.universe,[45,50,55])
cate['NLSX']=fuzz.trimf(cate.universe,[55,60,65])

wei['<5kg']=fuzz.trimf(wei.universe,[0,0,5])
wei['5-20kg']=fuzz.trimf(wei.universe,[0,5,10])
wei['20-90000kg']=fuzz.trimf(wei.universe,[5,10,15])
wei['>99999kg']=fuzz.trimf(wei.universe,[10,15,20])

tem['<0deg']=fuzz.trimf(tem.universe,[0,0,5])
tem['0-25deg']=fuzz.trimf(tem.universe,[0,5,10])
tem['>25deg']=fuzz.trimf(tem.universe,[5,10,15])

loc['DOM']=fuzz.trimf(loc.universe,[0,0,5])
loc['INT']=fuzz.trimf(loc.universe,[0,5,10])

area['0-0.29cub']=fuzz.trimf(area.universe,[0,0,5])
area['0-60cub']=fuzz.trimf(area.universe,[0,5,10])
area['0-90cub']=fuzz.trimf(area.universe,[5,10,15])

met['AIR']=fuzz.trimf(met.universe,[0,0,5])
met['SHIP']=fuzz.trimf(met.universe,[0,5,10])
met['ROAD']=fuzz.trimf(met.universe,[5,10,15])
#Hàng thực phẩm
r1=ctrl.Rule(cate['TP'] & wei['<5kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r2=ctrl.Rule(cate['TP'] & wei['5-20kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['AIR'] )
r3=ctrl.Rule(cate['TP'] & wei['20-90000kg'] & tem['>25deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r4=ctrl.Rule(cate['TP'] & wei['>99999kg'] & tem['>25deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])
r5=ctrl.Rule(cate['TP'] & wei['<5kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'])
r6=ctrl.Rule(cate['TP'] & wei['5-20kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['AIR'])
r7=ctrl.Rule(cate['TP'] & wei['20-90000kg'] & tem['>25deg'] & loc['INT'] & area['0-60cub'], met['SHIP'])
r8=ctrl.Rule(cate['TP'] & wei['>99999kg'] & tem['>25deg'] & loc['INT'] & area['0-90cub'], met['SHIP'])
#TPS
r9=ctrl.Rule(cate['TPS'] & wei['<5kg'] & tem['<0deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'] )
r10=ctrl.Rule(cate['TPS'] & wei['5-20kg'] & tem['<0deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r11=ctrl.Rule(cate['TPS'] & wei['20-90000kg'] & tem['<0deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r12=ctrl.Rule(cate['TPS'] & wei['>99999kg'] & tem['<0deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])

r13=ctrl.Rule(cate['TPS'] & wei['<5kg'] & tem['<0deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'] )
r14=ctrl.Rule(cate['TPS'] & wei['5-20kg'] & tem['<0deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'])
r15=ctrl.Rule(cate['TPS'] & wei['20-90000kg'] & tem['<0deg'] & loc['INT'] & area['0-60cub'], met['SHIP'])
r16=ctrl.Rule(cate['TPS'] & wei['>99999kg'] & tem['<0deg'] & loc['INT'] & area['0-90cub'],met['SHIP'])
#TPK
r17=ctrl.Rule(cate['TPK'] & wei['<5kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r18=ctrl.Rule(cate['TPK'] & wei['5-20kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r19=ctrl.Rule(cate['TPK'] & wei['20-90000kg'] & tem['>25deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r20=ctrl.Rule(cate['TPK'] & wei['>99999kg'] & tem['>25deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])
r21=ctrl.Rule(cate['TPK'] & wei['<5kg'] & tem['0-25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'] )
r22=ctrl.Rule(cate['TPK'] & wei['5-20kg'] & tem['0-25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r23=ctrl.Rule(cate['TPK'] & wei['20-90000kg'] & tem['0-25deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r24=ctrl.Rule(cate['TPK'] & wei['>99999kg'] & tem['0-25deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])

r25=ctrl.Rule(cate['TPK'] & wei['<5kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['AIR'])
r26=ctrl.Rule(cate['TPK'] & wei['5-20kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'])
r27=ctrl.Rule(cate['TPK'] & wei['20-90000kg'] & tem['>25deg'] & loc['INT'] & area['0-60cub'], met['SHIP'])
r28=ctrl.Rule(cate['TPK'] & wei['>99999kg'] & tem['>25deg'] & loc['INT'] & area['0-90cub'],  met['SHIP'])
r29=ctrl.Rule(cate['TPK'] & wei['<5kg'] & tem['0-25deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'])
r30=ctrl.Rule(cate['TPK'] & wei['5-20kg'] & tem['0-25deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'])
r31=ctrl.Rule(cate['TPK'] & wei['20-90000kg'] & tem['0-25deg'] & loc['INT'] & area['0-60cub'],met['SHIP'])
r32=ctrl.Rule(cate['TPK'] & wei['>99999kg'] & tem['0-25deg'] & loc['INT'] & area['0-90cub'], met['SHIP'])
#ELEC
r33=ctrl.Rule(cate['ELEC'] & wei['<5kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r34=ctrl.Rule(cate['ELEC'] & wei['5-20kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r35=ctrl.Rule(cate['ELEC'] & wei['20-90000kg'] & tem['>25deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r36=ctrl.Rule(cate['ELEC'] & wei['>99999kg'] & tem['>25deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])

r37=ctrl.Rule(cate['ELEC'] & wei['<5kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['AIR'])
r38=ctrl.Rule(cate['ELEC'] & wei['5-20kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['ROAD'])
r39=ctrl.Rule(cate['ELEC'] & wei['20-90000kg'] & tem['>25deg'] & loc['INT'] & area['0-60cub'], met['SHIP'])
r40=ctrl.Rule(cate['ELEC'] & wei['>99999kg'] & tem['>25deg'] & loc['INT'] & area['0-90cub'], met['SHIP'])
#CLO
r41=ctrl.Rule(cate['CLO'] & wei['<5kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r42=ctrl.Rule(cate['CLO'] & wei['5-20kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r43=ctrl.Rule(cate['CLO'] & wei['20-90000kg'] & tem['>25deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r44=ctrl.Rule(cate['CLO'] & wei['>99999kg'] & tem['>25deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])

r45=ctrl.Rule(cate['CLO'] & wei['<5kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'],met['AIR'])
r46=ctrl.Rule(cate['CLO'] & wei['5-20kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'],met['AIR'])
r47=ctrl.Rule(cate['CLO'] & wei['20-90000kg'] & tem['>25deg'] & loc['INT'] & area['0-60cub'], met['SHIP'])
r48=ctrl.Rule(cate['CLO'] & wei['>99999kg'] & tem['>25deg'] & loc['INT'] & area['0-90cub'], met['SHIP'])
#FUR
r49=ctrl.Rule(cate['FUR'] & wei['<5kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r50=ctrl.Rule(cate['FUR'] & wei['5-20kg'] & tem['>25deg'] & loc['DOM'] & area['0-0.29cub'], met['ROAD'])
r51=ctrl.Rule(cate['FUR'] & wei['20-90000kg'] & tem['>25deg'] & loc['DOM'] & area['0-60cub'], met['ROAD'])
r52=ctrl.Rule(cate['FUR'] & wei['>99999kg'] & tem['>25deg'] & loc['DOM'] & area['0-90cub'], met['ROAD'])

r53=ctrl.Rule(cate['FUR'] & wei['<5kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'],  met['AIR'])
r54=ctrl.Rule(cate['FUR'] & wei['5-20kg'] & tem['>25deg'] & loc['INT'] & area['0-0.29cub'], met['AIR'] )
r55=ctrl.Rule(cate['FUR'] & wei['20-90000kg'] & tem['>25deg'] & loc['INT'] & area['0-60cub'],  met['SHIP'])
r56=ctrl.Rule(cate['FUR'] & wei['>99999kg'] & tem['>25deg'] & loc['INT'] & area['0-90cub'], met['SHIP'])

shipping_ctrl=ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30])
shipping=ctrl.ControlSystemSimulation(shipping_ctrl)
shipping.input['cate'] = 4
shipping.input['wei'] = 4
shipping.input['tem'] = 14
shipping.input['loc'] = 7
shipping.input['area'] = 4
shipping.compute()
print('Phương thức vận chuyển: ', shipping.output['met'])
met.view(sim=shipping)
