import event_loop as loop
import attributes as att

filename = "/lstr/sahara/dune/tlabree/nutau-data/prodgenie_nutau_dune10kt_1x2x6_1000evts_gen_g4_detsim_reco_001.root"

loop.dump_events(filename, 10)

test = loop.read_attribute(filename, att.num_leptons, 10)
print(test)
test = loop.read_attribute(filename, att.num_pions, 10)
print(test)
test = loop.read_attribute(filename, att.leading_pion_energies, 10)
print(test)
test = loop.read_attribute(filename, att.other_particle_energy_sum, 10)
print(test)
