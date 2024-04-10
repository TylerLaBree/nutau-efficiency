import itertools as it
import functools as ft


def particles_in_event(event):
    "Gives a generator for particles given an event"
    return (event.product()[0].GetParticle(i) for i in range(num_particles(event)))


def get_status_code(particle):
    return particle.StatusCode()


def is_final_state(particle):
    """
    Status code 1 means stable final state
    Status code 15 means final state nuclear remnant
    """
    return get_status_code(particle) in [1, 15]


def is_neutrino(particle):
    return pdg_code(particle) in [12, 14, 16]


def is_neutron(particle):
    return pdg_code(particle) == 2112


def is_mystery_2000000002(particle):
    return pdg_code(particle) == 2000000002


def is_sufficient_energy(particle):
    pdg_code = particle.PdgCode()
    if pdg_code in [211, -211]:  # (anti)pion
        return energy(particle) > 0.1  # GeV
    if pdg_code == 2212:  # proton
        return energy(particle) > 0.05  # GeV
    if pdg_code in [22, 11, 13]:  # photon, electron, muon
        return energy(particle) > 0.03  # GeV
    return True


def is_visible(particle):
    return (
        is_final_state(particle)
        and (not is_neutrino(particle))
        and (not is_neutron(particle))
        and (not is_mystery_2000000002(particle))
        and is_sufficient_energy(particle)
    )


def is_kept(particle, criteria):
    checks = [criterion(particle) for criterion in criteria]
    return ft.reduce(lambda a, b: a and b, checks, True)


def kept_particles(event, criteria=[is_visible]):
    def is_kept_criteria(particle):
        return is_kept(particle, criteria)

    return map(is_kept_criteria, particles_in_event(event))


def pdg_code(particle):
    return particle.PdgCode()


def pdg_codes(event):
    return [pdg_code(particle) for particle in particles_in_event(event)]


def four_momentum(particle):
    return [particle.Momentum()[j] for j in range(4)]


def four_momentums(event):
    return [four_momentum(particle) for particle in particles_in_event(event)]


def momentum(particle):
    return four_momentum(particle)[:2]


def momentums(event):
    return [momentum(particle) for particle in particles_in_event(event)]


def energy(particle):
    return four_momentum(particle)[3]


def energies(event):
    return [energy(particle) for particle in particles_in_event(event)]


def num_particles(event):
    return event.product()[0].NParticles()


def is_lepton(particle):
    "Helper function for num_leptons"
    return pdg_code(particle) in [11, -11, 13, -13]


def num_leptons(event):
    """
    Machado N_lep
    Returns number of (anti)electrons and (anti)muons
    """
    return sum(map(int, kept_particles(event, [is_lepton, is_visible])))


def is_negative_pion(particle):
    "Helper function for num_pions and leading_pion_energies"
    return pdg_code(particle) == -211


def num_pions(event):
    """
    Machado N_(π^-)
    Returns number of negative pions.
    He says later that we may not be able to discriminate positive and negative pions.
    """
    return sum(map(int, kept_particles(event, [is_negative_pion, is_visible])))


def keep_event(event):
    return num_pions(event) != 0 and num_leptons(event) == 0


def leading_pion_energy(event):
    """
    Machado π^-_lead
    Returns the energy of the leading pion
    """

    return max(
        it.compress(energies(event), kept_particles(event, [is_negative_pion, is_visible])),
        default=0,
    )


def other_particle_energy_sum(event):
    """
    Machado Σ E_other
    Returns the sum of particles energies which are not the leading pion
    He says this is visible particle energies only!
    """

    def is_not_pion(particle):
        return not is_negative_pion(particle)

    return sum(
        it.compress(energies(event), kept_particles(event, [is_not_pion, is_visible]))
    )


def missing_transverse_momentum(event):
    """
    Machado p_T^miss
    Returns the transverse component of the momentum orthogonal to the beam-line
    """
    return 0


def num_jets(event):
    """
    Machado N_jet
    Returns the number of jets according to the following jet clustering algorithm:
    "In order to be clustered into a single jet, visible particles must be within
    radius of R = 0.6, with R = √(η^2 + φ^2) where η = −log tan(θ/2) is the pseudo-
    rapidity (θ is the angle between the particle and the jet axis) and φ is the
    azimuthal angle with respect to the jet axis."
    - Machado 2020
    """
    return 0
