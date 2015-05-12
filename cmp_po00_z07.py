"""
"""

from collections import OrderedDict as OD


import model
reload(model)


net_z07 = model.Network.from_sbml('zhu2.xml', id='z07')

net_z07.set_var_constant('species_21', True)
net_z07.set_var_constant('species_24', True)
for spidx in [22, 23, 25, 26, 27, 28]:
    net_z07.remove_component('species_%d'%spidx)
net_z07 = net_z07.add_ratevars()
    

net = net_z07
net0 = net_z07.copy()

## thought:
# carefully write codes for changing species names, reaction names
# it should be useful generally...

# change names for net
# MCA for net: not working so far - why? verify Es first

# cmpn = compare.Comparison(net, net2, dexpts, dexpts2, pexpts)
# eens, pens, z, zens = cmpn.fit(p=net.p, ens=True)
# zens.hist(pts=z)

ssvals = net.get_ssvals_type('concn')

spidmap = OD([(sp.id, sp.name) for sp in net.species])
net = net.change_varids(spidmap)

spidmap2 = OD([('Pi','P'),
               ('NADPp','NADP'),
               ('Ri5P', 'R5P'),
               ('Xu5P', 'X5P')])
net = net.change_varids(spidmap2)               
    
rxnidmap = OD([('reaction_1', 'RuBisCO'),
               ('reaction_2', 'PGAK'),
               ('reaction_3', 'GAPDH'),
               ('reaction_4', 'TPI'),
               ('reaction_5', 'ALDF'),
               ('reaction_6', 'FBPP'),
               ('reaction_7', 'TKLF'),
               ('reaction_8', 'ALDS'),
               ('reaction_9', 'SBPP'),
               ('reaction_10', 'TKLS'),
               ('reaction_11', 'PPI'),
               ('reaction_12', 'EPI'),
               ('reaction_13', 'RK'),
               ('reaction_14', 'HPI'),
               ('reaction_17', 'ATPS')])

pidmap = OD([('parameter 1', 'kf_ATPS'),
             ('parameter 2', 'kf_NADPH'),
             ('V1', 'Vf_RuBisCO'),
             ('KM11', 'KM_RuBisCO_C02'),
             ('KM12', 'KM_RuBisCO_02'),
             ('KM13', 'KM_RuBisCO_RuBP'),
             ('KI11', 'KI_RuBisCO)_PGA'),
             ('KI12', 'KI_RuBisCO_FBP'),
             ('KI13', 'KI_RuBisCO_SBP'),
             ('KI14', 'KI_RuBisCO_P'),
             ('KI15', 'KI_RuBisCO_NADPH'),
             ('V2', 'Vf_PGAK'),
             ('KE2', 'KE_PGAK'),
             ('KM21', 'KM_PGAK_PGA'),
             ('KM22', 'KM_PGAK_ATP'),
             ('KM23', 'KM_PGAK_ADP'),
             ('V3', 'Vf_GAPDH'),
             ('KM31', 'KM_GAPDH_BPGA'),
             ('KM32', 'KM_GAPDH_NADPH'),
             ('KE4', 'KE_TPI'),
             ('V4', 'Vf_TPI'),
             ('V5', 'Vf_ALDF'),
             ('KE5', 'KE_ALDF'),
             ('KM51', 'KM_ALDF_GAP'),
             ('KM52', 'KM_ALDF_DHAP'),
             ('KM53', 'KM_ALDF_FBP'),
             ('V6', 'Vf_FBPP'),
             ('KM61', 'KM_FBPP_FBP'),
             ('KI61', 'KI_FBPP_F6P'),
             ('KI62', 'KI_FBPP_P'),
             ('V7', 'Vf_TKLF'),
             ('KE7', 'KE_TKLF'),
             ('KM71', 'KM_TKLF_X5P'),
             ('KM72', 'KM_TKLF_E4P'),
             ('KM73', 'KM_TKLF_F6P'),
             ('KM74', 'KM_TKLF_GAP'),
             ('V8', 'Vf_ALDS'),
             ('KE8', 'KE_ALDS'),
             ('KM81', 'KM_ALDS_DHAP'),
             ('KM82', 'KM_ALDS_E4P'),
             ('V9', 'Vf_SBPP'),
             ('KM9', 'KM_SBPP_SBP'),
             ('KI9', 'KI_SBPP_P'),
             ('V10', 'Vf_TKLS'),
             ('KE10', 'KE_TKLS'),
             ('KM101', 'KM_TKLS_X5P'),
             ('KM102', 'KM_TKLS_GAP'),
             ('KM103', 'KM_TKLS_S7P'),
             ('KM10', 'KM_TKLS_R5P'),
             ('KE11', 'KE_PPI'),
             ('V11', 'Vf_PPI'),
             ('KE12', 'KE_EPI'),
             ('V12', 'Vf_EPI'),
             ('V13', 'Vf_RK'),
             ('KI134', 'KM_RK_ADP'),
             ('KM132', 'KM_RK_ATP'),
             ('KI135', 'KI_RK_ADP'),
             ('KM131', 'KM_RK_Ru5P'),
             ('KI131', 'KI_RK_PGA'),
             ('KI132', 'KI_RK_RuBP'),
             ('KI133', 'KI_RK_P'),
             ('VS1', 'Vf_HPI'),
             ('K1', 'KM_HPI_F6P'),
             ('reaction_15_V1', 'Vf_TPT'),
             ('reaction_15_K1', 'KM_TPT_PGA'),
             ('v_reaction_1', 'v_RuBisCO'),
             ('v_reaction_2', 'v_PGAK'),
             ('v_reaction_3', 'v_GAPDH'),
             ('v_reaction_4', 'v_TPI'),
             ('v_reaction_5', 'v_ALDF'),
             ('v_reaction_6', 'v_FBPP'),
             ('v_reaction_7', 'v_TKLF'),
             ('v_reaction_8', 'v_ALDS'),
             ('v_reaction_9', 'v_SBPP'),
             ('v_reaction_10', 'v_TKLS'),
             ('v_reaction_11', 'v_PPI'),
             ('v_reaction_12', 'v_EPI'),
             ('v_reaction_13', 'v_RK'),
             ('v_reaction_14', 'v_HPI'),
             ('v_reaction_17', 'v_ATPS'),
             ('v_reaction_18', 'v_NADPHS'),
             ('v_reaction_15', 'v_TPT')])
             
net = net.change_varids(rxnidmap)
    
ssvals2 = net.get_ssvals_type('concn')


